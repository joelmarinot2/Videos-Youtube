# Archivos Inexplicables — memoria del proyecto

Este archivo lo lee Claude al empezar cada sesión. Aquí se guarda lo que el dueño del canal ya explicó,
para no tener que repetirlo. El dueño es electricista, no programa y es de Colombia: hablarle en
español sencillo, sin jerga técnica.

## El canal

- Nombre: **Archivos Inexplicables**. Canal nuevo, empieza desde cero.
- Tema: misterio. Casos reales que nunca se resolvieron o que no tienen explicación.
- Regla: no se inventa ningún dato. Nombres, fechas, lugares y cifras salen del dueño o de fuentes
  que él revisó.

## La serie

- 10 videos. Cada uno lleva al siguiente (tienen continuidad).
- Video 1: **el lago de los cuerpos en el Himalaya, India** (lago Roopkund).
- Video 2: STENDEC (así lo anuncia el cierre del guion del video 1).
- Los otros 8: pendiente de que el dueño los confirme.

### Guion del video 1 (ya existe)

Está en la rama `claude/zen-mendel-940d1o` de GitHub, carpeta `guiones/`:
- `expediente-01-lago-de-los-esqueletos.md`: guion completo con las indicaciones de edición entre [corchetes].
- `expediente-01-narrador.md` y `Archivo Imposible 001 - Narrador.docx`: solo lo que se lee en voz alta.
- En `investigacion/` (misma rama) están las notas de investigación de casos para la serie.

Ojo: en ese guion el canal se llama **Archivo Imposible**, y ahora el dueño dice **Archivo(s)
Inexplicable(s)**. Pendiente confirmar el nombre final.

El guion trae estas reglas de ritmo:
- Cambiar de imagen cada 3 a 5 segundos (aunque sea un zoom o un movimiento sobre la misma foto).
- Cada 30 a 40 segundos algo "rompe": golpe de sonido, silencio total, texto grande o pregunta a cámara.
- Textos en pantalla de máximo 6 palabras, entrando con un golpe de sonido.
- Música grave y tensa; se corta en seco antes de cada revelación.
- Contador o línea de tiempo en pantalla cada vez que aparece una fecha.
- Toda imagen hecha con IA lleva la palabra "RECREACIÓN" en una esquina.
- El guion tiene partes de "presentador a cámara". Pendiente confirmar si el dueño sale en cámara.

## Cómo se hace cada video (reparto del trabajo)

1. **El dueño** graba la narración (audio) con su voz.
2. **El dueño** genera aparte los clips de video y las imágenes con IA, siguiendo una lista de cortes
   en Excel (escena por escena) que Claude le hizo en una conversación anterior que se borró.
3. **Claude**:
   - limpia y corta el audio (silencios, muletillas, frases repetidas);
   - arma el video final juntando el audio con los clips e imágenes, en el orden del Excel;
   - sigue el estilo de edición de los canales de referencia que pase el dueño.

## Identidad de la edición (lo que pidió el dueño)

- Edición **dinámica**, con movimiento constante.
- Estilo **oscuro**.
- Colores principales: **morado y verde**.
- **Recortes de películas** y **recortes de revistas**, con aire **antiguo / vintage** (collage).
- **Motion graphics** y movimientos de cámara sobre las imágenes.
- Pendiente: analizar los canales de referencia que va a mandar el dueño.
- No existían skills de edición de video guardadas (se revisó el 2026-11-13). Cuando la identidad
  quede definida, guardarla como skill para que no se pierda.

## Estado

- [ ] Audio del video 1 (pendiente que el dueño lo envíe)
- [ ] Excel de cortes y escenas (pendiente que el dueño lo vuelva a enviar)
- [ ] Canales de referencia para el estilo de edición (pendiente)
- [ ] Clips e imágenes del video 1 (pendiente)

## Herramientas en el entorno

- `ffmpeg` está instalado: sirve para cortar el audio y armar el video.
- YouTube y Google Drive están bloqueados desde aquí: no se pueden ver ni descargar videos de
  referencia directamente.
