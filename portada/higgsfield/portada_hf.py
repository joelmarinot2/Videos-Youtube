"""Portada animada en Higgsfield (aprobado por el dueño el 2026-11-16: 0,075 USD borrar letras + 0,525 USD animar 10 s = 0,60 USD).
Uso: python3 portada_hf.py borrar | animar <url de la imagen limpia> | revisar
La clave no está aquí: el sistema la pone sola en las peticiones a api.higgsfield.ai."""
import json, subprocess, sys, os, time
B = os.path.dirname(os.path.abspath(__file__)); EST = f"{B}/estado.json"; API = "https://api.higgsfield.ai"


def curl(*args, data=None):
    cmd = ["curl", "-sS", "--max-time", "120", *args]
    if data is not None: cmd += ["-H", "Content-Type: application/json", "-d", json.dumps(data)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    try: return json.loads(r.stdout)
    except Exception: return {"_texto": r.stdout[:500], "_error": r.stderr[:300]}


def estado(): return json.load(open(EST)) if os.path.exists(EST) else {}
def guardar(e): json.dump(e, open(EST, "w"), indent=1, ensure_ascii=False)


def subir(ruta):
    u = curl("-X", "POST", f"{API}/files/generate-upload-url", data={"content_type": "image/jpeg"})
    heads = []
    for k, v in u.get("upload_headers", {}).items(): heads += ["-H", f"{k}: {v}"]
    r = subprocess.run(["curl", "-sS", "-X", "PUT", *heads, "--upload-file", ruta, u["upload_url"], "-w", "%{http_code}", "-o", "/dev/null"], capture_output=True, text=True)
    if not r.stdout.startswith("2"): raise SystemExit(f"falló la subida: {r.stdout} {r.stderr[:200]}")
    return u["public_url"]


def pedir(clave, modelo, cuerpo, costo):
    e = estado()
    if clave in e and e[clave].get("estado") not in ("failed", "nsfw", "canceled", "error"):
        print(clave, "ya estaba pedido, no se repite:", e[clave]["estado"]); return
    r = curl("-X", "POST", f"{API}/{modelo}", "-H", f"Idempotency-Key: portada-{clave}-1", data=cuerpo)
    if "request_id" not in r: e[clave] = {"estado": "error", "detalle": r}; print("NO se aceptó:", r)
    else: e[clave] = {"estado": r["status"], "status_url": r["status_url"], "request_id": r["request_id"], "costo_usd": costo, "pedido": time.strftime("%Y-%m-%d %H:%M:%S")}; print(clave, "pedido:", r["status"])
    guardar(e)


def revisar():
    e = estado()
    for k, v in e.items():
        if "status_url" not in v or v.get("archivo"): continue
        r = curl(v["status_url"]); v["estado"] = r.get("status", v["estado"])
        if v["estado"] == "completed":
            url = (r.get("images") or [{}])[0].get("url") or (r.get("video") or {}).get("url")
            dest = f"{B}/{k}" + (".mp4" if "video" in r else ".png")
            subprocess.run(["curl", "-sS", "-L", "--max-time", "300", "-o", dest, url]); v["archivo"] = dest; v["url"] = url; print(k, "LISTO:", dest)
        elif v["estado"] in ("failed", "nsfw", "canceled"): v["costo_usd"] = 0; v["detalle"] = r; print(k, v["estado"], str(r)[:300])
        else: print(k, v["estado"])
    guardar(e)
    print("gastado: %.3f USD" % sum(v.get("costo_usd", 0) for v in e.values() if v.get("estado") == "completed"))


if __name__ == "__main__":
    if sys.argv[1] == "borrar":
        url = subir(f"{B}/original.jpg"); print("imagen subida")
        pedir("limpia", "alibaba/qwen-image-3/edit", {
            "prompt": "Remove the large golden title text \"ARCHIVOS INEXPLICABLES\" completely from the image. Fill the area where the letters were naturally with what is behind them: the old stamped paper folders, photographs and the big glowing golden question mark. Keep everything else exactly the same: the same composition, framing and camera, the round metal vault door, the thin orange and teal circles, the dark archive room, the shadowy figure, the paper clips and tape, the same colors and lighting. Do not add any new text.",
            "negative_prompt": "text, letters, title, words, typography, watermark, logo, changed composition",
            "image_urls": [url], "resolution": "2k", "aspect_ratio": "16:9"}, 0.075)
    elif sys.argv[1] == "animar":
        pedir("animada", "kling-video/v2.5-turbo/pro/image-to-video", {
            "prompt": "Cinematic animated background for a title intro. Static camera, no zoom, no camera movement. The metal rings of the round vault door rotate slowly in opposite directions. The thin orange and teal circles pulse softly with light. The big glowing golden question mark flickers like an old neon sign, with brief subtle glitch distortions. Dust particles and thin smoke drift slowly through the light rays. The shadowy figure in the background moves slightly and fades into the darkness. The stamped folders and papers stay still. Dark, mysterious, investigative atmosphere, film grain. One continuous shot, no cuts, no text, no letters.",
            "negative_prompt": "text, letters, words, title, camera movement, zoom, cuts, scene change, distortion, morphing",
            "image_url": sys.argv[2], "duration": 10}, 0.525)
    elif sys.argv[1] == "revisar": revisar()
