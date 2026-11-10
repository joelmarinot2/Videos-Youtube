"use client";

import Link from "next/link";
import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import { Marco } from "@/components/Marco";
import { EtapaCapitulos } from "@/components/etapas/Capitulos";
import { EtapaExportar } from "@/components/etapas/Exportar";
import { EtapaGuion } from "@/components/etapas/Guion";
import { EtapaIdea } from "@/components/etapas/Idea";
import { EtapaRefinar } from "@/components/etapas/Refinar";
import { EtapaSeo } from "@/components/etapas/Seo";
import { EtapaShorts } from "@/components/etapas/Shorts";
import { EtapaTitulo } from "@/components/etapas/Titulo";
import { obtenerPerfil } from "@/lib/almacen";
import { ETAPAS, PERFIL_VACIO, desbloqueada, etapaActual, type EtapaId, type PerfilCanal } from "@/lib/tipos";
import { useVideo, type EstadoGuardado } from "@/lib/useVideo";

const TEXTO_ESTADO: Record<EstadoGuardado, string> = {
  cargando: "Abriendo…", guardado: "Guardado", pendiente: "Cambios sin guardar…", guardando: "Guardando…",
  error: "No se pudo guardar", noexiste: "",
};

export default function PaginaVideo() {
  const { id } = useParams<{ id: string }>();
  const { video: v, cambiar, estado, detalle, guardarAhora } = useVideo(id);
  const [perfil, setPerfil] = useState<PerfilCanal>(PERFIL_VACIO);
  const [activa, setActiva] = useState<EtapaId | null>(null);

  useEffect(() => { obtenerPerfil().then(setPerfil).catch(() => {}); }, []);
  useEffect(() => { if (v && activa === null) setActiva(etapaActual(v)); }, [v, activa]);

  if (estado === "cargando" || (v && activa === null)) {
    return <Marco><p className="suave pulso">Abriendo el expediente…</p></Marco>;
  }
  if (!v) {
    return (
      <Marco>
        <div className="vacio">
          <h2>{estado === "error" ? "No se pudo abrir el expediente" : "Este expediente no existe"}</h2>
          {detalle && <p className="error" style={{ marginTop: 8 }}>{detalle}</p>}
          <p style={{ marginTop: 16 }}><Link href="/" className="boton">Volver a los expedientes</Link></p>
        </div>
      </Marco>
    );
  }

  const etapa = activa!;
  const irA = (e: EtapaId) => { setActiva(e); window.scrollTo({ top: 0, behavior: "smooth" }); };
  const siguiente = () => {
    const i = ETAPAS.findIndex((e) => e.id === etapa);
    if (i < ETAPAS.length - 1) irA(ETAPAS[i + 1].id);
  };
  const props = { v, cambiar, perfil, alAprobar: siguiente };

  return (
    <Marco>
      <div className="fila entre arriba">
        <div className="crece">
          <p className="sobretitulo"><Link href="/">← Expedientes</Link></p>
          <input className="entrada titulo-bloque" style={{ fontSize: "clamp(1.4rem, 3.4vw, 2.1rem)", width: "100%" }} value={v.titulo}
            aria-label="Nombre del expediente" onChange={(e) => cambiar((b) => { b.titulo = e.target.value; })} />
        </div>
        <div className="fila" role="status">
          <span className={`insignia ${estado === "error" ? "mal" : estado === "guardado" ? "bien" : "aviso"}`} title={detalle}>{TEXTO_ESTADO[estado]}</span>
          {estado === "error" && <button type="button" className="boton mini" onClick={() => void guardarAhora()}>Reintentar</button>}
        </div>
      </div>
      {estado === "error" && detalle && <p className="error" style={{ marginTop: 6 }}>{detalle}</p>}

      <div className="produccion">
        <ol className="pasos">
          {ETAPAS.map((e) => {
            const abierta = desbloqueada(v, e.id);
            return (
              <li key={e.id}>
                <button type="button" disabled={!abierta} aria-current={etapa === e.id ? "step" : undefined}
                  title={abierta ? undefined : "Se desbloquea al aprobar la etapa anterior"}
                  className={`paso ${v.aprobadas[e.id] ? "hecha" : ""} ${etapa === e.id ? "activa" : ""}`} onClick={() => irA(e.id)}>
                  <span style={{ display: "block" }}><b>{e.nombre}</b><span>{abierta ? e.resumen : "Bloqueada"}</span></span>
                </button>
              </li>
            );
          })}
        </ol>
        <div style={{ minWidth: 0 }}>
          {etapa === "idea" && <EtapaIdea {...props} />}
          {etapa === "guion" && <EtapaGuion {...props} />}
          {etapa === "refinar" && <EtapaRefinar {...props} />}
          {etapa === "titulo" && <EtapaTitulo {...props} />}
          {etapa === "seo" && <EtapaSeo {...props} />}
          {etapa === "capitulos" && <EtapaCapitulos {...props} />}
          {etapa === "shorts" && <EtapaShorts {...props} />}
          {etapa === "exportar" && <EtapaExportar {...props} />}
        </div>
      </div>
    </Marco>
  );
}
