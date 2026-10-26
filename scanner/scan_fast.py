#!/usr/bin/env python3
import json, os, html, re, concurrent.futures
import feedparser, requests

BASE = "/root/.openclaw/workspace/mindset-podcasts/scanner"
podcasts = json.load(open(os.path.join(BASE, "podcasts.json")))
state = json.load(open(os.path.join(BASE, "state.json")))
scanned = state.get("scannedEpisodes", {})
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}

def clean(s, n=20000):
    s = s or ""
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"</p>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()[:n]

def work(p):
    pid = p["id"]
    entry = {"id": pid, "name": p["name"], "host": p["host"], "rss": p["rss"],
             "status": None, "new": [], "last_known": None, "count": 0, "latest_n": []}
    try:
        r = requests.get(p["rss"], headers=HEADERS, timeout=40)
        entry["http"] = r.status_code
        feed = feedparser.parse(r.content)
        items = feed.entries
        entry["count"] = len(items)
        if not items:
            entry["status"] = "empty"
            return pid, entry
        seen = set(scanned.get(pid, []))
        for it in items:
            gid = it.get("id") or it.get("guid") or it.get("link")
            if not gid:
                continue
            rec = {
                "guid": gid,
                "title": it.get("title", ""),
                "pubDate": it.get("published", "") or it.get("updated", ""),
                "link": it.get("link", ""),
                "duration": it.get("itunes_duration", ""),
                "summary": clean(it.get("summary", ""), 20000),
                "content": clean((it.get("content")[0].get("value", "") if it.get("content") else ""), 30000),
            }
            if len(entry["latest_n"]) < 4:
                entry["latest_n"].append({k: rec[k] for k in ("guid","title","pubDate","link","duration","summary")})
            if gid not in seen:
                entry["new"].append(rec)
        first = items[0]
        entry["last_known"] = {
            "title": first.get("title", ""),
            "pubDate": first.get("published", "") or first.get("updated", ""),
            "link": first.get("link", ""),
            "guid": first.get("id") or first.get("guid") or first.get("link"),
        }
        entry["status"] = "ok"
    except Exception as e:
        entry["status"] = "error"
        entry["error"] = repr(e)
    return pid, entry

out = {}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    for pid, entry in ex.map(work, podcasts):
        out[pid] = entry

json.dump(out, open(os.path.join(BASE, "scan_result.json"), "w"), ensure_ascii=False, indent=1)
for pid, e in out.items():
    print(f"== {pid} [{e['status']}] http={e.get('http')} entries={e['count']} new={len(e['new'])}")
    for n in e["new"]:
        print(f"   NEW: {n['pubDate']} | {n['title']} | {n['duration']}")
    if e.get("last_known"):
        lk = e["last_known"]
        print(f"   last: {lk['pubDate']} | {lk['title']}")
    if e.get("error"):
        print("   ERR:", e["error"])
