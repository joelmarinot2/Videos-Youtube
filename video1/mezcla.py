"""Herramientas de mezcla de sonido para el video. Todos los tiempos se dan en segundos del AUDIO original
de la narración; el video empieza en OFF. Los efectos son grabaciones reales (Mixkit), alineadas por su golpe."""
import numpy as np, subprocess, wave, os

SR = 48000
BASE = os.path.dirname(os.path.abspath(__file__)); SFX = os.path.join(BASE, "..", "sfx")
_cache = {}


class Mezcla:
    def __init__(self, off, fin, voz):
        self.off, self.fin = off, fin; self.N = int((fin - off) * SR)
        self.fx = np.zeros((self.N, 2)); self.cama = np.zeros((self.N, 2))
        self.rng = np.random.default_rng(5)
        raw = subprocess.run(["ffmpeg", "-v", "quiet", "-ss", str(off), "-t", str(fin - off), "-i", voz, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
        v = np.frombuffer(raw, np.float32).astype(np.float64); self.voz = np.zeros(self.N); self.voz[:min(len(v), self.N)] = v[:self.N]

    def load(self, name):
        if name not in _cache:
            raw = subprocess.run(["ffmpeg", "-v", "quiet", "-i", f"{SFX}/{name}.mp3", "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
            _cache[name] = np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)
        return _cache[name]

    @staticmethod
    def attack(x):
        e = np.sqrt(np.convolve((x ** 2).mean(1), np.ones(480) / 480, "same")); return np.argmax(e > e.max() * .3) / SR

    def put(self, name, when, db=0.0, pan=0.0, start=0.0, length=None, align=True, fade=0.05, destino=None):
        """Pone un efecto para que su golpe suene en 'when' (segundos del audio original)."""
        x = self.load(name)
        if start or length: x = x[int(start * SR): int((start + length) * SR) if length else None]
        t0 = when - self.off - (self.attack(x) if align else 0.0)
        i0 = int(t0 * SR); a = max(0, -i0); x = x[a:]; i0 = max(0, i0); x = x[: max(0, self.N - i0)].copy()
        if len(x) == 0: return
        nf = int(fade * SR)
        if nf and len(x) > nf: x[-nf:] *= np.linspace(1, 0, nf)[:, None]
        g = 10 ** (db / 20); d = self.fx if destino is None else destino
        d[i0:i0 + len(x), 0] += x[:, 0] * g * min(1, 1 - pan); d[i0:i0 + len(x), 1] += x[:, 1] * g * min(1, 1 + pan)

    def bed(self, name, t0, t1, db, fade=0.6, start=0.0):
        """Ambiente continuo entre t0 y t1 (se repite si el archivo es más corto)."""
        x = self.load(name)[int(start * SR):]; n = int((t1 - t0) * SR)
        if len(x) < n: x = np.concatenate([x] * (n // len(x) + 1))
        x = x[:n].copy(); f = min(int(fade * SR), n // 2); env = np.ones(n); env[:f] = np.linspace(0, 1, f); env[-f:] = np.linspace(1, 0, f)
        i0 = int((t0 - self.off) * SR); x = x[: max(0, self.N - i0)]
        self.cama[i0:i0 + len(x)] += x * env[:len(x), None] * 10 ** (db / 20)

    def tecleo(self, t0, t1, n, db=-12):
        keys = ["tecla1", "tecla2", "tecla3"]
        for i in range(n):
            self.put(keys[i % 3], t0 + (t1 - t0) * i / max(1, n) + self.rng.normal(0, .01), db + self.rng.uniform(-2, 1), pan=self.rng.uniform(-.3, .3))

    def tics(self, t0, t1, n, db=-17, pan=.2):
        for i in range(n): self.put("tecla3", t0 + (t1 - t0) * (1 - (1 - i / (n - 1)) ** 0.5), db, pan=pan)

    def silencio(self, a, b):
        """Silencio total de efectos y ambiente entre a y b (la voz no se toca)."""
        t = np.arange(self.N) / SR + self.off; g = np.interp(t, [a - .05, a, b, b + .01], [1, 0, 0, 1])
        self.fx *= g[:, None]; self.cama *= g[:, None]

    def guardar(self, out, baja_cama=0.5):
        # el ambiente baja cuando habla la voz
        env = np.sqrt(np.convolve(self.voz ** 2, np.ones(4800) / 4800, "same")); k = np.clip((20 * np.log10(env + 1e-9) + 42) / 14, 0, 1)
        k = np.convolve(k, np.ones(9600) / 9600, "same")
        cama = self.cama * (1 - baja_cama * k)[:, None]; fx = self.fx * (1 - .25 * k)[:, None]
        mix = cama + fx + self.voz[:, None]
        t = np.arange(self.N) / SR; mix *= np.interp(t, [0, .25, t[-1] - .7, t[-1]], [0, 1, 1, 0])[:, None]
        mix = np.where(np.abs(mix) > .7, np.sign(mix) * (.7 + .19 * np.tanh((np.abs(mix) - .7) / .19)), mix)   # limitador suave
        with wave.open(out, "wb") as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(mix, -1, 1) * 32767).astype("<i2").tobytes())
        return mix
