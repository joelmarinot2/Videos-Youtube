// Tipos de datos del panel. Todo lo de un video vive en un solo objeto,
// que se guarda en Supabase (columna "datos") o en el navegador en modo demostracion.

export type EtapaId =
  | "idea" | "guion" | "refinar" | "titulo" | "seo" | "capitulos" | "shorts" | "exportar";

export const ETAPAS: { id: EtapaId; nombre: string; resumen: string }[] = [
  { id: "idea", nombre: "Idea", resumen: "El caso y lo que promete" },
  { id: "guion", nombre: "Guion", resumen: "Ganchos y bloques" },
  { id: "refinar", nombre: "Refinar", resumen: "Revisión bloque por bloque" },
  { id: "titulo", nombre: "Título y miniatura", resumen: "Un solo paquete" },
  { id: "seo", nombre: "Descripción", resumen: "Texto, etiquetas y búsquedas" },
  { id: "capitulos", nombre: "Capítulos", resumen: "Marcas de tiempo válidas" },
  { id: "shorts", nombre: "Shorts", resumen: "Momentos que viven solos" },
  { id: "exportar", nombre: "Exportar", resumen: "Listo para el creador de videos" },
];

export type TipoBloque = "gancho" | "giro" | "cuerpo" | "revelacion" | "cierre";

export interface Bloque {
  id: string;
  tipo: TipoBloque;
  titulo: string;
  narracion: string;
  enPantalla: string;
}

export interface Short {
  id: string;
  bloqueId: string;
  texto: string;
  primeraLinea: string;
  textoPantalla: string;
  bucle: string;
}

export interface Video {
  id: string;
  titulo: string;
  creado: string;
  actualizado: string;
  aprobadas: Partial<Record<EtapaId, boolean>>;
  idea: { tema: string; promesa: string; duracionMin: number; ppm: number; fuentes: string; notas: string };
  ganchos: string[];
  ganchoElegido: number | null;
  bloques: Bloque[];
  revision: Record<string, boolean>;
  titulos: string[];
  tituloElegido: number | null;
  miniaturaTexto: string;
  miniaturaBrief: string;
  seo: { primerasLineas: string; descripcion: string; etiquetas: string; consultas: string[] };
  capitulos: Record<string, { titulo: string; incluir: boolean }>;
  shorts: Short[];
  notasAgente: Partial<Record<string, string>>;
}

export interface PerfilCanal {
  audiencia: string;
  comoHablo: string;
  nuncaUso: string;
  siUso: string;
  noAfirmo: string;
  formato: string;
}

export const PERFIL_VACIO: PerfilCanal = {
  audiencia: "", comoHablo: "", nuncaUso: "", siUso: "", noAfirmo: "", formato: "",
};

export function nuevoId(): string {
  if (typeof crypto !== "undefined" && "randomUUID" in crypto) return crypto.randomUUID();
  return "id-" + Math.random().toString(36).slice(2) + Date.now().toString(36);
}

export function bloque(tipo: TipoBloque, titulo: string): Bloque {
  return { id: nuevoId(), tipo, titulo, narracion: "", enPantalla: "" };
}

export function videoNuevo(titulo: string): Video {
  const ahora = new Date().toISOString();
  return {
    id: nuevoId(),
    titulo,
    creado: ahora,
    actualizado: ahora,
    aprobadas: {},
    idea: { tema: "", promesa: "", duracionMin: 10, ppm: 150, fuentes: "", notas: "" },
    ganchos: ["", "", "", "", ""],
    ganchoElegido: null,
    bloques: [
      bloque("gancho", "Gancho"),
      bloque("giro", "El giro"),
      bloque("cuerpo", "Los hechos"),
      bloque("cuerpo", "Lo que no encaja"),
      bloque("cuerpo", "Las teorías"),
      bloque("revelacion", "La revelación"),
      bloque("cierre", "Cierre"),
    ],
    revision: {},
    titulos: ["", "", ""],
    tituloElegido: null,
    miniaturaTexto: "",
    miniaturaBrief: "",
    seo: { primerasLineas: "", descripcion: "", etiquetas: "", consultas: ["", "", ""] },
    capitulos: {},
    shorts: [],
    notasAgente: {},
  };
}

// Rellena campos que falten en videos guardados con una version anterior del panel.
export function normalizar(v: Partial<Video> & { id: string }): Video {
  const base = videoNuevo(v.titulo ?? "Sin título");
  return {
    ...base, ...v,
    idea: { ...base.idea, ...(v.idea ?? {}) },
    seo: { ...base.seo, ...(v.seo ?? {}) },
    bloques: v.bloques?.length ? v.bloques : base.bloques,
  } as Video;
}

export function etapaActual(v: Video): EtapaId {
  for (const e of ETAPAS) if (!v.aprobadas[e.id]) return e.id;
  return "exportar";
}

export function desbloqueada(v: Video, id: EtapaId): boolean {
  for (const e of ETAPAS) {
    if (e.id === id) return true;
    if (!v.aprobadas[e.id]) return false;
  }
  return false;
}
