import { useEffect, useMemo, useState } from 'react'
import { supabase } from './supabase'

const cop = (n) => (n ? '$' + Number(n).toLocaleString('es-CO') : '—')

function MotoCard({ moto, onClick }) {
  return (
    <button onClick={onClick} className="rounded-xl bg-white shadow hover:shadow-md transition text-left overflow-hidden">
      {moto.imagen_url
        ? <img src={moto.imagen_url} alt={moto.modelo} className="h-32 w-full object-cover" />
        : <div className="h-32 grid place-items-center bg-slate-200 text-3xl font-bold text-slate-400">{moto.marca.slice(0, 3).toUpperCase()}</div>}
      <div className="p-3">
        <div className="text-xs text-slate-500">{moto.marca} · {moto.cilindraje} cc</div>
        <div className="font-semibold leading-tight">{moto.modelo}</div>
      </div>
    </button>
  )
}

function ProductList({ items, empty }) {
  if (!items.length) return <p className="text-sm text-slate-500">{empty}</p>
  return (
    <ul className="divide-y rounded-lg bg-white shadow">
      {items.map(({ productos: p, tipo }) => (
        <li key={p.ref} className="flex items-center justify-between gap-3 p-3">
          <div>
            <div className="font-medium">{p.nombre}</div>
            <div className="text-xs text-slate-500">Ref. {p.ref} · {p.categoria || 'Sin categoría'}</div>
          </div>
          <div className="text-right text-sm">
            <div className="font-semibold">{cop(p.precio)}</div>
            <div className={p.inventario > 0 ? 'text-emerald-600' : 'text-red-500'}>{p.inventario > 0 ? `${p.inventario} en stock` : 'Agotado'}</div>
          </div>
        </li>
      ))}
    </ul>
  )
}

function MotoDetail({ moto, onBack }) {
  const [rows, setRows] = useState(null)
  const [q, setQ] = useState('')
  useEffect(() => {
    supabase.from('compatibilidades').select('tipo, productos(*)').eq('moto_id', moto.id).then(({ data }) => setRows(data || []))
  }, [moto.id])
  const filtered = useMemo(() => (rows || []).filter(r => r.productos.nombre.toLowerCase().includes(q.toLowerCase()) || r.productos.ref.toLowerCase().includes(q.toLowerCase())), [rows, q])
  const propios = filtered.filter(r => r.tipo !== 'homologable')
  const homol = filtered.filter(r => r.tipo === 'homologable')
  return (
    <div className="mx-auto max-w-3xl p-4">
      <button onClick={onBack} className="mb-3 text-sm text-blue-600">← Todas las motos</button>
      <h1 className="text-2xl font-bold">{moto.marca} {moto.modelo}</h1>
      <p className="mb-4 text-slate-500">{moto.cilindraje} cc · familia {moto.familia_motor}</p>
      <input value={q} onChange={e => setQ(e.target.value)} placeholder="Buscar producto o referencia…" className="mb-4 w-full rounded-lg border p-2" />
      {rows === null ? <p>Cargando…</p> : <>
        <h2 className="mb-2 mt-4 font-semibold">Productos específicos ({propios.length})</h2>
        <ProductList items={propios} empty="Sin productos específicos." />
        <h2 className="mb-2 mt-6 font-semibold">Pueden homologar ({homol.length})</h2>
        <ProductList items={homol} empty="Sin homologaciones registradas." />
      </>}
    </div>
  )
}

export default function App() {
  const [motos, setMotos] = useState([])
  const [sel, setSel] = useState(null)
  const [q, setQ] = useState('')
  const [marca, setMarca] = useState('')
  useEffect(() => { supabase.from('motos').select('*').order('marca').order('cilindraje').then(({ data }) => setMotos(data || [])) }, [])
  if (sel) return <MotoDetail moto={sel} onBack={() => setSel(null)} />
  const marcas = [...new Set(motos.map(m => m.marca))]
  const list = motos.filter(m => (!marca || m.marca === marca) && `${m.marca} ${m.modelo}`.toLowerCase().includes(q.toLowerCase()))
  return (
    <div className="mx-auto max-w-5xl p-4">
      <h1 className="mb-4 text-2xl font-bold">Repuestos 2D Motos</h1>
      <div className="mb-4 flex flex-wrap gap-2">
        <input value={q} onChange={e => setQ(e.target.value)} placeholder="Buscar moto…" className="flex-1 rounded-lg border p-2" />
        <select value={marca} onChange={e => setMarca(e.target.value)} className="rounded-lg border p-2">
          <option value="">Todas las marcas</option>{marcas.map(x => <option key={x}>{x}</option>)}
        </select>
      </div>
      <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 md:grid-cols-4">
        {list.map(m => <MotoCard key={m.id} moto={m} onClick={() => setSel(m)} />)}
      </div>
    </div>
  )
}
