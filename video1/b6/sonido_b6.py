"""Sonido del bloque 6 (Lo que se descartó). Papel, sello, un golpe por cada descarte."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from mezcla import Mezcla
B = os.path.dirname(os.path.abspath(__file__))
m = Mezcla(541.4, 630.0, os.path.join(B, "..", "voz_lista.wav"))
m.bed("zumbido_viento", 541.4, 630.0, -26, fade=1.0, start=12.0)
m.bed("cuarto_cerrado", 541.4, 607.4, -10, fade=1.0, start=1.0)        # el escritorio y el laboratorio
m.bed("viento_invierno", 567.4, 571.0, -14, fade=0.5, start=5.0)       # forasteros
m.bed("latido_misterio", 607.2, 629.6, -14, fade=1.0, start=40.0)      # la cita y la pregunta final
m.bed("viento_montana", 624.0, 630.0, -17, fade=1.0, start=4.0)

m.put("papel_mueve", 541.6, -10); m.put("periodico_cae", 543.4, -13, pan=.3); m.put("golpe_sordo", 546.8, -5)

def ficha(t0, q, st, r=None, entra=True, fuerte=-2):
    if entra: m.put("papel_desliza", t0 + .12, -7); m.put("periodico_cae", t0 + .3, -12)
    if q: m.tecleo(q[0], q[1], max(6, int((q[1] - q[0]) * 11)), -14)
    if r: m.tecleo(r[0], r[1], max(6, int((r[1] - r[0]) * 11)), -15)
    if st: m.put("sello_madera", st, fuerte); m.put("periodico_cae", st + .01, -10); m.put("golpe_hondo", st, -8)

ficha(550.1, (550.5, 555.9), 556.9)
m.put("obturador", 557.9, -13); m.tecleo(558.73, 560.0, 18, -15); m.tecleo(562.99, 563.9, 13, -15); m.tecleo(564.61, 565.9, 17, -16)
m.put("obturador", 567.6, -13); m.put("golpe_sordo", 568.53, -6)
ficha(570.9, (571.3, 572.4), 573.0, (573.95, 575.2))
ficha(576.4, (576.5, 577.9), 580.95, (578.25, 580.7))
ficha(582.3, (582.3, 583.7), None)
m.put("obturador", 584.1, -13)
ficha(587.6, None, 588.75, (587.67, 588.55), entra=False)
m.put("obturador", 590.1, -13); m.put("papel_desliza", 590.15, -10, pan=-.4); m.tecleo(590.3, 591.2, 12, -14)
m.put("papel_mueve", 597.9, -9)
for a, b in ((598.03, 598.5), (598.81, 599.4), (600.45, 600.9)): m.tecleo(a, b, 7, -14)
m.put("golpe_hondo", 604.6, -5); m.put("golpe_terror", 604.6, -10)
m.put("aire_suave", 607.2, -16); m.tecleo(608.2, 609.6, 22, -16); m.put("papel_rollo", 609.0, -9); m.tecleo(609.75, 610.6, 8, -14)
m.put("golpe_sordo", 612.85, -7); m.put("golpe_sordo", 616.41, -5)
ficha(617.7, (619.0, 623.3), 618.45, fuerte=-4)
m.put("barrido_oscuro", 624.1, -12); m.tecleo(624.41, 626.6, 24, -16)
m.put("golpe_hondo", 627.87, -1); m.put("tambor_terror", 627.87, -5); m.put("golpe_terror", 627.87, -8)
m.silencio(627.0, 627.83)                        # silencio antes de "¿Por qué?"
m.guardar(os.path.join(B, "sonido_b6.wav"))
print("sonido del bloque 6 listo")
