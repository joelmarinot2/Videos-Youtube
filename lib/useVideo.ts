"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { guardarVideo, obtenerVideo } from "./almacen";
import type { Video } from "./tipos";

export type EstadoGuardado = "cargando" | "guardado" | "pendiente" | "guardando" | "error" | "noexiste";

// Carga un video y guarda solo, poco despues de cada cambio.
export function useVideo(id: string) {
  const [video, setVideo] = useState<Video | null>(null);
  const [estado, setEstado] = useState<EstadoGuardado>("cargando");
  const [detalle, setDetalle] = useState("");
  const actual = useRef<Video | null>(null);
  const reloj = useRef<ReturnType<typeof setTimeout> | null>(null);
  const sucio = useRef(false);

  const guardarAhora = useCallback(async () => {
    if (reloj.current) { clearTimeout(reloj.current); reloj.current = null; }
    if (!sucio.current || !actual.current) return;
    sucio.current = false;
    setEstado("guardando");
    try {
      await guardarVideo(actual.current);
      setEstado(sucio.current ? "pendiente" : "guardado");
    } catch (e) {
      sucio.current = true;
      setDetalle(e instanceof Error ? e.message : String(e));
      setEstado("error");
    }
  }, []);

  useEffect(() => {
    let vivo = true;
    obtenerVideo(id)
      .then((v) => { if (!vivo) return; actual.current = v; setVideo(v); setEstado(v ? "guardado" : "noexiste"); })
      .catch((e) => { if (!vivo) return; setDetalle(e instanceof Error ? e.message : String(e)); setEstado("error"); });
    return () => { vivo = false; void guardarAhora(); };
  }, [id, guardarAhora]);

  useEffect(() => {
    const alSalir = (e: BeforeUnloadEvent) => { if (sucio.current) { void guardarAhora(); e.preventDefault(); } };
    window.addEventListener("beforeunload", alSalir);
    return () => window.removeEventListener("beforeunload", alSalir);
  }, [guardarAhora]);

  const cambiar = useCallback((mutar: (borrador: Video) => void) => {
    if (!actual.current) return;
    const copia = structuredClone(actual.current);
    mutar(copia);
    actual.current = copia;
    sucio.current = true;
    setVideo(copia);
    setEstado("pendiente");
    if (reloj.current) clearTimeout(reloj.current);
    reloj.current = setTimeout(() => { void guardarAhora(); }, 700);
  }, [guardarAhora]);

  return { video, cambiar, estado, detalle, guardarAhora };
}
