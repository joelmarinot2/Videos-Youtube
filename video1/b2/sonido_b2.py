"""Sonido del bloque 2 (La primera respuesta). Sin música: proyector de cine, radio lejana, viento y los golpes.
Los tiempos se escriben en segundos del AUDIO original; T() los pasa al tiempo del bloque, que lleva dos cortes."""
import sys, os, subprocess
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from mezcla import Mezcla
B = os.path.dirname(os.path.abspath(__file__)); VOZ = os.path.join(B, "..", "voz_lista.wav")
INI, FIN = 100.0, 196.9
CORTES = [(127.60, 130.35), (183.85, 185.80)]          # frases repetidas que se quitan


def T(ta):
    d = 0.0
    for a, b in CORTES:
        if ta >= b: d += b - a
        elif ta > a: d += ta - a
    return ta - INI - d


# voz del bloque con los cortes hechos (se corta en los silencios, con un fundido corto en cada unión)
tramos = [(INI, CORTES[0][0]), (CORTES[0][1], CORTES[1][0]), (CORTES[1][1], FIN)]
filtro = ";".join(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={b - a - 0.02}:d=0.02[v{i}]" for i, (a, b) in enumerate(tramos))
filtro += ";" + "".join(f"[v{i}]" for i in range(len(tramos))) + f"concat=n={len(tramos)}:v=0:a=1[o]"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", VOZ, "-filter_complex", filtro, "-map", "[o]", os.path.join(B, "voz_b2.wav")], check=True)
DUR = T(FIN)
m = Mezcla(0.0, DUR, os.path.join(B, "voz_b2.wav"))
put = lambda n, t, *a, **k: m.put(n, T(t), *a, **k)
bed = lambda n, a, b, *r, **k: m.bed(n, T(a), T(b), *r, **k)
tec = lambda a, b, *r, **k: m.tecleo(T(a), T(b), *r, **k)
tic = lambda a, b, *r, **k: m.tics(T(a), T(b), *r, **k)

# ---- Ambientes continuos ----
bed("zumbido_viento", 100.0, 196.9, -26, fade=1.0, start=6.0)
bed("viento_montana", 100.0, 105.4, -15, fade=0.8, start=20.0)          # baja de la montaña
bed("pasos_piedra2", 100.3, 105.2, -13, fade=0.5, start=3.0)
bed("proyector_trabaja", 105.0, 115.6, -15, fade=0.6, start=2.0)        # oficina: proyector de cine
bed("latido_misterio", 121.0, 127.5, -13, fade=0.8, start=1.0)          # cientos de cuerpos... una cosa
bed("viento_invierno", 130.4, 138.0, -13, fade=0.4, start=3.0)          # el ejército en la nieve
bed("pasos_nieve", 130.5, 136.2, -15, fade=0.5)
bed("proyector_trabaja", 143.4, 150.0, -16, fade=0.6, start=9.0)        # revisan los restos
bed("viento_montana", 149.8, 155.7, -20, fade=0.8, start=22.0)          # la foto de los huesos
bed("burbujas_hondas", 166.2, 173.7, -18, fade=0.8)                     # el cráneo bajo el agua
bed("latido_misterio", 166.6, 173.4, -14, fade=0.8, start=1.0)
bed("viento_montana", 175.6, 182.8, -14, fade=0.8, start=10.0)          # el lago se queda allá arriba
bed("viento_invierno", 179.8, 182.8, -15, fade=0.6, start=6.0)
bed("burbujas_hondas", 182.5, 188.9, -15, fade=0.8, start=2.0)          # con su secreto en el fondo
bed("viento_montana", 188.8, 196.9, -19, fade=1.2, start=2.0)          # el pueblo al anochecer

# ---- S2 · La noticia llega a los ingleses · Segunda Guerra Mundial ----
put("whoosh_rapido", 105.2, -11)
put("radio_estatica", 105.5, -17, pan=-.4)                              # radio lejana
put("papel_desliza", 107.35, -10, pan=-.4)
tec(107.6, 109.0, 20, -14)
put("golpe_zoom", 110.38, -13)
put("barrido_viento", 112.4, -14, pan=-.3)
tec(112.5, 112.9, 4, -15); tec(113.5, 113.9, 4, -15)
put("whoosh_trans", 113.75, -12)
put("golpe_zoom", 114.62, -11)
tec(114.6, 114.9, 4, -13)

# ---- S3 · Japón avanza por Asia ----
put("whoosh_rapido", 115.5, -9)
put("radio_ruido", 115.6, -20, pan=.4, length=2.6)
put("golpe_zoom", 115.78, -12, pan=.4)
for t, pan in ((116.35, .2), (116.9, .1), (117.35, .3), (117.85, 0), (118.3, .1), (118.8, -.1)):
    put("tecla3", t, -10, pan=pan); put("golpe_zoom", t, -19, pan=pan)
put("barrido_viento", 116.3, -13, pan=.3)
put("golpe_hondo", 119.3, -9)
put("golpe_zoom", 119.88, -13, pan=-.3)
tec(120.1, 120.6, 7, -14)
put("whoosh_viento", 121.05, -14)
put("papel_desliza", 121.3, -9, pan=.4)
put("papel_mueve", 124.4, -12, pan=.4)
put("barrido_oscuro", 124.9, -11)
tic(125.0, 126.55, 10, -17, pan=-.2)
put("golpe_zoom", 126.62, -10)

# ---- S4 · Un ejército japonés ----
put("golpe_hondo", 130.46, -2); put("tambor_terror", 130.46, -6)
put("cristal_suspenso", 135.6, -11)

# ---- S5 · La ficha: primera respuesta ----
put("papel_mueve", 137.95, -8)
tec(138.1, 138.9, 17, -13); tec(139.0, 139.45, 12, -15)
put("golpecito", 139.5, -1); put("periodico_cae", 139.51, -10); put("golpe_hondo", 139.5, -12)

# ---- S6 · Revisan los restos · El primer problema ----
put("whoosh_trans", 143.62, -12)
put("golpe_zoom", 147.52, -12)
put("golpe_terror", 149.04, -9)

# ---- S7 · Demasiado gastados, demasiado viejos ----
put("barrido_viento", 149.92, -13)
put("barrido_viento", 151.6, -16, pan=-.2)
tec(152.4, 153.5, 18, -13)
put("barrido_viento", 153.5, -16, pan=.3)
tec(153.9, 155.1, 16, -13)

# ---- S8 · No tienen meses. Tienen siglos ----
put("whoosh_rapido", 155.6, -12)
tec(155.84, 156.3, 9, -14)
put("golpe_zoom", 156.38, -9)
put("barrido_viento", 156.93, -10, pan=-.3)
tec(157.64, 158.1, 6, -14)
put("golpe_grande", 158.56, -5); put("golpe_hondo", 158.56, -6)

# ---- S9 · No son soldados japoneses ----
put("papel_mueve", 160.75, -9)
put("barrido_viento", 162.25, -9, pan=-.3)
put("golpe_terror", 162.32, -6)
put("barrido_viento", 162.6, -9, pan=.3)
put("golpecito", 162.68, -7)
put("barrido_viento", 164.88, -11)

# ---- S10 · ¿Quiénes son? ----
put("barrido_oscuro", 166.2, -11)
put("golpe_zoom", 168.98, -10)

# ---- S11 · La guerra termina ----
put("radio_senal", 173.75, -12, pan=.3)
put("barrido_viento", 173.85, -13)
tic(174.05, 175.0, 9, -17)
tec(174.3, 175.0, 14, -14)
put("golpe_hondo", 175.02, -8)

# ---- S12 a S15 · El lago se queda allá arriba ----
put("whoosh_viento", 175.8, -12)
put("cristal_suspenso", 180.15, -11)
put("barrido_oscuro", 186.0, -12)
put("whoosh_tunel", 188.7, -16)

m.silencio(T(127.25), T(130.42))                 # silencio total antes de "Un ejército japonés"
m.silencio(T(158.25), T(158.52))                 # y antes de "siglos"
m.guardar(os.path.join(B, "sonido_b2.wav"))
print("sonido del bloque 2 listo: %.2f s" % DUR)
