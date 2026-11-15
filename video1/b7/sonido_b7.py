"""Sonido del bloque 7 (El cierre). Mar que se convierte en viento; al final, el avión y el logo."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from mezcla import Mezcla
B = os.path.dirname(os.path.abspath(__file__))
m = Mezcla(630.0, 727.0, os.path.join(B, "..", "voz_lista.wav"))
m.bed("zumbido_viento", 630.0, 727.0, -27, fade=1.5, start=3.0)
m.bed("barco_madera", 630.0, 634.6, -12, fade=1.2, start=2.0)          # el barco
m.bed("mar_olas", 630.0, 647.8, -17, fade=1.5, start=3.0)              # el mar y el puerto
m.bed("mar_puerto", 633.4, 644.5, -6, fade=1.2, start=6.0)
m.bed("viento_montana", 645.0, 669.2, -17, fade=2.5, start=2.0)        # el mar se convierte en viento
m.bed("viento_invierno", 652.4, 659.5, -17, fade=1.0, start=2.0)
m.bed("agua_fluye", 661.5, 669.2, -21, fade=1.2, start=3.0)            # el hielo se derrite
m.bed("burbujas_hondas", 665.5, 669.0, -19, fade=0.8)
m.bed("viento_invierno", 668.7, 677.6, -16, fade=1.2, start=5.0)       # los turistas
m.bed("pasos_piedra", 669.0, 676.0, -19, fade=0.8, start=1.0)
m.bed("latido_misterio", 677.2, 697.8, -15, fade=1.5, start=10.0)      # lo que no ha podido decirnos
m.bed("viento_montana", 688.5, 704.2, -16, fade=1.5, start=6.0)
m.bed("proyector_trabaja", 709.5, 718.6, -17, fade=0.6, start=4.0)     # película de 1947
m.bed("avion_transporte", 713.2, 719.4, -9, fade=1.0, start=24.0)      # el avión

m.tics(648.75, 649.6, 10, -19, pan=.5); m.put("golpe_sordo", 649.62, -8, pan=.3)
m.put("papel_rollo", 656.6, -10); m.put("golpe_sordo", 658.0, -6)
m.put("papel_desliza", 659.32, -11, pan=-.4); m.tecleo(659.35, 659.7, 3, -15)
m.put("cristal_suspenso", 661.9, -14)
m.tecleo(677.27, 678.8, 24, -17)
for a in (678.87, 679.83, 681.93): m.tecleo(a, a + .5, 8, -15); m.put("garabato", a + .5, -9)
m.tecleo(686.1, 687.2, 9, -14); m.put("golpe_sordo", 686.15, -7)
m.put("papel_rollo", 691.0, -10)
m.put("golpe_sordo", 698.63, -7); m.tecleo(699.85, 701.1, 22, -16); m.tecleo(701.91, 702.8, 11, -16)
m.put("aire_suave", 703.9, -16); m.tecleo(704.37, 705.3, 13, -14); m.tecleo(705.87, 706.7, 12, -16)
m.put("golpe_sordo", 706.81, -5); m.put("garabato", 707.28, -5, pan=-.3); m.put("golpe_sordo", 708.03, -5); m.put("garabato", 708.73, -5, pan=.3)
m.put("obturador", 709.7, -13); m.tecleo(710.07, 712.9, 28, -17)
m.tics(710.7, 713.2, 18, -12, pan=0); m.put("golpe_sordo", 710.7, -8)
m.put("obturador", 713.4, -13); m.put("papel_desliza", 713.62, -10, pan=-.4); m.tecleo(713.77, 714.7, 13, -15); m.tecleo(715.45, 716.6, 16, -16)
m.put("aire_suave", 718.4, -15); m.tecleo(724.6, 725.4, 12, -16)
m.put("golpe_hondo", 721.3, -6); m.tecleo(723.4, 724.5, 15, -12); m.put("campana", 724.7, -14)
m.guardar(os.path.join(B, "sonido_b7.wav"))
print("sonido del bloque 7 listo")
