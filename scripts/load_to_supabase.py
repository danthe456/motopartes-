"""Sube los CSV revisados a Supabase. Requiere SUPABASE_URL y SUPABASE_SERVICE_KEY (nunca en el frontend).
Uso: python -I load_to_supabase.py ../data
"""
import csv, os, sys, pathlib
from supabase import create_client
d = pathlib.Path(sys.argv[1])
sb = create_client(os.environ['SUPABASE_URL'], os.environ['SUPABASE_SERVICE_KEY'])
rd = lambda f: list(csv.DictReader(open(d / f, encoding='utf-8')))
num = lambda v: float(v.replace(',', '.')) if v not in ('', None) else None
def up(table, rows, key):
    for i in range(0, len(rows), 500):
        sb.table(table).upsert(rows[i:i+500], on_conflict=key).execute()
    print(table, len(rows))
up('motos', [dict(id=r['id'], marca=r['marca'], modelo=r['modelo'], cilindraje=int(r['cilindraje'] or 0) or None,
    familia_motor=r['familia_motor'], imagen_url=r['imagen_url'] or None) for r in rd('motos.csv')], 'id')
up('productos', [dict(ref=r['ref'], nombre=r['nombre'], categoria=r['categoria'] or None,
    precio=int(num(r['precio']) or 0), inventario=num(r['inventario']), aplica_texto=r['aplica_texto'] or None) for r in rd('productos.csv')], 'ref')
sb.table('compatibilidades').delete().neq('ref', '').execute()
up('compatibilidades', rd('compatibilidades.csv'), 'ref,moto_id')
