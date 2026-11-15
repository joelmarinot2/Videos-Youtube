import sys, json, subprocess, numpy as np
from faster_whisper import WhisperModel
f = sys.argv[1]
raw = subprocess.run(["ffmpeg","-v","quiet","-i",f,"-f","s16le","-ac","1","-ar","16000","-"],capture_output=True).stdout
a = np.frombuffer(raw, np.int16).astype(np.float32)/32768
m = WhisperModel("medium", device="cpu", compute_type="int8")
segs, _ = m.transcribe(a, language="es", word_timestamps=True, vad_filter=False, condition_on_previous_text=True,
    initial_prompt="Archivos Inexplicables. Hari Kishan Madhwal, Himalaya, Jasdhaval, Nanda Devi, Roopkund, Niraj Rai, Creta, Oxford, National Geographic.")
out = []
for s in segs:
    out.append({"ini": round(s.start,2), "fin": round(s.end,2), "texto": s.text.strip(),
                "palabras": [{"p": w.word.strip(), "ini": round(w.start,2), "fin": round(w.end,2)} for w in (s.words or [])]})
    print(f"[{s.start:7.2f} - {s.end:7.2f}] {s.text.strip()}", flush=True)
json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print("TERMINADO")
