"use client";

import { REVISION_MANUAL, duracionTotal, ganchoElegido, revisionAutomatica } from "@/lib/guion";
import { marca } from "@/lib/texto";
import { EditorBloques } from "../EditorBloques";
import { PanelAgente } from "../PanelAgente";
import { PanelGancho } from "../PanelGancho";
import { Punto } from "../ui";
import { Aprobacion, Encabezado, type PropsEtapa } from "./comun";

export function EtapaRefinar({ v, cambiar, perfil, alAprobar }: PropsEtapa & { alAprobar: () => void }) {
  const chequeos = revisionAutomatica(v);
  const avisos = chequeos.filter((c) => !c.bien).length;
  const faltan = REVISION_MANUAL.filter((m) => !v.revision[m.id]).length;
  return (
    <>
      <Encabezado id="refinar">
        El panel revisa el guion contra las reglas del agente y te muestra qué falla. Corrige el bloque que haga falta
        sin tocar los demás; las tres últimas confirmaciones solo las puedes dar tú.
      </Encabezado>

      <div className="dos">
        <section className="tarjeta" style={{ margin: 0 }}>
          <div className="fila entre">
            <h3>Revisión automática</h3>
            <span className={`insignia ${avisos ? "aviso" : "bien"}`}>{avisos ? `${avisos} aviso${avisos === 1 ? "" : "s"}` : "Todo en orden"}</span>
          </div>
          <ul className="lista" style={{ marginTop: 10 }}>
            {chequeos.map((c) => (
              <li key={c.id}>
                <Punto tono={c.bien ? "bien" : "aviso"} />
                <span><b>{c.nombre}</b><br /><span className="suave chico">{c.detalle}</span></span>
              </li>
            ))}
          </ul>
        </section>
        <section className="tarjeta" style={{ margin: 0 }}>
          <div className="fila entre">
            <h3>Gancho en uso</h3>
            <span className="mono chico suave">Total {marca(duracionTotal(v))}</span>
          </div>
          <p style={{ margin: "10px 0 14px" }}>{ganchoElegido(v) ? `«${ganchoElegido(v)}»` : <span className="tenue">Sin gancho elegido.</span>}</p>
          <PanelGancho texto={ganchoElegido(v)} />
        </section>
      </div>

      <div style={{ marginTop: 16 }}>
        <PanelAgente id="refinar" perfil={perfil} video={v} notas={v.notasAgente.refinar}
          alCambiarNotas={(t) => cambiar((b) => { b.notasAgente.refinar = t; })} />
      </div>

      <section style={{ marginTop: 26 }}>
        <h3 style={{ marginBottom: 14 }}>Bloques</h3>
        <EditorBloques v={v} cambiar={cambiar} conDiagnostico />
      </section>

      <section className="tarjeta" style={{ marginTop: 16 }}>
        <h3>Solo tú puedes confirmar esto</h3>
        <ul className="lista" style={{ marginTop: 8 }}>
          {REVISION_MANUAL.map((m) => (
            <li key={m.id}>
              <label className="fila" style={{ cursor: "pointer", flexWrap: "nowrap", alignItems: "flex-start" }}>
                <input type="checkbox" checked={!!v.revision[m.id]} style={{ width: 18, height: 18, marginTop: 3, accentColor: "var(--rojo)" }}
                  onChange={(e) => cambiar((b) => { b.revision[m.id] = e.target.checked; })} />
                <span>{m.texto}</span>
              </label>
            </li>
          ))}
        </ul>
      </section>

      <Aprobacion id="refinar" v={v} cambiar={cambiar} avisos={avisos} alAprobar={alAprobar}
        faltan={faltan ? [`marcar ${faltan} confirmaci${faltan === 1 ? "ón" : "ones"} al final de la página`] : []} />
    </>
  );
}
