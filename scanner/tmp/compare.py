#!/usr/bin/env python3
"""Compare feeds against state.json, list new episodes."""
import xml.etree.ElementTree as ET
import json, re, sys
from datetime import datetime

ITUNES = '{http://www.itunes.com/dtds/podcast-1.0.dtd}'

state = json.load(open('/root/.openclaw/workspace/mindset-podcasts/scanner/state.json'))
scanned = state['scannedEpisodes']

feeds = {
    'acquired': 'acquired.xml',
    'founders': 'founders.xml',
    'all-in': 'allin2.xml',
    'my-first-million': 'mfm2.xml',
    'knowledge-project': 'kp.xml',
    'diary-of-a-ceo': 'doac.xml',
}

def parse(fn):
    tree = ET.parse(fn)
    ch = tree.getroot().find('channel')
    out = []
    for item in ch.findall('item'):
        def g(tag):
            el = item.find(tag)
            return el.text.strip() if el is not None and el.text else ''
        guid_el = item.find('guid')
        guid = guid_el.text.strip() if guid_el is not None and guid_el.text else ''
        out.append({
            'guid': guid,
            'title': g('title'),
            'pub': g('pubDate'),
            'link': g('link'),
            'desc': (item.findtext(ITUNES+'summary') or g('description') or '')[:500],
        })
    return out

for pid, fn in feeds.items():
    items = parse(fn)
    known = set(scanned.get(pid, []))
    new = [i for i in items if i['guid'] not in known]
    print(f"\n### {pid}: {len(items)} items in feed, {len(new)} NEW")
    for i in new[:10]:
        print(f"  NEW [{i['pub']}] {i['title']}")
        print(f"    guid={i['guid']}")
        print(f"    link={i['link']}")
