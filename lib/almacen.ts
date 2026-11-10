// Guardado de datos. Con Supabase configurado usa la base de datos (cada fila pertenece
// a quien inicio sesion). Sin Supabase usa el almacenamiento del navegador, solo para probar.

import { supabase } from "./supabase.ts";
import { normalizar, PERFIL_VACIO, type PerfilCanal, type Video } from "./tipos.ts";

const CLAVE_VIDEOS = "ai:videos", CLAVE_PERFIL = "ai:perfil";

function leerLocal<T>(clave: string, porDefecto: T): T {
  try {
    const crudo = localStorage.getItem(clave);
    return crudo ? (JSON.parse(crudo) as T) : porDefecto;
  } catch { return porDefecto; }
}

function escribirLocal(clave: string, valor: unknown) {
  try { localStorage.setItem(clave, JSON.stringify(valor)); } catch { /* sin espacio o bloqueado */ }
}

function fallar(error: { message: string } | null) {
  if (error) throw new Error(error.message);
}

export async function listarVideos(): Promise<Video[]> {
  if (!supabase) {
    return leerLocal<Video[]>(CLAVE_VIDEOS, []).map(normalizar)
      .sort((a, b) => b.actualizado.localeCompare(a.actualizado));
  }
  const { data, error } = await supabase.from("videos").select("id, datos").order("actualizado", { ascending: false });
  fallar(error);
  return (data ?? []).map((f) => normalizar({ ...(f.datos as Video), id: f.id }));
}

export async function obtenerVideo(id: string): Promise<Video | null> {
  if (!supabase) return (await listarVideos()).find((v) => v.id === id) ?? null;
  const { data, error } = await supabase.from("videos").select("id, datos").eq("id", id).maybeSingle();
  fallar(error);
  return data ? normalizar({ ...(data.datos as Video), id: data.id }) : null;
}

export async function guardarVideo(v: Video): Promise<void> {
  const video = { ...v, actualizado: new Date().toISOString() };
  if (!supabase) {
    const todos = leerLocal<Video[]>(CLAVE_VIDEOS, []).filter((x) => x.id !== video.id);
    escribirLocal(CLAVE_VIDEOS, [video, ...todos]);
    return;
  }
  const { error } = await supabase.from("videos")
    .upsert({ id: video.id, titulo: video.titulo, datos: video, actualizado: video.actualizado });
  fallar(error);
}

export async function eliminarVideo(id: string): Promise<void> {
  if (!supabase) {
    escribirLocal(CLAVE_VIDEOS, leerLocal<Video[]>(CLAVE_VIDEOS, []).filter((x) => x.id !== id));
    return;
  }
  const { error } = await supabase.from("videos").delete().eq("id", id);
  fallar(error);
}

export async function obtenerPerfil(): Promise<PerfilCanal> {
  if (!supabase) return { ...PERFIL_VACIO, ...leerLocal<Partial<PerfilCanal>>(CLAVE_PERFIL, {}) };
  const { data, error } = await supabase.from("perfil_canal").select("datos").maybeSingle();
  fallar(error);
  return { ...PERFIL_VACIO, ...((data?.datos as Partial<PerfilCanal>) ?? {}) };
}

export async function guardarPerfil(p: PerfilCanal): Promise<void> {
  if (!supabase) { escribirLocal(CLAVE_PERFIL, p); return; }
  const { data: sesion } = await supabase.auth.getUser();
  if (!sesion.user) throw new Error("La sesión se cerró. Vuelve a entrar.");
  const { error } = await supabase.from("perfil_canal")
    .upsert({ user_id: sesion.user.id, datos: p, actualizado: new Date().toISOString() });
  fallar(error);
}
