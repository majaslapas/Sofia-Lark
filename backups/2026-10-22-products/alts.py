import json, re, sys, os
os.chdir(sys.argv[1])
L = json.load(open('latvian.json'))
rows = [json.loads(l) for l in open('media.jsonl')]
products, media, variants = {}, {}, {}
for r in rows:
    gid = r['id']
    if '/Product/' in gid: products[gid] = dict(r, media=[], variants=[])
for r in rows:
    gid, parent = r['id'], r.get('__parentId')
    if '/MediaImage/' in gid and parent in products: products[parent]['media'].append(r)
    elif '/ProductVariant/' in gid: variants[gid] = dict(r, media=[]); products[parent]['variants'].append(variants[gid])
for r in rows:
    if '/MediaImage/' in r['id'] and r.get('__parentId') in variants: variants[r['__parentId']]['media'].append(r['id'])
TYPE = {'earrings': 'auskari', 'necklaces': 'kaklarota', 'kaklarotas': 'kaklarota', 'bracelets': 'aproce', 'rokassprādzes': 'aproce',
        'rings': 'gredzens', 'gredzeni': 'gredzens', 'brooch': 'piespraude', 'piespraudes': 'piespraude',
        'jewelry cleaning & care': 'rotu kopšanai'}
STEMS = ['auskar', 'kaklarot', 'aproc', 'rokassprādz', 'gredzen', 'piesprau', 'kopšan', 'drāniņ', 'tīrām']
def clean(t):
    t = re.sub(r'\s+', ' ', t).strip()
    if t.upper() == t and any(c.isalpha() for c in t): t = t[0] + t[1:].lower()
    t = t.replace('lidzekļu', 'līdzekļu')  # a typo in the product's own title
    return t
out, n_skip = [], 0
for p in products.values():
    handle = p['handle']
    title = clean(L[handle]['title'] if handle in L else p['title'])
    noun = TYPE.get((p['productType'] or '').strip().lower())
    base = title
    if noun and not any(s in title.lower() for s in STEMS): base = f'{title}, {noun}'
    vmap = {}
    for v in p['variants']:
        if v['title'] != 'Default Title':
            for m in v['media']: vmap.setdefault(m, v['title'])
    for i, m in enumerate(p['media']):
        if m['mediaContentType'] != 'IMAGE': continue
        if (m.get('alt') or '').strip(): n_skip += 1; continue
        vt = clean(vmap[m['id']]) if m['id'] in vmap else ''
        alt = base + (f' – {vt}' if vt and not vt.isdigit() else '')
        alt = alt[0].upper() + alt[1:]
        out.append({'id': m['id'], 'alt': alt[:500], 'handle': handle})
json.dump(out, open('alts.json', 'w'), ensure_ascii=False, indent=0)
print('products', len(products), 'images to fill', len(out), 'already had alt', n_skip)
import random; random.seed(3)
for o in random.sample(out, 25): print(o['handle'], '→', o['alt'])
