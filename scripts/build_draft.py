"""Genera borradores CSV: productos, motos, compatibilidades y tokens sin reconocer.
Uso: python -I build_draft.py ../data/export_items.csv ../data
"""
import csv, re, html, sys, unicodedata, collections, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from motos_catalog import M, GROUPS

src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
out.mkdir(exist_ok=True)

def norm(s):
    s = html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().upper()
    return re.sub(r'\s+', ' ', s).strip()

def alias_re(a):
    if a.startswith('re:'): return re.compile(a[3:])
    chars = [c for c in a.upper() if c not in ' -.']
    body = r'[\s\-\.]?'.join(re.escape(c) for c in chars)
    tail = r'(?!\d)' if chars[-1].isdigit() else r'(?![A-Z])'
    return re.compile(r'(?<![A-Z0-9])' + body + tail)

PAT = [(mid, [alias_re(a) for a in al]) for mid, _, _, _, _, al in M]
FAM = collections.defaultdict(list)
for mid, _, _, _, fam, _ in M: FAM[fam].append(mid)
GPAT = [(fam, [alias_re(a) for a in al]) for fam, al in GROUPS.items()]

def match(text):
    found = {mid for mid, pats in PAT if any(p.search(text) for p in pats)}
    for fam, pats in GPAT:
        if any(p.search(text) for p in pats): found.update(FAM[fam])
    return found

rows = list(csv.DictReader(open(src, encoding='utf-8-sig')))
prods, comp, unmatched = [], [], collections.Counter()
for r in rows:
    ref = r['REF'].strip()
    name = norm(r['Nombre'])
    first, _, rest = name.partition(' ')
    name_clean = rest if rest and re.search(r'\d', first) else name
    desc = norm(r['Descripción'])
    in_name, in_desc = match(name_clean), match(desc)
    ids = in_name | in_desc
    prods.append(dict(ref=ref, nombre=r['Nombre'].strip(), categoria=r['Categoria'].strip(),
        precio=r['Precio [Repuestos 2D Motos]'].strip(), inventario=r['En inventario [Repuestos 2D Motos]'].strip(),
        aplica_texto=desc, n_motos=len(ids)))
    for mid in sorted(ids):
        tipo = 'especifico' if (mid in in_name and len(in_name) == 1) else ('principal' if mid in in_name else 'homologable')
        comp.append(dict(ref=ref, moto_id=mid, tipo=tipo))
    if not ids and desc:
        for t in re.split(r'[/,]', desc):
            if t.strip(): unmatched[t.strip()] += 1
    if not ids: unmatched.setdefault('__sin_moto__:' + r['Nombre'].strip(), 0)

def w(fn, rows_, cols):
    with open(out / fn, 'w', newline='', encoding='utf-8') as f:
        wr = csv.DictWriter(f, cols); wr.writeheader(); wr.writerows(rows_)

w('productos.csv', prods, ['ref','nombre','categoria','precio','inventario','aplica_texto','n_motos'])
w('motos.csv', [dict(id=a,marca=b,modelo=c,cilindraje=d,familia_motor=e,imagen_url='') for a,b,c,d,e,_ in M],
  ['id','marca','modelo','cilindraje','familia_motor','imagen_url'])
w('compatibilidades.csv', comp, ['ref','moto_id','tipo'])
with open(out/'revisar_sin_reconocer.txt','w',encoding='utf-8') as f:
    for k,v in unmatched.items(): f.write(f'{k}\n')
cnt = collections.Counter(c['moto_id'] for c in comp)
print('productos', len(prods), '| con >=1 moto', sum(1 for p in prods if p['n_motos']), '| compat', len(comp))
print('motos sin productos:', [m[0] for m in M if cnt[m[0]] == 0])
print(cnt.most_common(12))
