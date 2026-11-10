"use client";

import { useState } from "react";
import { capitulosDe, descripcionCompleta, duracionTotal, exportarEscenas, exportarJSON, exportarNarracion, listaEtiquetas, textoShort, tituloFinal } from "@/lib/guion";
import { marca } from "@/lib/texto";
import { ETAPAS } from "@/lib/tipos";
import { BotonCopiar, Punto, descargar } from "../ui";
import { Aprobacion, Encabezado, type PropsEtapa } from "./comun";

type Formato = "escenas" | "narracion" | "json";
const FORMATOS: { id: Formato; nombre: string; ayuda: string }[] = [
  { id: "escenas", nombre: "Por escenas", ayuda: "Cada escena con su narración y lo que se ve en pantalla." },
  { id: "narracion", nombre: "Solo narración", ayuda: "Un solo texto corrido con lo que dice la voz." },
  { id: "json", nombre: "Datos (JSON)", ayuda: "El paquete completo en el formato que leen los programas. Es el que usaremos para conectar el creador de videos." },
];

export function EtapaExportar({ v, cambiar, alAprobar }: PropsEtapa & { alAprobar: () => void }) {
  const [formato, setFormato] = useState<Formato>("escenas");
  const texto = formato === "escenas" ? exportarEscenas(v) : formato === "narracion" ? exportarNarracion(v) : JSON.stringify(exportarJSON(v), null, 2);
  const nombre = (v.titulo || "video").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "video";
  const titulo = tituloFinal(v);
  const etiquetas = listaEtiquetas(v.seo.etiquetas).join(", ");
  const previas = ETAPAS.filter((e) => e.id !== "exportar");
  return (
    <>
      <Encabezado id="exportar">
        Todo lo aprobado, listo para copiar. El guion va al creador de videos; el resto, a YouTube cuando subas el video.
        Nada se publica desde aquí: tú subes.
      </Encabezado>

      <section className="tarjeta">
        <div className="fila entre">
          <h3>Estado del expediente</h3>
          <span className="mono chico suave">{marca(duracionTotal(v))} · {v.bloques.filter((b) => b.narracion.trim()).length} escenas · {v.shorts.length} Shorts</span>
        </div>
        <ul className="lista" style={{ marginTop: 8 }}>
          {previas.map((e) => (
            <li key={e.id}><Punto tono={v.aprobadas[e.id] ? "bien" : "aviso"} /><span>{e.nombre} <span className="tenue chico">· {v.aprobadas[e.id] ? "aprobada" : "sin aprobar"}</span></span></li>
          ))}
        </ul>
      </section>

      <section className="tarjeta">
        <h3>Guion para el creador de videos</h3>
        <div className="pestanas" role="tablist" style={{ marginTop: 12 }}>
          {FORMATOS.map((f) => (
            <button key={f.id} type="button" role="tab" aria-selected={formato === f.id} className={`pestana ${formato === f.id ? "activa" : ""}`} onClick={() => setFormato(f.id)}>{f.nombre}</button>
          ))}
        </div>
        <p className="chico suave">{FORMATOS.find((f) => f.id === formato)!.ayuda}</p>
        <pre className="pre" style={{ margin: "12px 0" }}>{texto || "El guion está vacío."}</pre>
        <div className="fila">
          <BotonCopiar clase="boton primario" texto={texto} deshabilitado={!texto}>Copiar guion</BotonCopiar>
          <button type="button" className="boton" disabled={!texto}
            onClick={() => descargar(`${nombre}.${formato === "json" ? "json" : "txt"}`, texto, formato === "json" ? "application/json" : "text/plain")}>
            Descargar archivo
          </button>
        </div>
      </section>

      <section className="tarjeta" style={{ borderStyle: "dashed" }}>
        <div className="fila">
          <span className="insignia aviso">Pendiente</span>
          <h3>Conexión con el creador de videos</h3>
        </div>
        <p className="chico suave" style={{ marginTop: 8 }}>
          Todavía no está conectado. Cuando tengamos el repositorio del creador de videos, aquí aparecerá el botón para
          enviarle el guion directamente, en el formato exacto que ese programa necesite. Mientras tanto, usa «Copiar guion».
        </p>
      </section>

      <section className="tarjeta">
        <h3>Para subir a YouTube</h3>
        <div className="pila" style={{ marginTop: 12 }}>
          <Pieza nombre="Título" valor={titulo} />
          <Pieza nombre="Texto de la miniatura" valor={v.miniaturaTexto.trim()} />
          <Pieza nombre="Indicaciones de la miniatura" valor={v.miniaturaBrief.trim()} />
          <Pieza nombre={`Descripción${capitulosDe(v).valido ? " (con capítulos)" : " (sin capítulos: no son válidos)"}`} valor={descripcionCompleta(v)} />
          <Pieza nombre="Etiquetas" valor={etiquetas} />
        </div>
      </section>

      {v.shorts.length > 0 && (
        <section className="tarjeta">
          <h3>Shorts</h3>
          <div className="pila" style={{ marginTop: 12 }}>
            {v.shorts.map((s, i) => (
              <Pieza key={s.id} nombre={`Short ${i + 1}`}
                valor={[`NARRACIÓN:\n${textoShort(s)}`, s.textoPantalla.trim() && `TEXTO EN PANTALLA:\n${s.textoPantalla.trim()}`, s.bucle.trim() && `BUCLE:\n${s.bucle.trim()}`].filter(Boolean).join("\n\n")} />
            ))}
          </div>
        </section>
      )}

      <Aprobacion id="exportar" v={v} cambiar={cambiar} alAprobar={alAprobar}
        faltan={previas.some((e) => !v.aprobadas[e.id]) ? ["aprobar las etapas anteriores"] : []} />
    </>
  );
}

function Pieza({ nombre, valor }: { nombre: string; valor: string }) {
  return (
    <div>
      <div className="fila entre" style={{ marginBottom: 6 }}>
        <span className="chico suave" style={{ textTransform: "uppercase", letterSpacing: "0.12em", fontWeight: 600, fontSize: "0.74rem" }}>{nombre}</span>
        <BotonCopiar texto={valor} deshabilitado={!valor} />
      </div>
      <pre className="pre" style={{ maxHeight: 220 }}>{valor || "— vacío —"}</pre>
    </div>
  );
}
