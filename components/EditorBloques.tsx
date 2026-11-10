"use client";

import { AYUDA_TIPO, NOMBRE_TIPO, diagnosticoBloque, tiempos } from "@/lib/guion";
import { marca } from "@/lib/texto";
import { bloque as bloqueNuevo, type Bloque, type TipoBloque } from "@/lib/tipos";
import type { PropsEtapa } from "./etapas/comun";
import { Area, Campo } from "./ui";

const TIPOS = Object.keys(NOMBRE_TIPO) as TipoBloque[];

export function EditorBloques({ v, cambiar, conDiagnostico }: Pick<PropsEtapa, "v" | "cambiar"> & { conDiagnostico?: boolean }) {
  const ts = tiempos(v);
  const editar = (id: string, mutar: (b: Bloque) => void) =>
    cambiar((borrador) => { const b = borrador.bloques.find((x) => x.id === id); if (b) mutar(b); });
  const mover = (i: number, paso: number) => cambiar((borrador) => {
    const j = i + paso;
    if (j < 0 || j >= borrador.bloques.length) return;
    [borrador.bloques[i], borrador.bloques[j]] = [borrador.bloques[j], borrador.bloques[i]];
  });

  return (
    <div className="pila">
      {ts.map((t, i) => {
        const b = t.bloque;
        const d = diagnosticoBloque(b, v.idea.ppm);
        return (
          <section key={b.id} className={`tarjeta bloque ${b.tipo}`}>
            <div className="fila entre">
              <div className="fila crece" style={{ gap: 8 }}>
                <span className="mono tenue chico">{marca(t.inicio)}</span>
                <input className="entrada titulo-bloque crece" value={b.titulo} aria-label="Nombre del bloque"
                  onChange={(e) => editar(b.id, (x) => { x.titulo = e.target.value; })} />
              </div>
              <div className="fila" style={{ gap: 4 }}>
                <select className="entrada" value={b.tipo} aria-label="Tipo de bloque"
                  onChange={(e) => editar(b.id, (x) => { x.tipo = e.target.value as TipoBloque; })}>
                  {TIPOS.map((tp) => <option key={tp} value={tp}>{NOMBRE_TIPO[tp]}</option>)}
                </select>
                <button type="button" className="boton mini fantasma" disabled={i === 0} onClick={() => mover(i, -1)} aria-label="Subir bloque">↑</button>
                <button type="button" className="boton mini fantasma" disabled={i === ts.length - 1} onClick={() => mover(i, 1)} aria-label="Bajar bloque">↓</button>
                <button type="button" className="boton mini fantasma peligro" aria-label="Eliminar bloque"
                  onClick={() => {
                    if (!b.narracion.trim() || confirm(`¿Eliminar el bloque "${b.titulo}" con todo su texto?`)) {
                      cambiar((borrador) => { borrador.bloques = borrador.bloques.filter((x) => x.id !== b.id); });
                    }
                  }}>✕</button>
              </div>
            </div>
            <p className="chico tenue" style={{ margin: "2px 0 12px" }}>{AYUDA_TIPO[b.tipo]}</p>
            <div className="pila">
              <Campo titulo="Narración">
                <Area className="entrada narracion" value={b.narracion} placeholder="Lo que dice la voz…"
                  onChange={(e) => editar(b.id, (x) => { x.narracion = e.target.value; })} />
              </Campo>
              <Campo titulo="En pantalla">
                <Area value={b.enPantalla} placeholder="Qué se ve mientras la voz dice esto: imagen, documento, mapa, texto…"
                  onChange={(e) => editar(b.id, (x) => { x.enPantalla = e.target.value; })} />
              </Campo>
            </div>
            <div className="fila chico suave" style={{ marginTop: 12 }}>
              <span className="mono">{d.palabras} palabras · {marca(d.segundos)}</span>
              {conDiagnostico && d.sinImagen && <span className="insignia aviso">Falta qué se ve</span>}
              {conDiagnostico && d.muletillas.length > 0 && <span className="insignia aviso">Muletillas: {d.muletillas.join(", ")}</span>}
              {conDiagnostico && b.tipo === "cuerpo" && d.segundos > 150 && <span className="insignia aviso">Bloque largo: ¿son dos ideas?</span>}
              <button type="button" className="boton mini fantasma" style={{ marginLeft: "auto" }}
                onClick={() => cambiar((borrador) => { borrador.bloques.splice(i + 1, 0, bloqueNuevo("cuerpo", "Nuevo bloque")); })}>
                + Agregar bloque debajo
              </button>
            </div>
          </section>
        );
      })}
    </div>
  );
}
