"""Ajusta un molde de letra (tipografía) sobre cada letra de la portada para recortarlas limpias."""
import cv2, numpy as np, json
from PIL import Image, ImageDraw, ImageFont
F="/tmp/claude-0/-home-user-Videos-Youtube/d0439da4-483c-5507-a0b0-74fc8beb0f19/scratchpad/video1/b1/fonts/"
o=cv2.imread("original_1080.png").astype(np.float32); al=cv2.imread("limpia_alineada.png").astype(np.float32)
d=np.abs(cv2.GaussianBlur(o,(0,0),1.0)-cv2.GaussianBlur(al,(0,0),1.0)).max(2)
T=(d>60).astype(np.float32)
def glifo(ch,fuente,alto):
    f=ImageFont.truetype(fuente,400); bb=f.getbbox(ch); w,h=bb[2]-bb[0],bb[3]-bb[1]
    im=Image.new("L",(w+4,h+4),0); ImageDraw.Draw(im).text((2-bb[0],2-bb[1]),ch,font=f,fill=255)
    a=np.asarray(im).astype(np.float32)/255; a=a[2:-2,2:-2] if a.shape[0]>4 else a
    return a,w/h
def colocar(lienzo,g,x,y,alto,ancho_rel,esc_x=1.0):
    gh=int(round(alto)); gw=max(1,int(round(alto*ancho_rel*esc_x)))
    gg=cv2.resize(g,(gw,gh),interpolation=cv2.INTER_AREA); x=int(round(x)); y=int(round(y))
    y0,x0=max(0,y),max(0,x); y1,x1=min(1080,y+gh),min(1920,x+gw)
    if y1>y0 and x1>x0: lienzo[y0:y1,x0:x1]=np.maximum(lienzo[y0:y1,x0:x1],gg[y0-y:y1-y,x0-x:x1-x])
def puntaje(m,reg):
    y0,y1,x0,x1=reg; a=m[y0:y1,x0:x1]; b=T[y0:y1,x0:x1]; i=(a*b).sum(); u=a.sum()+b.sum()-i; return i/max(u,1)
res={}
for palabra,(ytop,alto,x0,x1) in {"ARCHIVOS":(428,72,712,1210),"INEXPLICABLES":(522,136,480,1440)}.items():
    reg=(ytop-20,ytop+alto+20,x0-30,x1+30); mejor=None
    for nombre in ["BebasNeue-Regular.ttf","Oswaldwght.ttf"]:
        gl=[glifo(c,F+nombre,alto) for c in palabra]
        for alto2 in np.arange(alto-12,alto+13,3):
            for yy in range(ytop-10,ytop+11,2):
                for ex in (0.9,1.0,1.1,1.2):
                    anchos=[alto2*r*ex for _,r in gl]; libre=(x1-x0)-sum(anchos); paso=libre/(len(palabra)-1)
                    m=np.zeros((1080,1920),np.float32); x=x0
                    for (g,r),w in zip(gl,anchos): colocar(m,g,x,yy,alto2,r,ex); x+=w+paso
                    s=puntaje(m,reg)
                    if mejor is None or s>mejor[0]: mejor=(s,nombre,alto2,yy,ex,paso)
    s,nombre,alto2,yy,ex,paso=mejor; print(palabra,"mejor",mejor)
    gl=[glifo(c,F+nombre,alto2) for c in palabra]; anchos=[alto2*r*ex for _,r in gl]
    xs=[]; x=x0
    for w in anchos: xs.append(x); x+=w+paso
    # afinar cada letra por separado (posición y ancho)
    letras=[]
    for i,((g,r),w) in enumerate(zip(gl,anchos)):
        best=None
        for dx in range(-14,15,2):
            for e2 in (0.9,0.95,1.0,1.05,1.1):
                for dy in (-4,-2,0,2,4):
                    m=np.zeros((1080,1920),np.float32); colocar(m,g,xs[i]+dx,yy+dy,alto2,r,ex*e2)
                    rx0=int(xs[i]-20); rx1=int(xs[i]+w+20); sc=puntaje(m,(yy-15,int(yy+alto2+15),rx0,rx1))
                    if best is None or sc>best[0]: best=(sc,dx,e2,dy)
        sc,dx,e2,dy=best; letras.append({"letra":palabra[i],"x":float(xs[i]+dx),"y":float(yy+dy),"alto":float(alto2),"ancho_rel":float(r*ex*e2),"puntaje":float(sc)})
    res[palabra]={"fuente":nombre,"letras":letras}
    print(" ".join("%s:%.2f"%(l["letra"],l["puntaje"]) for l in letras))
json.dump(res,open("letras.json","w"),indent=1)
# molde final
m=np.zeros((1080,1920),np.float32)
for palabra,v in res.items():
    for l in v["letras"]:
        g,r=glifo(l["letra"],F+v["fuente"],l["alto"]); colocar(m,g,l["x"],l["y"],l["alto"],l["ancho_rel"])
cv2.imwrite("molde.png",(m*255).astype(np.uint8))
vis=o.copy(); vis[...,1]=np.maximum(vis[...,1],m*255*0.7)
cv2.imwrite("molde_sobre.jpg",vis[360:720,440:1480].astype(np.uint8))
