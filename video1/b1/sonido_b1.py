"""Sonido del bloque 1 (El hallazgo). Sin música: viento, pasos en piedra, hielo y agua, más los golpes."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from mezcla import Mezcla
B = os.path.dirname(os.path.abspath(__file__))
m = Mezcla(2.2, 100.0, os.path.join(B, "..", "voz_lista.wav"))

# ---- Ambientes continuos ----
m.bed("zumbido_viento", 2.2, 100.0, -25, fade=1.0, start=2.0)
m.bed("viento_montana", 9.6, 35.6, -15, fade=1.0, start=4.0)         # guardabosques, hoyo, lago
m.bed("pasos_piedra2", 10.0, 21.6, -17, fade=0.8, start=1.0)         # camina solo
m.bed("viento_invierno", 22.0, 35.4, -17, fade=0.8, start=1.0)
m.bed("agua_fluye", 35.2, 44.9, -22, fade=1.2, start=3.0)            # el hielo se derrite
m.bed("viento_montana", 35.2, 44.6, -21, fade=1.0, start=14.0)
m.bed("latido_misterio", 44.9, 47.7, -11, fade=0.3, start=1.0)       # se acerca
m.bed("burbujas_hondas", 48.2, 63.6, -19, fade=0.8)                  # bajo el agua
m.bed("viento_montana", 84.7, 91.9, -17, fade=0.8, start=8.0)        # el lago de los esqueletos

# ---- E1 · Año 1942 · Norte de la India · El mundo está en guerra ----
m.put("barrido_viento", 2.75, -12)
m.tecleo(3.6, 3.95, 3, -10)
m.tics(3.3, 4.75, 12, -18)
m.put("golpe_hondo", 4.80, -7)
m.put("whoosh_trans", 5.80, -9)
m.put("papel_desliza", 5.95, -8, pan=.3)
m.tecleo(6.15, 6.85, 17, -13)
m.put("golpe_zoom", 6.35, -15)
m.put("periodico_cae", 7.27, -7, pan=.4)
m.put("periodico_cae", 7.72, -8, pan=-.4)
m.put("whoosh_rapido", 9.85, -9)

# ---- E2 · El guardabosques ----
m.tics(10.55, 11.85, 14, -19, pan=.5)
m.put("golpe_zoom", 11.85, -14, pan=.3)
m.put("papel_desliza", 15.1, -10, pan=-.4)
m.tecleo(15.36, 16.9, 19, -13)
m.tecleo(17.0, 17.9, 14, -16)
m.put("papel_mueve", 21.25, -10, pan=-.4)

# ---- E3 y E4 · El hoyo y el lago ----
m.put("whoosh_viento", 22.25, -13)
m.put("barrido_viento", 29.65, -13)
m.put("golpe_zoom", 33.0, -14)
m.tecleo(32.7, 33.5, 10, -15)

# ---- E5 · El hielo se derrite. En el fondo hay algo ----
m.put("cristal_suspenso", 35.45, -12)
m.put("cristal_suspenso", 38.7, -15, pan=.3)
m.put("barrido_oscuro", 43.3, -10)

# ---- E6 · Se acerca (lupa) ----
m.put("burbujas_hondas", 44.95, -11)
m.put("subida_trailer", 47.04, -5)

# ---- E7 · Son huesos ----
m.put("golpe_hondo", 48.06, -1)
m.put("tambor_terror", 48.06, -4)
m.put("golpe_terror", 48.06, -7)
m.put("golpe_zoom", 50.08, -10)
m.put("barrido_viento", 54.80, -12, pan=-.3)
m.put("golpe_grande", 56.40, -6)
m.put("golpe_zoom", 58.30, -13)
m.put("barrido_viento", 59.68, -14, pan=.4)
m.put("golpe_zoom", 61.48, -13)

# ---- E8 · Más de ochenta años ----
m.put("whoosh_trans", 63.62, -9)
m.put("papel_desliza", 63.95, -7, pan=-.4)
m.tecleo(68.3, 68.7, 4, -13)
m.put("barrido_viento", 68.45, -14, pan=.3)
m.tics(70.0, 71.5, 12, -18, pan=.4)
m.put("golpe_zoom", 71.52, -11, pan=.3)
m.tecleo(71.2, 71.5, 3, -14)

# ---- E9 · Resuelto dos veces... y las dos veces se va a equivocar ----
m.put("papel_mueve", 72.75, -8)
m.tecleo(72.95, 73.75, 18, -13)
m.tecleo(73.8, 74.9, 22, -16)
for t in (75.18, 76.55):                         # los dos sellos
    m.put("golpecito", t, -1); m.put("periodico_cae", t + .01, -9); m.put("golpe_hondo", t, -12)
m.put("barrido_viento", 82.50, -9, pan=-.3)      # los dos tachones
m.put("golpe_terror", 82.60, -6)
m.put("barrido_viento", 82.86, -9, pan=.3)
m.put("golpecito", 82.95, -6)

# ---- E10 · El lago de los esqueletos · Narra Joel Marino ----
m.put("whoosh_tunel", 84.95, -12)
m.put("barrido_viento", 86.5, -15, pan=-.4)
m.put("barrido_viento", 89.5, -15, pan=-.4)

# ---- E11 · Archivos Inexplicables · Archivo 001 ----
m.put("whoosh_trans", 91.72, -11)
m.put("golpe_hondo", 93.85, -6)
m.tecleo(95.75, 96.9, 15, -11)
m.put("campana", 97.0, -13)

m.silencio(47.74, 48.02)                         # silencio total antes de "Son huesos"
m.guardar(os.path.join(B, "sonido_b1.wav"))
print("sonido del bloque 1 listo")
