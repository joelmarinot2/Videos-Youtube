# Archivo 001 · El lago de los esqueletos — plan de montaje

Material: carpeta de Drive del dueño (ver CLAUDE.md). Narración de 12 min 05 s. Todos los tiempos de este
documento son **segundos del audio original** (`voz archivos inexplicables_001_edit.wav`).

## Voz

- Limpia, casi sin ruido de fondo (pausas a -70 dB). No se filtra.
- Se le sube y empareja el volumen: paso alto 70 Hz, compresor suave, +14,5 dB y limitador → -15,7 LUFS
  (`voz_lista.wav`).
- **Cortes pendientes (frases repetidas):**
  1. 127,7 – 130,2: sobra el primer «Un ejército japonés.» (lo repite enseguida).
  2. 182,8 – 186,9: «Con su secreto. Su secreto en el fondo.» → dejar una sola vez.
  3. 490,9 – 494,9: sobra la segunda «cuando le ponen fecha a estos 14 esqueletos».
- **Posible error de lectura (avisado al dueño):** en 247,3 dice «piedras de **hierro**, duras como el hierro»;
  el guion dice «piedras de **hielo**». Si quiere, regraba esa frase.
- Cambios pequeños respecto al guion que no hay que tocar: «viven en Grecia o en la isla de Creta», «esto fue
  Archivos Inexplicables», y no dijo «Y nadie les cree».

## Bloques (según la voz)

| Bloque | Va de | a | Dura | Clips que hay | Imagen que cubren |
|---|---|---|---|---|---|
| 1 · El hallazgo | 3,7 | 98,5 | 95 s | b1-01, b1-03, b1-04, b1-07 | 24 s |
| 2 · La primera respuesta | 101,2 | 195,0 | 94 s | b2-02, b2-03, b2-04, b2-06 | 24 s |
| 3 · La leyenda | 197,4 | 270,5 | 73 s | b3-01, b3-04, b3-05, b3-06 | 24 s |
| 4 · La segunda respuesta | 272,5 | 389,7 | 117 s | b4-01, 03, 04, 06, 07, 08 + foto b4-10 | 31 s |
| 5 · El giro | 392,0 | 540,5 | 148 s | b5-01, 03, 04, 05, 06, 07, 08, 09 | 40 s |
| 6 · Lo que se descartó | 542,2 | 628,5 | 86 s | b6-01, b6-02, b6-04 + fotos b6-05, b6-06 | 15 s |
| 7 · El cierre | 630,8 | 724,6 | 94 s | b7-01, b7-02 + fotos b7-05, b7-06, b7-08 | 10 s |

Los clips suman unos 170 s y la voz 725 s. Lo que falta se cubre con: cámara lenta con interpolación
(`preparar_clip.sh`), acercamientos dentro del mismo clip, fotos impresas tipo collage, y gráficos (fechas con
contador, mapa, líneas de tiempo, fichas con sello, citas, contadores).

## Bloque 1 (hecho, en `b1/`)

| Tiempo | Voz | Imagen |
|---|---|---|
| 2,2 – 5,7 | «Año 1942.» | Línea verde que se dibuja + contador que frena en 1942 |
| 5,7 – 9,9 | «Norte de la India. El mundo está en guerra.» | Mapa de 1909 en 3D con pin, tira mecanografiada, recortes de periódico de 1942 |
| 9,9 – 22,2 | «A cinco mil metros… se llama Hari Kishan Madhwal…» | b1-01 lento (2,08×), altímetro 5.000 m, tira con el nombre |
| 22,2 – 29,6 | «Llega a un hoyo de roca y nieve…» | b1-03 lento (1,25×) |
| 29,6 – 35,3 | «Tan pequeño que se puede rodear caminando en dos minutos.» | b5-09 aéreo con anillo punteado que rodea el lago (seguido cuadro a cuadro) y «2 MIN» |
| 35,3 – 44,8 | «El hielo se está derritiendo… En el fondo hay algo.» | b1-04 lento (1,6×), al final se cierra en círculo oscuro |
| 44,8 – 47,9 | «Madhwal se acerca.» | b1-07 visto por una lupa verde que se abre y enfoca el cráneo |
| 47,9 – 63,6 | «Son huesos. Huesos humanos. No es uno… Cientos…» | b1-07 a pantalla completa (3,15×), frases en dos letras, acercamientos en cada frase |
| 63,6 – 72,7 | «Lo que ese hombre no sabe… más de ochenta años.» | Foto impresa del guardabosques + línea de tiempo 1942 → HOY y «+80 AÑOS» |
| 72,7 – 84,9 | «…resuelto dos veces. Y las dos veces se va a equivocar.» | Ficha de expediente (b6-06) con dos sellos RESUELTO que luego se tachan |
| 84,9 – 91,7 | «Esta es la historia del lago de los esqueletos. Soy Joel Marino» | b7-06 con título y crédito del narrador |
| 91,7 – 100 | «y esto es Archivos Inexplicables. Archivo 001.» | Logo serio (símbolo de mira/lago, serif, línea verde, «ARCHIVO N.º 001») |

Sonido del bloque 1 (`b1/sonido_b1.py`, usa `mezcla.py`): viento de montaña, pasos en piedra, agua, burbujas,
latido antes de la revelación, silencio total y golpe en «Son huesos», sellos, máquina de escribir. Sin música.
El ambiente baja solo cuando habla la voz.

## Cómo se arma un bloque

1. `preparar_clip.sh` → cuadros de cada clip en cámara lenta, recortados a 1920×1080.
2. Página `bloqueN.html`: `render(t)` dibuja el cuadro exacto del tiempo `t` (carga el cuadro del clip y
   coloca textos y gráficos). `capturar.js ver <tiempos>` saca capturas para revisar; `capturar.js tramo`
   genera el video a 24 cuadros/s (se lanzan 3 tramos en paralelo y se unen).
3. `sonido_bN.py` → mezcla de voz, ambientes y efectos.
4. ffmpeg une video + sonido y añade el grano de película.
