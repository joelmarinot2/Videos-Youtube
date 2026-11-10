"use client";

import { avisosCapitulo, capitulosDe, textoCapitulos, tiempos } from "@/lib/guion";
import { marca } from "@/lib/texto";
import { PanelAgente } from "../PanelAgente";
import { BotonCopiar, Punto } from "../ui";
import { Aprobacion, Encabezado, type PropsEtapa } from "./comun";

export function EtapaCapitulos({ v, cambiar, perfil, alAprobar }: PropsEtapa & { alAprobar: () => void }) {
  const caps = capitulosDe(v);
  const porBloque = new Map(caps.lista.map((c) => [c.bloqueId, c]));
  const filas = tiempos(v);
  return (
    <>
      <Encabezado id="capitulos">
        Los tiempos salen del guion: cada bloque empieza donde termina el anterior. YouTube solo los convierte en
        capítulos si el primero está en 00:00, hay al menos tres y cada uno dura 10 segundos o más.
      </Encabezado>

      <section className="tarjeta">
        <div className="fila entre">
          <h3>Capítulos</h3>
          <span className={`insignia ${caps.valido ? "bien" : "aviso"}`}>{caps.valido ? "Válidos para YouTube" : "Todavía no son válidos"}</span>
        </div>
        {!caps.valido && (
          <ul className="lista" style={{ marginTop: 8 }}>
            {caps.errores.map((e) => <li key={e}><Punto tono="aviso" /><span className="chico">{e}</span></li>)}
          </ul>
        )}
        <table className="tabla" style={{ marginTop: 12 }}>
          <tbody>
            {filas.map((t, i) => {
              const cap = porBloque.get(t.bloque.id);
              const cfg = v.capitulos[t.bloque.id];
              const avisos = cap ? avisosCapitulo(cap) : [];
              return (
                <tr key={t.bloque.id} style={cap ? undefined : { opacity: 0.55 }}>
                  <td className="mono" style={{ width: 62 }}>{cap ? cap.etiqueta : "↳"}</td>
                  <td>
                    {cap ? (
                      <>
                        <input className="entrada" value={cfg?.titulo ?? t.bloque.titulo} aria-label={`Título del capítulo ${cap.etiqueta}`}
                          onChange={(e) => cambiar((b) => { b.capitulos[t.bloque.id] = { incluir: true, titulo: e.target.value }; })} />
                        {avisos.map((a) => <p key={a} className="chico" style={{ color: "var(--aviso)", marginTop: 4 }}>{a}</p>)}
                      </>
                    ) : (
                      <span className="chico suave">«{t.bloque.titulo}» queda dentro del capítulo anterior</span>
                    )}
                  </td>
                  <td className="mono chico suave" style={{ width: 70, textAlign: "right" }}>{marca(cap ? cap.segundos : t.segundos)}</td>
                  <td style={{ width: 150, textAlign: "right" }}>
                    {i > 0 && (
                      <button type="button" className="boton mini"
                        onClick={() => cambiar((b) => {
                          const previo = b.capitulos[t.bloque.id];
                          b.capitulos[t.bloque.id] = { titulo: previo?.titulo ?? t.bloque.titulo, incluir: !cap };
                        })}>
                        {cap ? "Unir al anterior" : "Separar"}
                      </button>
                    )}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </section>

      <PanelAgente id="capitulos" perfil={perfil} video={v} notas={v.notasAgente.capitulos}
        alCambiarNotas={(t) => cambiar((b) => { b.notasAgente.capitulos = t; })} />

      <section className="tarjeta">
        <div className="fila entre">
          <h3>Bloque para la descripción</h3>
          <BotonCopiar texto={() => textoCapitulos(v)} deshabilitado={!caps.valido} />
        </div>
        <pre className="pre" style={{ marginTop: 12 }}>{textoCapitulos(v)}</pre>
        {!caps.valido && <p className="chico suave" style={{ marginTop: 8 }}>Si apruebas así, el video se exporta sin capítulos.</p>}
      </section>

      <Aprobacion id="capitulos" v={v} cambiar={cambiar} faltan={[]} avisos={caps.errores.length} alAprobar={alAprobar} />
    </>
  );
}
