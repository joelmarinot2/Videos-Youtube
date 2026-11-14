# Archivos Inexplicables — memoria del proyecto

Este archivo lo lee Claude al empezar cada sesión. Aquí se guarda lo que el dueño del canal ya explicó,
para no tener que repetirlo. El dueño es electricista, no programa y es de Colombia: hablarle en
español sencillo, sin jerga técnica.

## El canal

- Nombre: **Archivos Inexplicables** (confirmado por el dueño el 2026-11-13; el guion viejo dice
  "Archivo Imposible" y hay que cambiarlo). Canal nuevo, empieza desde cero.
- El dueño **no sale en cámara**. Su presentador es un **avatar dibujado** (aprobado 2026-11-13): detective
  de pelo crespo, barba y gabardina, con lupa y libreta, en línea negra estilo cómic. Originales en
  `avatar/original/` (traen el fondo de cuadros PINTADO, no es transparente). `avatar/avatar.py` lo recorta,
  tapa la base abierta de los bustos, limpia los cuadros de la lupa y lo pasa a la paleta (tinta morada,
  relleno crema, borde de calcomanía). Recortes listos en `avatar/recortes/`: `retrato_1` (busto de frente),
  `pose_1` (lupa y libreta), `pose_2` (cuerpo entero caminando), `pose_3` (guiño con lupa), `pose_4`
  (asombrado inclinado), `pose_5` (busto serio con lupa), `pose_6` (señalando), `pose_7` (pensando, mano en
  la barbilla). Se anima como recorte: entra con rebote, respira, se balancea y cambia de pose en seco
  con cada frase. Clip de prueba con el avatar de gafas: `muestras/muestra-avatar-gafas.mp4`
  ("Soy Joel Marino" = `v2a_2`, "y esto es Archivos Inexplicables" = `v2b_8`, "Archivo cero cero uno" = `v2a_3`).
- **Avatar versión 2 (2026-11-13):** el dueño mandó otro personaje: pelo crespo, **gafas**, barba y
  **camisa negra estampada** (a veces con gabardina), en poses de investigación. Originales con fondo blanco
  en `avatar/v2/original/`; recortes en `avatar/v2/recortes/` (hecho con `avatar/v2/avatar_v2.py`, que además
  quita la etiqueta "trace evidence" y separa dos poses que venían pegadas). Poses: `v2a_1`/`v2b_1` escribiendo
  huellas en libreta, `v2a_2`/`v2b_2` retrato sonriendo, `v2a_3`/`v2b_3` leyendo un mapa con gabardina,
  `v2a_4` frente a tablero de huellas con tarjeta, `v2a_5`/`v2b_5` agachado con brocha y cámara, `v2a_6`
  libro abierto (accesorio), `v2a_7` con microscopio, `v2b_4` caminando con linterna, `v2b_6` mesa con
  trípode, `v2b_7` con lupa y tela, `v2b_8` entregando una caja de evidencia.
  **DECIDIDO (2026-11-13): es el mismo personaje y se usan las ÚLTIMAS imágenes, las de gafas (v2).** Las de
  gabardina sin gafas (v1) quedan como versión vieja; no usarlas.
- **CAMBIO DE CONCEPTO (2026-11-14):** el dueño quiso cambiar el avatar a "Detective Psyduck" (Pokémon). Se le
  advirtió el riesgo (personaje de Nintendo + dibujos con firma de otro artista "WTPD") y **eligió crear un
  personaje propio** con la misma idea (detective torpe y chistoso, sombrero viejo, gabardina rota, lupa,
  libreta). Recomendado: búho morado de ojos verdes (alternativas: cuervo, pato morado). Instrucciones para
  generarlo en `avatar/v3/instrucciones-personaje.md`. PENDIENTE: que el dueño mande las imágenes del nuevo
  personaje; entonces recortarlas, mejorarlas (hdlib, conservando sus colores) y rehacer el clip de presentación.
  No usar Psyduck ni ningún personaje con dueño.
- **Versiones mejoradas (alta calidad, 3x):** `avatar/recortes-hd/` y `avatar/v2/recortes-hd/` (~2000×3000 px).
  USAR ESTAS en los videos. Se hacen con `avatar/hdlib.py`: agranda 3x y retraza las líneas como vectores con
  potrace en 3 tonos (tinta, gris medio, gris claro), así no se ven borrosas ni con cuadros de JPG.
  Recetas: `avatar/recorte_v1_hd.py` y `avatar/v2/recorte_v2_hd.py` (leen los originales de la carpeta de
  subidas de la sesión; cambiar la ruta `UP` a `avatar/original` o `avatar/v2/original`).
  Requiere `apt-get install potrace librsvg2-bin`.
- Tema: misterio. Casos reales que nunca se resolvieron o que no tienen explicación.
- Regla: no se inventa ningún dato. Nombres, fechas, lugares y cifras salen del dueño o de fuentes
  que él revisó.

## La serie

- 10 videos. Cada uno lleva al siguiente (tienen continuidad).
- Video 1: **el lago de los cuerpos en el Himalaya, India** (lago Roopkund).
- Video 2: STENDEC (así lo anuncia el cierre del guion del video 1).
- Los otros 8: pendiente de que el dueño los confirme.

### Guion del video 1 — VERSIÓN NUEVA (la que vale, recibida 2026-11-13)

`guiones/ARCHIVO 001 - El lago de los esqueletos - Guion nuevo.docx` y su copia en texto
`guiones/archivo-001-guion-nuevo.md` (en la rama de trabajo). Es el último guion según el dueño.
- 7 bloques, ~1.300 palabras, 10–11 min. Narrado en presente, frases cortas.
- Lo presenta "Soy Joel Marino, y esto es Archivos Inexplicables. Archivo cero cero uno."
- Al final trae: fuentes de cada dato, reglas de edición ("expediente frío", 10 tipos de escena,
  ritmo y sonido por bloque, sin música, 7 de cada 10 cambios son cortes secos, el círculo como forma
  que se repite) y la lista de clips a generar en Adobe Firefly (50 clips de 5 s + 4 imágenes).
- El video 2 es el de la palabra en clave morse enviada desde un avión en los Andes (STENDEC).

### Guion del video 1 — versión vieja

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
(Benjamín Cordero, youtube.com/watch?v=n1gtF-TAv0s). El dueño pegó la transcripción.

### Análisis de los canales (2026-11-13, videos que el dueño subió a Drive)

**Detrás del Enigma** ("Ruja Ignatova", 28 min):
- Cambio de plano cada ~5 s (mediana) y animaciones dentro de cada plano.
- Paleta negro + rojo intenso. Imágenes hechas con IA, muy cinematográficas.
- Tablero de investigación con hilo rojo que une fotos. Siluetas rojas sobre fondo oscuro.
- Textos grandes en mayúscula, blancos y rojos, algunos con brillo de neón, que entran palabra por palabra.
- Recortes de revistas y periódicos (portadas de Forbes en collage), calendarios, mapas con banderas,
  monedas con contadores de cifras, íconos simples, lluvia de números binarios.

**LEMMiNO** ("The Dyatlov Pass Case", 17 min):
- Ritmo lento y elegante: la imagen cambia cada 5–10 s, casi siempre con fundido suave, nunca corte seco.
- Fotos de archivo reales en blanco y negro, con grano, rayas y manchas de película vieja.
- Movimiento lento constante sobre cada foto (Ken Burns).
- Mapa 3D del terreno con la ruta en línea punteada que se dibuja sola.
- Tipografía limpia y mínima: cifras grandes (-30 °C), citas en cursiva sobre fondo desenfocado,
  títulos de capítulo con letra de sello.
- Colores apagados y fríos (gris, azul); el único color fuerte es un rosa/rojo para marcar.

### Repositorios útiles encontrados (2026-11-13)

- **lemomo-ai/lemo-opuscar** (MIT): 99 estilos de video hechos con código, y permite crear un estilo
  propio. Estilos que encajan con el canal: `vintage-collage` (collage de revista antigua: grabados,
  fotos viejas y recortes con borde de papel, que se mueven como recortes animados), `halftone-dossier`
  (expediente impreso retro con sellos), `visual-investigation` (mesa de investigación con evidencias),
  `dark-documentary`, `scratch-film`, `newsreel`, `double-exposure`, `briefing-board`.
  Necesita Node 20+, ffmpeg 7+ y Python 3.11+.
- **JuneYaooo/rea-video**: desarma un video plano a plano (cámara, ritmo, transición) y dice cómo rehacerlo.
- **Leonxlnx/earshot**: "oídos" para Claude: escucha el video, pone efectos de sonido calzados con los
  cortes y trae una librería gratis de efectos.
- Otros mencionados: mromidev/claude-animated-shorts, alchaincyf/huashu-motion,
  Vincentwei1021/video-shotcraft.

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

## Muestra de estilo (2026-11-13)

`muestras/muestra-archivo-001.mp4` (24,5 s, sin voz): inicio del bloque 1 con el estilo propuesto.
Cómo se hizo (en `muestras/archivo-001-estilo/`): `hornear.py` prepara los recortes (duotono morado/crema,
trama de puntos, borde de papel rasgado) desde fotos de Wikimedia; `muestra.html` anima cada escena en
función del tiempo; `capturar.js` saca los cuadros con Playwright; `sonido.py` genera el sonido (viento,
proyector, papel, máquina de escribir, golpes, silencio antes del golpe). Colores: fondo #0b0612,
morado #7046b2 / #2a1240, crema #e9e1cc, verde #5cf29a. Letras: Bebas Neue, Playfair Display (cursiva para
la palabra clave, en verde), Courier Prime.

**Opinión del dueño sobre la v1:** NO le gustaron (1) los efectos de sonido generados por computador,
(2) se veía "muy soso", (3) los recortes no se veían pulidos. Lecciones:
- Sonido: usar efectos REALES grabados, nunca sintetizados. Fuente que funciona desde aquí: Mixkit
  (assets.mixkit.co/active_storage/sfx/ID/ID-preview.mp3; licencia libre para videos). Freesound bloquea
  la descarga (403). Earshot no se pudo instalar (el sistema bloqueó ejecutar código externo).
- Nada de fondos planos u oscuros vacíos: cada escena lleva capas (fondo de color que se mueve, foto
  desenfocada de fondo, piezas, partículas, destellos de luz, viñeta y grano).
- Bordes de recortes con campo de distancia (sin dientes), fotos como impresión con borde blanco limpio.
- Golpes con aberración de color, destello y temblor; desenfoque de movimiento (render a 60 cuadros/s y
  mezclar de a 2); cámara 3D sobre el mapa; hilo verde que une pistas; transiciones con barrido.

v2: `muestras/muestra-archivo-001-v2.mp4`, hecha con `hornear2.py`, `muestra2.html`, `sonido2.py`.
**Al dueño le gustó la dirección de la v2** ("así me gusta como va"). Seguir por ahí.

## Estado

- [ ] Audio del video 1 (pendiente que el dueño lo envíe)
- [ ] Excel de cortes y escenas (pendiente que el dueño lo vuelva a enviar)
- [x] Canales de referencia analizados (Detrás del Enigma y LEMMiNO)
- [ ] Clips e imágenes del video 1 (pendiente)

## Herramientas en el entorno

- `ffmpeg` está instalado: sirve para cortar el audio y armar el video.
- Red del entorno: acceso completo a internet (aprobado por el dueño el 2026-11-13).
- TikTok: se descarga bien con `yt-dlp`.
- YouTube: se puede listar videos de un canal, pero la descarga la bloquea YouTube ("confirma que no
  eres un bot"). No intentar saltarse ese bloqueo. Para analizar un video de YouTube, el dueño lo
  descarga en su computador y lo sube a Google Drive con enlace compartido.
- `faster-whisper` (convertir voz a texto) se instala con pip.
