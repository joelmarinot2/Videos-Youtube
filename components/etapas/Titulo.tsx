"use client";

import { CELULAR, ESCRITORIO, MAX_MINIATURA, revisarTitulo } from "@/lib/titulo";
import { contarPalabras } from "@/lib/texto";
import { PanelAgente } from "../PanelAgente";
import { Area, Campo, Punto, tonoPuntaje } from "../ui";
import { Aprobacion, Encabezado, type PropsEtapa } from "./comun";

const cortar = (t: string, n: number) => ([...t].length > n ? [...t].slice(0, n).join("").replace(/\s+\S*$/, "") + "…" : t);

export function EtapaTitulo({ v, cambiar, perfil, alAprobar }: PropsEtapa & { alAprobar: () => void }) {
  const revisados = v.titulos.map((t, i) => ({ i, t, r: t.trim() ? revisarTitulo(t, v.miniaturaTexto) : null }));
  const mejor = revisados.filter((x) => x.r).sort((a, b) => b.r!.puntaje - a.r!.puntaje)[0]?.i ?? -1;
  const elegido = v.tituloElegido !== null ? v.titulos[v.tituloElegido]?.trim() ?? "" : "";
  const revisionElegido = elegido ? revisarTitulo(elegido, v.miniaturaTexto) : null;
  const palabrasMini = contarPalabras(v.miniaturaTexto);
  const faltan = [!elegido && "elegir un título", !v.miniaturaTexto.trim() && "escribir el texto de la miniatura"].filter(Boolean) as string[];

  function pegarLista() {
    const texto = prompt("Pega aquí la lista de títulos del agente, uno por línea:");
    if (!texto) return;
    const nuevos = texto.split("\n").map((l) => l.replace(/^\s*(\d+[.)-]|[-*•])\s*/, "").replace(/^["«“]|["»”]$/g, "").trim()).filter(Boolean);
    if (!nuevos.length) return;
    cambiar((b) => {
      const actuales = b.titulos.filter((t) => t.trim());
      b.titulos = [...actuales, ...nuevos].slice(0, 12);
      if (b.tituloElegido !== null && b.tituloElegido >= actuales.length) b.tituloElegido = null;
    });
  }

  return (
    <>
      <Encabezado id="titulo">
        El título y la miniatura son una sola pieza: si dicen lo mismo, la mitad del espacio se desperdicia. Escribe
        varios títulos; el panel los califica contra el texto de la miniatura mientras escribes.
      </Encabezado>

      <PanelAgente id="titulo" perfil={perfil} video={v} notas={v.notasAgente.titulo}
        alCambiarNotas={(t) => cambiar((b) => { b.notasAgente.titulo = t; })} />

      <section className="tarjeta" style={{ marginTop: 16 }}>
        <h3>Miniatura</h3>
        <div className="dos" style={{ marginTop: 12 }}>
          <Campo titulo={`Texto de la miniatura · ${palabrasMini} de ${MAX_MINIATURA} palabras`}
            ayuda="Máximo tres palabras, distintas a las del título. A tamaño de celular, la cuarta palabra es una mancha gris.">
            <input className="entrada" value={v.miniaturaTexto} placeholder="Ej.: NADIE A BORDO"
              onChange={(e) => cambiar((b) => { b.miniaturaTexto = e.target.value; })} />
          </Campo>
          <Campo titulo="Indicaciones de imagen" ayuda="Qué se ve, el encuadre y qué hace el fondo para que haya contraste.">
            <Area value={v.miniaturaBrief} placeholder="Ej.: barco de vela visto de lejos, niebla, mar negro; texto en blanco arriba a la izquierda."
              onChange={(e) => cambiar((b) => { b.miniaturaBrief = e.target.value; })} />
          </Campo>
        </div>
      </section>

      <section className="tarjeta">
        <div className="fila entre">
          <h3>Títulos</h3>
          <div className="fila">
            <button type="button" className="boton mini" onClick={pegarLista}>Pegar lista del agente</button>
            <button type="button" className="boton mini" disabled={v.titulos.length >= 12} onClick={() => cambiar((b) => { b.titulos.push(""); })}>+ Otro título</button>
          </div>
        </div>
        <div className="pila" style={{ marginTop: 14 }}>
          {revisados.map(({ i, t, r }) => {
            const enUso = v.tituloElegido === i;
            return (
              <div key={i} className={`tarjeta ${enUso ? "elegido" : ""}`} style={{ padding: 16, background: "var(--panel-2)" }}>
                <div className="fila arriba">
                  <div className="crece">
                    <input className="entrada" value={t} placeholder="Escribe una opción de título…" aria-label={`Título ${i + 1}`}
                      onChange={(e) => cambiar((b) => { b.titulos[i] = e.target.value; })} />
                  </div>
                  {r && <div className={`puntaje ${tonoPuntaje(r.puntaje)}`} title="Puntaje de 0 a 100">{r.puntaje}</div>}
                </div>
                {r && (
                  <ul className="lista" style={{ marginTop: 8 }}>
                    {r.problemas.map((p) => <li key={p.clave}><Punto tono="aviso" /><span className="chico">{p.mensaje}</span></li>)}
                    {r.aciertos.map((a) => <li key={a}><Punto tono="bien" /><span className="chico suave">{a}</span></li>)}
                  </ul>
                )}
                <div className="fila" style={{ marginTop: 10 }}>
                  {mejor === i && <span className="insignia bien">Mayor puntaje</span>}
                  {enUso && <span className="insignia rojo">Elegido</span>}
                  <span className="mono chico tenue">{[...t.trim()].length} caracteres</span>
                  <button type="button" className="boton mini" style={{ marginLeft: "auto" }} disabled={!t.trim() || enUso}
                    onClick={() => cambiar((b) => { b.tituloElegido = i; })}>{enUso ? "En uso" : "Usar este título"}</button>
                  <button type="button" className="boton mini fantasma peligro" aria-label="Quitar título" disabled={v.titulos.length <= 1}
                    onClick={() => cambiar((b) => {
                      b.titulos.splice(i, 1);
                      if (b.tituloElegido === i) b.tituloElegido = null;
                      else if (b.tituloElegido !== null && b.tituloElegido > i) b.tituloElegido -= 1;
                    })}>✕</button>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {elegido && (
        <section className="tarjeta">
          <h3>Así se va a ver</h3>
          <div className="vista-yt" style={{ marginTop: 12 }}>
            {[{ nombre: "Computador", n: ESCRITORIO }, { nombre: "Celular", n: CELULAR }].map((d) => (
              <div key={d.nombre} className="mini-yt">
                <div className="imagen">{v.miniaturaTexto || "TEXTO"}</div>
                <div className="pie">{cortar(elegido, d.n)}<small>Archivos Inexplicables · {d.nombre} (corte cerca de {d.n} caracteres)</small></div>
              </div>
            ))}
          </div>
        </section>
      )}

      <Aprobacion id="titulo" v={v} cambiar={cambiar} faltan={faltan} avisos={revisionElegido?.problemas.length ?? 0} alAprobar={alAprobar} />
    </>
  );
}
