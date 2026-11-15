"""Une los siete bloques en el video completo, con el sonido calzado exactamente a los cuadros de cada bloque.
Uso: python3 unir.py <carpeta de trabajo con b1..b7>  -> final/archivo-001-el-lago-de-los-esqueletos.mp4"""
import subprocess, wave, sys, os, numpy as np
S = sys.argv[1]; F = os.path.join(S, "final"); os.makedirs(F, exist_ok=True)
vids = [f"{S}/b1/archivo-001-bloque-1-v3.mp4"] + [f"{S}/b{n}/archivo-001-bloque-{n}.mp4" for n in range(2, 8)]
partes = []
with open(f"{F}/todo.h264", "wb") as out:
    for n, v in enumerate(vids, 1):
        fr = int(subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", v], capture_output=True, text=True).stdout.strip())
        out.write(subprocess.run(["ffmpeg", "-v", "error", "-i", v, "-an", "-c:v", "copy", "-bsf:v", "h264_mp4toannexb", "-f", "h264", "-"], capture_output=True).stdout)
        w = wave.open(f"{S}/b{n}/sonido_b{n}.wav"); x = np.frombuffer(w.readframes(w.getnframes()), "<i2").reshape(-1, 2); w.close()
        q = round(fr / 24 * 48000)                      # el sonido de cada bloque dura exactamente lo que sus cuadros
        x = x[:q].copy() if len(x) >= q else np.vstack([x, np.zeros((q - len(x), 2), "<i2")])
        partes.append(x); print("bloque", n, fr, "cuadros")
a = np.vstack(partes); w = wave.open(f"{F}/sonido_completo.wav", "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(48000); w.writeframes(a.tobytes()); w.close()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-r", "24", "-i", f"{F}/todo.h264", "-i", f"{F}/sonido_completo.wav", "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                "-movflags", "+faststart", f"{F}/archivo-001-el-lago-de-los-esqueletos.mp4"], check=True)
print("video completo listo")
