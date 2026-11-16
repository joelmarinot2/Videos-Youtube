"""Cada letra de la portada como imagen con transparencia: la cara exacta (molde) + su relieve, tomados de la portada original."""
import cv2, numpy as np, json
from PIL import Image, ImageDraw, ImageFont
F="/tmp/claude-0/-home-user-Videos-Youtube/d0439da4-483c-5507-a0b0-74fc8beb0f19/scratchpad/video1/b1/fonts/"
o=cv2.imread("original_1080.png"); res=json.load(open("letras_cara.json"))
def glifo(ch,fuente):
    f=ImageFont.truetype(fuente,400); bb=f.getbbox(ch); w,h=bb[2]-bb[0],bb[3]-bb[1]
    im=Image.new("L",(w,h),0); ImageDraw.Draw(im).text((-bb[0],-bb[1]),ch,font=f,fill=255); return np.asarray(im).astype(np.float32)/255
piezas=[]; total=np.zeros((1080,1920),np.float32)
for palabra,v in res.items():
    E=6 if palabra=="ARCHIVOS" else 10
    for k,l in enumerate(v["letras"]):
        g=glifo(l["letra"],F+v["fuente"]); gh=int(round(l["alto"])); gw=max(1,int(round(l["alto"]*l["ancho_rel"])))
        gg=cv2.resize(g,(gw,gh),interpolation=cv2.INTER_AREA); m=np.zeros((1080,1920),np.float32)
        x,y=int(round(l["x"])),int(round(l["y"])); m[y:y+gh,x:x+gw]=gg
        m=cv2.dilate(m,np.ones((3,3),np.uint8))                       # un poco del borde oscuro
        a=m.copy()
        for s in range(1,E+1): a=np.maximum(a,np.roll(np.roll(m,s,0),int(s*0.8),1))   # relieve hacia abajo-derecha
        a=cv2.GaussianBlur(a,(0,0),0.6)
        ys,xs=np.where(a>0.02); x0,y0,x1,y1=int(xs.min())-2,int(ys.min())-2,int(xs.max())+3,int(ys.max())+3
        crop=np.dstack([o[y0:y1,x0:x1],(np.clip(a[y0:y1,x0:x1],0,1)*255).astype(np.uint8)])
        nombre=f"sprites/{palabra[0].lower()}{k:02d}.png"; cv2.imwrite(nombre,crop)
        piezas.append({"palabra":palabra,"i":k,"letra":l["letra"],"src":nombre,"x":x0,"y":y0,"w":x1-x0,"h":y1-y0}); total=np.maximum(total,a)
json.dump(piezas,open("sprites.json","w"),indent=1)
al=cv2.imread("limpia_alineada.png").astype(np.float32); A=total[...,None]
sh=cv2.GaussianBlur(np.roll(np.roll(total,8,0),6,1),(0,0),8)[...,None]*0.65
fondo=al*(1-sh)
cv2.imwrite("prueba_fondo.png",(o*A+fondo*(1-A)).astype(np.uint8)); cv2.imwrite("prueba_negro.png",(o*A).astype(np.uint8))
print(len(piezas),"letras")
