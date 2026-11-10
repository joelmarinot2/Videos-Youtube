# Archivos Inexplicables · Panel de producción

Panel web para llevar cada video del canal **Archivos Inexplicables** de la idea al guion listo para el
creador de videos con IA, paso a paso y con aprobación en cada etapa.

Está construido a partir de los 11 agentes de
[youtube-agent-skill](https://github.com/jakeschincariol/youtube-agent-skill) (licencia MIT), adaptados
al español.

## Qué hace

Cada video es un **expediente** que pasa por ocho etapas. Ninguna se abre hasta aprobar la anterior.

| Etapa | Qué haces | Qué revisa el panel solo |
| --- | --- | --- |
| 1. Idea | El caso, la promesa, la duración y los datos comprobados | Que haya caso y promesa |
| 2. Guion | Hasta 5 ganchos y el guion por bloques (narración + qué se ve) | Puntaje de cada gancho mientras escribes; duración |
| 3. Refinar | Corriges bloque por bloque | Saludos al inicio, bloques sin imagen, duración, pedidos del cierre |
| 4. Título y miniatura | Varios títulos y el texto de la miniatura | Largo, corte en celular, palabras repetidas, mayúsculas |
| 5. Descripción | Primeras líneas, descripción, etiquetas | Que las búsquedas que quieres ganar estén en el título |
| 6. Capítulos | Nombras cada capítulo | Las tres reglas de YouTube (00:00, mínimo 3, 10 s cada uno) |
| 7. Shorts | Eliges los momentos y escribes su primera línea | Propone los bloques que se sostienen solos; duración 20–55 s |
| 8. Exportar | Copias o descargas | Arma el guion por escenas, solo narración o en datos (JSON) |

En la página **Canal** está el perfil de voz (lo leen todos los agentes) y los agentes que trabajan sobre
el canal completo: plan de la semana, qué está funcionando, auditoría, comentarios, retención y edición.

### Lo que todavía NO hace

- **No genera texto con IA por sí solo.** Cada etapa tiene un botón «Copiar instrucciones del agente»:
  se pegan en una conversación con Claude y la respuesta se trae al panel. El botón «Generar aquí con IA»
  está puesto pero apagado hasta que se conecte un motor de IA.
- **No está conectado al creador de videos.** La etapa Exportar entrega el guion para copiar o descargar.
  El formato exacto se define cuando esté el repositorio del creador de videos.
- **No publica nada en YouTube.** El panel escribe; tú subes.
- Los puntajes de ganchos y títulos son una guía, no una predicción.

## Cómo ponerlo en internet (sin saber programar)

Necesitas tres cuentas gratuitas: GitHub (ya la tienes), Supabase y Vercel. Los nombres de los menús
pueden cambiar un poco con el tiempo.

### Paso 1 · Supabase (donde se guardan tus guiones)

1. Entra a <https://supabase.com>, crea una cuenta y un proyecto nuevo. Guarda la contraseña que te pide.
2. En el menú de la izquierda abre **SQL Editor**, pega TODO el contenido del archivo
   [`supabase/schema.sql`](supabase/schema.sql) y pulsa **Run**. Debe decir que terminó sin errores.
3. Abre **Authentication → Users → Add user**. Escribe tu correo y una contraseña, y marca
   **Auto Confirm User**. Ese será tu usuario para entrar al panel.
4. Abre **Authentication → Sign In / Providers** y apaga **Allow new users to sign up**. Así nadie más
   puede crearse una cuenta.
5. Abre **Project Settings → API** y copia dos datos: **Project URL** y la clave **anon / public**.

### Paso 2 · Vercel (donde vive la página)

1. Entra a <https://vercel.com> con tu cuenta de GitHub.
2. **Add New → Project** y elige el repositorio `Videos-Youtube`.
3. Antes de pulsar Deploy, abre **Environment Variables** y agrega estas dos, con los datos del paso 1.5:

   | Nombre | Valor |
   | --- | --- |
   | `NEXT_PUBLIC_SUPABASE_URL` | el Project URL |
   | `NEXT_PUBLIC_SUPABASE_ANON_KEY` | la clave anon / public |

4. Pulsa **Deploy**. En uno o dos minutos Vercel te da la dirección de tu panel.
5. Entra con el correo y la contraseña del paso 1.3.

Si abres la página sin haber puesto esas dos variables, el panel funciona en **modo demostración**:
no pide contraseña y guarda solo en ese navegador. Sirve para probar, no para trabajar.

## Para quien toque el código

```bash
npm install
```

```bash
npm run dev
```

```bash
npm test
```

- `app/` páginas · `components/` piezas de pantalla · `lib/` reglas y cálculos (sin pantalla, con pruebas)
- `lib/agentes.ts` instrucciones de cada agente; es el único punto que hay que conectar al motor de IA
- `lib/guion.ts` `exportarJSON` es el paquete que recibirá el creador de videos
- `specs/001-panel-produccion/` especificación, plan y tareas (método de spec-kit)
- `.claude/skills/` los 11 agentes originales, para usarlos desde Claude Code
