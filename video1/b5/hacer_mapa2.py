"""Mapa de Europa a la India (Natural Earth, dominio público) para la línea de Creta al lago."""
import json, sys, math
src, out = sys.argv[1], sys.argv[2]
K = 20.0; KX = K * math.cos(math.radians(25)); LON0, LAT0 = 5.0, 54.0
def xy(lon, lat): return ((lon - LON0) * KX, (LAT0 - lat) * K)
d = json.load(open(src)); paises = {}
for f in d["features"]:
    pr = f["properties"]; nombre = pr.get("ADMIN") or pr.get("NAME"); g = f["geometry"]
    polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
    partes = []
    for poly in polys:
        anillo = poly[0]; lons = [p[0] for p in anillo]; lats = [p[1] for p in anillo]
        if max(lons) < -5 or min(lons) > 112 or max(lats) < -4 or min(lats) > 60: continue
        pts = []
        for lon, lat in anillo:
            x, y = xy(lon, lat)
            if not pts or abs(x - pts[-1][0]) + abs(y - pts[-1][1]) > 1.4: pts.append((x, y))
        if len(pts) < 4: continue
        area = abs(sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1] for i in range(len(pts)))) / 2
        if area < 4: continue
        partes.append("M" + "L".join("%.1f %.1f" % p for p in pts) + "Z")
    if partes: paises[nombre] = "".join(partes)
open(out, "w").write("window.MAPA2=" + json.dumps(paises, ensure_ascii=False) + ";\n")
print(len(paises), "países;", "Greece" in paises, "India" in paises, "lago", xy(79.73, 30.26), "creta", xy(24.9, 35.2))
