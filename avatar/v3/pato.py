"""Recorta el pato detective (fondo blanco), separa poses y caras, y lo mejora a 3x CONSERVANDO SUS COLORES:
el color se agranda y se limpia del ruido JPG, y las líneas negras se vuelven a trazar como vectores."""
import os, subprocess, tempfile, numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as nd

BASE = os.path.dirname(os.path.abspath(__file__))
UP = "/root/.claude/uploads/d0439da4-483c-5507-a0b0-74fc8beb0f19"
OUT = f"{BASE}/pato"; os.makedirs(OUT, exist_ok=True)
ESCALA = 3; BORDE = 14
TINTA = np.array([24, 14, 30.]); PAPEL = np.array([246, 241, 230.])


def sdf(m): return nd.distance_transform_edt(m) - nd.distance_transform_edt(~m)


def trazar(binario, tmp):
    h, w = binario.shape
    pbm, svg, png = f"{tmp}/c.pbm", f"{tmp}/c.svg", f"{tmp}/c.png"
    Image.fromarray(np.where(binario, 0, 255).astype(np.uint8)).convert("1").save(pbm)
    subprocess.run(["potrace", pbm, "-s", "-o", svg, "--turdsize", "3", "--alphamax", "1.0",
                    "--opttolerance", "0.25", "-W", f"{w}pt", "-H", f"{h}pt"], check=True)
    subprocess.run(["rsvg-convert", "-w", str(w), "-h", str(h), "-b", "white", svg, "-o", png], check=True)
    return 1 - np.asarray(Image.open(png).convert("L"), np.float32) / 255


def cuerpo(rgb):
    l = rgb.mean(2)
    oscuro = l < 110
    cerrado = nd.binary_dilation(oscuro, iterations=3)
    lleno = nd.binary_fill_holes(cerrado)
    body = nd.binary_erosion(lleno, iterations=3) | (oscuro & lleno)
    return nd.binary_opening(body, iterations=2)


def mejorar(rgb, mm):
    h, w = mm.shape; H, W = h * ESCALA, w * ESCALA
    im = Image.fromarray(rgb.astype(np.uint8))
    color = im.filter(ImageFilter.MedianFilter(3)).resize((W, H), Image.LANCZOS)
    color = np.asarray(color.filter(ImageFilter.GaussianBlur(1.2)), np.float32)   # color limpio y suave
    l = np.asarray(im.convert("L").resize((W, H), Image.LANCZOS), np.float32)
    l = nd.gaussian_filter(l, 0.6)
    with tempfile.TemporaryDirectory() as tmp:
        tinta = trazar(l < 95, tmp)                        # contorno y líneas negras, nítidos
    out = color * (1 - tinta[..., None]) + TINTA * tinta[..., None]
    d = nd.zoom(nd.gaussian_filter(sdf(mm), 1.2), ESCALA, order=1)[:H, :W] * ESCALA
    a_in = np.clip(d + .5, 0, 1); a_out = np.clip(d + BORDE * ESCALA + .5, 0, 1)
    out = PAPEL * (1 - a_in[..., None]) + out * a_in[..., None]
    return Image.fromarray(np.dstack([out, a_out * 255]).clip(0, 255).astype(np.uint8))


def procesar(archivo, nombre, fila):
    rgb = np.asarray(Image.open(f"{UP}/{archivo}").convert("RGB"), np.float32)
    body = cuerpo(rgb)
    lab, n = nd.label(body)
    sizes = nd.sum(body, lab, range(1, n + 1))
    piezas = []
    for k in [i + 1 for i, s in enumerate(sizes) if s > 20000]:
        m = lab == k; ys, xs = np.where(m); pad = BORDE + 20
        y0, y1, x0, x1 = max(ys.min() - pad, 0), ys.max() + pad, max(xs.min() - pad, 0), xs.max() + pad
        mm, cc = m[y0:y1, x0:x1].copy(), rgb[y0:y1, x0:x1]
        # fondo blanco atrapado entre los pies: zonas blancas en la parte de abajo de la pieza
        blanco = (cc.min(2) > 232) & mm
        lb, nb = nd.label(blanco)
        for j, sl in enumerate(nd.find_objects(lb)):
            area = (lb[sl] == j + 1).sum()
            if area > 250 and sl[0].start > mm.shape[0] * .78:
                mm[nd.binary_dilation(lb == j + 1, iterations=3)] = False
        piezas.append(((y0 + y1) / 2, (x0 + x1) / 2, mm, cc))
    piezas.sort(key=lambda p: (round(p[0] / fila), p[1]))
    for i, (_, _, mm, cc) in enumerate(piezas):
        mejorar(cc, mm).save(f"{OUT}/{nombre}_{i + 1}.png")
    return len(piezas)


print("caras:", procesar("b9b473ce-image.jpg", "cara", 600))
print("poses:", procesar("f76bba33-image.jpg", "pose", 500))
