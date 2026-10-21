#!/usr/bin/env python3
import json, feedparser, re, html, sys
from datetime import datetime

BASE = "/root/.openclaw/workspace/mindset-podcasts/scanner/"
pods = json.load(open(BASE + "podcasts.json"))
state = json.load(open(BASE + "state.json"))

def clean(t):
    if not t: return ""
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"\s+", " ", t).strip()
    return t

out = {}
for p in pods:
    pid = p["id"]
    print("="*90)
    print(f"PODCAST: {pid} | {p['name']}")
    try:
        f = feedparser.parse(p["rss"], agent="Mozilla/5.0 (compatible; PodcastScan/1.0)")
        print("entries:", len(f.entries), "| feed title:", clean(f.feed.get("title",""))[:80])
        if not f.entries:
            print("!! NO ENTRIES / FETCH FAIL")
            out[pid] = []
            continue
        known = set(state["scannedEpisodes"].get(pid, []))
        new = []
        for e in f.entries:
            g = e.get("id") or e.get("guid") or e.get("link","")
            g = str(g)
            if g in known: continue
            new.append({
                "guid": g,
                "title": clean(e.get("title","")),
                "date": e.get("published",""),
                "link": e.get("link",""),
                "duration": e.get("itunes_duration",""),
                "desc": clean(e.get("summary", "")),
                "content": clean(" ".join(c.get("value","") for c in e.get("content", []))),
            })
        print("NEW:", len(new))
        for n in new:
            print("-"*80)
            print("GUID:", n["guid"])
            print("TITLE:", n["title"])
            print("DATE:", n["date"], "| DUR:", n["duration"])
            print("LINK:", n["link"])
            d = n["content"] if len(n["content"]) > len(n["desc"]) else n["desc"]
            print("DESC:", d[:6000])
        out[pid] = new
    except Exception as ex:
        print("ERROR:", ex)
        out[pid] = []

json.dump(out, open("/tmp/new_episodes.json","w"), ensure_ascii=False, indent=1)
