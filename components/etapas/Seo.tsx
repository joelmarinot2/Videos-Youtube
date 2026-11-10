"use client";

import { descripcionCompleta, listaEtiquetas, revisarConsulta, tituloFinal } from "@/lib/guion";
import { PanelAgente } from "../PanelAgente";
import { Area, BotonCopiar, Campo, Punto } from "../ui";
import { Aprobacion, Encabezado, type PropsEtapa } from "./comun";

export function EtapaSeo({ v, cambiar, perfil, alAprobar }: PropsEtapa & { alAprobar: () => void }) {
  const etiquetas = listaEtiquetas(v.seo.etiquetas);
  const titulo = tituloFinal(v);
  const consultas = v.seo.consultas.map((c) => ({ c, faltan: c.trim() ? revisarConsulta(c, titulo, v.seo.primerasLineas) : null }));
  const avisos = consultas.filter((x) => x.faltan?.length).length + (etiquetas.length > 15 ? 1 : 0);
  return (
    <>
      <Encabezado id="seo">
        Las dos primeras líneas son las únicas que alguien lee: aparecen antes de «…más» y son el resumen en el buscador.
        Las etiquetas pesan poco; quince bastan.
      </Encabezado>

      <PanelAgente id="seo" perfil={perfil} video={v} notas={v.notasAgente.seo}
        alCambiarNotas={(t) => cambiar((b) => { b.notasAgente.seo = t; })} />

      <div className="tarjeta pila" style={{ marginTop: 16 }}>
        <Campo titulo="Primeras dos líneas" ayuda="Di qué le da el video al espectador, con las palabras que él escribiría en el buscador.">
          <Area value={v.seo.primerasLineas} onChange={(e) => cambiar((b) => { b.seo.primerasLineas = e.target.value; })} />
        </Campo>
        <Campo titulo="Descripción larga" ayuda="Qué cubre, para quién es, fuentes y enlaces. Los capítulos los agrega el panel solo.">
          <Area value={v.seo.descripcion} style={{ minHeight: 140 }} onChange={(e) => cambiar((b) => { b.seo.descripcion = e.target.value; })} />
        </Campo>
        <Campo titulo={`Etiquetas · ${etiquetas.length} de 15`} ayuda="Separadas por comas. Solo variantes de escritura, nombres propios y siglas que la gente escribe de verdad.">
          <Area value={v.seo.etiquetas} placeholder="mary celeste, barco fantasma, …" onChange={(e) => cambiar((b) => { b.seo.etiquetas = e.target.value; })} />
        </Campo>
        {etiquetas.length > 15 && <p className="chico" style={{ color: "var(--aviso)" }}>Son {etiquetas.length} etiquetas. Un muro de etiquetas no es una estrategia: deja quince.</p>}
      </div>

      <section className="tarjeta">
        <h3>La prueba de las tres búsquedas</h3>
        <p className="chico suave" style={{ margin: "6px 0 12px" }}>
          Escribe las tres búsquedas que este video debería ganar. El panel comprueba que sus palabras estén en el título
          {titulo ? ` («${titulo}»)` : ""} o en las dos primeras líneas. Si faltan, el problema es el título, no la descripción.
        </p>
        <div className="pila">
          {consultas.map(({ c, faltan }, i) => (
            <div key={i}>
              <input className="entrada" value={c} placeholder={`Búsqueda ${i + 1}`} aria-label={`Búsqueda ${i + 1}`}
                onChange={(e) => cambiar((b) => { b.seo.consultas[i] = e.target.value; })} />
              {faltan && (
                <p className="fila chico" style={{ marginTop: 6, gap: 8 }}>
                  <Punto tono={faltan.length ? "aviso" : "bien"} />
                  <span className="suave">{faltan.length ? `No aparecen: ${faltan.join(", ")}` : "Todas sus palabras aparecen."}</span>
                </p>
              )}
            </div>
          ))}
        </div>
      </section>

      <section className="tarjeta">
        <div className="fila entre">
          <h3>Descripción final</h3>
          <BotonCopiar texto={() => descripcionCompleta(v)} deshabilitado={!descripcionCompleta(v)} />
        </div>
        <pre className="pre" style={{ marginTop: 12 }}>{descripcionCompleta(v) || "Aquí verás la descripción armada, con los capítulos en medio cuando sean válidos."}</pre>
      </section>

      <Aprobacion id="seo" v={v} cambiar={cambiar} avisos={avisos} alAprobar={alAprobar}
        faltan={v.seo.primerasLineas.trim() ? [] : ["escribir las dos primeras líneas"]} />
    </>
  );
}
