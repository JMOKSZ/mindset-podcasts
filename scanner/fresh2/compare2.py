#!/usr/bin/env python3
"""Compare fresh feeds against state.json, list NEW episodes with full info."""
import xml.etree.ElementTree as ET
import json, sys, html, re
from datetime import datetime

NS = {
    'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'dc': 'http://purl.org/dc/elements/1.1/',
}
BASE = '/root/.openclaw/workspace/mindset-podcasts/scanner'
state = json.load(open(BASE + '/state.json'))
scanned = state.get('scannedEpisodes', {})

feeds = {
    'acquired': 'acquired.xml',
    'founders': 'founders.xml',
    'all-in': 'all-in.xml',
    'my-first-million': 'my-first-million.xml',
    'knowledge-project': 'knowledge-project.xml',
    'diary-of-a-ceo': 'diary-of-a-ceo.xml',
}

def dtkey(pub):
    for fmt in ('%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M:%S %Z',
                '%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%SZ'):
        try:
            return datetime.strptime(pub.strip(), fmt).timestamp()
        except Exception:
            continue
    return 0

def clean(t):
    if not t: return ''
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()

def parse(fn):
    tree = ET.parse(fn)
    ch = tree.getroot().find('channel')
    out = []
    for item in ch.findall('item'):
        def g(tag):
            el = item.find(tag)
            return el.text.strip() if el is not None and el.text else ''
        def gns(tag):
            el = item.find(tag, NS)
            return el.text.strip() if el is not None and el.text else ''
        guid_el = item.find('guid')
        guid = guid_el.text.strip() if guid_el is not None and guid_el.text else ''
        summary = gns('summary') or g('description') or gns('subtitle')
        content = g('encoded')
        out.append({
            'guid': guid,
            'title': clean(g('title')),
            'pub': g('pubDate'),
            'link': g('link'),
            'summary': clean(summary),
            'content': clean(content),
            'duration': gns('duration'),
        })
    out.sort(key=lambda i: dtkey(i['pub']), reverse=True)
    return out

results = {}
for pid, fn in feeds.items():
    items = parse(BASE + '/fresh2/' + fn)
    known = set(scanned.get(pid, []))
    new = [i for i in items if i['guid'] not in known]
    results[pid] = {'total': len(items), 'new': new}
    print(f"\n{'='*70}\n### {pid}: {len(items)} items in feed, {len(new)} NEW")
    for i in new[:12]:
        print(f"\n  NEW [{i['pub']}] {i['title']}")
        print(f"    guid: {i['guid']}")
        print(f"    link: {i['link']}")
        print(f"    dur: {i['duration']}")
        print(f"    summary: {i['summary'][:600]}")

json.dump({k: v['new'] for k, v in results.items()},
          open(BASE + '/fresh/new.json', 'w'), ensure_ascii=False, indent=2)
print("\n\nSaved new.json")
