"use client";

import { Area, Campo } from "../ui";
import { Aprobacion, Encabezado, type PropsEtapa } from "./comun";

export function EtapaIdea({ v, cambiar, alAprobar }: PropsEtapa & { alAprobar: () => void }) {
  const faltan = [!v.idea.tema.trim() && "describir el caso", !v.idea.promesa.trim() && "escribir la promesa"].filter(Boolean) as string[];
  const numero = (texto: string, min: number, max: number) => Math.max(min, Math.min(max, Math.round(Number(texto) || min)));
  return (
    <>
      <Encabezado id="idea">
        Antes de escribir una sola línea: qué caso es, qué le promete al espectador y qué datos tienes comprobados.
        Todo lo demás sale de aquí.
      </Encabezado>
      <div className="tarjeta pila">
        <Campo titulo="El caso" ayuda="Qué pasó, dónde y cuándo, en dos o tres frases.">
          <Area value={v.idea.tema} placeholder="Ej.: En 1872 apareció un barco navegando solo en el Atlántico…"
            onChange={(e) => cambiar((b) => { b.idea.tema = e.target.value; })} />
        </Campo>
        <Campo titulo="La promesa" ayuda="Una sola frase: qué va a saber el espectador al final que no sabía al empezar.">
          <Area value={v.idea.promesa} placeholder="Ej.: Vas a ver la única explicación que encaja con la bitácora."
            onChange={(e) => cambiar((b) => { b.idea.promesa = e.target.value; })} />
        </Campo>
        <div className="dos">
          <Campo titulo="Duración meta (minutos)" ayuda={`Unas ${v.idea.duracionMin * v.idea.ppm} palabras de narración.`}>
            <input className="entrada" type="number" min={1} max={120} value={v.idea.duracionMin}
              onChange={(e) => cambiar((b) => { b.idea.duracionMin = numero(e.target.value, 1, 120); })} />
          </Campo>
          <Campo titulo="Palabras por minuto de la voz" ayuda="150 es lo normal. Ajústalo cuando sepas a qué ritmo habla la voz de tu creador de videos.">
            <input className="entrada" type="number" min={90} max={220} value={v.idea.ppm}
              onChange={(e) => cambiar((b) => { b.idea.ppm = numero(e.target.value, 90, 220); })} />
          </Campo>
        </div>
        <Campo titulo="Datos y fuentes comprobados"
          ayuda="Cifras, fechas, nombres y de dónde salen. Los agentes tienen orden de usar solo lo que escribas aquí y de no inventar nada.">
          <Area value={v.idea.fuentes} placeholder={"Ej.: 5 de diciembre de 1872 — fecha del hallazgo (informe del tribunal de Gibraltar)\n10 personas a bordo…"}
            onChange={(e) => cambiar((b) => { b.idea.fuentes = e.target.value; })} />
        </Campo>
        <Campo titulo="Notas" ayuda="Tono, cosas que quieres evitar, ideas sueltas.">
          <Area value={v.idea.notas} onChange={(e) => cambiar((b) => { b.idea.notas = e.target.value; })} />
        </Campo>
      </div>
      <Aprobacion id="idea" v={v} cambiar={cambiar} faltan={faltan} alAprobar={alAprobar} />
    </>
  );
}
