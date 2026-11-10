"use client";

import { useState } from "react";
import { FORMULAS, REGLAS } from "@/lib/formulas";
import { puntuar } from "@/lib/gancho";
import { duracionTotal } from "@/lib/guion";
import { marca } from "@/lib/texto";
import { EditorBloques } from "../EditorBloques";
import { PanelAgente } from "../PanelAgente";
import { PanelGancho } from "../PanelGancho";
import { Area, Medidor } from "../ui";
import { Aprobacion, Encabezado, type PropsEtapa } from "./comun";

export function EtapaGuion({ v, cambiar, perfil, alAprobar }: PropsEtapa & { alAprobar: () => void }) {
  const [verFormulas, setVerFormulas] = useState(false);
  const total = duracionTotal(v), meta = v.idea.duracionMin * 60;
  const escritos = v.ganchos.map((g, i) => ({ i, g: g.trim() })).filter((x) => x.g);
  const mejor = escritos.length > 1 ? escritos.reduce((a, b) => (puntuar(b.g).veredicto > puntuar(a.g).veredicto ? b : a)).i : -1;
  const faltan = [
    v.ganchoElegido === null || !v.ganchos[v.ganchoElegido]?.trim() ? "elegir un gancho" : "",
    !v.bloques.some((b) => b.narracion.trim()) ? "escribir al menos un bloque" : "",
  ].filter(Boolean);

  function elegir(i: number) {
    const texto = v.ganchos[i].trim();
    const primero = v.bloques.find((b) => b.tipo === "gancho");
    const yaEsUnGancho = !!primero && v.ganchos.some((g) => g.trim() && g.trim() === primero.narracion.trim());
    const reemplazar = !!primero && (!primero.narracion.trim() || yaEsUnGancho
      || confirm("El bloque de gancho ya tiene texto escrito. ¿Lo reemplazo por este gancho?"));
    cambiar((b) => {
      b.ganchoElegido = i;
      const destino = b.bloques.find((x) => x.tipo === "gancho");
      if (destino && reemplazar) destino.narracion = texto;
    });
  }

  return (
    <>
      <Encabezado id="guion">
        Primero el gancho: escribe hasta cinco opciones y el panel las califica mientras escribes. Después el guion,
        bloque por bloque, cada uno con lo que dice la voz y lo que se ve.
      </Encabezado>

      <PanelAgente id="guion" perfil={perfil} video={v} notas={v.notasAgente.guion}
        alCambiarNotas={(t) => cambiar((b) => { b.notasAgente.guion = t; })} />

      <section className="tarjeta" style={{ marginTop: 16 }}>
        <div className="fila entre">
          <h3>Ganchos · los primeros 15 segundos</h3>
          <button type="button" className="boton mini" onClick={() => setVerFormulas(!verFormulas)}>
            {verFormulas ? "Ocultar las 21 fórmulas" : "Ver las 21 fórmulas"}
          </button>
        </div>
        <p className="chico suave" style={{ marginTop: 6 }}>
          El puntaje es una guía, no una predicción: un puntaje bajo es motivo para revisar; uno alto no promete vistas.
        </p>
        {verFormulas && (
          <div className="pila" style={{ marginTop: 14 }}>
            <ul className="lista">{REGLAS.map((r) => <li key={r}><span className="punto mal">•</span>{r}</li>)}</ul>
            <div className="dos">
              {FORMULAS.map((f, n) => (
                <div key={f.id} className="tarjeta" style={{ padding: 14, margin: 0 }}>
                  <b>{n + 1}. {f.nombre}</b>
                  <p className="chico suave">{f.forma}</p>
                  <p className="chico" style={{ margin: "6px 0" }}>«{f.ejemplo}»</p>
                  <p className="chico tenue">{f.falla}</p>
                </div>
              ))}
            </div>
          </div>
        )}
        <div className="pila" style={{ marginTop: 16 }}>
          {v.ganchos.map((g, i) => {
            const elegido = v.ganchoElegido === i;
            return (
              <div key={i} className={`tarjeta ${elegido ? "elegido" : ""}`} style={{ padding: 16, background: "var(--panel-2)" }}>
                <div className="fila" style={{ marginBottom: 8 }}>
                  <span className="mono tenue chico">GANCHO {i + 1}</span>
                  {mejor === i && <span className="insignia bien">Mayor puntaje</span>}
                  {elegido && <span className="insignia rojo">Elegido</span>}
                  <button type="button" className="boton mini" style={{ marginLeft: "auto" }} disabled={!g.trim() || elegido} onClick={() => elegir(i)}>
                    {elegido ? "En uso" : "Usar este gancho"}
                  </button>
                </div>
                <Area value={g} placeholder="Escribe una opción de gancho (de 9 a 24 palabras)…" style={{ minHeight: 60 }}
                  onChange={(e) => cambiar((b) => { b.ganchos[i] = e.target.value; })} />
                {g.trim() && <div style={{ marginTop: 12 }}><PanelGancho texto={g} /></div>}
              </div>
            );
          })}
        </div>
      </section>

      <section style={{ marginTop: 26 }}>
        <div className="fila entre" style={{ marginBottom: 6 }}>
          <h3>Bloques del guion</h3>
          <span className="mono chico suave">{marca(total)} de {marca(meta)}</span>
        </div>
        <Medidor valor={meta ? (total / meta) * 100 : 0} tono={meta && Math.abs(total - meta) / meta <= 0.15 ? "bien" : undefined} />
        <div style={{ marginTop: 16 }}><EditorBloques v={v} cambiar={cambiar} /></div>
      </section>

      <Aprobacion id="guion" v={v} cambiar={cambiar} faltan={faltan} alAprobar={alAprobar} />
    </>
  );
}
