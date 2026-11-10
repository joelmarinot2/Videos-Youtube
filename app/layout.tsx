import type { Metadata, Viewport } from "next";
import "@fontsource/cinzel/500.css";
import "@fontsource/cinzel/700.css";
import "@fontsource/barlow/400.css";
import "@fontsource/barlow/500.css";
import "@fontsource/barlow/600.css";
import "./globals.css";
import { Sesion } from "@/components/Sesion";

export const metadata: Metadata = {
  title: "Archivos Inexplicables · Panel",
  description: "Panel de producción del canal Archivos Inexplicables",
  robots: { index: false, follow: false },
};

export const viewport: Viewport = { themeColor: "#070509", width: "device-width", initialScale: 1 };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <body>
        <div className="niebla" aria-hidden="true" />
        <div className="grano" aria-hidden="true" />
        <Sesion>{children}</Sesion>
      </body>
    </html>
  );
}
