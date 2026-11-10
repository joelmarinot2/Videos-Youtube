"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import type { ReactNode } from "react";
import { useSesion } from "./Sesion";
import { Sello } from "./ui";

export function Marco({ children }: { children: ReactNode }) {
  const ruta = usePathname();
  const { correo, demo, salir } = useSesion();
  return (
    <>
      <header className="cabecera">
        <Link href="/" className="marca">
          <Sello />
          <span>ARCHIVOS INEXPLICABLES<small>PANEL DE PRODUCCIÓN</small></span>
        </Link>
        <nav className="nav">
          <Link href="/" className={ruta === "/" || ruta.startsWith("/video") ? "activo" : ""}>Expedientes</Link>
          <Link href="/canal" className={ruta.startsWith("/canal") ? "activo" : ""}>Canal</Link>
          {!demo && (
            <>
              <span className="cuenta" title={correo ?? ""}>{correo}</span>
              <button type="button" className="boton mini fantasma" onClick={salir}>Salir</button>
            </>
          )}
        </nav>
      </header>
      {demo && (
        <div className="demo" role="status">
          Modo demostración: Supabase no está conectado, así que todo se guarda solo en este navegador y no hay contraseña.
        </div>
      )}
      <main className="pagina">{children}</main>
    </>
  );
}
