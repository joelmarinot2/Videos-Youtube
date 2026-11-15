"""Sonido del bloque 5 (El giro). Laboratorio: cuarto cerrado y zumbido; silencio antes de "Catorce personas"."""
import sys, os, subprocess
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from mezcla import Mezcla
B = os.path.dirname(os.path.abspath(__file__)); VOZ = os.path.join(B, "..", "voz_lista.wav")
INI, FIN = 391.4, 541.4
CORTES = [(491.25, 495.21)]                         # frase repetida que se quita


def T(ta):
    d = 0.0
    for a, b in CORTES:
        if ta >= b: d += b - a
        elif ta > a: d += ta - a
    return ta - INI - d


tramos = [(INI, CORTES[0][0]), (CORTES[0][1], FIN)]
filtro = ";".join(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={b - a - 0.02}:d=0.02[v{i}]" for i, (a, b) in enumerate(tramos))
filtro += ";" + "".join(f"[v{i}]" for i in range(len(tramos))) + f"concat=n={len(tramos)}:v=0:a=1[o]"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", VOZ, "-filter_complex", filtro, "-map", "[o]", os.path.join(B, "voz_b5.wav")], check=True)
DUR = T(FIN)
m = Mezcla(0.0, DUR, os.path.join(B, "voz_b5.wav"))
put = lambda n, t, *a, **k: m.put(n, T(t), *a, **k)
bed = lambda n, a, b, *r, **k: m.bed(n, T(a), T(b), *r, **k)
tec = lambda a, b, *r, **k: m.tecleo(T(a), T(b), *r, **k)
tic = lambda a, b, *r, **k: m.tics(T(a), T(b), *r, **k)

# ---- Ambientes ----
bed("zumbido_viento", 391.4, 541.4, -26, fade=1.0, start=8.0)
bed("cuarto_cerrado", 393.4, 418.6, -8, fade=1.0)                     # laboratorio
bed("viento_montana", 418.4, 424.6, -16, fade=0.8, start=6.0)         # lo que se esperaba: un solo grupo
bed("cuarto_cerrado", 424.4, 458.4, -9, fade=0.8, start=3.0)
bed("latido_misterio", 437.0, 455.6, -15, fade=1.0, start=1.0)        # la primera grieta
bed("viento_invierno", 458.2, 476.3, -19, fade=1.0, start=1.0)        # el mapa
bed("cuarto_cerrado", 476.0, 503.5, -9, fade=0.8, start=5.0)
bed("latido_misterio", 484.1, 498.4, -13, fade=0.8, start=20.0)       # y falta lo peor
bed("viento_montana", 503.2, 518.4, -15, fade=1.0, start=10.0)        # el mismo lago perdido
bed("viento_invierno", 512.0, 518.4, -13, fade=0.6, start=4.0)
bed("latido_misterio", 518.2, 541.2, -14, fade=1.0, start=30.0)       # tres grupos, dos épocas

# ---- Año 2019 · las muestras ----
put("papel_rollo", 392.1, -8); tic(392.2, 392.9, 10, -18); put("golpe_hondo", 392.92, -8)
put("whoosh_rapido", 393.6, -11)
for t in (394.9, 395.75, 396.7): tec(t, t + .5, 8, -15)
tic(398.3, 399.0, 9, -18, pan=.5); put("golpe_sordo", 399.02, -6, pan=.4); tec(399.2, 400.2, 14, -16)
put("obturador", 402.6, -13); put("golpe_hondo", 403.32, -6)
# ---- La cédula ----
put("aire_suave", 405.4, -16); put("papel_desliza", 405.75, -8)
tec(406.4, 407.2, 12, -15); tec(407.3, 408.9, 22, -15); tec(409.68, 409.95, 4, -15); tec(410.1, 411.9, 24, -15)
put("obturador", 412.0, -14); put("obturador", 418.5, -14)
put("papel_desliza", 418.62, -10, pan=-.4); tec(418.78, 419.8, 12, -15); tec(421.5, 422.6, 14, -16)
put("obturador", 424.5, -13)
# ---- 23 personas ----
put("aire_suave", 428.2, -16); tic(428.24, 429.24, 23, -15); put("golpe_sordo", 429.26, -5); tec(429.64, 431.2, 20, -15)
put("obturador", 434.6, -13)
put("papel_rollo", 437.2, -8); tec(437.9, 438.4, 6, -15)
put("papel_desliza", 441.4, -9); tec(441.3, 443.4, 22, -15); tec(445.06, 446.9, 24, -15)
# ---- Primera grieta ----
put("papel_mueve", 448.22, -9); put("golpe_terror", 448.86, -6); put("piedras_caen", 448.86, -2, align=False, length=1.6)
# ---- 14 personas ----
put("aire_suave", 452.7, -16); put("golpe_hondo", 456.44, -2); put("tambor_terror", 456.44, -6); tec(456.9, 457.6, 8, -15)
# ---- No es de India, no es de Asia · el Mediterráneo ----
put("whoosh_rapido", 458.3, -10); tec(458.6, 459.1, 7, -15)
put("golpe_sordo", 459.3, -4); put("garabato", 459.83, -4, pan=-.3); put("golpe_sordo", 461.1, -4); put("garabato", 461.68, -4, pan=.3)
put("whoosh_viento", 464.5, -10); put("golpe_sordo", 466.0, -6); tec(465.32, 466.6, 16, -16)
put("golpe_sordo", 470.4, -5); tec(470.38, 470.9, 6, -15); put("golpe_sordo", 471.88, -6); tec(471.86, 472.3, 5, -15)
put("aire_suave", 472.7, -15); put("papel_rollo", 473.0, -8); tic(473.5, 475.4, 16, -18); put("golpe_hondo", 475.42, -6)
# ---- La cita · y falta lo peor ----
put("aire_suave", 476.2, -16); put("papel_rollo", 477.2, -9); tec(477.2, 478.9, 26, -16)
put("golpe_sordo", 480.26, -7); put("golpe_sordo", 482.14, -5)
put("obturador", 484.1, -13); put("golpe_terror", 485.14, -8)
put("obturador", 487.7, -13); put("papel_desliza", 488.25, -10, pan=-.4); tec(488.45, 490.3, 17, -15); tec(490.4, 491.2, 15, -16)
# ---- No da el año 800. Da el año 1800 ----
put("whoosh_rapido", 495.4, -12); put("golpe_sordo", 496.35, -4); put("garabato", 497.03, -4)
put("subida_trailer", 498.1, -10); tic(498.35, 498.85, 8, -16)
put("golpe_hondo", 498.87, -1); put("tambor_terror", 498.87, -5); put("golpe_terror", 498.87, -8)
put("papel_rollo", 501.0, -8); tec(501.03, 502.3, 16, -15)
# ---- Piénsalo ----
put("barrido_oscuro", 503.4, -12)
put("papel_desliza", 508.45, -10, pan=-.4); tec(508.75, 509.9, 14, -15); tec(510.83, 511.9, 16, -16)
put("obturador", 512.2, -13); put("papel_desliza", 514.02, -10, pan=-.4); tec(514.11, 514.8, 8, -15); tec(515.15, 516.9, 24, -16)
put("aire_suave", 518.2, -16); put("golpe_hondo", 521.99, -5); tec(522.1, 522.9, 14, -15)
for t, db in ((527.32, -5), (528.75, -5), (530.25, -3)): put("golpe_sordo", t, db)
put("golpe_hondo", 530.25, -9); tec(530.75, 532.0, 12, -15)
put("obturador", 533.2, -13); put("piedras_escombro", 533.4, -4, align=False, fade=.6); put("trueno_medio", 534.2, -13)
put("barrido_oscuro", 538.0, -11); put("papel_rollo", 539.3, -8); put("golpe_hondo", 540.13, -3); put("golpe_terror", 540.13, -8)

m.silencio(T(455.6), T(456.4))                   # silencio antes de "Catorce personas"
m.silencio(T(498.4), T(498.83))                  # y antes de "mil ochocientos"
m.guardar(os.path.join(B, "sonido_b5.wav"))
print("sonido del bloque 5 listo: %.2f s" % DUR)
