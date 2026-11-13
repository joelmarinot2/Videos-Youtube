"""Sonido v2 con efectos reales de Mixkit (licencia libre para videos), puestos en el cuadro exacto.
Cada efecto se alinea por su ataque: 'cuando' es el instante en que debe sonar el golpe en el video."""
import numpy as np, subprocess, wave, os

SR = 48000; DUR = 6.5; N = int(SR * DUR)
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


# ---- Presentación del avatar ----
bed("zumbido_viento", 0.0, 6.5, -14, fade=0.8, start=2.0)
put("papel_desliza", 0.40, -2, pan=-.5)
put("papel_mueve", 0.85, -3, pan=-.2)
typing(1.0, 1.6, 11, -6)
put("whoosh_trans", 2.20, -3)
put("papel_mueve", 2.17, -6, pan=-.5)
put("golpe_hondo", 3.00, 0)
put("periodico_cae", 3.02, -4)
put("papel_mueve", 3.97, -5, pan=-.5)
put("golpe_zoom", 4.25, -3)
put("papel_desliza", 4.15, -4, pan=.4)
put("campana", 4.40, -9)
# silencio total antes del golpe del cráneo y final
t = np.arange(N) / SR
gate = np.interp(t, [0, 6.0, 6.5], [1, 1, 0])
mix *= gate[:, None]
# normalizar a -1 dBFS con limitador suave
peak = np.abs(mix).max()
mix = np.tanh(mix / peak * 1.25) / np.tanh(1.25) * 0.89
with wave.open(f"{BASE}/sonido_avatar.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(mix, -1, 1) * 32767).astype("<i2").tobytes())
print("sonido avatar listo")
