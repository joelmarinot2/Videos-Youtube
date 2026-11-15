#!/bin/bash
# Uso: preparar_clip.sh <archivo.mp4> <nombre> <factor de lentitud> <recorte o "no">
# Hace cámara lenta con interpolación de movimiento, recorta barras, pasa a 1920x1080 y guarda los cuadros.
V="$1"; N="$2"; F="$3"; C="$4"
OUT="b1/frames/$N"; mkdir -p "$OUT"
FPS=$(python3 -c "print(round(24*$F,3))")
if [ "$C" = "no" ]; then CROP=""; else CROP="crop=$C,"; fi
ffmpeg -v error -y -i "$V" -vf "minterpolate=fps=$FPS:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1,setpts=$F*PTS,fps=24,${CROP}scale=1920:1080:flags=lanczos,unsharp=5:5:0.5:5:5:0" -q:v 2 "$OUT/%04d.jpg"
echo "$N listo: $(ls $OUT | wc -l) cuadros"
