"""Mejora de calidad del avatar: agranda 3 veces y vuelve a trazar las líneas como vectores (potrace),
en dos capas (tinta negra y sombreado gris), para que se vea nítido aunque salga grande en el video."""
import subprocess, tempfile, numpy as np
from PIL import Image
from scipy import ndimage as nd

ESCALA = 3
INK = np.array([22, 10, 40.]); MID = np.array([78, 62, 104.]); LIGHT = np.array([176, 164, 190.]); CREAM = np.array([238, 231, 214.]); PAPER = np.array([244, 239, 228.])


def _sdf(m): return nd.distance_transform_edt(m) - nd.distance_transform_edt(~m)


def _trazar(binario, tmp):
    """Vectoriza un mapa de bits (True = tinta) y lo devuelve como cobertura suave 0..1 del mismo tamaño."""
    h, w = binario.shape
    pbm, svg, png = f"{tmp}/c.pbm", f"{tmp}/c.svg", f"{tmp}/c.png"
    Image.fromarray(np.where(binario, 0, 255).astype(np.uint8)).convert("1").save(pbm)
    subprocess.run(["potrace", pbm, "-s", "-o", svg, "--turdsize", "3", "--alphamax", "1.0",
                    "--opttolerance", "0.25", "-W", f"{w}pt", "-H", f"{h}pt"], check=True)
    subprocess.run(["rsvg-convert", "-w", str(w), "-h", str(h), "-b", "white", svg, "-o", png], check=True)
    return 1 - np.asarray(Image.open(png).convert("L"), np.float32) / 255


def hd(ll, mm, border=16):
    """ll: luminancia del recorte (0..255); mm: máscara de la pose. Devuelve imagen RGBA a 3x."""
    h, w = ll.shape; H, W = h * ESCALA, w * ESCALA
    big = np.asarray(Image.fromarray(ll.clip(0, 255).astype(np.uint8)).resize((W, H), Image.LANCZOS), np.float32)
    big = nd.gaussian_filter(big, 0.6)                      # quita el ruido de la compresión JPG
    with tempfile.TemporaryDirectory() as tmp:
        tinta = _trazar(big < 105, tmp)                     # líneas negras
        medio = _trazar(big < 165, tmp)                     # trazos grises (pelos de la barba, sombras)
        claro = _trazar(big < 218, tmp)                     # sombreado muy suave
    claro = np.clip(claro - medio, 0, 1); medio = np.clip(medio - tinta, 0, 1)
    resto = np.clip(1 - tinta - medio - claro, 0, 1)
    rgb = (CREAM * resto[..., None] + LIGHT * claro[..., None] + MID * medio[..., None] + INK * tinta[..., None])
    # máscara a 3x con borde liso (campo de distancia agrandado)
    d = nd.zoom(nd.gaussian_filter(_sdf(mm), 1.2), ESCALA, order=1)[:H, :W] * ESCALA
    a_in = np.clip(d + .5, 0, 1); a_out = np.clip(d + border * ESCALA + .5, 0, 1)
    rgb = PAPER * (1 - a_in[..., None]) + rgb * a_in[..., None]
    return Image.fromarray(np.dstack([rgb, a_out * 255]).clip(0, 255).astype(np.uint8))
