"""Genera en Higgsfield los clips que faltan del Archivo 001 (Kling 2.5 Turbo Pro, 10 s, 1080p).
REGLA: solo se ejecuta con el permiso del dueño y sin pasar del monto aprobado.
Uso:  python3 generar.py enviar b7-04 b7-03 ...   (pide los clips indicados; no repite los ya pedidos)
      python3 generar.py revisar                   (consulta el estado y descarga los terminados)
La clave no está aquí: el sistema la pone sola en las peticiones a api.higgsfield.ai."""
import json, subprocess, sys, os, time

B = os.path.dirname(os.path.abspath(__file__)); EST = f"{B}/estado.json"; OUT = f"{B}/nuevos"; os.makedirs(OUT, exist_ok=True)
API = "https://api.higgsfield.ai"; T2V = "kling-video/v2.5-turbo/pro/text-to-video"; I2V = "kling-video/v2.5-turbo/pro/image-to-video"
DUR = 10; PRECIO_SEG = 0.0525
FOTOS = "/tmp/claude-0/-home-user-Videos-Youtube/d0439da4-483c-5507-a0b0-74fc8beb0f19/scratchpad/video1/material/videos e imagenes"
NEG = "text, letters, captions, subtitles, watermark, logo, cuts, scene change, distorted hands, extra fingers, deformed faces"
CINE = "Realistic cinematic shot, slow continuous camera movement, single take with no cuts, cold bluish light, very dark, deep shadows, fog, film grain, horizontal 16:9 widescreen, no text or letters."
V1942 = "Old black-and-white film from 1942, with grain, scratches and a slight projector flicker, slow continuous movement, single take with no cuts, horizontal 16:9 widescreen, no text or letters."
LAB = "Realistic cinematic shot in a dark laboratory, dim blue and green light, slow camera movement, single take with no cuts, deep shadows, horizontal 16:9 widescreen, no readable text."
MINI = "An antique Indian painting in traditional miniature style that comes to life with gentle movement, warm colors of fire and gold, aged paper, no cuts, horizontal 16:9 widescreen, no text or letters."

CLIPS = {
 "b7-04": ("b7-04-lago-caminantes", None, "Present-day image: three hikers with colorful jackets and backpacks, seen from afar and from behind, standing at the edge of a small Himalayan lake, overcast day. Present-day documentary footage, handheld camera with slight movement, cold natural light, single take with no cuts, horizontal 16:9 widescreen, no text or letters."),
 "b7-03": ("b7-03-silla-vacia", None, "The interior of a stone house on a Greek island, a set table with an empty chair, a candle slowly burning out until only smoke remains, through the window the sea at night. An antique oil painting that comes to life with very gentle movement, very dark, candlelight, craquelure of old paint, no cuts, horizontal 16:9 widescreen, no text or letters."),
 "b7-07": ("b7-07-avion-1947", None, "A four-propeller passenger airliner flies at night among clouds over a snowy mountain range and disappears into a cloud. Old black-and-white film from 1947, with grain, scratches and a slight projector flicker, slow continuous movement, single take with no cuts, horizontal 16:9 widescreen, no text or letters."),
 "b6-03": ("b6-03-microscopio", None, "A female scientist in a lab coat and gloves looks through a microscope and slowly turns the focus knob, empty Petri dishes beside her. " + LAB),
 "b5-02": ("b5-02-tubos-pipeta", None, "Hands in blue gloves transfer a liquid with a pipette into a row of small laboratory tubes, close-up. " + LAB),
 "b3-02": ("b3-02-caravana-rey", None, "A royal caravan climbs a snowy mountain trail: a king on horseback, servants, banners moving in the wind. " + MINI),
 "b4-02": ("b4-02-camarografo", None, "A cameraman seen from behind, with a large video camera on his shoulder, crouches to film ancient human skulls on the rocky shore of a mountain lake. Early-2000s documentary footage, handheld camera with slight movement, cold natural light, single take with no cuts, horizontal 16:9 widescreen, no text or letters."),
 "b4-05": ("b4-05-anillo-lanza", None, "On a dark cloth, an ancient rusted metal ring and a corroded iron spearhead, lit by a single lamp, the camera moves slowly from one to the other. Realistic cinematic macro shot, single take with no cuts, deep shadows, horizontal 16:9 widescreen, no text or letters."),
 "b4-09": ("b4-09-laboratorio-fechado", None, "A scientist in a white lab coat places a small bone fragment into a large laboratory machine with lights, and closes the lid. " + LAB),
 "b2-01": ("b2-01-guardabosques-bajando", None, "A forest ranger from India wearing a long coat and a turban, carrying a walking stick, hurries down a mountain trail toward a misty valley, seen from behind. " + V1942),
 "b2-05": ("b2-05-lago-congelandose", None, "Time-lapse: a small Himalayan lake gradually freezes over with ice and snow while clouds race past and night falls, no people. " + CINE),
 "b3-03": ("b3-03-reina-palanquin", None, "A pregnant queen of ancient India seated in an ornate palanquin carried by four servants along a snowy trail, veils moving in the wind. " + MINI),
 "b1-08": ("b1-08-orilla-huesos", None, "The camera glides slowly at ground level along the shore of a mountain lake covered with ancient human skulls and bones among stones and snow, as far as the eye can see, snowflakes falling. " + CINE),
 "b1-06": ("b1-06-cara-guardabosques", None, "Close-up of the face of a forest ranger from India, about 40 years old, with a turban and a mustache, looking down and gradually changing expression to fear and astonishment, snow in the air. " + V1942),
 "b1-02": ("b1-02-botas-piedra", None, "Ground-level close-up of old leather boots stepping on loose stones and snow on a mountain slope, step by step, a wooden walking stick planted beside them. " + V1942),
 "b1-05": ("b1-05-agua-transparente", None, "Top-down shot of the clear, shallow water of a glacial lake, gentle ripples, at the bottom pale blurry shapes can be made out among the stones, the camera descends very slowly toward the water. " + CINE),
 "b7-05": ("b7-05-mano-recoge-hueso", "b7-05-mano-recoge-hueso.jpg", "The hand in the colorful wool glove slowly picks up the small bone from among the stones and lifts it. Slow movement, static camera, fog drifting in the background. Realistic cinematic shot, cold bluish light, film grain, no cuts."),
 "b7-06": ("b7-06-lago-alejandose", "b7-06-lago-alejandose.jpg", "The camera pulls back very slowly upward and backward; clouds drift slowly between the mountains. No people. Realistic cinematic shot, cold bluish dusk light, film grain, no cuts."),
 "b7-08": ("b7-08-clave-morse", "b7-08-clave-morse.jpg", "The hand taps the telegraph key several times and the paper tape advances. Old black-and-white film from 1947, grain, scratches, slight projector flicker, no cuts."),
}


def curl(*args, data=None):
    cmd = ["curl", "-sS", "--max-time", "120", *args]
    if data is not None: cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(data)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    try: return json.loads(r.stdout)
    except Exception: return {"_texto": r.stdout[:500], "_error": r.stderr[:300]}


def estado(): return json.load(open(EST)) if os.path.exists(EST) else {}
def guardar(e): json.dump(e, open(EST, "w"), indent=1, ensure_ascii=False)


def subir(foto):
    u = curl("-X", "POST", f"{API}/files/generate-upload-url", data={"content_type": "image/jpeg"})
    if "upload_url" not in u: raise SystemExit(f"no se pudo crear la subida: {u}")
    heads = []
    for k, v in u.get("upload_headers", {}).items(): heads += ["-H", f"{k}: {v}"]
    r = subprocess.run(["curl", "-sS", "-X", "PUT", *heads, "--upload-file", f"{FOTOS}/{foto}", u["upload_url"], "-w", "%{http_code}", "-o", "/dev/null"], capture_output=True, text=True)
    if not r.stdout.startswith("2"): raise SystemExit(f"falló la subida de {foto}: {r.stdout} {r.stderr[:200]}")
    return u["public_url"]


def enviar(claves):
    e = estado()
    for k in claves:
        nombre, foto, prompt = CLIPS[k]
        if k in e and e[k].get("estado") not in ("failed", "nsfw", "canceled", "error"):
            print(f"{k}: ya estaba pedido ({e[k]['estado']}), no se repite"); continue
        intento = e.get(k, {}).get("intento", 0) + 1
        cuerpo = {"prompt": prompt, "duration": DUR, "negative_prompt": NEG}
        modelo = T2V
        if foto: cuerpo["image_url"] = subir(foto); modelo = I2V
        r = curl("-X", "POST", f"{API}/{modelo}", "-H", f"Idempotency-Key: archivo001-{k}-{intento}", data=cuerpo)
        if "request_id" not in r:
            e[k] = {"nombre": nombre, "estado": "error", "detalle": r, "intento": intento}; print(f"{k}: NO se aceptó: {r}")
        else:
            e[k] = {"nombre": nombre, "estado": r["status"], "request_id": r["request_id"], "status_url": r["status_url"], "intento": intento,
                    "costo_usd": round(DUR * PRECIO_SEG, 3), "pedido": time.strftime("%Y-%m-%d %H:%M:%S")}
            print(f"{k}: pedido ({r['status']})")
        guardar(e)


def revisar():
    e = estado(); pend = 0
    for k, v in e.items():
        if v.get("estado") in ("completed",) and os.path.exists(v.get("archivo", "")): continue
        if "status_url" not in v: continue
        if v["estado"] in ("failed", "nsfw", "canceled"): continue
        r = curl(v["status_url"]); v["estado"] = r.get("status", v["estado"])
        if v["estado"] == "completed":
            url = r["video"]["url"]; dest = f"{OUT}/{v['nombre']}.mp4"
            subprocess.run(["curl", "-sS", "-L", "--max-time", "300", "-o", dest, url]); v["archivo"] = dest; v["url"] = url
            print(f"{k}: LISTO → {os.path.basename(dest)} ({os.path.getsize(dest)/1e6:.1f} MB)")
        elif v["estado"] in ("failed", "nsfw", "canceled"):
            v["detalle"] = r; v["costo_usd"] = 0; print(f"{k}: {v['estado']} (no se cobra): {str(r)[:200]}")
        else: pend += 1; print(f"{k}: {v['estado']}")
        guardar(e)
    hechos = [v for v in e.values() if v.get("estado") == "completed"]
    print(f"--- terminados: {len(hechos)} | en proceso: {pend} | gastado: {sum(v.get('costo_usd', 0) for v in hechos):.2f} USD")
    return pend


if __name__ == "__main__":
    if sys.argv[1] == "enviar": enviar(sys.argv[2:])
    elif sys.argv[1] == "revisar": revisar()
    elif sys.argv[1] == "esperar":
        for _ in range(int(sys.argv[2]) if len(sys.argv) > 2 else 40):
            if revisar() == 0: break
            time.sleep(20)
