"use client";

import { NOMBRES, puntuar, type Panel } from "@/lib/gancho";
import { Medidor, tonoPuntaje } from "./ui";

export function PanelGancho({ texto, compacto }: { texto: string; compacto?: boolean }) {
  if (!texto.trim()) return <p className="tenue chico">Escribe el gancho para ver su puntaje.</p>;
  const p = puntuar(texto);
  const tono = tonoPuntaje(p.veredicto);
  return (
    <div className="fila arriba" style={{ gap: 18 }}>
      <div style={{ textAlign: "center" }}>
        <div className={`puntaje ${tono}`}>{p.veredicto}</div>
        <span className={`insignia ${tono}`} style={{ marginTop: 6 }}>{p.banda}</span>
      </div>
      <div className="crece">
        {!compacto && (
          <div className="barras" style={{ marginBottom: 10 }}>
            {(Object.keys(p.propiedades) as (keyof Panel["propiedades"])[]).map((k) => (
              <Fila key={k} nombre={NOMBRES[k]} valor={p.propiedades[k]} debil={k === p.masDebil} />
            ))}
          </div>
        )}
        <p className="chico suave">
          <b style={{ color: "var(--texto)" }}>Fórmula:</b>{" "}
          {p.coincidencias ? p.formula : "ninguna reconocida (suele ser un resumen, no un gancho)"}
        </p>
        <p className="chico suave"><b style={{ color: "var(--texto)" }}>Para subirlo:</b> {p.arreglo}.</p>
      </div>
    </div>
  );
}

function Fila({ nombre, valor, debil }: { nombre: string; valor: number; debil: boolean }) {
  return (
    <>
      <span style={debil ? { color: "var(--rojo-vivo)" } : undefined}>{nombre}</span>
      <Medidor valor={valor} tono={valor >= 72 ? "bien" : valor >= 55 ? "aviso" : undefined} />
      <span className="mono">{valor}</span>
    </>
  );
}
