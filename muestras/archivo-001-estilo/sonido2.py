"""Sonido v2 con efectos reales de Mixkit (licencia libre para videos), puestos en el cuadro exacto.
Cada efecto se alinea por su ataque: 'cuando' es el instante en que debe sonar el golpe en el video."""
import numpy as np, subprocess, wave, os

SR = 48000; DUR = 24.5; N = int(SR * DUR)
BASE = os.path.dirname(os.path.abspath(__file__)); SFX = os.path.join(BASE, "..", "sfx")
mix = np.zeros((N, 2)); rng = np.random.default_rng(5)
cache = {}


def load(name):
    if name not in cache:
        raw = subprocess.run(["ffmpeg", "-v", "quiet", "-i", f"{SFX}/{name}.mp3", "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
        cache[name] = np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)
    return cache[name]


def attack(x):
    """Instante (s) en que el sonido alcanza el 30 % de su máximo: su 'golpe'."""
    e = np.sqrt(np.convolve((x ** 2).mean(1), np.ones(480) / 480, "same"))
    return np.argmax(e > e.max() * .3) / SR


def put(name, when, gain_db=0.0, align="attack", pan=0.0, start=0.0, length=None, fade_out=0.05):
    x = load(name)
    if start or length:
        x = x[int(start * SR): int((start + length) * SR) if length else None]
    off = attack(x) if align == "attack" else 0.0
    t0 = when - off
    i0 = int(t0 * SR); a = max(0, -i0); x = x[a:]; i0 = max(0, i0)
    x = x[: max(0, N - i0)].copy()
    if len(x) == 0: return
    nf = int(fade_out * SR)
    if nf and len(x) > nf: x[-nf:] *= np.linspace(1, 0, nf)[:, None]
    g = 10 ** (gain_db / 20)
    gl, gr = g * min(1, 1 - pan), g * min(1, 1 + pan)
    mix[i0:i0 + len(x), 0] += x[:, 0] * gl; mix[i0:i0 + len(x), 1] += x[:, 1] * gr


def bed(name, t0, t1, gain_db, fade=0.6, start=0.0):
    x = load(name)[int(start * SR):]
    n = int((t1 - t0) * SR); x = x[:n].copy()
    f = int(fade * SR); env = np.ones(len(x)); env[:f] = np.linspace(0, 1, f); env[-f:] = np.linspace(1, 0, f)
    i0 = int(t0 * SR); g = 10 ** (gain_db / 20)
    mix[i0:i0 + len(x)] += x * env[:, None] * g


def typing(t0, t1, n, gain_db=-6):
    keys = ["tecla1", "tecla2", "tecla3"]
    for i in range(n):
        put(keys[i % 3], t0 + (t1 - t0) * i / max(1, n) + rng.normal(0, .01), gain_db + rng.uniform(-2, 1), pan=rng.uniform(-.3, .3))


# ---- Ambiente continuo (sin música) ----
bed("zumbido_viento", 0.0, 24.5, -14, fade=1.0, start=2.0)
bed("viento_montana", 10.3, 18.2, -4, fade=0.8, start=4.0)
bed("viento_invierno", 10.6, 14.9, -10, fade=0.6, start=1.0)
bed("latido_misterio", 15.0, 18.15, -6, fade=0.4, start=1.0)

# ---- 1 · Año 1942 ----
put("barrido_viento", 0.35, -6)
typing(0.30, 0.60, 3, -4)
for i in range(14):                       # tic del contador que va frenando
    tt = 0.45 + 1.40 * (1 - (1 - i / 13) ** 0.5)
    put("tecla3", tt, -14 + i * .3, pan=.2)
put("golpe_hondo", 1.85, 0)
put("whoosh_rapido", 3.30, -2, align="peak" if False else "attack")

# ---- 2 · Mapa ----
put("papel_desliza", 3.55, -2, pan=.3)
put("golpe_zoom", 4.55, -8)
put("papel_mueve", 4.95, 0, pan=.4)
put("papel_desliza", 5.55, -3, pan=-.4)
typing(5.75, 6.55, 17, -6)
put("whoosh_trans", 7.10, 0)

# ---- 3 · Periódicos ----
for tt, pn in [(7.27, -.4), (7.47, .4), (7.67, 0)]:
    put("periodico_cae", tt, 2, pan=pn)
put("golpe_grande", 8.25, -2)
put("golpe_terror", 8.25, -6)
put("whoosh_viento", 10.20, -2)

# ---- 4 · Himalaya ----
put("papel_desliza", 10.85, -4, pan=-.4)
typing(11.0, 11.6, 8, -7)
for i in range(16):
    put("tecla3", 11.3 + 1.7 * (1 - (1 - i / 15) ** 0.5), -16, pan=.5)
put("golpe_zoom", 13.0, -4)
put("barrido_oscuro", 14.80, -4, align="peak" if False else "attack")

# ---- 5 · Lago ----
put("cristal_suspenso", 15.05, -5)
put("barrido_viento", 15.95, -10, pan=-.4)
put("barrido_viento", 16.60, -8, pan=-.4)
put("subida_trailer", 15.57 + 1.90, -2)   # la subida termina justo cuando se cierra el círculo

# ---- 6 · Cráneo (después de un cuarto de segundo de silencio total) ----
put("golpe_hondo", 18.40, 1)
put("tambor_terror", 18.40, -1)
put("golpe_terror", 18.40, -3)
put("papel_mueve", 18.62, -1, pan=-.5)
put("barrido_viento", 19.10, -10, pan=.4)
put("golpe_zoom", 19.50, -6)

# ---- 7 · Logo ----
put("whoosh_tunel", 21.45, -5)
put("golpe_hondo", 22.30, -1)
put("periodico_cae", 22.32, -2)
put("papel_desliza", 22.98, -4)
put("campana", 23.05, -8)

# silencio total antes del golpe del cráneo y final
t = np.arange(N) / SR
gate = np.interp(t, [0, 18.12, 18.17, 18.39, 18.40, 24.0, 24.5], [1, 1, 0, 0, 1, 1, 0])
mix *= gate[:, None]
# normalizar a -1 dBFS con limitador suave
peak = np.abs(mix).max()
mix = np.tanh(mix / peak * 1.25) / np.tanh(1.25) * 0.89
with wave.open(f"{BASE}/sonido2.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(mix, -1, 1) * 32767).astype("<i2").tobytes())
print("sonido2 listo")
