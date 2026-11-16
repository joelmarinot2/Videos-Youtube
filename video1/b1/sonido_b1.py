"""Sonido del bloque 1 (El hallazgo). Sin música: viento, pasos en piedra, hielo y agua, más los golpes."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from mezcla import Mezcla
B = os.path.dirname(os.path.abspath(__file__))
import subprocess
OFF, FIN = 2.2, 100.0
CORTES = [(77.70, 80.25)]                       # pausa larga entre "dos veces." y "Y las dos veces"


def T(ta):
    d = 0.0
    for a, b in CORTES:
        if ta >= b: d += b - a
        elif ta > a: d += ta - a
    return ta - OFF - d


VOZ = os.path.join(B, "..", "voz_lista.wav")
tramos = [(OFF, CORTES[0][0]), (CORTES[0][1], FIN)]
filtro = ";".join(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={b - a - 0.02}:d=0.02[v{i}]" for i, (a, b) in enumerate(tramos))
filtro += ";" + "".join(f"[v{i}]" for i in range(len(tramos))) + f"concat=n={len(tramos)}:v=0:a=1[o]"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", VOZ, "-filter_complex", filtro, "-map", "[o]", os.path.join(B, "voz_b1.wav")], check=True)
DUR = T(FIN)
m = Mezcla(0.0, DUR, os.path.join(B, "voz_b1.wav"))
put = lambda n, t, *a, **k: m.put(n, T(t), *a, **k)
bed = lambda n, a, b, *r, **k: m.bed(n, T(a), T(b), *r, **k)
tec = lambda a, b, *r, **k: m.tecleo(T(a), T(b), *r, **k)
tic = lambda a, b, *r, **k: m.tics(T(a), T(b), *r, **k)

# ---- Ambientes continuos ----
bed("zumbido_viento", 2.2, 100.0, -25, fade=1.0, start=2.0)
bed("viento_montana", 9.6, 35.6, -15, fade=1.0, start=4.0)         # guardabosques, hoyo, lago
bed("pasos_piedra2", 10.0, 17.9, -17, fade=0.8, start=1.0)         # camina solo
bed("pasos_piedra2", 17.9, 22.2, -11, fade=0.3, start=9.0)         # primer plano de las botas
bed("viento_invierno", 22.0, 35.4, -17, fade=0.8, start=1.0)
bed("agua_fluye", 35.2, 44.9, -22, fade=1.2, start=3.0)            # el hielo se derrite
bed("viento_montana", 35.2, 44.6, -21, fade=1.0, start=14.0)
bed("latido_misterio", 42.1, 47.7, -12, fade=0.5, start=1.0)       # la lupa y la cara
bed("burbujas_hondas", 48.2, 63.6, -19, fade=0.8)                  # bajo el agua
bed("viento_montana", 84.7, 91.9, -17, fade=0.8, start=8.0)        # el lago de los esqueletos

# ---- E1 · Año 1942 · Norte de la India · El mundo está en guerra ----
put("papel_rollo", 2.75, -7)
tec(3.6, 3.95, 3, -10)
tic(3.3, 4.75, 12, -18)
put("golpe_hondo", 4.80, -7)
put("aire_suave", 5.80, -13)
put("papel_desliza", 5.95, -8, pan=.3)
tec(6.15, 6.85, 17, -13)
put("golpe_sordo", 6.35, -9)
put("periodico_cae", 7.27, -7, pan=.4)
put("periodico_cae", 7.72, -8, pan=-.4)
put("whoosh_rapido", 9.85, -9)

# ---- E2 · El guardabosques ----
tic(10.55, 11.85, 14, -19, pan=.5)
put("golpe_sordo", 11.85, -8, pan=.3)
put("papel_desliza", 15.1, -10, pan=-.4)
tec(15.36, 16.9, 19, -13)
tec(17.0, 17.9, 14, -16)
put("papel_mueve", 21.25, -10, pan=-.4)

# ---- E3 y E4 · El hoyo y el lago ----
put("whoosh_viento", 22.25, -13)
put("papel_rollo", 29.65, -8)
put("golpe_sordo", 33.0, -8)
tec(32.7, 33.5, 10, -15)

# ---- E5 · El hielo se derrite. En el fondo hay algo ----
put("cristal_suspenso", 35.45, -12)
put("cristal_suspenso", 38.7, -15, pan=.3)
put("barrido_oscuro", 41.2, -11)

# ---- E6 · Se acerca (lupa) ----
put("burbujas_hondas", 42.05, -11)
put("obturador", 44.9, -14)
put("subida_trailer", 47.04, -5)

# ---- E7 · Son huesos ----
put("golpe_hondo", 48.06, -1)
put("tambor_terror", 48.06, -4)
put("golpe_terror", 48.06, -7)
put("golpe_sordo", 50.08, -4)
put("papel_rollo", 54.80, -7, pan=-.3)
put("golpe_grande", 56.40, -6)
put("obturador", 58.30, -15)
put("papel_rollo", 59.68, -9, pan=.4)
put("obturador", 61.48, -15)

# ---- E8 · Más de ochenta años ----
put("aire_suave", 63.62, -13)
put("papel_desliza", 63.95, -7, pan=-.4)
tec(68.3, 68.7, 4, -13)
put("papel_rollo", 68.45, -9, pan=.3)
tic(70.0, 71.5, 12, -18, pan=.4)
put("golpe_sordo", 71.52, -5, pan=.3)
tec(71.2, 71.5, 3, -14)

# ---- E9 · Resuelto dos veces... y las dos veces se va a equivocar ----
put("papel_mueve", 72.75, -8)
tec(72.95, 73.75, 18, -13)
tec(73.8, 74.9, 22, -16)
for t in (75.18, 76.55):                         # los dos sellos
    put("sello_madera", t, -3); put("periodico_cae", t + .01, -9); put("golpe_hondo", t, -12)
put("garabato", 82.50, -5, pan=-.3)      # los dos tachones
put("golpe_terror", 82.60, -6)
put("garabato", 82.86, -5, pan=.3)

# ---- E10 · El lago de los esqueletos · Narra Joel Marino ----
put("whoosh_tunel", 84.95, -12)
put("papel_rollo", 86.5, -10, pan=-.4)

# ---- E11 · Archivos Inexplicables · Archivo 001 ----
put("aire_suave", 91.72, -15)
put("golpe_hondo", 93.85, -6)
tec(95.75, 96.9, 15, -11)
tec(97.1, 98.0, 14, -15)
put("campana", 98.1, -14)

m.silencio(T(47.74), T(48.02))                         # silencio total antes de "Son huesos"
m.guardar(os.path.join(B, "sonido_b1.wav"))
print("sonido del bloque 1 listo")
