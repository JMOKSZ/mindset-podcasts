#!/usr/bin/env python3
"""Parse podcast RSS feeds and list recent episodes."""
import xml.etree.ElementTree as ET
import sys, json
from datetime import datetime, timezone

def parse(fn, limit=15):
    ns = {
        'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'dc': 'http://purl.org/dc/elements/1.1/',
    }
    try:
        tree = ET.parse(fn)
    except Exception as e:
        print(f"  PARSE ERROR: {e}")
        return []
    root = tree.getroot()
    ch = root.find('channel')
    items = []
    for item in ch.findall('item'):
        def g(tag):
            el = item.find(tag)
            return el.text.strip() if el is not None and el.text else ''
        def gns(tag):
            el = item.find(tag, ns)
            return el.text.strip() if el is not None and el.text else ''
        guid_el = item.find('guid')
        guid = guid_el.text.strip() if guid_el is not None and guid_el.text else ''
        title = g('title')
        pub = g('pubDate')
        link = g('link')
        desc = gns('description')
        items.append({'guid': guid, 'title': title, 'pub': pub, 'link': link})
    # sort by pubDate desc best-effort
    def dtkey(i):
        for fmt in ('%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M:%S %Z', '%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%SZ'):
            try:
                return datetime.strptime(i['pub'].strip(), fmt).timestamp()
            except Exception:
                continue
        return 0
    items.sort(key=dtkey, reverse=True)
    return items[:limit]

for fn in sys.argv[1:]:
    print(f"\n===== {fn} =====")
    for it in parse(fn):
        print(f"- [{it['pub']}] {it['title']}\n    GUID: {it['guid']}")
