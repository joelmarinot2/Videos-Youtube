// Revision del titulo y la miniatura como UNA sola pareja. Version en espanol de title.py (yt-package).
// YouTube corta cerca de 60 caracteres en la busqueda de escritorio y cerca de 40 en el inicio del celular.

import { palabras } from "./texto.ts";

export const ESCRITORIO = 60, CELULAR = 40, MAXIMO = 100, MAX_MINIATURA = 3;

const VAGAS = new Set(["increíble", "increíbles", "impresionante", "impactante", "alucinante", "loco", "enorme",
  "masivo", "definitivo", "mejor", "poderoso", "secreto", "secretos", "revolucionario", "épico", "perfecto",
  "completo", "todo", "aterrador", "escalofriante", "terrorífico", "misterioso", "inexplicable", "sorprendente"]);
const VACIAS = new Set(["el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al", "para", "a", "en",
  "y", "o", "es", "son", "con", "tu", "tus", "mi", "yo", "esto", "este", "esta", "eso", "que", "qué", "cómo",
  "por", "se", "lo", "su", "sus", "no"]);

export interface Problema { clave: string; mensaje: string }
export interface RevisionTitulo {
  titulo: string; caracteres: number; puntaje: number; problemas: Problema[]; aciertos: string[];
}

export function revisarTitulo(titulo: string, miniatura?: string): RevisionTitulo {
  const t = titulo.trim();
  const n = [...t].length;
  const problemas: Problema[] = [], aciertos: string[] = [];
  if (n > MAXIMO) problemas.push({ clave: "largo", mensaje: `${n} caracteres: el límite de YouTube es ${MAXIMO}` });
  else if (n > ESCRITORIO) problemas.push({ clave: "largo", mensaje: `${n} caracteres: la búsqueda en computador corta cerca de ${ESCRITORIO}` });
  else aciertos.push(`${n} caracteres, dentro del corte de ${ESCRITORIO} del computador`);
  if (n > CELULAR) {
    const cabeza = t.slice(0, CELULAR).replace(/\s+\S*$/, "");
    problemas.push({ clave: "celular", mensaje: `en el celular se ve más o menos "${cabeza}…": revisa que el sujeto sobreviva` });
  }
  const mayus = t.split(/\s+/).filter((w) => [...w].length > 2 && /\p{L}/u.test(w) && w === w.toUpperCase());
  if (mayus.length > 2) problemas.push({ clave: "gritos", mensaje: `${mayus.length} palabras en mayúsculas: dos es el tope antes de parecer spam` });
  else if (mayus.length) aciertos.push(`${mayus.length} palabra${mayus.length > 1 ? "s" : ""} en mayúsculas para dar énfasis`);
  const vagas = [...new Set(palabras(t).filter((w) => VAGAS.has(w)))].sort();
  if (vagas.length) problemas.push({ clave: "vago", mensaje: `${vagas.join(", ")}: cámbialo por una cifra, un nombre o una fecha` });
  const cifras = t.match(/\d[\d,.]*%?/g);
  if (cifras) aciertos.push(`lleva un dato concreto (${cifras.slice(0, 3).join(", ")})`);
  else problemas.push({ clave: "sin-cifra", mensaje: "no tiene cifra ni fecha: es el arreglo más confiable que existe" });
  if (t.endsWith("?")) aciertos.push("pregunta abierta en el título");
  const frente = palabras(t).slice(0, 3).filter((w) => !VACIAS.has(w));
  if (palabras(t).length && !frente.length) problemas.push({ clave: "arranque", mensaje: "las tres primeras palabras son relleno: trae el sujeto al frente" });
  if (miniatura && miniatura.trim()) {
    const pt = new Set(palabras(t).filter((w) => !VACIAS.has(w)));
    const repetidas = [...new Set(palabras(miniatura).filter((w) => !VACIAS.has(w) && pt.has(w)))].sort();
    if (repetidas.length) problemas.push({ clave: "repetido", mensaje: `la miniatura repite el título en: ${repetidas.join(", ")}. La miniatura debe decir lo que el título no dice` });
    else aciertos.push("miniatura y título usan palabras distintas");
    const pm = palabras(miniatura).length;
    if (pm > MAX_MINIATURA) problemas.push({ clave: "miniatura-larga", mensaje: `${pm} palabras en la miniatura: ${MAX_MINIATURA} es el tope al tamaño en que se ve` });
  }
  const puntaje = Math.max(0, Math.min(100, 100 - 14 * problemas.length + 4 * aciertos.length));
  return { titulo: t, caracteres: n, puntaje, problemas, aciertos };
}
