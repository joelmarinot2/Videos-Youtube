"""Prepara los recortes del collage: duotono morado/crema, trama de puntos y bordes de papel rasgado."""
import os, numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage as nd

BASE = os.path.dirname(os.path.abspath(__file__))
RAW, OUT = f"{BASE}/raw", f"{BASE}/assets"
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(7)

INK = np.array([11, 6, 18]); PURPLE_DEEP = np.array([42, 18, 64]); PURPLE = np.array([112, 70, 178])
CREAM = np.array([233, 225, 204]); PAPER = np.array([239, 233, 218]); NEWS = np.array([214, 206, 186])


def lum(im):
    a = np.asarray(im.convert("L"), dtype=np.float32) / 255
    return a


def tritone(l, stops=((0, INK), (0.38, PURPLE_DEEP), (0.68, PURPLE), (1.0, CREAM))):
    out = np.zeros(l.shape + (3,), np.float32)
    xs = [s[0] for s in stops]
    for c in range(3):
        out[..., c] = np.interp(l, xs, [s[1][c] for s in stops])
    return out.astype(np.uint8)


def contrast(l, lo=0.05, hi=0.95, gamma=1.0):
    a, b = np.quantile(l, lo), np.quantile(l, hi)
    return np.clip((l - a) / (b - a + 1e-6), 0, 1) ** gamma


def noise_field(shape, scale, amp):
    n = rng.standard_normal(shape)
    return nd.gaussian_filter(n, scale) * amp / (nd.gaussian_filter(n, scale).std() + 1e-6)


def rough_mask(inner, rough=6, scale=3):
    """Rasga el borde de una máscara booleana con ruido fractal."""
    d = nd.distance_transform_edt(inner) - nd.distance_transform_edt(~inner)
    n = noise_field(inner.shape, scale, rough) + noise_field(inner.shape, 0.8, rough * 0.35)
    return (d + n) > 0


def torn_piece(rgb, margin=16, rough=5, paper=PAPER, name=None, fiber=True):
    """Recorte con margen blanco de papel rasgado alrededor."""
    h, w = rgb.shape[:2]
    H, W = h + 2 * margin + 20, w + 2 * margin + 20
    canvas = np.zeros((H, W, 4), np.uint8)
    rect = np.zeros((H, W), bool); rect[margin + 10:margin + 10 + h, margin + 10:margin + 10 + w] = True
    inner = rough_mask(rect, rough * 0.6, 2.5) & rect
    outer = rough_mask(nd.binary_dilation(rect, iterations=margin), rough, 3)
    canvas[outer, :3] = paper
    if fiber:  # fibras blancas en el borde exterior
        edge = outer & ~nd.binary_erosion(outer, iterations=2)
        canvas[edge, :3] = np.clip(paper + 10, 0, 255)
    full = np.zeros((H, W, 3), np.uint8); full[margin + 10:margin + 10 + h, margin + 10:margin + 10 + w] = rgb
    canvas[inner, :3] = full[inner]
    canvas[outer, 3] = 255
    im = Image.fromarray(canvas)
    if name: im.save(f"{OUT}/{name}")
    return im


def halftone(l, cell=9, angle=45, ink=PURPLE_DEEP, paper=NEWS):
    """Trama de puntos de periódico a 45 grados."""
    im = Image.fromarray((l * 255).astype(np.uint8))
    big = im.rotate(angle, expand=True, fillcolor=255)
    a = np.asarray(big, np.float32) / 255
    H, W = a.shape
    dots = Image.new("L", (W * 2, H * 2), 255); dr = ImageDraw.Draw(dots)
    for y in range(0, H, cell):
        for x in range(0, W, cell):
            dark = 1 - a[y:y + cell, x:x + cell].mean()
            r = cell * 0.74 * np.sqrt(dark)
            if r > 0.3:
                cx, cy = (x + cell / 2) * 2, (y + cell / 2) * 2
                dr.ellipse([cx - r * 2, cy - r * 2, cx + r * 2, cy + r * 2], fill=0)
    dots = dots.resize((W, H), Image.LANCZOS).rotate(-angle, expand=True, fillcolor=255)
    w0, h0 = im.size; W2, H2 = dots.size
    dots = dots.crop(((W2 - w0) // 2, (H2 - h0) // 2, (W2 - w0) // 2 + w0, (H2 - h0) // 2 + h0))
    t = np.asarray(dots, np.float32)[..., None] / 255
    return (ink * (1 - t) + paper * t).astype(np.uint8)


def load(name, maxw=None):
    im = Image.open(f"{RAW}/{name}").convert("RGB")
    if maxw and im.width > maxw: im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    return im


# 1. Mapa: duotono de tinta morada sobre papel crema, con borde rasgado
m = load("mapa.jpg")
lm = contrast(lum(m), 0.02, 0.98)
map_rgb = tritone(lm, ((0, INK), (0.45, PURPLE_DEEP), (0.8, np.array([150, 120, 170])), (1, CREAM)))
torn_piece(map_rgb, margin=14, rough=6, name="mapa.png")

# 2. Montaña (Trisul): blanco y negro morado, en dos capas para el paralaje
t = load("trisul.jpg")
lt = contrast(lum(t), 0.01, 0.995, 0.9)
Image.fromarray(tritone(lt)).save(f"{OUT}/montana_fondo.jpg", quality=92)
# capa del frente: las colinas oscuras de abajo
lt_s = nd.gaussian_filter(lum(t), 3)
rows = np.arange(lt.shape[0])[:, None] > lt.shape[0] * 0.45
front = (lt_s < np.quantile(lt_s[int(lt.shape[0] * .6):], 0.6)) & rows
front = nd.binary_closing(front, iterations=6); front = nd.binary_fill_holes(front)
front = nd.gaussian_filter(front.astype(np.float32), 2.5)
fr = np.dstack([tritone(lt * 0.8), (front * 255).astype(np.uint8)])
Image.fromarray(fr).save(f"{OUT}/montana_frente.png")

# 3. Lago: trama de puntos (recorte de revista) y versión duotono
lg = load("lago.jpg", 1400)
ll = contrast(lum(lg), 0.02, 0.98)
Image.fromarray(tritone(ll)).save(f"{OUT}/lago_duo.jpg", quality=92)
torn_piece(halftone(ll ** 0.6, cell=8), margin=12, rough=5, paper=NEWS, name="lago_trama.png")

# 4. Huesos: trama de puntos, recorte de periódico
hu = load("huesos.jpg", 1300)
lh = contrast(lum(hu), 0.02, 0.98, 1.1)
torn_piece(halftone(lh ** 0.6, cell=8), margin=12, rough=6, paper=NEWS, name="huesos_trama.png")
Image.fromarray(tritone(lh)).save(f"{OUT}/huesos_duo.jpg", quality=92)

# 5. Cráneo: se recorta la figura del grabado (la de frente) con margen blanco
c = Image.open(f"{RAW}/craneo.jpg").convert("L")
W, H = c.size
c = c.crop((int(W * 0.12), int(H * 0.08), int(W * 0.95), int(H * 0.52)))
lc = np.asarray(c, np.float32) / 255
ink = nd.gaussian_filter(lc, 1.2) < 0.86
ink = nd.binary_opening(ink, iterations=2)
lab, n = nd.label(ink); sizes = nd.sum(ink, lab, range(1, n + 1))
fig = lab == (np.argmax(sizes) + 1)
fig = nd.binary_closing(fig, iterations=8); fig = nd.binary_fill_holes(fig)
fig = nd.binary_opening(fig, iterations=4)
ys, xs = np.where(fig); pad = 40
y0, y1, x0, x1 = max(ys.min() - pad, 0), ys.max() + pad, max(xs.min() - pad, 0), xs.max() + pad
fig, lc = fig[y0:y1, x0:x1], lc[y0:y1, x0:x1]
margin = rough_mask(nd.binary_dilation(fig, iterations=14), 5, 3)
rgb = tritone(contrast(lc, 0.01, 0.99), ((0, INK), (0.5, PURPLE_DEEP), (0.85, np.array([190, 175, 200])), (1, CREAM)))
out = np.zeros(fig.shape + (4,), np.uint8)
out[margin, :3] = PAPER; out[margin, 3] = 255
out[fig, :3] = rgb[fig]
Image.fromarray(out).save(f"{OUT}/craneo.png")

# 6. Periódico: solo columnas de texto como textura (el titular real dice lo contrario)
p = load("periodico.jpg")
pw, ph = p.size
for i, box in enumerate([(0.05, 0.535, 0.48, 0.75), (0.5, 0.5, 0.95, 0.8), (0.05, 0.76, 0.6, 0.97)]):
    crop = p.crop((int(pw * box[0]), int(ph * box[1]), int(pw * box[2]), int(ph * box[3])))
    lp = contrast(lum(crop), 0.02, 0.98)
    rgb = tritone(lp, ((0, INK), (0.5, PURPLE_DEEP), (0.8, np.array([170, 160, 160])), (1, NEWS)))
    torn_piece(rgb, margin=6, rough=7, paper=NEWS, name=f"periodico_{i}.png", fiber=False)

# 7. Papeles en blanco: titular de periódico y tiras de máquina de escribir
def blank(w, h, color, name, rough=5, margin=4):
    base = np.ones((h, w, 3), np.float32) * color
    base += noise_field((h, w), 6, 5)[..., None] + rng.normal(0, 3, (h, w, 1))
    torn_piece(np.clip(base, 0, 255).astype(np.uint8), margin=margin, rough=rough, paper=color, name=name, fiber=False)
blank(1240, 230, NEWS, "papel_titular.png", rough=8)
blank(760, 96, CREAM, "tira.png", rough=3, margin=3)
blank(560, 96, CREAM, "tira_corta.png", rough=3, margin=3)

# 8. Textura de sello (desgaste) y mesa de papel oscuro
st = rng.random((400, 1200))
st = nd.gaussian_filter(st, 1.2); st = (st > np.quantile(st, 0.18)).astype(np.uint8) * 255
Image.fromarray(st).save(f"{OUT}/sello_textura.png")
mesa = np.ones((1080, 1920, 3), np.float32) * np.array([20, 12, 30])
mesa += noise_field((1080, 1920), 40, 6)[..., None] + noise_field((1080, 1920), 3, 3)[..., None]
Image.fromarray(np.clip(mesa, 0, 255).astype(np.uint8)).save(f"{OUT}/mesa.jpg", quality=90)
print("listo:", sorted(os.listdir(OUT)))
