#!/bin/bash
# Uso: ver.sh <nombre de la hoja> <tiempos del audio separados por coma>  -> hoja de capturas en revisar/
cd "$(dirname "$0")"; node capturar.js ver "$2" 2>&1 | tail -3
L=""; for t in ${2//,/ }; do L="$L -i revisar/a$(printf '%06.2f' $t).jpg"; done
N=$(echo "$2" | tr ',' '\n' | wc -l); C=4; [ $N -le 6 ] && C=3; R=$(( (N + C - 1) / C ))
ffmpeg -v error -y $L -filter_complex "concat=n=$N:v=1:a=0,scale=640:360,tile=${C}x${R}" -frames:v 1 -q:v 3 revisar/$1.jpg && echo "hoja revisar/$1.jpg"
