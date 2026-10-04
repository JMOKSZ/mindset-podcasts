#!/usr/bin/env python3
import json, sys, os, html, re
import feedparser
import requests

BASE = "/root/.openclaw/workspace/mindset-podcasts/scanner"
podcasts = json.load(open(os.path.join(BASE, "podcasts.json")))
state = json.load(open(os.path.join(BASE, "state.json")))
scanned = state.get("scannedEpisodes", {})

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; MindsetPodcastScanner/1.0)"}

out = {}
for p in podcasts:
    pid = p["id"]
    url = p["rss"]
    entry = {"id": pid, "name": p["name"], "host": p["host"], "rss": url,
             "status": None, "new": [], "last_known": None, "count": 0}
    try:
        r = requests.get(url, headers=HEADERS, timeout=45)
        entry["http"] = r.status_code
        feed = feedparser.parse(r.content)
        items = feed.entries
        entry["count"] = len(items)
        if not items:
            entry["status"] = "empty"
            out[pid] = entry
            continue
        seen = set(scanned.get(pid, []))
        new = []
        for it in items:
            gid = it.get("id") or it.get("guid") or it.get("link")
            if not gid:
                continue
            if gid in seen:
                continue
            new.append({
                "guid": gid,
                "title": it.get("title", ""),
                "pubDate": it.get("published", "") or it.get("updated", ""),
                "link": it.get("link", ""),
                "duration": it.get("itunes_duration", ""),
                "summary": html.unescape(re.sub("<[^>]+>", " ", it.get("summary", "") or "")).strip()[:4000],
                "content": html.unescape(re.sub("<[^>]+>", " ", (it.get("content")[0].get("value", "") if it.get("content") else ""))).strip()[:8000],
            })
        entry["new"] = new
        # last known = most recent item in feed regardless
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
        entry["error"] = str(e)
    out[pid] = entry

json.dump(out, open(os.path.join(BASE, "scan_result.json"), "w"), ensure_ascii=False, indent=1)
# concise console summary
for pid, e in out.items():
    print(f"== {pid} [{e['status']}] http={e.get('http')} entries={e['count']} new={len(e['new'])}")
    for n in e["new"]:
        print(f"   NEW: {n['pubDate']} | {n['title']} | {n['duration']}")
        print(f"        guid={n['guid']}")
    if e.get("last_known"):
        lk = e["last_known"]
        print(f"   last: {lk['pubDate']} | {lk['title']}")
