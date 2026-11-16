#!/bin/bash
# Uso: remendar.sh <carpeta bN> <N> <cuadro inicial> <cuadro final> [archivo de salida]
# Vuelve a generar solo los cuadros [ini, fin) del bloque, los encaja en mudo_bN.mp4 y rehace el video con grano y sonido.
cd "$(dirname "$0")/$1" || exit 1; N=$2; A=$3; B=$4; OUT=${5:-archivo-001-bloque-$N.mp4}
TA=$(python3 -c "print($A/24)"); TB=$(python3 -c "print($B/24)")
node capturar.js tramo $TA $TB remiendo.mp4 > qr.log 2>&1 || exit 1
ffmpeg -v error -y -i mudo_b$N.mp4 -i remiendo.mp4 -filter_complex "[0:v]trim=end_frame=$A,setpts=PTS-STARTPTS[a];[1:v]setpts=PTS-STARTPTS[b];[0:v]trim=start_frame=$B,setpts=PTS-STARTPTS[c];[a][b][c]concat=n=3:v=1:a=0[o]" -map "[o]" -c:v libx264 -preset medium -crf 13 -pix_fmt yuv420p mudo_nuevo.mp4 || exit 1
mv mudo_nuevo.mp4 mudo_b$N.mp4
echo "bloque $N cuadros: $(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 mudo_b$N.mp4)"
VF="noise=c0s=6:c0f=t+u:c1s=2:c1f=t+u:c2s=2:c2f=t+u,eq=contrast=1.04:saturation=1.05"
ffmpeg -v error -y -i mudo_b$N.mp4 -vf "$VF" -c:v libx264 -preset slow -b:v 2600k -pass 1 -passlogfile p_b$N -an -f mp4 /dev/null
ffmpeg -v error -y -i mudo_b$N.mp4 -i sonido_b$N.wav -vf "$VF" -c:v libx264 -preset slow -b:v 2600k -maxrate 5M -bufsize 8M -pass 2 -passlogfile p_b$N -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart -shortest $OUT
echo "LISTO bloque $N"
