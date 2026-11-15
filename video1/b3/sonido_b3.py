"""Sonido del bloque 3 (La leyenda). Sin música: fogata, campana, trueno y granizo; al final vuelve el escritorio."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from mezcla import Mezcla
B = os.path.dirname(os.path.abspath(__file__))
m = Mezcla(196.9, 271.0, os.path.join(B, "..", "voz_lista.wav"))

# ---- Ambientes ----
m.bed("zumbido_viento", 196.9, 271.0, -27, fade=1.0, start=10.0)
m.bed("fogata", 196.9, 204.6, 9, fade=1.0, start=2.0)                 # las mujeres junto al fuego
m.bed("fogata", 203.6, 239.8, 0, fade=1.5, start=0.5)                 # el fuego sigue lejos: la canción cuenta
m.bed("viento_montana", 203.4, 230.8, -21, fade=1.2, start=5.0)       # la caravana sube
m.bed("trueno_hondo", 230.6, 244.2, -19, fade=1.5, start=6.0)         # a la diosa no le gusta: trueno lejano
m.bed("viento_invierno", 239.4, 244.2, -15, fade=1.0, start=2.0)      # el cielo se cierra
m.bed("lluvia_tormenta", 244.7, 255.2, -13, fade=1.0, start=3.0)      # la tormenta
m.bed("trueno_hondo", 246.5, 255.0, -15, fade=1.2, start=0.5)
m.bed("viento_montana", 266.8, 271.0, -15, fade=0.5, start=12.0)      # de vuelta al lago

# ---- La canción · el rey · la diosa ----
m.put("campana_templo", 211.15, -14)                                  # Nanda Devi
m.put("papel_desliza", 207.25, -11, pan=-.4); m.tecleo(207.5, 208.9, 13, -15); m.tecleo(209.2, 210.0, 12, -17)
m.put("papel_desliza", 213.05, -11, pan=-.4); m.tecleo(213.2, 214.1, 10, -15); m.tecleo(214.8, 216.4, 20, -17)
m.put("golpe_sordo", 222.18, -5)                                      # "un rey"
for t in (223.6, 225.6, 227.2, 228.8): m.put("golpe_sordo", t, -8)    # lleva... lleva... lleva...
m.put("campana_templo", 233.6, -17, pan=.2)                           # un lugar sagrado

# ---- El cielo se cierra · el granizo ----
m.put("trueno_medio", 241.6, -9)
m.put("trueno_fuerte", 244.96, -3); m.put("golpe_hondo", 244.96, -6)
m.put("piedras_escombro", 247.4, 2, align=False, fade=.4)
m.put("piedras_caen", 248.9, 2, pan=-.3, align=False)
m.put("trueno_medio", 249.2, -6)
m.put("piedras_escombro", 250.2, 0, pan=.3, align=False, fade=.4)
m.put("piedras_caen", 251.6, 0, pan=.2, align=False)

# ---- Bonita historia ----
m.put("papel_desliza", 255.95, -9, pan=-.4); m.tecleo(256.03, 256.9, 17, -13)
for t, pan in ((257.3, -.4), (258.7, 0), (260.3, .4)): m.put("papel_desliza", t + .15, -7, pan=pan); m.put("periodico_cae", t + .3, -11, pan=pan)
m.put("sello_madera", 261.92, -3); m.put("periodico_cae", 261.93, -10); m.put("golpe_hondo", 261.92, -12)
m.put("obturador", 267.0, -12)
m.put("golpe_hondo", 269.54, -5); m.put("golpe_terror", 269.54, -9)

m.silencio(243.9, 244.72)                        # silencio antes de "La diosa les lanza desde arriba"
m.silencio(254.3, 255.9)                         # y después de "No se salva nadie"
m.guardar(os.path.join(B, "sonido_b3.wav"))
print("sonido del bloque 3 listo")
