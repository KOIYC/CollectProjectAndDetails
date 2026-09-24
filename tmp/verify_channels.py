import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path('tools').resolve()))
import kb_common as KB

def load(p):
    return KB.load_channels_yaml(pathlib.Path(p))

old = load('_meta/channels.yaml')
new = load('tmp/channels_deduped.yaml')

def summarize(cfg):
    ch = cfg.get('channels') or []
    d = {}
    for c in ch:
        d.setdefault(c['id'], []).append(c)
    return d

so, sn = summarize(old), summarize(new)
print('old ids', len(so), 'entries', sum(len(v) for v in so.values()))
print('new ids', len(sn), 'entries', sum(len(v) for v in sn.values()))
print('top-level keys old', sorted(old.keys()))
print('top-level keys new', sorted(new.keys()))
print('content_gate same:', old.get('content_gate') == new.get('content_gate'))
print('backends same:', old.get('backends') == new.get('backends'))
print('disabled same:', old.get('disabled') == new.get('disabled'))
print()
bad = 0
for cid, lst in sn.items():
    assert len(lst) == 1, cid
    n = lst[0]
    o = so[cid][0] if cid in so else None
    for k in ('adapter','profile','enabled','limit','enrich','auth'):
        if (n.get(k) if n else None) != (o.get(k) if o else None):
            print(f'  !! {cid}.{k}: old={o.get(k) if o else None} new={n.get(k)}'); bad += 1
    if n.get('status') not in (o.get('status') if o else None, *(x.get('status') for x in so.get(cid,[]))):
        print(f'  !! {cid}.status new={n.get("status")} old={[x.get("status") for x in so.get(cid,[])]}'); bad += 1
print('field-consistency mismatches:', bad)
en = [c['id'] for c in new['channels'] if c.get('enabled')]
print('enabled(%d):' % len(en), en)
print('disabled(%d):' % len(new['channels'] and [c["id"] for c in new["channels"] if not c.get("enabled")]), [c['id'] for c in new['channels'] if not c.get('enabled')])
c1 = [c for c in new['channels'] if c['id']=='c1c7'][0]
print('c1c7 params:', c1.get('params'))
print('c1c7 meta_unavailable:', list((c1.get('meta_unavailable') or {}).keys()))
rd = [c for c in new['channels'] if c['id']=='reddit'][0]
print('reddit limit_note present:', bool(rd.get('limit_note')))
dv = [c for c in new['channels'] if c['id']=='devto'][0]
print('devto limit_note present:', bool(dv.get('limit_note')))
xh = [c for c in new['channels'] if c['id']=='xiaohongshu'][0]
print('xiaohongshu unlock:', (xh.get('unlock') or '')[:40], '| note_unlock present:', 'note_unlock' in xh)
