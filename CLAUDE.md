# Archivos Inexplicables — memoria del proyecto

Este archivo lo lee Claude al empezar cada sesión. Aquí se guarda lo que el dueño del canal ya explicó,
para no tener que repetirlo. El dueño es electricista, no programa y es de Colombia: hablarle en
español sencillo, sin jerga técnica.

## El canal

- Nombre: **Archivos Inexplicables** (confirmado por el dueño el 2026-11-13; el guion viejo dice
  "Archivo Imposible" y hay que cambiarlo). Canal nuevo, empieza desde cero.
- El dueño **no sale en cámara**. Quiere un **avatar** (personaje) que haga de presentador.
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

Ojo: en ese guion el canal se llama **Archivo Imposible**; el nombre correcto es **Archivos Inexplicables**.

El guion trae estas reglas de ritmo:
- Cambiar de imagen cada 3 a 5 segundos (aunque sea un zoom o un movimiento sobre la misma foto).
- Cada 30 a 40 segundos algo "rompe": golpe de sonido, silencio total, texto grande o pregunta a cámara.
- Textos en pantalla de máximo 6 palabras, entrando con un golpe de sonido.
- Música grave y tensa; se corta en seco antes de cada revelación.
- Contador o línea de tiempo en pantalla cada vez que aparece una fecha.
- Toda imagen hecha con IA lleva la palabra "RECREACIÓN" en una esquina.
- Las partes de "presentador a cámara" del guion las hace el avatar.

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

### Referencias que mandó el dueño (2026-11-13)

Canales de estilo (YouTube): Detrás del Enigma (@detrasdelenimga) y LEMMiNO (@LEMMiNO).
Video que pidió analizar: "Probé 100+ repos de Github para editar videos. Este es mi TOP 10"
(Benjamín Cordero, youtube.com/watch?v=n1gtF-TAv0s). No se pudo ver (ver Herramientas).

Repositorios para hacer el video con código:
- github.com/haidrrrry/claude-remotion-skill: skill de Claude para Remotion. Gratis (MIT). Trae
  reglas de movimiento, gradación de color, grano de película, Ken Burns, subtítulos y sonido.
- github.com/heygen-com/hyperframes: video a partir de HTML. La base es gratis; las skills que copian
  el estilo de un video (reverse-any-video, style-sampling) son de pago (Pro).

TikToks de técnicas (ya analizados, transcritos):
- romel.media (5 efectos): texto que aparece desde una máscara; movimientos encadenados (un
  elemento empuja al siguiente); la cámara sigue lo importante; un objeto se transforma en la
  siguiente escena; las entradas van sincronizadas con la narración (si dice una cifra, aparece la cifra).
- romel.media (sonido): librería de efectos clasificada (woosh, golpe, click), nunca repetir el mismo
  sonido seguido, cada sonido justo en su cuadro, bajar efectos cuando habla la voz, revisar el audio
  completo antes de entregar.
- sanmunoz.ia (5 instrucciones): curvas suaves con un pequeño rebote; elementos que entran
  escalonados; paralaje (fondo, medio y frente a distinta velocidad); micro-movimiento constante
  para que nunca quede quieto.
- elbecariodemurphy.ia: reels hechos con código; algo pasa en pantalla cada ~0,3 s; personaje
  ilustrado como presentador (buena idea para el avatar); medir el ritmo y arreglar partes flojas.
- No existían skills de edición de video guardadas (se revisó el 2026-11-13). Cuando la identidad
  quede definida, guardarla como skill para que no se pierda.

## Estado

- [ ] Audio del video 1 (pendiente que el dueño lo envíe)
- [ ] Excel de cortes y escenas (pendiente que el dueño lo vuelva a enviar)
- [ ] Canales de referencia para el estilo de edición (pendiente)
- [ ] Clips e imágenes del video 1 (pendiente)

## Herramientas en el entorno

- `ffmpeg` está instalado: sirve para cortar el audio y armar el video.
- Red del entorno: acceso completo a internet (aprobado por el dueño el 2026-11-13).
- TikTok: se descarga bien con `yt-dlp`.
- YouTube: se puede listar videos de un canal, pero la descarga la bloquea YouTube ("confirma que no
  eres un bot"). No intentar saltarse ese bloqueo. Para analizar un video de YouTube, el dueño lo
  descarga en su computador y lo sube a Google Drive con enlace compartido.
- `faster-whisper` (convertir voz a texto) se instala con pip.
