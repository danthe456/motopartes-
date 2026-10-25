create table if not exists motos (
  id text primary key,
  marca text not null,
  modelo text not null,
  cilindraje int,
  familia_motor text,
  imagen_url text
);
create table if not exists productos (
  ref text primary key,
  nombre text not null,
  categoria text,
  precio int,
  inventario numeric,
  aplica_texto text
);
create table if not exists compatibilidades (
  ref text references productos(ref) on delete cascade,
  moto_id text references motos(id) on delete cascade,
  tipo text check (tipo in ('especifico','principal','homologable')),
  primary key (ref, moto_id)
);
create index if not exists comp_moto_idx on compatibilidades(moto_id);

alter table motos enable row level security;
alter table productos enable row level security;
alter table compatibilidades enable row level security;
create policy "lectura publica motos" on motos for select using (true);
create policy "lectura publica productos" on productos for select using (true);
create policy "lectura publica compat" on compatibilidades for select using (true);
-- Imágenes: crea un bucket público "motos" en Storage y guarda la URL en motos.imagen_url
