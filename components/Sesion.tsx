"use client";

import { createContext, useContext, useEffect, useState, type FormEvent, type ReactNode } from "react";
import { MODO_DEMO, supabase } from "@/lib/supabase";
import { Sello } from "./ui";

interface DatosSesion { correo: string | null; demo: boolean; salir: () => void }
const Contexto = createContext<DatosSesion>({ correo: null, demo: true, salir: () => {} });
export const useSesion = () => useContext(Contexto);

export function Sesion({ children }: { children: ReactNode }) {
  const [estado, setEstado] = useState<"cargando" | "fuera" | "dentro">(MODO_DEMO ? "dentro" : "cargando");
  const [correo, setCorreo] = useState<string | null>(null);

  useEffect(() => {
    if (!supabase) return;
    supabase.auth.getSession().then(({ data }) => {
      setCorreo(data.session?.user.email ?? null);
      setEstado(data.session ? "dentro" : "fuera");
    });
    const { data } = supabase.auth.onAuthStateChange((_evento, sesion) => {
      setCorreo(sesion?.user.email ?? null);
      setEstado(sesion ? "dentro" : "fuera");
    });
    return () => data.subscription.unsubscribe();
  }, []);

  if (estado === "cargando") {
    return <div className="puerta"><p className="suave pulso">Abriendo el archivo…</p></div>;
  }
  if (estado === "fuera") return <Puerta />;
  return (
    <Contexto.Provider value={{ correo, demo: MODO_DEMO, salir: () => { void supabase?.auth.signOut(); } }}>
      {children}
    </Contexto.Provider>
  );
}

function Puerta() {
  const [correo, setCorreo] = useState("");
  const [clave, setClave] = useState("");
  const [error, setError] = useState("");
  const [enviando, setEnviando] = useState(false);

  async function entrar(e: FormEvent) {
    e.preventDefault();
    if (!supabase) return;
    setEnviando(true); setError("");
    const { error: fallo } = await supabase.auth.signInWithPassword({ email: correo.trim(), password: clave });
    setEnviando(false);
    if (fallo) {
      setError(fallo.message.includes("Invalid login") ? "El correo o la contraseña no coinciden." : `No se pudo entrar: ${fallo.message}`);
    }
  }

  return (
    <main className="puerta">
      <form className="tarjeta pila" onSubmit={entrar}>
        <div style={{ textAlign: "center" }}>
          <Sello />
          <p className="sobretitulo">Acceso restringido</p>
          <h1 style={{ fontSize: "1.5rem" }}>Archivos Inexplicables</h1>
        </div>
        <label className="campo">
          <span>Correo</span>
          <input className="entrada" type="email" autoComplete="username" required value={correo} onChange={(e) => setCorreo(e.target.value)} />
        </label>
        <label className="campo">
          <span>Contraseña</span>
          <input className="entrada" type="password" autoComplete="current-password" required value={clave} onChange={(e) => setClave(e.target.value)} />
        </label>
        {error && <p className="error" role="alert">{error}</p>}
        <button className="boton primario" style={{ width: "100%" }} disabled={enviando}>
          {enviando ? "Verificando…" : "Entrar al archivo"}
        </button>
      </form>
    </main>
  );
}
