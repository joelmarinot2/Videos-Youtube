"""Convierte el mapa libre de países (Natural Earth, dominio público) en trazos para el mapa de Asia del bloque 2."""
import json, sys, math
src, out = sys.argv[1], sys.argv[2]
K = 20.0; KX = K * math.cos(math.radians(25)); LON0, LAT0 = 58.0, 56.0
def xy(lon, lat): return ((lon - LON0) * KX, (LAT0 - lat) * K)
d = json.load(open(src)); paises = {}
for f in d["features"]:
    pr = f["properties"]; nombre = pr.get("ADMIN") or pr.get("NAME"); g = f["geometry"]
    polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
    partes = []
    for poly in polys:
        anillo = poly[0]
        lons = [p[0] for p in anillo]; lats = [p[1] for p in anillo]
        if max(lons) < 50 or min(lons) > 158 or max(lats) < -16 or min(lats) > 60: continue
        pts = []; 
        for lon, lat in anillo:
            x, y = xy(lon, lat)
            if not pts or abs(x - pts[-1][0]) + abs(y - pts[-1][1]) > 1.4: pts.append((x, y))
        if len(pts) < 4: continue
        area = abs(sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1] for i in range(len(pts)))) / 2
        if area < 5: continue
        partes.append("M" + "L".join("%.1f %.1f" % p for p in pts) + "Z")
    if partes: paises[nombre] = "".join(partes)
json.dump(paises, open(out + ".json", "w"))
open(out, "w").write("window.MAPA=" + json.dumps(paises, ensure_ascii=False) + ";\n")
print(len(paises), "países;", sum(len(v) for v in paises.values()) // 1024, "KB")
for n in ["Japan", "North Korea", "South Korea", "Taiwan", "Philippines", "Vietnam", "Laos", "Cambodia", "Thailand", "Malaysia", "Indonesia", "Myanmar", "India", "China"]:
    print(n, "sí" if n in paises else "NO ESTÁ")
print("lago", xy(79.73, 30.26), "tokio", xy(139.7, 35.7))
