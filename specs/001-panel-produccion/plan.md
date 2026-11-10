# Plan de implementación: Panel de producción

**Rama**: `claude/funny-keller-tkdr3z` | **Fecha**: 2026-11-10 | **Especificación**: [spec.md](spec.md)

## Resumen

Aplicación web de una sola persona, desplegada en Vercel, con datos en Supabase. Toda la lógica de los
agentes (puntajes, revisiones, capítulos, Shorts, exportación) se escribió como funciones puras en
TypeScript, portadas de las herramientas Python de youtube-agent-skill y adaptadas al español.

## Contexto técnico

- **Lenguaje**: TypeScript, React 19
- **Marco**: Next.js 16 (App Router); todas las páginas son componentes de cliente
- **Datos**: Supabase (Postgres + Auth). Dos tablas: `videos` y `perfil_canal`, con `datos jsonb` y RLS
- **Sin Supabase**: modo demostración con `localStorage`, para probar sin cuentas
- **Estilo**: CSS propio en `app/globals.css`; fuentes Cinzel y Barlow empaquetadas (sin pedirlas a terceros)
- **Pruebas**: `node --test` sobre `lib/`; recorrido completo en navegador real (Chromium) antes de entregar
- **Despliegue**: Vercel detecta Next.js; solo necesita dos variables de entorno
- **Restricción**: no hay clave de IA ni servidor propio en esta fase

## Revisión contra la constitución

| Principio | Cómo se cumple |
| --- | --- |
| I. Aprobación en cada paso | `desbloqueada()` en `lib/tipos.ts`; barra de aprobación en cada etapa |
| II. Nunca se inventa un dato | Regla común en `lib/agentes.ts`; campo «Datos comprobados»; confirmación manual en Refinar |
| III. Reglas calculadas | `lib/gancho.ts`, `lib/titulo.ts`, `lib/guion.ts` con `tests/herramientas.test.ts` |
| IV. Para quien no programa | Interfaz en español; README paso a paso; errores visibles |
| V. Privado y simple | RLS por usuario; sin registro; solo Next.js, el cliente de Supabase y dos fuentes como dependencias |

## Estructura

```text
app/                     páginas: expedientes (/), video (/video/[id]), canal (/canal)
components/              Sesion, Marco, EditorBloques, PanelGancho, PanelAgente, ui
components/etapas/       una pantalla por etapa
lib/                     tipos, texto, formulas, gancho, titulo, guion, agentes, almacen, supabase, useVideo
supabase/schema.sql      tablas y permisos
tests/                   pruebas de lib/
specs/001-panel-produccion/   este plan, la especificación y las tareas
.specify/memory/         constitución
.claude/skills/          los 11 agentes originales
```

## Decisiones y por qué

- **Un solo objeto por video en `jsonb`**: el formato va a cambiar cuando se conecte el creador de videos;
  así no hay que migrar tablas cada vez. `normalizar()` rellena lo que falte en videos viejos.
- **Capítulos desde los bloques, no desde una transcripción**: el video aún no existe cuando se escribe el
  guion; los tiempos se calculan con palabras por minuto.
- **Puente de copiar y pegar**: el dueño eligió no conectar IA todavía. `instrucciones()` arma el mismo texto
  que después se enviará al motor de IA, así conectar la IA no cambia las pantallas.
- **Adaptación al español del puntaje**: límites de palabra que respetan tildes; se cuenta el trato directo
  sin pronombre («¿sabías…?»); vocabulario de riesgo propio del género.

## Fases siguientes (no hechas)

1. **Conectar la IA**: ruta de servidor que reciba `instrucciones()` y devuelva el texto; activar el botón
   «Generar aquí con IA». La clave va como variable secreta en Vercel, nunca en el navegador.
2. **Conectar el creador de videos**: ajustar `exportarJSON()` al formato de su repositorio y agregar el
   botón «Enviar» en la etapa Exportar, siempre después de la aprobación.
3. **Herramientas de después de publicar**: leer el archivo de retención y la transcripción dentro del panel
   (hoy esos agentes funcionan solo copiando instrucciones).
