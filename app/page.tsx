"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState, type FormEvent } from "react";
import { Marco } from "@/components/Marco";
import { Medidor } from "@/components/ui";
import { eliminarVideo, guardarVideo, listarVideos } from "@/lib/almacen";
import { duracionTotal } from "@/lib/guion";
import { marca } from "@/lib/texto";
import { ETAPAS, etapaActual, videoNuevo, type Video } from "@/lib/tipos";

export default function PaginaExpedientes() {
  const router = useRouter();
  const [videos, setVideos] = useState<Video[] | null>(null);
  const [nombre, setNombre] = useState("");
  const [error, setError] = useState("");
  const [creando, setCreando] = useState(false);

  useEffect(() => {
    listarVideos().then(setVideos).catch((e) => { setError(e instanceof Error ? e.message : String(e)); setVideos([]); });
  }, []);

  async function crear(e: FormEvent) {
    e.preventDefault();
    if (!nombre.trim()) return;
    setCreando(true); setError("");
    try {
      const v = videoNuevo(nombre.trim());
      await guardarVideo(v);
      router.push(`/video/${v.id}`);
    } catch (fallo) {
      setError(fallo instanceof Error ? fallo.message : String(fallo));
      setCreando(false);
    }
  }

  async function borrar(v: Video) {
    if (!confirm(`¿Eliminar el expediente "${v.titulo}"? Se borra el guion y todo lo demás. No se puede deshacer.`)) return;
    try {
      await eliminarVideo(v.id);
      setVideos((lista) => (lista ?? []).filter((x) => x.id !== v.id));
    } catch (fallo) { setError(fallo instanceof Error ? fallo.message : String(fallo)); }
  }

  return (
    <Marco>
      <p className="sobretitulo">Archivo central</p>
      <h1>Expedientes</h1>
      <p className="bajada">Cada expediente es un video. Entra a uno para llevarlo, paso a paso, de la idea al guion listo para el creador de videos.</p>

      <form className="tarjeta fila" style={{ marginTop: 24 }} onSubmit={crear}>
        <input className="entrada crece" value={nombre} onChange={(e) => setNombre(e.target.value)} maxLength={120}
          placeholder="Nombre del caso. Ej.: El barco que navegó sin tripulación" aria-label="Nombre del nuevo expediente" />
        <button className="boton primario" disabled={!nombre.trim() || creando}>{creando ? "Abriendo…" : "Abrir expediente"}</button>
      </form>
      {error && <p className="error" role="alert" style={{ marginTop: 10 }}>No se pudo completar: {error}</p>}

      <div style={{ marginTop: 26 }}>
        {videos === null ? (
          <p className="suave pulso">Buscando en el archivo…</p>
        ) : videos.length === 0 ? (
          <div className="vacio">
            <h2>El archivo está vacío</h2>
            <p style={{ marginTop: 8 }}>Escribe arriba el nombre de tu primer caso para abrir un expediente.</p>
          </div>
        ) : (
          <div className="rejilla">
            {videos.map((v, i) => {
              const hechas = ETAPAS.filter((e) => v.aprobadas[e.id]).length;
              const terminado = hechas === ETAPAS.length;
              const etapa = ETAPAS.find((e) => e.id === etapaActual(v))!;
              return (
                <article key={v.id} className="tarjeta expediente" style={{ margin: 0 }}>
                  <div className="fila entre">
                    <span className="numero">EXPEDIENTE {String(videos.length - i).padStart(3, "0")}</span>
                    <span className={`insignia ${terminado ? "bien" : "rojo"}`}>{terminado ? "Terminado" : etapa.nombre}</span>
                  </div>
                  <h2><Link href={`/video/${v.id}`}>{v.titulo || "Sin nombre"}</Link></h2>
                  <div>
                    <Medidor valor={(hechas / ETAPAS.length) * 100} tono={terminado ? "bien" : undefined} />
                    <p className="chico suave" style={{ marginTop: 6 }}>{hechas} de {ETAPAS.length} etapas aprobadas · guion de {marca(duracionTotal(v))}</p>
                  </div>
                  <div className="fila entre" style={{ marginTop: "auto" }}>
                    <span className="chico tenue">{new Date(v.actualizado).toLocaleDateString("es-CO", { day: "numeric", month: "short", year: "numeric" })}</span>
                    <div className="fila">
                      <button type="button" className="boton mini fantasma peligro" onClick={() => void borrar(v)}>Eliminar</button>
                      <Link href={`/video/${v.id}`} className="boton mini">Abrir</Link>
                    </div>
                  </div>
                </article>
              );
            })}
          </div>
        )}
      </div>
    </Marco>
  );
}
