// Puntaje de ganchos. Version en espanol de hookscore.py (yt-script).
// Cinco propiedades de 0 a 100; el veredicto es 60% el promedio y 40% la mas debil,
// porque un gancho con cuatro propiedades fuertes y una muerta pierde gente por la muerta.
//
// ES UNA GUIA, NO UNA PREDICCION: separa bien un gancho malo de uno real, y casi nada
// un exito de un fracaso del mismo creador. Un puntaje bajo es motivo para revisar;
// un puntaje alto no promete nada.

import { FORMULAS } from "./formulas.ts";
import { contar, palabras, rx } from "./texto.ts";

const MULETILLAS = new Set(["básicamente", "realmente", "literalmente", "simplemente", "muy", "pues", "bueno",
  "entonces", "hola", "bienvenidos", "bienvenido", "bienvenidas", "hoy", "video", "vídeo", "suscríbete",
  "canal", "amigos", "chicos", "gente"]);
const VAGAS = new Set(["increíble", "increíbles", "asombroso", "asombrosa", "impresionante", "impactante", "alucinante",
  "loco", "locura", "enorme", "gigantesco", "masivo", "secreto", "secretos", "poderoso", "definitivo", "mejor",
  "revolucionario", "inimaginable", "aterrador", "aterradora", "escalofriante", "terrorífico", "misterioso",
  "misteriosa", "inexplicable", "extraño", "extraña", "sorprendente"]);

const CONCRETO = rx("«(\\d[\\d.,]*\\s?(%|k|m|x)?|\\$\\s?\\d+|\\d+\\s?(segundo|minuto|hora|día|semana|mes|año)s?)»");
// En espanol se le habla al espectador sin pronombre ("¿sabias que...?", "imagina..."),
// asi que tambien cuentan los verbos en segunda persona mas comunes.
const TU = rx("«(tú|tu|tus|te|ti|contigo|usted|ustedes|vos|sabías|sabes|crees|creerías|imagina|imagínate|mira|piensa|recuerdas|conoces|viste|has|vas|puedes|podrías|quieres|verás|escucha|fíjate|eres|estás|tienes)»");
const RIESGO = rx("«(p[ei]erd\\p{L}*|muer\\p{L}*|muri\\p{L}*|mori\\p{L}*|desapare\\p{L}*|desaparic\\p{L}*|fracas\\p{L}*|cuesta\\p{L}*|cost[óo]\\p{L}*|riesgo\\p{L}*|peligro\\p{L}*|nunca|jamás|antes|deja de|dejó de|prohibid\\p{L}*|mortal\\p{L}*|abandon\\p{L}*|hund\\p{L}*|asesin\\p{L}*|v[ií]ctima\\p{L}*|sobreviv\\p{L}*)»");
const CURIOSIDAD = rx("«(por qué|cómo|qué|cuál|hasta|antes|pero|nadie|casi|excepto|salvo|razón|motivo|en realidad|sin embargo)»");
const CERRADO = rx("«(porque|así que|lo que significa|por eso)»");

export interface Panel {
  gancho: string;
  propiedades: { especificidad: number; apelacion: number; riesgo: number; curiosidad: number; brevedad: number };
  veredicto: number;
  banda: "FUERTE" | "ACEPTABLE" | "DÉBIL";
  formula: string;
  coincidencias: number;
  masDebil: keyof Panel["propiedades"];
  arreglo: string;
}

const tope = (n: number) => Math.max(0, Math.min(100, Math.round(n)));

function especificidad(t: string): number {
  const w = palabras(t);
  if (!w.length) return 0;
  const cifras = contar(CONCRETO, t);
  const vagas = w.filter((x) => VAGAS.has(x)).length;
  const muletillas = w.filter((x) => MULETILLAS.has(x)).length;
  // un nombre propio que no abre la frase se lee como algo con nombre
  const propios = t.split(/\s+/).slice(1).filter((x) => /^[¿¡"'(]*\p{Lu}/u.test(x)).length;
  return tope(34 + cifras * 22 - vagas * 16 - muletillas * 5 + Math.min(18, 6 * propios));
}

function apelacion(t: string): number {
  const n = contar(TU, t);
  const alInicio = TU.test(t.split(/\s+/).slice(0, 6).join(" ")) ? 30 : 0;
  return tope(26 + n * 20 + alInicio);
}

function riesgo(t: string): number {
  return tope(22 + contar(RIESGO, t) * 26 + (CONCRETO.test(t) ? 14 : 0));
}

function curiosidad(t: string): number {
  const pregunta = t.trim().endsWith("?") ? 18 : 0;
  // un gancho que se responde solo ya no deja hueco
  const cerrado = CERRADO.test(t) ? -18 : 0;
  return tope(24 + contar(CURIOSIDAD, t) * 17 + pregunta + cerrado);
}

function brevedad(t: string): number {
  const n = palabras(t).length;
  if (n === 0) return 0;
  // de 9 a 24 palabras es lo que cabe dicho en voz alta en unos 10 segundos
  if (n >= 9 && n <= 24) return 100;
  if (n < 9) return Math.max(30, 100 - (9 - n) * 11);
  return Math.max(10, 100 - (n - 24) * 7);
}

export function clasificar(t: string): { nombre: string; coincidencias: number } {
  let mejor = "Sin clasificar", max = 0;
  for (const f of FORMULAS) {
    const n = f.patrones.filter((p) => rx(p).test(t.trim())).length;
    if (n > max) { mejor = f.nombre; max = n; }
  }
  return { nombre: mejor, coincidencias: max };
}

export const ARREGLO: Record<keyof Panel["propiedades"], string> = {
  especificidad: "cambia un adjetivo por una cifra, un nombre o una fecha",
  apelacion: "háblale al espectador (tú, te) en las primeras seis palabras",
  riesgo: "di qué se perdió, quién desapareció o qué está en juego",
  curiosidad: "quita la mitad de la frase que se responde sola",
  brevedad: "de 9 a 24 palabras: léelo en voz alta y corta donde se te acaba el aire",
};

export const NOMBRES: Record<keyof Panel["propiedades"], string> = {
  especificidad: "Especificidad", apelacion: "Apelación", riesgo: "Riesgo",
  curiosidad: "Curiosidad", brevedad: "Brevedad",
};

export function banda(v: number): Panel["banda"] {
  return v >= 72 ? "FUERTE" : v >= 55 ? "ACEPTABLE" : "DÉBIL";
}

export function puntuar(t: string): Panel {
  const propiedades = {
    especificidad: especificidad(t), apelacion: apelacion(t), riesgo: riesgo(t),
    curiosidad: curiosidad(t), brevedad: brevedad(t),
  };
  const vals = Object.values(propiedades);
  const veredicto = Math.round(0.6 * (vals.reduce((a, b) => a + b, 0) / vals.length) + 0.4 * Math.min(...vals));
  const { nombre, coincidencias } = clasificar(t);
  const masDebil = (Object.keys(propiedades) as (keyof Panel["propiedades"])[])
    .reduce((a, b) => (propiedades[b] < propiedades[a] ? b : a));
  return { gancho: t.trim(), propiedades, veredicto, banda: banda(veredicto), formula: nombre,
    coincidencias, masDebil, arreglo: ARREGLO[masDebil] };
}
