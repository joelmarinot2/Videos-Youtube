"""Recorta el avatar del fondo de cuadros (pintado dentro del JPG), separa las poses y las pasa a la
paleta del canal: línea en tinta morada, relleno crema, borde de calcomanía y versión con brillo verde."""
import os, sys, numpy as np
from PIL import Image
from scipy import ndimage as nd
from hdlib import hd

BASE = os.path.dirname(os.path.abspath(__file__))
UP = "/root/.claude/uploads/d0439da4-483c-5507-a0b0-74fc8beb0f19"
OUT = f"{BASE}/avatar_hd"; os.makedirs(OUT, exist_ok=True)
INK = np.array([22, 10, 40.]); MID = np.array([118, 92, 160.]); CREAM = np.array([238, 231, 214.]); PAPER = np.array([244, 239, 228.])


def sdf(m): return nd.distance_transform_edt(m) - nd.distance_transform_edt(~m)


def cut(path):
    rgb = np.asarray(Image.open(path).convert("RGB"), np.float32)
    l = rgb.mean(2)
    dark = l < 120                                   # líneas negras del dibujo
    closed = nd.binary_dilation(dark, iterations=4)  # cierra huecos del contorno
    # tapa la base abierta de cada pose (los bustos se desvanecen abajo): línea en el borde inferior
    lab, n = nd.label(nd.binary_dilation(dark, iterations=10))
    for sl in nd.find_objects(lab):
        y0, y1, x0, x1 = sl[0].start, sl[0].stop, sl[1].start, sl[1].stop
        if (y1 - y0) * (x1 - x0) < 150000: continue
        band = dark[y1 - int((y1 - y0) * .12):y1, x0:x1]
        cols = np.where(band.any(0))[0]
        if len(cols): closed[y1 - 14:y1 - 6, x0 + cols.min():x0 + cols.max()] = True
    filled = nd.binary_fill_holes(closed)            # todo lo encerrado por el contorno = personaje
    body = nd.binary_erosion(filled, iterations=4) | (dark & filled)
    body = nd.binary_opening(body, iterations=2)
    m = nd.uniform_filter(l, 7); v = nd.uniform_filter(l * l, 7) - m * m
    flat_gray = (v < 14) & (l > 160) & (l < 232)
    flat_gray = nd.binary_dilation(nd.binary_opening(flat_gray, iterations=3), iterations=6) & body & ~nd.binary_dilation(dark, iterations=2)
    l = l.copy(); l[flat_gray] = 246
    return rgb, l, body


def stylize(l, body, name, border=16):
    lab, n = nd.label(body)
    sizes = nd.sum(body, lab, range(1, n + 1))
    keep = [i + 1 for i, s in enumerate(sizes) if s > 40000]
    poses = []
    for k in keep:
        m = lab == k
        ys, xs = np.where(m); pad = border + 24
        y0, y1, x0, x1 = max(ys.min() - pad, 0), ys.max() + pad, max(xs.min() - pad, 0), xs.max() + pad
        mm, ll = m[y0:y1, x0:x1], l[y0:y1, x0:x1]
        im = hd(ll, mm, border)
        poses.append(((y0 + y1) / 2, (x0 + x1) / 2, im))
    poses.sort(key=lambda p: (round(p[0] / 500), p[1]))  # orden de lectura: filas y luego columnas
    for i, (_, _, im) in enumerate(poses):
        im.save(f"{OUT}/{name}_{i + 1}.png")
    return len(poses)


rgb, l, body = cut(f"{UP}/806cae74-image.jpg")
print("retrato:", stylize(l, body, "retrato"))
rgb, l, body = cut(f"{UP}/d25367c3-image.jpg")
print("poses:", stylize(l, body, "pose"))
