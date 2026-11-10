"use client";

import { useEffect, useRef, useState } from "react";
import { Marco } from "@/components/Marco";
import { PanelAgente } from "@/components/PanelAgente";
import { Area, Campo } from "@/components/ui";
import { guardarPerfil, listarVideos, obtenerPerfil } from "@/lib/almacen";
import { AGENTES, type AgenteId } from "@/lib/agentes";
import { PERFIL_VACIO, type PerfilCanal, type Video } from "@/lib/tipos";

const CAMPOS: { id: keyof PerfilCanal; titulo: string; ayuda: string }[] = [
  { id: "audiencia", titulo: "A quién le hablo", ayuda: "Una sola persona, descrita de verdad. No «gente que le gusta el misterio», sino quién es, qué ve y por qué se queda." },
  { id: "comoHablo", titulo: "Cómo habla el canal de verdad", ayuda: "Pega aquí el texto de tu mejor video, o de tres. No como te gustaría sonar: como suenas." },
  { id: "nuncaUso", titulo: "Palabras que nunca uso", ayuda: "Las que no son tuyas. Sé específico." },
  { id: "siUso", titulo: "Palabras que sí uso", ayuda: "Tus frases de siempre. Las que hacen que se reconozca el canal." },
  { id: "noAfirmo", titulo: "Lo que el canal no afirma", ayuda: "Cifras que no puedes mostrar, teorías que no vas a dar por ciertas. Escríbelo para que los agentes lo rechacen por ti." },
  { id: "formato", titulo: "Formato del canal", ayuda: "Duración, cómo abre un video, si hay presentación, qué tipo de imágenes, qué voz." },
];

const DEL_CANAL: AgenteId[] = ["plan", "viral", "auditoria", "comentarios", "retencion", "edicion"];
const CON_VIDEO: AgenteId[] = ["comentarios", "retencion", "edicion"];

export default function PaginaCanal() {
  const [perfil, setPerfil] = useState<PerfilCanal | null>(null);
  const [estado, setEstado] = useState<"guardado" | "guardando" | "error">("guardado");
  const [error, setError] = useState("");
  const [videos, setVideos] = useState<Video[]>([]);
  const [entradas, setEntradas] = useState<Partial<Record<AgenteId, string>>>({});
  const [videoDe, setVideoDe] = useState<Partial<Record<AgenteId, string>>>({});
  const reloj = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    obtenerPerfil().then(setPerfil).catch((e) => { setError(String(e instanceof Error ? e.message : e)); setPerfil(PERFIL_VACIO); });
    listarVideos().then(setVideos).catch(() => {});
    return () => { if (reloj.current) clearTimeout(reloj.current); };
  }, []);

  function editar(id: keyof PerfilCanal, texto: string) {
    if (!perfil) return;
    const nuevo = { ...perfil, [id]: texto };
    setPerfil(nuevo); setEstado("guardando");
    if (reloj.current) clearTimeout(reloj.current);
    reloj.current = setTimeout(() => {
      guardarPerfil(nuevo).then(() => { setEstado("guardado"); setError(""); })
        .catch((e) => { setEstado("error"); setError(e instanceof Error ? e.message : String(e)); });
    }, 700);
  }

  return (
    <Marco>
      <p className="sobretitulo">Identidad</p>
      <h1>El canal</h1>
      <p className="bajada">
        La voz del canal y los agentes que trabajan sobre el canal completo, no sobre un video. Todos los agentes leen este
        perfil antes de escribir: diez minutos aquí valen más que cualquier instrucción.
      </p>

      <section className="tarjeta" style={{ marginTop: 24 }}>
        <div className="fila entre">
          <h3>Perfil de voz</h3>
          <span className={`insignia ${estado === "error" ? "mal" : estado === "guardado" ? "bien" : "aviso"}`} role="status">
            {estado === "error" ? "No se pudo guardar" : estado === "guardado" ? "Guardado" : "Guardando…"}
          </span>
        </div>
        {error && <p className="error" role="alert" style={{ marginTop: 8 }}>{error}</p>}
        {perfil === null ? <p className="suave pulso" style={{ marginTop: 12 }}>Abriendo…</p> : (
          <div className="pila" style={{ marginTop: 14 }}>
            {CAMPOS.map((c) => (
              <Campo key={c.id} titulo={c.titulo} ayuda={c.ayuda}>
                <Area value={perfil[c.id]} onChange={(e) => editar(c.id, e.target.value)} />
              </Campo>
            ))}
          </div>
        )}
      </section>

      <h2 style={{ margin: "34px 0 6px" }}>Agentes del canal</h2>
      <p className="suave" style={{ marginBottom: 16 }}>Para planear la semana, ver qué funciona en tu tema y revisar lo que ya publicaste.</p>
      <div className="pila">
        {DEL_CANAL.map((id) => {
          const video = videos.find((x) => x.id === videoDe[id]);
          return (
            <div key={id}>
              <PanelAgente id={id} perfil={perfil ?? PERFIL_VACIO} video={video} entrada={entradas[id]} />
              <div className="tarjeta pila" style={{ marginTop: 6, borderStyle: "dashed" }}>
                {CON_VIDEO.includes(id) && videos.length > 0 && (
                  <Campo titulo="Video relacionado (opcional)" ayuda="Si eliges uno, las instrucciones incluyen su guion.">
                    <select className="entrada" style={{ width: "100%" }} value={videoDe[id] ?? ""} onChange={(e) => setVideoDe({ ...videoDe, [id]: e.target.value })}>
                      <option value="">Ninguno</option>
                      {videos.map((x) => <option key={x.id} value={x.id}>{x.titulo}</option>)}
                    </select>
                  </Campo>
                )}
                <Campo titulo={`Datos para ${AGENTES[id].nombre.toLowerCase()}`} ayuda={AGENTES[id].pideEntrada}>
                  <Area value={entradas[id] ?? ""} onChange={(e) => setEntradas({ ...entradas, [id]: e.target.value })} />
                </Campo>
              </div>
            </div>
          );
        })}
      </div>
    </Marco>
  );
}
