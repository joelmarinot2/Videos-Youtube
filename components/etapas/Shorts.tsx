"use client";

import { SHORT_MAX, SHORT_MIN, candidatosShort, revisarShort, textoShort } from "@/lib/guion";
import { nuevoId } from "@/lib/tipos";
import { PanelAgente } from "../PanelAgente";
import { PanelGancho } from "../PanelGancho";
import { Area, BotonCopiar, Campo, Punto } from "../ui";
import { Aprobacion, Encabezado, type PropsEtapa } from "./comun";

export function EtapaShorts({ v, cambiar, perfil, alAprobar }: PropsEtapa & { alAprobar: () => void }) {
  const candidatos = candidatosShort(v);
  const usados = new Set(v.shorts.map((s) => s.bloqueId));
  const avisos = v.shorts.reduce((n, s) => n + revisarShort(s, v.idea.ppm).avisos.length, 0);
  return (
    <>
      <Encabezado id="shorts">
        Un Short no es un recorte del mejor momento: es un momento que sobrevive sin el video alrededor. El panel propone
        los bloques que mejor se sostienen solos; tú eliges cuáles quedan y les escribes una primera línea nueva.
      </Encabezado>

      <section className="tarjeta">
        <h3>Momentos propuestos</h3>
        <p className="chico suave" style={{ margin: "6px 0 12px" }}>
          Se buscan tramos de {SHORT_MIN} a {SHORT_MAX} segundos que abran con una idea completa, tengan un giro y terminen en una frase cerrada.
        </p>
        {candidatos.length === 0 && <p className="tenue">El guion todavía no tiene bloques escritos.</p>}
        <div className="pila">
          {candidatos.map((c, n) => (
            <div key={c.bloque.id} className="tarjeta" style={{ padding: 16, background: "var(--panel-2)" }}>
              <div className="fila">
                {n < 3 && <span className="insignia rojo">Propuesta {n + 1}</span>}
                <b>{c.bloque.titulo}</b>
                <span className="mono chico suave">{Math.round(c.segundos)} s · {c.puntaje} puntos</span>
                <button type="button" className="boton mini" style={{ marginLeft: "auto" }} disabled={usados.has(c.bloque.id)}
                  onClick={() => cambiar((b) => {
                    b.shorts.push({ id: nuevoId(), bloqueId: c.bloque.id, texto: c.bloque.narracion.trim(), primeraLinea: "", textoPantalla: "", bucle: "" });
                  })}>
                  {usados.has(c.bloque.id) ? "Ya es un Short" : "Crear Short con este bloque"}
                </button>
              </div>
              <p className="chico suave" style={{ margin: "8px 0" }}>«{c.bloque.narracion.trim().slice(0, 170)}{c.bloque.narracion.trim().length > 170 ? "…" : ""}»</p>
              <ul className="lista">
                {c.motivos.map((m) => <li key={m}><Punto tono="bien" /><span className="chico suave">{m}</span></li>)}
                {c.avisos.map((m) => <li key={m}><Punto tono="aviso" /><span className="chico">{m}</span></li>)}
              </ul>
            </div>
          ))}
        </div>
      </section>

      <PanelAgente id="shorts" perfil={perfil} video={v} notas={v.notasAgente.shorts}
        alCambiarNotas={(t) => cambiar((b) => { b.notasAgente.shorts = t; })} />

      {v.shorts.map((s, n) => {
        const r = revisarShort(s, v.idea.ppm);
        const editar = (mutar: (x: typeof s) => void) => cambiar((b) => { const x = b.shorts.find((y) => y.id === s.id); if (x) mutar(x); });
        const dentro = r.segundos >= SHORT_MIN && r.segundos <= SHORT_MAX;
        return (
          <section key={s.id} className="tarjeta bloque gancho">
            <div className="fila entre">
              <h3>Short {n + 1}</h3>
              <div className="fila">
                <span className={`insignia ${dentro ? "bien" : "aviso"}`}>{Math.round(r.segundos)} s</span>
                <BotonCopiar texto={() => textoShort(s)}>Copiar narración</BotonCopiar>
                <button type="button" className="boton mini fantasma peligro"
                  onClick={() => { if (confirm("¿Eliminar este Short?")) cambiar((b) => { b.shorts = b.shorts.filter((x) => x.id !== s.id); }); }}>Eliminar</button>
              </div>
            </div>
            <div className="pila" style={{ marginTop: 12 }}>
              <Campo titulo="Primera línea nueva" ayuda="La del video largo da por sabido un contexto que aquí no existe. De 9 a 24 palabras.">
                <Area value={s.primeraLinea} style={{ minHeight: 60 }} onChange={(e) => editar((x) => { x.primeraLinea = e.target.value; })} />
              </Campo>
              {s.primeraLinea.trim() && <PanelGancho texto={s.primeraLinea} compacto />}
              <Campo titulo="Resto del Short" ayuda="Recorta hasta que quepa. Debe terminar en una frase, no a medias.">
                <Area className="entrada narracion" value={s.texto} onChange={(e) => editar((x) => { x.texto = e.target.value; })} />
              </Campo>
              <div className="dos">
                <Campo titulo="Texto en pantalla (primeros 2 segundos)" ayuda="Con palabras distintas a las que se dicen.">
                  <input className="entrada" value={s.textoPantalla} onChange={(e) => editar((x) => { x.textoPantalla = e.target.value; })} />
                </Campo>
                <Campo titulo="Punto de bucle" ayuda="Qué deja abierto la última frase para que la primera lo responda.">
                  <input className="entrada" value={s.bucle} onChange={(e) => editar((x) => { x.bucle = e.target.value; })} />
                </Campo>
              </div>
              {r.avisos.length > 0 && (
                <ul className="lista">{r.avisos.map((a) => <li key={a}><Punto tono="aviso" /><span className="chico">{a}</span></li>)}</ul>
              )}
            </div>
          </section>
        );
      })}

      <Aprobacion id="shorts" v={v} cambiar={cambiar} faltan={[]} avisos={avisos} alAprobar={alAprobar} />
      {v.shorts.length === 0 && <p className="chico tenue" style={{ marginTop: 8 }}>Puedes aprobar sin Shorts si este video no los necesita.</p>}
    </>
  );
}
