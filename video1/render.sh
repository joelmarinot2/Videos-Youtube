#!/bin/bash
# Uso: render.sh <carpeta del bloque> <número> <duración en segundos>  -> genera mudo_bN.mp4 en 4 procesos y lo une con el sonido
cd "$(dirname "$0")/$1" || exit 1; N=$2; D=$3
Q=$(python3 -c "print(round($D/4,3))"); A=0
L=""; for i in 1 2 3 4; do if [ $i = 4 ]; then Bf=$D; else Bf=$(python3 -c "print(round($Q*$i*24)/24)"); fi
  node capturar.js tramo $A $Bf parte_$i.mp4 > q$i.log 2>&1 & A=$Bf; L="$L\nfile 'parte_$i.mp4'"; done; wait
printf "$L\n" | sed '/^$/d' > partes.txt
ffmpeg -v error -y -f concat -safe 0 -i partes.txt -c copy mudo_b$N.mp4 || exit 1
echo "cuadros: $(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 mudo_b$N.mp4)"
VF="noise=c0s=6:c0f=t+u:c1s=2:c1f=t+u:c2s=2:c2f=t+u,eq=contrast=1.04:saturation=1.05"
ffmpeg -v error -y -i mudo_b$N.mp4 -vf "$VF" -c:v libx264 -preset slow -b:v 2600k -pass 1 -passlogfile p_b$N -an -f mp4 /dev/null
ffmpeg -v error -y -i mudo_b$N.mp4 -i sonido_b$N.wav -vf "$VF" -c:v libx264 -preset slow -b:v 2600k -maxrate 5M -bufsize 8M -pass 2 -passlogfile p_b$N -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart -shortest archivo-001-bloque-$N.mp4
ffmpeg -v error -y -i archivo-001-bloque-$N.mp4 -vf "select='not(mod(n\,$(python3 -c "print(max(1,round($D*24/42)))")))',scale=384:216,tile=7x6" -frames:v 1 -q:v 3 revisar/hoja_final.jpg
echo "LISTO bloque $N: $(ffprobe -v error -show_entries format=duration,size -of csv=p=0 archivo-001-bloque-$N.mp4)"
