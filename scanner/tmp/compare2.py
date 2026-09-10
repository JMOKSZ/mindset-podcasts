#!/usr/bin/env python3
"""Find episodes published after lastScan date."""
import xml.etree.ElementTree as ET
import json
from datetime import datetime, timezone

ITUNES = '{http://www.itunes.com/dtds/podcast-1.0.dtd}'
state = json.load(open('/root/.openclaw/workspace/mindset-podcasts/scanner/state.json'))
last_scan = datetime.fromisoformat(state['lastScan'].replace('Z', '+00:00'))
scanned = state['scannedEpisodes']

feeds = {
    'acquired': 'acquired.xml',
    'founders': 'founders.xml',
    'all-in': 'allin2.xml',
    'my-first-million': 'mfm2.xml',
    'knowledge-project': 'kp.xml',
    'diary-of-a-ceo': 'doac.xml',
}

def parse_dt(s):
    s = s.strip()
    for fmt in ('%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M:%S %Z',
                '%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%SZ', '%a, %d %b %Y %H:%M:%S GMT'):
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    try:
        return datetime.fromisoformat(s.replace('Z', '+00:00'))
    except Exception:
        return None

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
        pub = parse_dt(g('pubDate'))
        out.append({'guid': guid, 'title': g('title'), 'pub': pub, 'pubraw': g('pubDate'), 'link': g('link')})
    return out

for pid, fn in feeds.items():
    items = parse(fn)
    dated = [i for i in items if i['pub']]
    if dated:
        newest = max(i['pub'] for i in dated)
    else:
        newest = None
    print(f"\n### {pid}: {len(items)} items, feed newest = {newest}")
    # candidates: published after last scan, or (if no pub date) not in scanned
    cands = []
    for i in items:
        if i['pub'] and i['pub'] > last_scan:
            cands.append(i)
        elif not i['pub'] and i['guid'] not in scanned.get(pid, []):
            cands.append(i)
    cands.sort(key=lambda x: (x['pub'] or datetime.min.replace(tzinfo=timezone.utc)), reverse=True)
    print(f"  Published after last scan ({last_scan}): {len(cands)}")
    for i in cands[:12]:
        print(f"  * [{i['pubraw']}] {i['title']} | guid={i['guid']}")
