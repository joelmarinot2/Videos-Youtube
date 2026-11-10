// Utilidades de texto compartidas. JavaScript no reconoce las tildes como parte
// de una palabra con \b, asi que se usan limites propios: « inicio y » fin de palabra.

const INI = "(?<![\\p{L}\\p{N}])";
const FIN = "(?![\\p{L}\\p{N}])";

export function rx(fuente: string, banderas = "iu"): RegExp {
  return new RegExp(fuente.replaceAll("«", INI).replaceAll("»", FIN), banderas);
}

export function palabras(t: string): string[] {
  return t.toLowerCase().match(/[\p{L}\p{N}'%$]+/gu) ?? [];
}

export function contarPalabras(t: string): number {
  return palabras(t).length;
}

export function segundosDe(texto: string, ppm = 150): number {
  return (contarPalabras(texto) / (ppm || 150)) * 60;
}

export function marca(seg: number): string {
  const t = Math.floor(seg);
  const h = Math.floor(t / 3600), m = Math.floor((t % 3600) / 60), s = t % 60;
  const ss = String(s).padStart(2, "0");
  return h ? `${h}:${String(m).padStart(2, "0")}:${ss}` : `${m}:${ss}`;
}

export function contar(re: RegExp, t: string): number {
  const g = new RegExp(re.source, re.flags.includes("g") ? re.flags : re.flags + "g");
  return (t.match(g) ?? []).length;
}

export function primeraOracion(t: string): string {
  const limpio = t.trim();
  const m = limpio.match(/^[\s\S]*?[.!?…](?=\s|$)/);
  return (m ? m[0] : limpio).trim();
}
