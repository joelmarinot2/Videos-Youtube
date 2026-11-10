"use client";

import type { ReactNode } from "react";
import { ETAPAS, type EtapaId, type PerfilCanal, type Video } from "@/lib/tipos";

export interface PropsEtapa {
  v: Video;
  cambiar: (mutar: (borrador: Video) => void) => void;
  perfil: PerfilCanal;
}

export function Encabezado({ id, children }: { id: EtapaId; children: ReactNode }) {
  const i = ETAPAS.findIndex((e) => e.id === id);
  return (
    <header style={{ marginBottom: 18 }}>
      <p className="sobretitulo">Etapa {i + 1} de {ETAPAS.length}</p>
      <h2 style={{ fontSize: "1.6rem" }}>{ETAPAS[i].nombre}</h2>
      <p className="bajada">{children}</p>
    </header>
  );
}

// Barra de aprobacion: nada avanza hasta que el dueño del canal lo aprueba.
export function Aprobacion({ id, v, cambiar, faltan, avisos = 0, alAprobar }: {
  id: EtapaId; v: Video; cambiar: PropsEtapa["cambiar"]; faltan: string[]; avisos?: number; alAprobar: () => void;
}) {
  const aprobada = !!v.aprobadas[id];
  const ultima = id === "exportar";
  return (
    <div className="tarjeta aprobacion fila entre">
      <div className="crece">
        {aprobada ? (
          <p><span className="insignia bien">Aprobada</span> <span className="suave chico">Puedes reabrirla si necesitas cambiar algo.</span></p>
        ) : faltan.length ? (
          <p className="chico"><b style={{ color: "var(--aviso)" }}>Para aprobar falta:</b> <span className="suave">{faltan.join(" · ")}</span></p>
        ) : (
          <p className="chico suave">
            {avisos ? `Hay ${avisos} aviso${avisos === 1 ? "" : "s"} sin resolver. Puedes aprobar de todos modos: tú decides.` : "Todo listo. Revisa y aprueba para continuar."}
          </p>
        )}
      </div>
      {aprobada ? (
        <button type="button" className="boton" onClick={() => cambiar((b) => { b.aprobadas[id] = false; })}>Reabrir etapa</button>
      ) : (
        <button type="button" className="boton primario" disabled={faltan.length > 0}
          onClick={() => { cambiar((b) => { b.aprobadas[id] = true; }); alAprobar(); }}>
          {ultima ? "Marcar video como terminado" : avisos ? "Aprobar con avisos y continuar" : "Aprobar y continuar"}
        </button>
      )}
    </div>
  );
}
