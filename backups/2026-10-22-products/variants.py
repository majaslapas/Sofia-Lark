# Latvian variant names (2026-10-22). Option names become "Krāsa" (one spelling instead of
# Color / KRĀSA / krāsa); English colour names become Latvian; SHOUTED values are written
# normally; two typos (PERIODOTS, BALA) are fixed. Left as they are, on purpose:
# - Calypso (its colour names belong to the design);
# - the Kalliope "Izpildījums" finishes (Montana Crystal, Creamrose Light Pearl … are the
#   crystal maker's own names) and the Habaha stone names, which are already Latvian.
# The values before are in options-before.jsonl.
import json
SKIP = {'earrings-calypso'}
OPTION = {'Color': 'Krāsa', 'KRĀSA': 'Krāsa', 'krāsa': 'Krāsa', 'Style': 'Variants'}
VALUE = {
    'Red': 'Sarkana', 'Gray': 'Pelēka', 'Green': 'Zaļa', 'Blue': 'Zila', 'Orange': 'Oranža',
    'White': 'Balta', 'Purple': 'Violeta', 'Aqua blue': 'Gaiši zila', 'Silver': 'Sudraba',
    'Gold': 'Zelta', 'White pearls': 'Baltas pērles', 'Dark pearls': 'Tumšas pērles',
    'mix': 'Dažādas krāsas', 'Mix': 'Dažādi akmeņi',
    'SUDRABA': 'Sudraba', 'ZELTA': 'Zelta', 'MAIGI ZAĻŠ': 'Maigi zaļa', 'ROZĀ': 'Rozā',
    'MELNS': 'Melna', 'MELNA': 'Melna', 'BALA': 'Balta', 'AMETISTS': 'Ametists',
    'PERIODOTS': 'Peridots', 'SUDRABS/ZELTS': 'Sudrabs/zelts', 'Pelēks': 'Pelēka', 'Balts': 'Balta',
}
out = []
for r in map(json.loads, open('options-before.jsonl')):
    if r['handle'] in SKIP: continue
    for o in r['options']:
        if o['name'] in ('Title', 'Izpildījums'): continue
        name = OPTION.get(o['name'], o['name'])
        keep = {'Balts'} if r['handle'] == 'kalliope-kaklarota-gk1799' else set()  # next to stone names
        vals = [{'id': v['id'], 'name': VALUE[v['name']]} for v in o['optionValues'] if v['name'] in VALUE and v['name'] not in keep]
        if name != o['name'] or vals:
            out.append({'handle': r['handle'], 'productId': r['id'], 'option': {'id': o['id'], 'name': name},
                        'values': vals, 'before': [o['name']] + [v['name'] for v in o['optionValues']]})
json.dump(out, open('variants.json', 'w'), ensure_ascii=False, indent=1)
for x in out: print(x['handle'], x['before'], '->', x['option']['name'], [v['name'] for v in x['values']])
print(len(out))
