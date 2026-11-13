"""Recortes pulidos v2: bordes suaves sin dientes (campo de distancia), papel con textura,
fotos impresas con borde blanco limpio, fondos a pantalla completa y rayos de luz."""
import os, numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage as nd

BASE = os.path.dirname(os.path.abspath(__file__))
RAW, OUT = f"{BASE}/raw", f"{BASE}/assets2"
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(11)

INK = np.array([10, 5, 18.]); PD = np.array([38, 16, 62.]); PU = np.array([104, 64, 172.])
LAV = np.array([178, 160, 205.]); CREAM = np.array([236, 229, 210.]); PAPER = np.array([241, 236, 224.])
NEWS = np.array([220, 212, 194.]); GREEN = np.array([92, 242, 154.])


def L(im): return np.asarray(im.convert("L"), np.float32) / 255
def load(n, w=None):
    im = Image.open(f"{RAW}/{n}").convert("RGB")
    if w and im.width != w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    return im
def stretch(l, lo=.02, hi=.98, g=1.0):
    a, b = np.quantile(l, lo), np.quantile(l, hi); return np.clip((l - a) / (b - a + 1e-6), 0, 1) ** g
def grade(l, stops):
    xs = [s[0] for s in stops]; out = np.zeros(l.shape + (3,), np.float32)
    for c in range(3): out[..., c] = np.interp(l, xs, [s[1][c] for s in stops])
    return out
DUO = ((0, INK), (.32, PD), (.62, PU), (.86, LAV), (1, CREAM))
def smooth_noise(shape, scale, amp):
    n = nd.gaussian_filter(rng.standard_normal(shape), scale); return n / (n.std() + 1e-6) * amp
def sdf(mask): return nd.distance_transform_edt(mask) - nd.distance_transform_edt(~mask)
def paper_tex(shape, base, amp=6):
    t = smooth_noise(shape, 18, amp) + smooth_noise(shape, 2, amp * .5) + rng.normal(0, 1.5, shape)
    return np.clip(base[None, None, :] + t[..., None], 0, 255)
def save_rgba(rgb, a, name):
    Image.fromarray(np.dstack([np.clip(rgb, 0, 255), np.clip(a * 255, 0, 255)]).astype(np.uint8)).save(f"{OUT}/{name}")


def piece(img_rgb, border=22, torn=0.0, paper=PAPER, name="x.png", round_=4):
    """Pieza de papel: imagen con borde de papel. torn=0 foto impresa limpia; torn>0 borde rasgado suave."""
    h, w = img_rgb.shape[:2]; pad = border + 30
    H, W = h + 2 * pad, w + 2 * pad
    rect = np.zeros((H, W), bool); rect[pad:pad + h, pad:pad + w] = True
    d_in = sdf(rect)                                   # distancia al borde de la foto
    outer_d = d_in + border                            # borde exterior del papel
    if round_: outer_d = nd.gaussian_filter(outer_d, round_ * .5)
    if torn:
        outer_d = outer_d + smooth_noise((H, W), 9, torn) + smooth_noise((H, W), 2.2, torn * .35)
    a = np.clip(outer_d + .5, 0, 1)
    fringe = np.clip(outer_d + 2.5, 0, 1) - a          # fibras claras del rasgado
    rgb = paper_tex((H, W), paper)
    full = np.zeros((H, W, 3), np.float32); full[pad:pad + h, pad:pad + w] = img_rgb
    k = np.clip(d_in + .5, 0, 1)[..., None]            # mezcla suave foto/papel
    rgb = rgb * (1 - k) + full * k
    edge = np.exp(-np.abs(d_in) / 1.2)[..., None] * .18 # línea fina donde la foto toca el papel
    rgb = rgb * (1 - edge)
    if torn:
        rgb = rgb * (1 - fringe[..., None]) + (paper + 12) * fringe[..., None]; a = np.maximum(a, fringe * .55)
    save_rgba(rgb, a, name)


# ---- Fotos y planchas ----
def plate(src, name, w=2200, blur=10, dark=.55, g=1.0):
    l = stretch(L(load(src, w)), g=g)
    rgb = grade(l, DUO) * dark
    im = Image.fromarray(rgb.astype(np.uint8)).filter(ImageFilter.GaussianBlur(blur))
    im.save(f"{OUT}/{name}", quality=90)

plate("periodico.jpg", "plate_periodico.jpg", 2200, 7, .42)
plate("mapa.jpg", "plate_mapa.jpg", 2200, 9, .45)
plate("lago.jpg", "plate_lago.jpg", 2200, 14, .5)
plate("huesos.jpg", "plate_huesos.jpg", 2200, 9, .38)

# mapa impreso (borde rasgado suave)
m = stretch(L(load("mapa.jpg", 960)))
piece(grade(m, ((0, INK), (.45, PD), (.75, np.array([140, 112, 172.])), (1, CREAM))), border=16, torn=4.5, paper=CREAM, name="mapa.png")
# Trisul como foto impresa
t = load("trisul.jpg", 1100); tl = stretch(L(t), .01, .995)
piece(grade(tl, DUO), border=24, torn=0, name="foto_trisul.png")
# huesos como foto impresa (sin trama, más limpia)
hb = stretch(L(load("huesos.jpg", 900)), g=.9)
piece(grade(hb, DUO), border=24, torn=0, name="foto_huesos.png")
# lago a pantalla completa para el círculo
lg = stretch(L(load("lago.jpg", 2200)))
Image.fromarray(grade(lg, ((0, INK), (.3, PD), (.6, PU), (.85, np.array([170, 230, 200.])), (1, CREAM))).astype(np.uint8)).save(f"{OUT}/lago_full.jpg", quality=92)

# montaña en capas
tf = load("trisul.jpg", 2600); lt = stretch(L(tf), .01, .995, .9)
Image.fromarray(grade(lt, DUO).astype(np.uint8)).save(f"{OUT}/montana_fondo.jpg", quality=92)
ls = nd.gaussian_filter(L(tf), 4); Hh = ls.shape[0]
rows = np.arange(Hh)[:, None] > Hh * .45
front = (ls < np.quantile(ls[int(Hh * .62):], .62)) & rows
front = nd.binary_fill_holes(nd.binary_closing(front, iterations=8))
fa = np.clip(nd.gaussian_filter(sdf(front), 1.5) + .5, 0, 1)
save_rgba(grade(lt * .7, DUO), fa, "montana_frente.png")

# ---- Recortes de periódico (rasgado suave) ----
p = load("periodico.jpg"); pw, ph = p.size
for i, box in enumerate([(0.05, 0.535, 0.48, 0.75), (0.05, 0.76, 0.6, 0.97), (0.47, 0.75, 0.95, 0.97), (0.62, 0.47, 0.97, 0.62)]):
    c = p.crop((int(pw * box[0]), int(ph * box[1]), int(pw * box[2]), int(ph * box[3])))
    c = c.resize((int(c.width * .85), int(c.height * .85)), Image.LANCZOS)
    lp = stretch(L(c))
    piece(grade(lp, ((0, INK), (.5, PD), (.85, np.array([175, 165, 165.])), (1, NEWS))), border=6, torn=5, paper=NEWS, name=f"recorte_{i}.png", round_=0)

# ---- Cráneo como pegatina con contorno suave ----
c = Image.open(f"{RAW}/craneo.jpg").convert("L"); W, H = c.size
c = c.crop((int(W * .12), int(H * .08), int(W * .95), int(H * .52)))
lc = np.asarray(c, np.float32) / 255
ink = nd.gaussian_filter(lc, 1.2) < .86
ink = nd.binary_opening(ink, iterations=2)
lab, n = nd.label(ink); sizes = nd.sum(ink, lab, range(1, n + 1)); fig = lab == np.argmax(sizes) + 1
fig = nd.binary_fill_holes(nd.binary_closing(fig, iterations=10))
ys, xs = np.where(fig); pad = 60
y0, y1, x0, x1 = max(ys.min() - pad, 0), ys.max() + pad, max(xs.min() - pad, 0), xs.max() + pad
fig, lc = fig[y0:y1, x0:x1], lc[y0:y1, x0:x1]
d = nd.gaussian_filter(sdf(fig), 5)                        # contorno suavizado
a_fig = np.clip(d + .5, 0, 1); a_out = np.clip(d + 18 + .5, 0, 1)
rgb_fig = grade(stretch(lc, .01, .99), ((0, INK), (.5, PD), (.85, np.array([200, 188, 212.])), (1, CREAM)))
rgb = paper_tex(fig.shape, PAPER) * (1 - a_fig[..., None]) + rgb_fig * a_fig[..., None]
save_rgba(rgb, a_out, "craneo.png")

# ---- Papeles en blanco: titular y tiras ----
def blank(w, h, color, name, torn=5, border=4):
    piece(paper_tex((h, w), color), border=border, torn=torn, paper=color, name=name, round_=0)
blank(1300, 210, NEWS, "titular.png", torn=6)
blank(720, 92, CREAM, "tira.png", torn=3)
blank(520, 92, CREAM, "tira_corta.png", torn=3)

# ---- Rayos de luz (para la montaña) y destello ----
H2, W2 = 1080, 1920
yy, xx = np.mgrid[0:H2, 0:W2]; cx, cy = 1350, -200
ang = np.arctan2(yy - cy, xx - cx); r = np.hypot(yy - cy, xx - cx)
beams = (np.sin(ang * 23) * .5 + .5) ** 6 + (np.sin(ang * 9 + 1) * .5 + .5) ** 8 * .7
beams *= np.exp(-r / 1300)
beams = nd.gaussian_filter(beams, 6)
rays = np.dstack([beams * 200, beams * 175, beams * 255, np.clip(beams * 255 * .9, 0, 255)])
Image.fromarray(np.clip(rays, 0, 255).astype(np.uint8)).save(f"{OUT}/rayos.png")
print("listo", sorted(os.listdir(OUT)))
