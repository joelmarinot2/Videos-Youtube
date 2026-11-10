"use client";

import { AGENTES, IA_CONECTADA, instrucciones, type AgenteId } from "@/lib/agentes";
import type { PerfilCanal, Video } from "@/lib/tipos";
import { Area, BotonCopiar, Campo } from "./ui";

// El agente de cada etapa. Mientras la IA no este conectada, arma las instrucciones completas
// (reglas del agente + voz del canal + datos del video) para pegarlas en Claude.
export function PanelAgente({ id, perfil, video, entrada, notas, alCambiarNotas, abierto }: {
  id: AgenteId; perfil: PerfilCanal; video?: Video; entrada?: string;
  notas?: string; alCambiarNotas?: (t: string) => void; abierto?: boolean;
}) {
  const a = AGENTES[id];
  return (
    <details className="tarjeta agente" open={abierto}>
      <summary>
        <span className="insignia rojo">Agente</span>
        <span><b>{a.nombre}</b> <span className="tenue chico">· {a.queHace}</span></span>
      </summary>
      <div className="pila" style={{ marginTop: 16 }}>
        <div className="fila">
          <BotonCopiar clase="boton" texto={() => instrucciones(id, perfil, video, entrada)}>Copiar instrucciones del agente</BotonCopiar>
          <button type="button" className="boton" disabled title="Se activa cuando conectemos el motor de IA">
            {IA_CONECTADA ? "Generar aquí con IA" : "Generar aquí con IA · sin conectar"}
          </button>
        </div>
        <p className="chico suave">
          Por ahora funciona así: copias las instrucciones, las pegas en una conversación con Claude y traes la respuesta a los
          campos de esta etapa. Las instrucciones ya incluyen la voz del canal y los datos de este video.
        </p>
        {alCambiarNotas && (
          <Campo titulo="Respuesta del agente" ayuda="Opcional: pégala aquí para tenerla a la mano mientras llenas la etapa.">
            <Area value={notas ?? ""} onChange={(e) => alCambiarNotas(e.target.value)} placeholder="Pega aquí lo que respondió el agente…" />
          </Campo>
        )}
      </div>
    </details>
  );
}
