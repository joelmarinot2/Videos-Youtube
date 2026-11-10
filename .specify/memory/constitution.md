# Constitución del Panel de Archivos Inexplicables

Documento de principios del proyecto, con la estructura de [spec-kit](https://github.com/github/spec-kit).
Toda especificación, plan y cambio de código se revisa contra estos principios.

## Principios

### I. El dueño del canal aprueba cada paso
Nada avanza solo. Cada etapa de un video se desbloquea únicamente cuando la persona aprueba la anterior,
y cualquier etapa aprobada puede reabrirse. Ninguna automatización futura (IA, creador de videos) puede
saltarse una aprobación. El panel nunca publica: escribe, y la persona sube.

### II. Nunca se inventa un dato
Ninguna cifra, fecha, nombre ni fuente aparece en un guion si la persona no la escribió como dato
comprobado. Las instrucciones de todos los agentes llevan esta regla, y el panel pide confirmarla a mano
antes de aprobar el guion. Los ejemplos incluidos en el código usan solo hechos conocidos o frases
genéricas.

### III. Las reglas se calculan, no se opinan
Lo que se pueda medir se mide con código probado: puntaje de ganchos, revisión de títulos, reglas de
capítulos de YouTube, duración. Toda regla vive en `lib/`, sin pantalla, con pruebas en `tests/`. Una
regla nueva entra con su prueba. Los puntajes se presentan como guía y nunca como promesa de resultado.

### IV. Hecho para alguien que no programa
Toda la interfaz está en español claro, sin jerga técnica. Cada aviso dice qué pasa y qué hacer. Poner el
panel en internet debe poder hacerse siguiendo el README, sin tocar código. Los errores se muestran en
pantalla; nunca se pierde trabajo en silencio.

### V. Privado y simple
Un solo usuario. Los datos viven en Supabase con seguridad por fila: cada fila pertenece a quien inició
sesión. No hay claves secretas en el navegador ni en el repositorio. Se prefiere la solución con menos
piezas; no se agrega una dependencia ni un servicio sin una necesidad concreta.

## Identidad visual

Estética «misterio cinematográfico»: fondo casi negro, niebla roja y violeta, rojo intenso como único
color de acción, títulos en Cinzel y texto en Barlow. El verde y el ámbar se reservan para estados
(bien / aviso). Debe verse bien en celular y en computador.

## Forma de trabajo

- Método de spec-kit: constitución → especificación → plan → tareas → implementación, en `specs/`.
- Prácticas tomadas de [superpowers](https://github.com/obra/superpowers): preguntar antes de construir,
  escribir pruebas para la lógica, y no declarar algo terminado sin haberlo comprobado en un navegador real.
- Los 11 agentes de origen están en `.claude/skills/`; su versión en español vive en `lib/agentes.ts`.

## Gobierno

Esta constitución manda sobre cualquier otra práctica. Cambiarla requiere que el dueño del canal lo
apruebe y que se anote aquí la fecha y el motivo.

**Versión**: 1.0.0 | **Ratificada**: 2026-11-10 | **Última enmienda**: 2026-11-10
