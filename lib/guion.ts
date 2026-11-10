// Calculos sobre el guion: tiempos, revision automatica, capitulos, Shorts y exportacion.

import { puntuar } from "./gancho.ts";
import { marca, palabras, contarPalabras, segundosDe, rx, contar } from "./texto.ts";
import type { Bloque, Short, Video } from "./tipos.ts";

export const NOMBRE_TIPO: Record<Bloque["tipo"], string> = {
  gancho: "Gancho", giro: "El giro", cuerpo: "Desarrollo", revelacion: "La revelación", cierre: "Cierre",
};

export const AYUDA_TIPO: Record<Bloque["tipo"], string> = {
  gancho: "Los primeros 15 segundos. Confirma el título, abre una pregunta que no se pueda cerrar y prueba que la respuesta existe.",
  giro: "De 0:15 a 0:45. Di en una frase qué va a hacer el video y empieza a hacerlo. Sin saludo, sin presentación del canal, sin pedir suscripción.",
  cuerpo: "Una sola idea por bloque. Si no puedes nombrarlo en cinco palabras, son dos bloques o es relleno.",
  revelacion: "Entrega lo que prometió el gancho, de forma explícita, y di que lo estás entregando.",
  cierre: "Un solo pedido. No tres.",
};

export interface Tiempo { bloque: Bloque; palabras: number; segundos: number; inicio: number }

export function tiempos(v: Video): Tiempo[] {
  let inicio = 0;
  return v.bloques.map((bloque) => {
    const segundos = segundosDe(bloque.narracion, v.idea.ppm);
    const fila = { bloque, palabras: contarPalabras(bloque.narracion), segundos, inicio };
    inicio += segundos;
    return fila;
  });
}

export function duracionTotal(v: Video): number {
  return tiempos(v).reduce((a, t) => a + t.segundos, 0);
}

export function ganchoElegido(v: Video): string {
  return v.ganchoElegido === null ? "" : (v.ganchos[v.ganchoElegido] ?? "").trim();
}

// ---------- Revision automatica (etapa Refinar) ----------

const SALUDO = rx("«(bienvenid[oa]s?|hola a todos|hola amigos|suscr[ií]b\\p{L}*|antes de (empezar|comenzar)|dale (a )?like|en este canal|mi nombre es)»");
const PEDIDO = rx("«(suscr[ií]b\\p{L}*|coment\\p{L}*|like|me gusta|compart\\p{L}*|campan\\p{L}*|s[ií]gue(me|nos)|activa\\p{L}*)»");
const MULETILLA = rx("«(básicamente|literalmente|realmente|simplemente|o sea|digamos|la verdad es que|como tal|de alguna manera|un poco)»");

export interface Chequeo { id: string; nombre: string; bien: boolean; detalle: string }

export function revisionAutomatica(v: Video): Chequeo[] {
  const ts = tiempos(v);
  const conTexto = v.bloques.filter((b) => b.narracion.trim());
  const g = ganchoElegido(v);
  const panel = g ? puntuar(g) : null;
  const apertura = v.bloques.filter((b) => b.tipo === "gancho" || b.tipo === "giro").map((b) => b.narracion).join(" ");
  const saludo = apertura.match(SALUDO)?.[0];
  const sinImagen = conTexto.filter((b) => !b.enPantalla.trim());
  const vacios = v.bloques.filter((b) => !b.narracion.trim());
  const total = ts.reduce((a, t) => a + t.segundos, 0);
  const meta = v.idea.duracionMin * 60;
  const desvio = meta ? Math.abs(total - meta) / meta : 0;
  const cierre = v.bloques.filter((b) => b.tipo === "cierre").map((b) => b.narracion).join(" ");
  const pedidos = contar(PEDIDO, cierre);
  return [
    { id: "gancho", nombre: "El gancho pasa de 55 puntos", bien: !!panel && panel.veredicto >= 55,
      detalle: panel ? `${panel.veredicto} puntos (${panel.banda}). Lo más flojo: ${panel.arreglo}.` : "Todavía no has elegido un gancho en la etapa Guion." },
    { id: "saludo", nombre: "La apertura no saluda ni presenta el canal", bien: !saludo,
      detalle: saludo ? `Aparece "${saludo}" en los primeros 45 segundos: es la causa más común de que la gente se vaya en el segundo 30.` : "Sin saludo, sin presentación y sin pedir suscripción al inicio." },
    { id: "pantalla", nombre: "Cada bloque dice qué se ve en pantalla", bien: conTexto.length > 0 && sinImagen.length === 0,
      detalle: sinImagen.length ? `Falta en: ${sinImagen.map((b) => b.titulo).join(", ")}. El creador de videos necesita saber qué mostrar.` : conTexto.length ? "Todos los bloques tienen su indicación visual." : "Aún no hay bloques escritos." },
    { id: "vacios", nombre: "No quedan bloques vacíos", bien: vacios.length === 0,
      detalle: vacios.length ? `Vacíos: ${vacios.map((b) => b.titulo).join(", ")}. Escríbelos o elimínalos.` : "Todos los bloques tienen narración." },
    { id: "duracion", nombre: "La duración se acerca a la meta", bien: total > 0 && desvio <= 0.15,
      detalle: `Va en ${marca(total)} y la meta es ${marca(meta)} (${Math.round(desvio * 100)}% de diferencia; se acepta hasta 15%).` },
    { id: "cierre", nombre: "El cierre hace un solo pedido", bien: pedidos <= 1,
      detalle: pedidos > 1 ? `El cierre pide ${pedidos} cosas. Deja una sola.` : pedidos === 1 ? "Un solo pedido." : "Sin pedidos en el cierre (está bien; si pides algo, que sea una sola cosa)." },
  ];
}

export const REVISION_MANUAL: { id: string; texto: string }[] = [
  { id: "datos", texto: "Cada cifra, fecha y nombre del guion tiene fuente. Nada es inventado." },
  { id: "promesa", texto: "La revelación entrega exactamente lo que prometió el gancho, y lo dice." },
  { id: "voz", texto: "Lo leí en voz alta y suena como el canal." },
];

export function diagnosticoBloque(b: Bloque, ppm: number) {
  return {
    palabras: contarPalabras(b.narracion),
    segundos: segundosDe(b.narracion, ppm),
    muletillas: [...new Set((b.narracion.match(new RegExp(MULETILLA.source, "giu")) ?? []).map((m) => m.toLowerCase()))],
    sinImagen: !!b.narracion.trim() && !b.enPantalla.trim(),
  };
}

// ---------- Capitulos ----------
// Reglas de YouTube: el primero en 00:00, minimo tres, y cada uno de al menos 10 segundos.
// Si se rompe una, la lista no se convierte en capitulos y nadie avisa.

export interface Capitulo { bloqueId: string; inicio: number; etiqueta: string; titulo: string; segundos: number }

export function capitulosDe(v: Video): { lista: Capitulo[]; valido: boolean; errores: string[] } {
  const lista: Capitulo[] = [];
  for (const t of tiempos(v)) {
    const cfg = v.capitulos[t.bloque.id];
    const incluir = lista.length === 0 || (cfg?.incluir ?? true);
    if (incluir) {
      lista.push({ bloqueId: t.bloque.id, inicio: t.inicio, etiqueta: marca(t.inicio),
        titulo: (cfg?.titulo ?? t.bloque.titulo).trim(), segundos: t.segundos });
    } else {
      lista[lista.length - 1].segundos += t.segundos;
    }
  }
  const errores: string[] = [];
  if (lista.length < 3) errores.push(`Hay ${lista.length} capítulo${lista.length === 1 ? "" : "s"}: YouTube exige al menos 3.`);
  if (lista.length && lista[0].segundos < 10) errores.push(`El primer capítulo («${lista[0].titulo || "00:00"}») dura menos de 10 segundos. Une el bloque siguiente a él.`);
  const cortos = lista.slice(1).filter((c) => c.segundos < 10);
  if (cortos.length) errores.push(`Duran menos de 10 segundos: ${cortos.map((c) => c.titulo || c.etiqueta).join(", ")}. Únelos al anterior.`);
  const sinTitulo = lista.filter((c) => !c.titulo);
  if (sinTitulo.length) errores.push(`${sinTitulo.length} capítulo${sinTitulo.length === 1 ? "" : "s"} sin título.`);
  return { lista, valido: errores.length === 0, errores };
}

export function avisosCapitulo(c: Capitulo): string[] {
  const n = contarPalabras(c.titulo);
  return n > 5 ? [`${n} palabras: lo ideal es de 3 a 5. Si no cabe en cinco, son dos secciones o es relleno.`] : [];
}

export function textoCapitulos(v: Video): string {
  return capitulosDe(v).lista.map((c) => `${c.etiqueta === "0:00" ? "00:00" : c.etiqueta} ${c.titulo}`).join("\n");
}

// ---------- Shorts ----------
// Un Short no es el mejor momento: es un momento que sobrevive sin el video alrededor.

export const SHORT_MIN = 20, SHORT_MAX = 55;
const GIRO = rx("«(pero|sin embargo|hasta que|excepto|aunque|en realidad|y sin embargo|lo extraño es|el problema es)»");
const DEPENDE = rx("^(y|pero|entonces|además|por eso|así que|también|luego|después|esto|eso|él|ella|ellos|ellas|como dijimos|como vimos)»");

export interface Candidato { bloque: Bloque; segundos: number; puntaje: number; motivos: string[]; avisos: string[] }

export function candidatosShort(v: Video): Candidato[] {
  return tiempos(v)
    .filter((t) => t.bloque.narracion.trim())
    .map((t) => {
      const texto = t.bloque.narracion.trim();
      const motivos: string[] = [], avisos: string[] = [];
      let puntaje = 0;
      if (t.segundos >= SHORT_MIN && t.segundos <= SHORT_MAX) { puntaje += 40; motivos.push(`dura ${Math.round(t.segundos)} s, dentro de ${SHORT_MIN} a ${SHORT_MAX}`); }
      else if (t.segundos > SHORT_MAX) { puntaje += 15; avisos.push(`dura ${Math.round(t.segundos)} s: habrá que recortarlo a ${SHORT_MAX} o menos`); }
      else avisos.push(`dura ${Math.round(t.segundos)} s: es muy corto para sostenerse solo`);
      if (!DEPENDE.test(texto)) { puntaje += 20; motivos.push("abre con una idea completa"); }
      else avisos.push("la primera frase depende de lo anterior");
      if (GIRO.test(texto)) { puntaje += 25; motivos.push("tiene un giro: afirma algo y luego lo complica"); }
      else avisos.push("no se ve un giro (pero, sin embargo, hasta que…)");
      if (/[.!?…]["»)]?$/.test(texto)) { puntaje += 15; motivos.push("termina en una frase cerrada"); }
      else avisos.push("termina a medias");
      return { bloque: t.bloque, segundos: t.segundos, puntaje, motivos, avisos };
    })
    .sort((a, b) => b.puntaje - a.puntaje);
}

export function textoShort(s: Short): string {
  return [s.primeraLinea.trim(), s.texto.trim()].filter(Boolean).join(" ");
}

export function revisarShort(s: Short, ppm: number): { segundos: number; avisos: string[] } {
  const segundos = segundosDe(textoShort(s), ppm);
  const avisos: string[] = [];
  if (!s.primeraLinea.trim()) avisos.push("Falta la primera línea nueva: la del video largo da por sabido un contexto que aquí no existe.");
  if (segundos < SHORT_MIN) avisos.push(`Dura ${Math.round(segundos)} s: menos de ${SHORT_MIN} no alcanza a tener un giro.`);
  if (segundos > SHORT_MAX) avisos.push(`Dura ${Math.round(segundos)} s: recorta hasta ${SHORT_MAX} o menos.`);
  if (s.textoPantalla.trim() && s.primeraLinea.trim()) {
    const dichas = new Set(palabras(s.primeraLinea).filter((w) => w.length > 3));
    const repetidas = [...new Set(palabras(s.textoPantalla).filter((w) => dichas.has(w)))];
    if (repetidas.length) avisos.push(`El texto en pantalla repite lo que se dice (${repetidas.join(", ")}): usa otras palabras.`);
  }
  if (!s.textoPantalla.trim()) avisos.push("Falta el texto en pantalla de los dos primeros segundos.");
  if (!s.bucle.trim()) avisos.push("Falta el punto de bucle: qué deja abierto la última frase para que la primera lo responda.");
  return { segundos, avisos };
}

// ---------- Busquedas (etapa Descripcion) ----------

const VACIAS = new Set(["el", "la", "los", "las", "un", "una", "de", "del", "al", "para", "a", "en", "y", "o", "es",
  "con", "que", "qué", "por", "se", "lo", "su", "como", "cómo"]);

export function revisarConsulta(consulta: string, titulo: string, primerasLineas: string): string[] {
  const donde = new Set(palabras(`${titulo} ${primerasLineas}`));
  return [...new Set(palabras(consulta).filter((w) => !VACIAS.has(w) && !donde.has(w)))];
}

export function listaEtiquetas(texto: string): string[] {
  return texto.split(/[,\n]/).map((e) => e.trim()).filter(Boolean);
}

// ---------- Exportacion ----------

export function tituloFinal(v: Video): string {
  return v.tituloElegido === null ? "" : (v.titulos[v.tituloElegido] ?? "").trim();
}

export function exportarNarracion(v: Video): string {
  return v.bloques.map((b) => b.narracion.trim()).filter(Boolean).join("\n\n");
}

export function exportarEscenas(v: Video): string {
  return tiempos(v)
    .filter((t) => t.bloque.narracion.trim())
    .map((t, i) => [
      `ESCENA ${i + 1} · ${t.bloque.titulo.toUpperCase()} · ${marca(t.inicio)} · ${Math.round(t.segundos)} s`,
      "NARRACIÓN:", t.bloque.narracion.trim(),
      "EN PANTALLA:", t.bloque.enPantalla.trim() || "(sin indicación)",
    ].join("\n"))
    .join("\n\n---\n\n");
}

export function descripcionCompleta(v: Video): string {
  const caps = capitulosDe(v);
  return [v.seo.primerasLineas.trim(), caps.valido ? textoCapitulos(v) : "", v.seo.descripcion.trim()]
    .filter(Boolean).join("\n\n");
}

export function exportarJSON(v: Video) {
  return {
    canal: "Archivos Inexplicables",
    version: 1,
    titulo: tituloFinal(v) || v.titulo,
    miniatura: { texto: v.miniaturaTexto.trim(), indicaciones: v.miniaturaBrief.trim() },
    palabrasPorMinuto: v.idea.ppm,
    duracionSegundos: Math.round(duracionTotal(v)),
    escenas: tiempos(v).filter((t) => t.bloque.narracion.trim()).map((t, i) => ({
      numero: i + 1, tipo: t.bloque.tipo, titulo: t.bloque.titulo,
      inicioSegundos: Math.round(t.inicio), duracionSegundos: Math.round(t.segundos),
      narracion: t.bloque.narracion.trim(), enPantalla: t.bloque.enPantalla.trim(),
    })),
    descripcion: descripcionCompleta(v),
    etiquetas: listaEtiquetas(v.seo.etiquetas),
    capitulos: capitulosDe(v).lista.map((c) => ({ inicioSegundos: Math.round(c.inicio), marca: c.etiqueta, titulo: c.titulo })),
    shorts: v.shorts.map((s, i) => ({
      numero: i + 1, narracion: textoShort(s), textoEnPantalla: s.textoPantalla.trim(), bucle: s.bucle.trim(),
      duracionSegundos: Math.round(segundosDe(textoShort(s), v.idea.ppm)),
    })),
  };
}
