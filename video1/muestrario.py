"""Muestrario de efectos de sonido: cada efecto suena solo, con su número, nombre y dónde se usó en el bloque 1."""
import os, subprocess, wave, numpy as np
from PIL import Image, ImageDraw, ImageFont

B = os.path.dirname(os.path.abspath(__file__)); SFX = f"{B}/../sfx"; OUT = f"{B}/muestrario"; os.makedirs(OUT, exist_ok=True)
F = f"{B}/b1/fonts"; SR = 48000; W, H = 1280, 720
f_num = ImageFont.truetype(f"{F}/BebasNeue-Regular.ttf", 300); f_nom = ImageFont.truetype(f"{F}/BebasNeue-Regular.ttf", 92)
f_txt = ImageFont.truetype(f"{F}/CourierPrime-Regular.ttf", 32); f_peq = ImageFont.truetype(f"{F}/CourierPrime-Regular.ttf", 24)

# (archivo, nombre, dónde suena en el bloque 1, modo)
EFECTOS = [
 ("golpe_hondo", "Golpe grave", "En «1942», en «Son huesos», en el logo\ny debajo de los sellos", "uno"),
 ("tambor_terror", "Tambor seco", "En «Son huesos» (junto con el golpe grave)", "uno"),
 ("golpe_terror", "Golpe oscuro", "En «Son huesos» y en los tachones\nde «se va a equivocar»", "uno"),
 ("golpe_grande", "Golpe grande con eco", "En «Cientos»", "uno"),
 ("golpe_zoom", "Golpe corto", "Pin del mapa, «5.000 metros», «2 MIN»,\n«Huesos humanos», «+80 años» y los acercamientos", "uno"),
 ("golpecito", "Golpe del sello", "Los dos sellos «RESUELTO»", "uno"),
 ("whoosh_trans", "Barrido de aire", "Cuando entra el mapa, la foto del guardabosques\ny el logo", "uno"),
 ("whoosh_rapido", "Barrido rápido", "Al pasar del mapa a la montaña", "uno"),
 ("whoosh_viento", "Barrido de viento", "Al llegar al hoyo del lago", "uno"),
 ("whoosh_tunel", "Barrido largo con eco", "Cuando aparece «El lago de los esqueletos»", "uno"),
 ("barrido_viento", "Barrido corto", "La línea de la fecha, el anillo del lago,\nlos acercamientos y los tachones", "uno"),
 ("barrido_oscuro", "Barrido oscuro", "Cuando dice «En el fondo hay algo»", "uno"),
 ("subida_trailer", "Sonido que sube", "Justo antes de «Son huesos»", "uno"),
 ("cristal_suspenso", "Cristal o hielo", "Cuando el hielo se derrite", "uno"),
 ("tecla", "Máquina de escribir", "Cuando se escriben los textos: «Norte de la India»,\nel nombre del guardabosques, la ficha, «Archivo 001»", "teclas"),
 ("tecla3", "Tics del contador", "Cuando cuentan los números: el año 1942,\nlos 5.000 metros y los +80 años", "tics"),
 ("papel_desliza", "Papel que se desliza", "Cuando entran las tiras de papel y la foto", "uno"),
 ("papel_mueve", "Papel que se mueve", "Cuando aparece la ficha del expediente", "uno"),
 ("periodico_cae", "Periódico que cae", "Los recortes de periódico de 1942\ny junto a los sellos", "uno"),
 ("campana", "Campanita de máquina", "Al final, después de «Archivo 001»", "uno"),
]


def load(n):
    raw = subprocess.run(["ffmpeg", "-v", "quiet", "-i", f"{SFX}/{n}.mp3", "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)


def sonido(n, modo):
    if modo == "uno":
        x = load(n)[: int(5.0 * SR)].copy()
    elif modo == "teclas":
        x = np.zeros((int(2.6 * SR), 2)); rng = np.random.default_rng(1)
        for i in range(16):
            k = load(f"tecla{i % 3 + 1}"); i0 = int((0.1 + i * 0.14 + rng.normal(0, .012)) * SR); k = k[: len(x) - i0]; x[i0:i0 + len(k)] += k
    else:
        x = np.zeros((int(2.8 * SR), 2)); k0 = load("tecla3")
        for i in range(14):
            i0 = int((0.1 + 1.9 * (1 - (1 - i / 13) ** 0.5)) * SR); k = k0[: len(x) - i0]; x[i0:i0 + len(k)] += k * .8
    n_f = int(.08 * SR); x[-n_f:] *= np.linspace(1, 0, n_f)[:, None]
    pk = np.abs(x).max(); return x / pk * 0.6 if pk > 0 else x


def tarjeta(i, nombre, donde, total):
    im = Image.new("RGB", (W, H), (11, 6, 18)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 8], fill=(92, 242, 154))
    d.text((70, 40), "MUESTRARIO DE EFECTOS · BLOQUE 1", font=f_peq, fill=(150, 140, 165))
    d.text((W - 70, 40), f"{i} de {total}", font=f_peq, fill=(150, 140, 165), anchor="ra")
    d.text((70, 110), str(i), font=f_num, fill=(92, 242, 154))
    x0 = 70 + d.textlength(str(i), font=f_num) + 50
    d.text((x0, 190), nombre.upper(), font=f_nom, fill=(236, 229, 210))
    d.text((x0, 300), "Dónde suena:", font=f_peq, fill=(176, 140, 255))
    d.multiline_text((x0, 338), donde, font=f_txt, fill=(236, 229, 210), spacing=10)
    d.text((70, H - 70), "Anote los números de los que NO le gustan.", font=f_peq, fill=(150, 140, 165))
    p = f"{OUT}/t{i:02d}.png"; im.save(p); return p


partes = []; lista = []
for i, (arch, nombre, donde, modo) in enumerate(EFECTOS, 1):
    x = sonido(arch, modo); dur = max(2.6, len(x) / SR) + 0.9
    a = np.zeros((int(dur * SR), 2)); i0 = int(0.5 * SR); a[i0:i0 + len(x)] = x[: len(a) - i0]
    partes.append(a); lista.append((tarjeta(i, nombre, donde, len(EFECTOS)), dur))
aud = np.concatenate(partes)
with wave.open(f"{OUT}/audio.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(aud, -1, 1) * 32767).astype("<i2").tobytes())
with open(f"{OUT}/lista.txt", "w") as f:
    for p, dur in lista: f.write(f"file '{p}'\nduration {dur:.3f}\n")
    f.write(f"file '{lista[-1][0]}'\n")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{OUT}/lista.txt", "-i", f"{OUT}/audio.wav", "-vf", "fps=12,format=yuv420p",
                "-c:v", "libx264", "-preset", "medium", "-crf", "24", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", f"{OUT}/muestrario-efectos.mp4"], check=True)
print("muestrario listo: %.0f s, %d efectos" % (len(aud) / SR, len(EFECTOS)))
