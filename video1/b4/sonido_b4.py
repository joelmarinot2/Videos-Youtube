"""Sonido del bloque 4 (La segunda respuesta). Montaña, luego cuarto cerrado y metal; granizo en la revelación."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from mezcla import Mezcla
B = os.path.dirname(os.path.abspath(__file__))
m = Mezcla(271.0, 391.4, os.path.join(B, "..", "voz_lista.wav"))

# ---- Ambientes ----
m.bed("zumbido_viento", 271.0, 391.4, -27, fade=1.0, start=4.0)
m.bed("viento_montana", 272.8, 282.8, -14, fade=1.0, start=2.0)        # la expedición sube
m.bed("pasos_piedra2", 273.0, 280.0, -15, fade=0.6, start=12.0)
m.bed("viento_invierno", 284.6, 290.0, -16, fade=0.8, start=1.0)       # el frío lo ha conservado todo
m.bed("cuarto_cerrado", 289.8, 338.3, -9, fade=1.0)                    # mesa de laboratorio: cuarto cerrado
m.bed("latido_misterio", 313.3, 332.0, -15, fade=1.0, start=1.0)       # las fracturas están arriba
m.bed("viento_montana", 338.0, 348.3, -15, fade=1.2, start=14.0)       # a cinco mil metros, sin dónde esconderse
m.bed("lluvia_tormenta", 348.76, 352.1, -11, fade=0.3, start=5.0)      # granizo
m.bed("cuarto_cerrado", 351.9, 361.4, -9, fade=0.6, start=2.0)         # laboratorio de Oxford
m.bed("fogata", 361.2, 364.8, 8, fade=0.6, start=6.0)                  # la canción tenía razón
m.bed("lluvia_tormenta", 364.4, 373.1, -15, fade=1.0, start=2.0)       # el recuerdo de una tormenta real
m.bed("trueno_hondo", 366.0, 373.0, -17, fade=1.2, start=2.0)
m.bed("cuarto_cerrado", 386.3, 391.4, -9, fade=0.6, start=4.0)         # una prueba más

# ---- Año 2003 · la expedición ----
m.put("papel_rollo", 271.15, -8); m.tics(271.2, 271.9, 10, -18); m.put("golpe_hondo", 271.92, -8)
m.put("whoosh_rapido", 273.0, -11)
m.put("papel_desliza", 274.55, -10, pan=-.4); m.tecleo(274.8, 276.0, 18, -14); m.tecleo(276.7, 278.2, 22, -16)
m.put("obturador", 280.0, -13); m.put("obturador", 284.8, -14)
# ---- Lo que encontraron ----
m.put("obturador", 289.9, -14); m.tecleo(290.5, 291.3, 14, -15)
m.put("obturador", 292.2, -14); m.tecleo(292.3, 292.7, 6, -15)
m.tecleo(293.58, 294.4, 13, -15); m.tecleo(295.24, 296.4, 19, -15)
m.put("metal_cae", 295.3, -16, pan=.3)
# ---- 30 esqueletos · las fracturas ----
m.put("obturador", 298.4, -13); m.tics(299.2, 299.9, 9, -18, pan=.5); m.put("golpe_sordo", 299.92, -6, pan=.4); m.tecleo(299.7, 300.3, 8, -15)
m.put("aire_suave", 304.6, -15)
m.put("papel_desliza", 306.55, -10, pan=-.4); m.tecleo(306.7, 307.9, 18, -14)
m.tecleo(309.0, 309.5, 8, -15); m.put("garabato", 309.72, -6, pan=.4)
m.tecleo(310.2, 310.8, 10, -15); m.put("garabato", 311.08, -6, pan=-.4)
m.put("barrido_oscuro", 313.3, -12)
m.put("papel_rollo", 316.7, -8); m.tecleo(317.3, 317.7, 5, -14); m.tecleo(318.0, 319.5, 18, -16)
m.put("obturador", 320.7, -13); m.put("metal_herramienta", 320.95, -12, pan=.2)
for t in (321.42, 322.26, 323.34): m.put("golpe_sordo", t, -6, pan=.4)
m.put("metal_herramienta", 324.9, -15, pan=-.2)
m.put("aire_suave", 327.0, -16); m.tecleo(327.7, 328.3, 9, -15); m.tecleo(328.3, 329.4, 15, -14)
m.put("subida_trailer", 331.0, -12)
m.put("golpe_hondo", 331.76, -3); m.put("piedras_caen", 331.8, 0, align=False)
# ---- No es una avalancha. No es una batalla ----
m.tecleo(333.26, 333.8, 7, -15); m.put("golpe_sordo", 333.88, -4); m.put("garabato", 334.23, -4, pan=-.3)
m.tecleo(335.24, 335.9, 7, -15); m.put("golpe_sordo", 335.96, -4); m.put("garabato", 336.28, -4, pan=.3)
# ---- Algo redondo, algo duro, que cae del cielo ----
m.put("papel_rollo", 338.85, -8); m.tecleo(338.88, 339.5, 10, -15); m.tecleo(340.06, 340.5, 8, -15); m.tecleo(341.08, 341.9, 14, -15)
m.put("obturador", 342.6, -14); m.tics(342.65, 343.6, 12, -18, pan=.5); m.put("golpe_sordo", 343.62, -6, pan=.3)
# ---- Granizo ----
m.put("trueno_fuerte", 348.78, -2); m.put("golpe_hondo", 348.78, -3); m.put("tambor_terror", 348.78, -7)
m.put("piedras_escombro", 349.0, 3, align=False, fade=.4); m.put("piedras_caen", 350.6, 1, pan=.3, align=False)
# ---- Oxford · año 850 ----
m.put("obturador", 352.0, -13); m.put("papel_desliza", 354.05, -10, pan=-.4); m.tecleo(354.2, 355.4, 18, -14); m.tecleo(355.5, 356.3, 16, -16)
m.put("whoosh_rapido", 356.6, -12); m.tics(356.7, 357.1, 8, -17); m.put("golpe_hondo", 357.1, -5)
m.put("papel_rollo", 359.0, -8); m.tecleo(359.04, 360.2, 17, -14)
m.put("campana_templo", 362.3, -17)
m.put("trueno_medio", 369.6, -9)
# ---- El documental · caso cerrado ----
m.put("radio_crujidos", 373.0, -13, start=1.0, length=2.4, align=False, fade=.5)
m.put("papel_mueve", 375.42, -8); m.tecleo(375.5, 376.2, 15, -13); m.tecleo(376.3, 377.0, 14, -15)
m.put("periodico_cae", 375.9, -9, pan=-.4); m.put("periodico_cae", 376.6, -10, pan=.4)
m.put("sello_madera", 378.3, -3); m.put("periodico_cae", 378.31, -10); m.put("golpe_hondo", 378.3, -12)
m.put("sello_madera", 380.05, -1); m.put("periodico_cae", 380.06, -9); m.put("golpe_hondo", 380.05, -5); m.put("golpe_terror", 380.05, -10)
# ---- Y así se quedó quince años ----
m.put("papel_rollo", 383.6, -9); m.tecleo(383.3, 383.9, 10, -15); m.tics(383.9, 384.8, 9, -18); m.put("golpe_sordo", 384.82, -5); m.tecleo(384.85, 385.3, 4, -14)
m.put("obturador", 386.5, -13)

m.silencio(282.9, 284.7)                         # "los deja en silencio"
m.silencio(347.9, 348.74)                        # silencio antes de "Granizo"
m.silencio(380.9, 382.9)                         # pausa después de "Caso cerrado"
m.guardar(os.path.join(B, "sonido_b4.wav"))
print("sonido del bloque 4 listo")
