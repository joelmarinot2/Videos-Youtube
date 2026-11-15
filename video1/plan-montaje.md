# Archivo 001 · El lago de los esqueletos — plan de montaje

Material: carpeta de Drive del dueño (ver CLAUDE.md). Narración de 12 min 05 s. Todos los tiempos de este
documento son **segundos del audio original** (`voz archivos inexplicables_001_edit.wav`).

## Voz

- Limpia, casi sin ruido de fondo (pausas a -70 dB). No se filtra.
- Se le sube y empareja el volumen: paso alto 70 Hz, compresor suave, +14,5 dB y limitador → -15,7 LUFS
  (`voz_lista.wav`).
- **Cortes de frases repetidas** (los dos primeros ya están hechos en el bloque 2; falta el tercero, en el bloque 5):
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

## Bloque 2 (hecho, en `b2/`)

Va del segundo 100,0 al 196,9 del audio, con **dos cortes de frases repetidas ya hechos**: se quita
127,60 – 130,35 (el primer «Un ejército japonés.») y 183,85 – 185,80 («Su secreto»; queda «Con su secreto… en
el fondo.», como en el guion). Dura 92,2 s. En `bloque2.html` los tiempos siguen escritos en segundos del
audio original; las funciones `aAudio()` y `aVideo()` hacen el paso al tiempo del video (y `T()` en el sonido).

| Tiempo | Voz | Imagen |
|---|---|---|
| 100,0 – 105,2 | «El guardabosques baja de la montaña rápido y avisa.» | b2-01 (Higgsfield) un poco acelerado |
| 105,2 – 115,5 | «La noticia llega a los ingleses… plena Segunda Guerra Mundial.» | b2-02 lento (1,8×): plano abierto con tira «INDIA BRITÁNICA · 1942», luego acercamiento a las caras con línea de tiempo 1939–1945 y punto verde en 1942 |
| 115,5 – 127,6 | «Y Japón avanza por Asia. Cientos de cuerpos… una cosa.» | Mapa de Asia (Natural Earth, dominio público) en 3D: Japón se ilumina, los países ocupados se rayan uno a uno, flecha hasta la frontera de la India, pin verde «EL LAGO», foto de los huesos, y línea punteada que llega al lago |
| 130,35 – 137,9 | «Un ejército japonés intentó entrar… murió congelado.» | b2-03 lento (1,4×) con frase en dos letras; en «congelado» la imagen se detiene y se pone fría |
| 137,9 – 143,6 | «Eso es lo lógico…» | Ficha «PRIMERA RESPUESTA · UN EJÉRCITO JAPONÉS · 1942» con sello RESUELTO |
| 143,6 – 149,9 | «Así que mandan a revisar los restos. Y ahí aparece el primer problema.» | b2-04 lento (1,2×), acercamiento y frase «El primer problema.» |
| 149,9 – 155,6 | «Los huesos están demasiado gastados. Demasiado viejos.» | Foto b2-07 con dos anillos verdes y rótulos |
| 155,6 – 160,7 | «No tienen meses. Tienen siglos.» | Letras grandes: MESES tachado, y «siglos.» en verde con golpe |
| 160,7 – 166,2 | «No son soldados japoneses. No son de esa guerra.» | La misma ficha: se tacha el sello y la línea |
| 166,2 – 173,7 | «Entonces, ¿quiénes son? Nadie tiene la respuesta.» | b1-07 (cráneo bajo el agua) con acercamiento lento y la pregunta |
| 173,7 – 175,8 | «La guerra termina.» | Contador 1942 → 1945 y línea verde |
| 175,8 – 180,1 | «Los ingleses se van y el lago se queda allá arriba.» | b1-03 al revés (la cámara se aleja) |
| 180,1 – 182,6 | «Congelado casi todo el año.» | b1-04 al revés (el hielo se forma) |
| 182,6 – 188,9 | «Con su secreto… en el fondo.» | b1-05 (agua transparente) cerrándose en círculo oscuro |
| 188,9 – 196,9 | «Pero abajo, en los pueblos de la montaña…» | b2-06 lento (1,5×), funde a negro |

No se usó `b2-05-lago-congelandose` (tiene pinos y bosque, no cuadra con un lago a 5.000 m).
Sonido (`b2/sonido_b2.py`): proyector de cine en las escenas de oficina, estática de radio lejana, viento, pasos
en nieve, latido antes de «Un ejército japonés», silencio total antes de los dos golpes. Sonidos nuevos de
Mixkit: proyector 1443, estática de radio 2548 y 1026, señal de radio 2556.

## Bloques 3 a 7 (hechos, en `b3/` … `b7/`)

Desde el bloque 3 cada escena es una función y pueden fundirse una con otra. Desde el bloque 4 la página se
arma con `python3 bN/armar.py` (usa `partes.py` y `comun.txt`, que traen los estilos y las funciones comunes) y
el video completo del bloque sale con `./render.sh bN N <duración>`: genera los cuadros en 4 procesos, los une,
les pone grano y el sonido (`bN/sonido_bN.py`) y saca una hoja de capturas en `bN/revisar/hoja_final.jpg`.
`bN/ver.sh <nombre> <tiempos del audio>` saca capturas sueltas para revisar antes de generar.

| Bloque | Audio | Dura | Cómo se resolvió |
|---|---|---|---|
| 3 · La leyenda | 196,9 – 271,0 | 74,1 s | Tono cálido (fuego y oro). Mujeres junto al fuego, pinturas del rey, la reina, músicos y bailarinas con cortes en cada «Lleva…», la diosa, el granizo. Al final vuelve el escritorio: tres fotos y el sello LEYENDA. Sonido: fogata, campana, truenos, tormenta y piedras |
| 4 · La segunda respuesta | 271,0 – 391,4 | 120,4 s | Contador «AÑO 2003», expedición, lista de objetos, «30 esqueletos», el cráneo recortado (`b4/craneo.png`) con rótulos tachados y anillo en la fractura, la bola que cae, «AVALANCHA» y «BATALLA» tachadas, «Granizo.», Oxford y «AÑO 850», ficha con RESUELTO y CASO CERRADO, «15 años» |
| 5 · El giro | 391,4 – 541,4 (corte 491,25 – 495,21) | 146,0 s | «AÑO 2019», la cédula del ADN, **las 38 personas como puntos** (23 crema, 14 verdes, 1 morado), la línea del tiempo, la grieta en la ficha, mapa de Grecia y Creta al lago con «5.000 KM» (`b5/mapa_ea.js`), la cita, «800» tachado y «1800», «3 grupos, 2 épocas, 1 lago» |
| 6 · Lo que se descartó | 541,4 – 630,0 | 88,6 s | Una ficha por posibilidad con sello morado DESCARTADO (griegos de la India, familia, ejército, epidemia), microscopio, archivo, diario en blanco, cita de Niraj Rai, ficha «ESTO ES DATO» con sello verde y «¿Por qué?» |
| 7 · El cierre | 630,0 – 727,0 | 97,0 s | Barco, puerto, pueblo, la mujer en la ventana, la silla vacía, de vuelta al lago («5.000 metros», «En el mismo sitio.»), el lago hoy, la mano que recoge el hueso, lista con tres vistos buenos y «¿POR QUÉ?» sin marcar, «¿Tienes una teoría?», anuncio del archivo 002 (clave morse y avión) y logo final |

Notas:
- La transcripción automática se equivoca en algunos nombres («Hasdabal», «rey investigado»): en pantalla se
  escribe como en el guion (Jasdhaval). En 226–231 se le escaparon «Lleva músicos. Lleva bailarinas.»; los
  tiempos se sacaron de las pausas de la voz.
- La tira de puntos y rayas del bloque 7 es la palabra del video 2 en clave morse (sin letras).
- `b3-02-caravana-rey` trae letras falsas arriba a la izquierda: siempre va ampliado desde abajo a la derecha.

## Cómo se arma un bloque

1. `preparar_clip.sh` → cuadros de cada clip en cámara lenta, recortados a 1920×1080.
2. Página `bloqueN.html`: `render(t)` dibuja el cuadro exacto del tiempo `t` (carga el cuadro del clip y
   coloca textos y gráficos). `capturar.js ver <tiempos>` saca capturas para revisar; `capturar.js tramo`
   genera el video a 24 cuadros/s (se lanzan 3 tramos en paralelo y se unen).
3. `sonido_bN.py` → mezcla de voz, ambientes y efectos.
4. ffmpeg une video + sonido y añade el grano de película.
