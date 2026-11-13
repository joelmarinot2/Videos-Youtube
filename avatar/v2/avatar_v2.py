"""Recorta el avatar del fondo de cuadros (pintado dentro del JPG), separa las poses y las pasa a la
paleta del canal: línea en tinta morada, relleno crema, borde de calcomanía y versión con brillo verde."""
import os, sys, numpy as np
from PIL import Image
from scipy import ndimage as nd

BASE = os.path.dirname(os.path.abspath(__file__))
UP = "/root/.claude/uploads/d0439da4-483c-5507-a0b0-74fc8beb0f19"
OUT = f"{BASE}/avatar_v2"; os.makedirs(OUT, exist_ok=True)
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
        d = nd.gaussian_filter(sdf(mm), 1.2)
        a_in = np.clip(d + .5, 0, 1); a_out = np.clip(d + border + .5, 0, 1)
        t = np.clip((ll - 40) / 200, 0, 1)[..., None]   # 0 = línea, 1 = blanco
        ink = INK * (1 - t) + CREAM * t
        ink = np.where(t < .55, INK * (1 - t / .55)[..., :] + MID * (t / .55), ink) if False else ink
        rgb = PAPER * (1 - a_in[..., None]) + ink * a_in[..., None]
        out = np.dstack([rgb, a_out * 255]).clip(0, 255).astype(np.uint8)
        poses.append(((y0 + y1) / 2, (x0 + x1) / 2, Image.fromarray(out)))
    poses.sort(key=lambda p: (round(p[0] / 500), p[1]))  # orden de lectura: filas y luego columnas
    for i, (_, _, im) in enumerate(poses):
        im.save(f"{OUT}/{name}_{i + 1}.png")
    return len(poses)



from PIL import ImageDraw
# hoja 1: quitar la etiqueta "trace evidence" y separar la pose del tablero de la del microscopio
src = Image.open(f"{UP}/77509fdf-image.jpg").convert("RGB")
ImageDraw.Draw(src).rectangle([1612, 2132, 1742, 2212], fill=(255, 255, 255))
src.save(f"{OUT}/_hoja1_limpia.png")
rgb, l, body = cut(f"{OUT}/_hoja1_limpia.png")
lab0, _ = nd.label(body)
comp = lab0 == lab0[1400, 1000]                      # la pieza pegada (tablero + microscopio)
yy, xx = np.mgrid[0:body.shape[0], 0:body.shape[1]]
A = comp & (((xx <= 1250) & (yy <= 1592)) | ((xx < 1100) & (yy < 1765)))   # tablero y su personaje
B = comp & ~A                                        # el del microscopio
body = body & ~comp
body |= nd.binary_erosion(A, iterations=2) | nd.binary_erosion(B, iterations=2)
print("v2a", stylize(l, body, "v2a"))
rgb, l, body = cut(f"{UP}/6d518dad-image.jpg")
print("v2b", stylize(l, body, "v2b"))
