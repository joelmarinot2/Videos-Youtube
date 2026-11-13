"""Diseño de sonido de la muestra, hecho desde cero (sin música, como pide el guion):
viento continuo, proyector de cine, papel, máquina de escribir, golpes graves y silencio antes de la revelación."""
import numpy as np, wave, os
from scipy import signal

SR = 48000; DUR = 24.5; N = int(SR * DUR)
rng = np.random.default_rng(3)
L = np.zeros(N); R = np.zeros(N)
BASE = os.path.dirname(os.path.abspath(__file__))


def env_curve(points):
    """Curva de volumen por puntos (tiempo, ganancia)."""
    t = np.arange(N) / SR
    xs, ys = zip(*points)
    return np.interp(t, xs, ys)


def bp(x, lo, hi, order=2):
    sos = signal.butter(order, [lo, hi], btype="band", fs=SR, output="sos")
    return signal.sosfilt(sos, x)


def lp(x, f, order=2):
    return signal.sosfilt(signal.butter(order, f, btype="low", fs=SR, output="sos"), x)


def add(x, t0, gain=1.0, pan=0.0):
    i = int(t0 * SR); x = x[: max(0, N - i)]
    gl, gr = gain * np.sqrt((1 - pan) / 2), gain * np.sqrt((1 + pan) / 2)
    L[i:i + len(x)] += x * gl; R[i:i + len(x)] += x * gr


def tail(n, k):
    return np.exp(-np.arange(n) / SR * k)


# --- Viento (dos capas estéreo que respiran) ---
def wind(seed):
    g = np.random.default_rng(seed)
    w = np.cumsum(g.standard_normal(N)); w -= lp(w, 0.5, 1)  # ruido café sin deriva
    w = bp(w, 120, 1400) / 400
    lfo = 0.6 + 0.4 * np.sin(2 * np.pi * (0.13 * np.arange(N) / SR) + seed) * np.sin(2 * np.pi * 0.051 * np.arange(N) / SR + seed * 2)
    gust = bp(g.standard_normal(N), 500, 2600) * 0.02 * np.clip(lfo - 0.6, 0, 1)
    return w * lfo + gust
wv = env_curve([(0, .25), (3.6, .3), (10.8, .35), (11.5, 1.0), (15.4, 1.0), (16, .7), (18.55, .7), (18.62, 0), (19.6, 0), (20.6, .45), (21.6, .3), (24.0, .25), (24.5, 0)])
wl, wr = wind(1), wind(2)
L += wl * wv * 7.0; R += wr * wv * 7.0

# --- Proyector de cine (traqueteo de 24 cuadros/s) en las escenas de archivo ---
t = np.arange(N) / SR
clicks = (np.sin(2 * np.pi * 24 * t) > 0.97).astype(float)
proj = bp(np.convolve(clicks, rng.standard_normal(200) * tail(200, 900), "same"), 900, 5000) * 0.55
proj += bp(rng.standard_normal(N), 2500, 7000) * 0.01
pv = env_curve([(0, 0), (0.2, .5), (10.6, .5), (10.9, 0), (21.6, 0), (21.8, .25), (24.5, 0)])
L += proj * pv; R += proj * pv * 0.9


# --- Efectos sueltos ---
def thump(f0=110, f1=38, dur=1.2, k=4.5, noise=0.3):
    n = int(SR * dur); tt = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-tt * 18)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * tail(n, k)
    hit = bp(rng.standard_normal(n), 150, 3000) * tail(n, 40) * noise
    return np.tanh((body + hit) * 1.6)


def whoosh(dur=0.7, lo=300, hi=3000):
    n = int(SR * dur); x = rng.standard_normal(n)
    out = np.zeros(n); seg = 2400
    for i in range(0, n, seg):
        k = i / n; c = lo + (hi - lo) * np.sin(np.pi * k)
        out[i:i + seg] = bp(x[i:i + seg], max(80, c * 0.6), min(SR / 2 - 100, c * 1.6))[: len(out[i:i + seg])]
    return out * np.sin(np.pi * np.linspace(0, 1, n)) ** 2 * 0.9


def paper(dur=0.25):
    n = int(SR * dur)
    x = bp(rng.standard_normal(n), 700, 6000) * tail(n, 18) * (0.5 + 0.5 * (rng.random(n) > 0.6))
    th = thump(90, 50, dur, 25, 0.1); return x * 0.6 + th[:n] * 0.25


def key():
    n = int(SR * 0.09)
    return bp(rng.standard_normal(n), 1500, 6000) * tail(n, 120) * 0.7 + thump(220, 120, 0.09, 60, 0) * 0.25


def tick():
    n = int(SR * 0.03)
    return bp(rng.standard_normal(n), 3000, 8000) * tail(n, 260) * 0.35


def ice(dur=1.6):
    n = int(SR * dur); tt = np.arange(n) / SR
    cr = np.zeros(n)
    for _ in range(40):
        i = int(rng.random() ** 1.6 * (n - 4000)); m = 1500
        cr[i:i + m] += bp(rng.standard_normal(m), 1800, 7000) * tail(m, 90) * rng.random()
    tone = np.sin(2 * np.pi * (260 - 60 * tt) * tt) * tail(n, 2.2) * 0.08
    return cr * 0.5 + tone


def typing(t0, t1, chars):
    for i in range(chars):
        add(key(), t0 + (t1 - t0) * i / max(1, chars) + rng.normal(0, 0.008), 0.5, rng.uniform(-.3, .3))


# Escena 1 · Año 1942
add(whoosh(0.9, 200, 1800), 0.15, 0.35)
typing(0.35, 0.75, 3)
for i, tt in enumerate(np.linspace(0.7, 2.0, 22) ** 1.0):
    add(tick(), 0.7 + (1.3) * (1 - (1 - i / 21) ** 2), 0.7)
add(thump(95, 40, 1.4, 3.5), 2.0, 0.55)
# Escena 2 · Mapa
add(whoosh(0.6, 400, 3500), 3.55, 0.6, 0.4)
add(paper(), 4.3, 0.8)
add(tick() * 2, 5.2, 0.8); add(thump(300, 200, 0.2, 30, 0) , 5.2, 0.15)
add(paper(0.2), 5.45, 0.6, -0.4)
typing(5.8, 6.6, 17)
# Escena 3 · Periódicos
add(thump(70, 35, 0.6, 8, 0.4), 7.4, 0.35)
for tt, pn in [(7.5, -.5), (7.75, .5), (8.0, 0)]:
    add(paper(0.3), tt, 0.9, pn)
add(whoosh(0.25, 800, 4000), 8.42, 0.4)
add(thump(130, 36, 1.8, 2.8, 0.5), 8.82, 0.95)
# Escena 4 · Himalaya
add(whoosh(1.4, 150, 900), 10.6, 0.5)
add(paper(0.2), 11.15, 0.5, -.5)
typing(11.5, 12.1, 8)
for i in range(25):
    add(tick(), 11.7 + 1.8 * (1 - (1 - i / 24) ** 2), 0.5, 0.6)
add(thump(90, 42, 1.2, 4), 13.5, 0.4)
typing(13.5, 13.9, 6)
# Escena 5 · Lago
add(ice(1.8), 15.4, 0.8)
add(whoosh(0.8, 200, 1200), 15.3, 0.4)
add(thump(60, 45, 2.0, 1.6, 0.0), 16.5, 0.25)
add(whoosh(0.3, 600, 2600), 16.45, 0.18, -.4)
add(whoosh(0.35, 500, 2200), 17.25, 0.22, -.4)
# Escena 6 · Golpe del cráneo (después de medio segundo de silencio total)
add(thump(150, 34, 2.2, 2.2, 0.6), 18.8, 1.0)
add(paper(0.3), 19.0, 0.7, -.6)
add(thump(110, 40, 1.4, 3.5, 0.3), 19.95, 0.6)
# Escena 7 · Logo
add(whoosh(0.9, 300, 2500), 21.55, 0.5)
add(thump(160, 45, 1.3, 4, 0.7), 22.32, 0.85)
add(paper(0.25), 23.0, 0.7)
add(thump(200, 90, 0.3, 14, 0.4), 23.15, 0.4)

# silencio total antes del golpe del cráneo
gate = env_curve([(0, 1), (18.55, 1), (18.6, 0), (18.79, 0), (18.8, 1), (24.5, 1)])
L *= gate; R *= gate
# mezcla: normalizar a -1 dBFS con un limitador suave
mix = np.stack([L, R], 1)
mix = np.tanh(mix / (np.abs(mix).max() + 1e-9) * 1.3) * 0.89
mix[-int(SR * .5):] *= np.linspace(1, 0, int(SR * .5))[:, None]
with wave.open(f"{BASE}/sonido.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype("<i2").tobytes())
print("sonido listo")
