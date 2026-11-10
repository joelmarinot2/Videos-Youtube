"use client";

import { useEffect, useRef, useState, type ReactNode, type TextareaHTMLAttributes } from "react";

export function Sello() {
  return (
    <svg className="sello" viewBox="0 0 64 64" fill="none" aria-hidden="true">
      <circle cx="32" cy="32" r="29" stroke="#ff3b52" strokeWidth="2" />
      <circle cx="32" cy="32" r="22" stroke="#ff3b52" strokeWidth="1" strokeDasharray="2 5" />
      <path d="M10 32c6-10 14-15 22-15s16 5 22 15c-6 10-14 15-22 15s-16-5-22-15Z" stroke="#ff3b52" strokeWidth="2" />
      <circle cx="32" cy="32" r="6.5" fill="#ff3b52" />
    </svg>
  );
}

export async function copiar(texto: string): Promise<boolean> {
  try {
    await navigator.clipboard.writeText(texto);
    return true;
  } catch {
    const area = document.createElement("textarea");
    area.value = texto; area.style.position = "fixed"; area.style.opacity = "0";
    document.body.appendChild(area); area.select();
    const ok = document.execCommand("copy");
    area.remove();
    return ok;
  }
}

export function BotonCopiar({ texto, children = "Copiar", clase = "boton mini", deshabilitado }:
  { texto: string | (() => string); children?: ReactNode; clase?: string; deshabilitado?: boolean }) {
  const [estado, setEstado] = useState<"" | "ok" | "error">("");
  return (
    <button type="button" className={clase} disabled={deshabilitado}
      onClick={async () => {
        const ok = await copiar(typeof texto === "function" ? texto() : texto);
        setEstado(ok ? "ok" : "error");
        setTimeout(() => setEstado(""), 1800);
      }}>
      {estado === "ok" ? "Copiado ✓" : estado === "error" ? "No se pudo copiar" : children}
    </button>
  );
}

export function descargar(nombre: string, contenido: string, tipo = "text/plain") {
  const url = URL.createObjectURL(new Blob([contenido], { type: `${tipo};charset=utf-8` }));
  const a = document.createElement("a");
  a.href = url; a.download = nombre; a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

// Area de texto que crece con lo que se escribe, para no tener barras de desplazamiento internas.
export function Area({ value, className = "entrada", ...resto }: TextareaHTMLAttributes<HTMLTextAreaElement> & { value: string }) {
  const ref = useRef<HTMLTextAreaElement>(null);
  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    el.style.height = "auto";
    el.style.height = `${el.scrollHeight + 2}px`;
  }, [value]);
  return <textarea ref={ref} className={className} value={value} {...resto} />;
}

export function Campo({ titulo, ayuda, children }: { titulo: string; ayuda?: ReactNode; children: ReactNode }) {
  return (
    <label className="campo">
      <span>{titulo}</span>
      {children}
      {ayuda && <em>{ayuda}</em>}
    </label>
  );
}

export function Medidor({ valor, tono }: { valor: number; tono?: "bien" | "aviso" }) {
  return <div className={`medidor ${tono ?? ""}`}><i style={{ width: `${Math.max(0, Math.min(100, valor))}%` }} /></div>;
}

export function Punto({ tono }: { tono: "bien" | "aviso" | "mal" }) {
  return <span className={`punto ${tono}`} aria-hidden="true">{tono === "bien" ? "✓" : "!"}</span>;
}

export function tonoPuntaje(n: number): "bien" | "aviso" | "mal" {
  return n >= 72 ? "bien" : n >= 55 ? "aviso" : "mal";
}
