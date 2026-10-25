# Repuestos 2D Motos
1. Supabase: ejecuta `supabase/schema.sql` en el SQL Editor.
2. Revisa `data/motos.csv`, `data/compatibilidades.csv` (y `scripts/motos_catalog.py` si quieres corregir alias; luego `python -I scripts/build_draft.py data/export_items.csv data`).
3. Carga: `pip install -r scripts/requirements.txt` y `SUPABASE_URL=... SUPABASE_SERVICE_KEY=... python -I scripts/load_to_supabase.py data`
4. Web: `cd web && cp .env.example .env` (pon URL y anon key), `npm install && npm run dev`.
5. Netlify: conecta el repo, base directory `web`, variables VITE_SUPABASE_URL y VITE_SUPABASE_ANON_KEY.
