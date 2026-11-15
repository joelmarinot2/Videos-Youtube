"""Piezas comunes para armar la página de cada bloque (estilos, funciones de ayuda y trozos de HTML que se repiten)."""
import os
B = os.path.dirname(os.path.abspath(__file__))
CAB, AYUDA = open(os.path.join(B, "comun.txt")).read().split("\n@@@\n")
A = "../b1/assets"

def clip(i, extra=""): return f'<div class="scene" id="{i}"><img class="full" id="{i}i">{extra}</div>'

def frase(i, a, b, lado="izq", top=600, g=210):
    if lado == "izq":
        return f'''<div class="abs" style="width:1920px;height:1080px;background:linear-gradient(90deg,rgba(4,0,10,.85) 0,rgba(4,0,10,.45) 40%,transparent 66%)" id="{i}s"></div>
    <div class="abs" id="{i}f" style="left:130px;top:{top}px"><div class="ph" style="font-size:104px"><span class="mask"><span id="{i}f1">{a}</span></span></div>
      <div class="phi" style="font-size:{g}px;margin-top:-46px"><span class="mask" style="padding:0 22px 34px 0"><span id="{i}f2">{b}</span></span></div></div>'''
    return f'''<div class="abs" style="width:1920px;height:1080px;background:linear-gradient(270deg,rgba(4,0,10,.85) 0,rgba(4,0,10,.45) 40%,transparent 66%)" id="{i}s"></div>
    <div class="abs" id="{i}f" style="left:900px;top:{top}px;width:900px;text-align:right"><div class="ph" style="font-size:104px"><span class="mask" style="padding:0 0 14px 22px"><span id="{i}f1">{a}</span></span></div>
      <div class="phi" style="font-size:{g}px;margin-top:-46px"><span class="mask" style="padding:0 0 34px 22px"><span id="{i}f2">{b}</span></span></div></div>'''

def tira(i, w=860, h=170): return f'''<div class="abs pc" id="{i}tag" style="opacity:0"><img src="{A}/tira.png" style="display:block;width:{w}px;height:{h}px">
      <div class="abs typer" id="{i}n1" style="left:60px;top:48px;font-family:TyperB;font-size:42px"></div><div class="abs typer" id="{i}n2" style="left:60px;top:100px;font-size:26px;color:#3b2a52"></div></div>'''

def foto(i, src, w=600, h=380): return f'<div class="abs pc" id="{i}" style="background:#efe9da;padding:20px 20px 26px 20px;width:{w}px;opacity:0"><div style="width:{w}px;height:{h}px;overflow:hidden"><img id="{i}i" src="{src}" style="display:block;width:{w}px;height:{h}px;object-fit:cover"></div></div>'

def fondo(i, plate="plate_periodico.jpg"): return f'<img class="abs" id="{i}plate" src="{A}/{plate}" style="left:-140px;top:-80px;width:2200px;opacity:.4"><div class="abs" id="{i}mesh" style="width:1920px;height:1080px"></div>'

def fecha(i, rot="AÑO"): return f'''<div class="abs typer" id="{i}rot" style="left:0;top:250px;width:1920px;text-align:center;color:#ece5d2;font-size:38px;letter-spacing:18px"></div>
    <div class="abs big" id="{i}num" style="left:0;top:300px;width:1920px;text-align:center;font-size:330px;letter-spacing:6px"></div>
    <svg class="abs" width="1920" height="1080"><line id="{i}line" x1="460" y1="690" x2="460" y2="690" stroke="#5cf29a" stroke-width="4" style="filter:drop-shadow(0 0 8px rgba(92,242,154,.8))"/>
      <circle id="{i}d0" cx="460" cy="690" r="0" fill="#5cf29a"/><circle id="{i}dot" cx="460" cy="690" r="0" fill="#5cf29a" style="filter:drop-shadow(0 0 10px #5cf29a)"/></svg>
    <div class="abs typer" id="{i}sub" style="left:0;top:730px;width:1920px;text-align:center;color:#5cf29a;font-size:46px;letter-spacing:14px"></div>'''

def sello(i, txt, w=470): return f'''<g id="{i}" filter="url(#gastado)"><rect x="{-w/2}" y="-62" width="{w}" height="124" rx="10" fill="none" stroke="#1f7d4c" stroke-width="9"/><rect x="{-w/2+16}" y="-46" width="{w-32}" height="92" rx="5" fill="none" stroke="#1f7d4c" stroke-width="3"/>
          <text y="33" text-anchor="middle" font-family="Bebas" font-size="100" letter-spacing="10" fill="#1f7d4c">{txt}</text></g>'''

def ficha(i, sellos="", extra=""): return f'''<div class="scene" id="{i}"><img class="full" id="{i}img" src="../b1/img/ficha.jpg">
    <div class="abs" id="{i}over" style="width:1920px;height:1080px;transform-origin:center center">
      <div class="abs" id="{i}t1" style="left:720px;top:292px;font-family:TyperB;font-size:40px;letter-spacing:4px;color:#2a1d18;opacity:.86;white-space:pre"></div>
      <div class="abs" id="{i}t2" style="left:720px;top:352px;font-family:Typer;font-size:30px;letter-spacing:3px;color:#3a2a22;opacity:.82;white-space:pre"></div>
      <svg class="abs" width="1920" height="1080" style="mix-blend-mode:multiply">{sellos}</svg>{extra}</div></div>'''

CAPAS = '''
 <div id="recre">RECREACIÓN</div>
 <div id="tinte"></div>
 <div id="leak"></div>
 <canvas id="fx" width="1920" height="1080"></canvas>
 <div id="vig"></div>
 <div id="flash"></div>
 <div id="black"></div>
</div>
'''
# Funciones de JavaScript que usan todos los bloques desde el 3
JS = r'''
async function pon(img,src){if(img.dataset.src!==src){img.dataset.src=src;img.src=src;try{await img.decode()}catch(e){}}}
async function cuadro(img,dir,n,ta,ini,s0=0,vel=1){const i=clamp(Math.floor(((ta-ini)*vel+s0)*24)+1,1,n);await pon(img,`${dir}/${String(i).padStart(4,'0')}.jpg`);return i}
function enc(img,ox,oy,s){img.style.transformOrigin=`${ox}% ${oy}%`;img.style.transform=`scale(${s})`}
function etiqueta(id,t,a,b,x,y,t1,t2,a1,b1,a2,b2){const tg=spring(p(twos(t),a,a+.5),2.4,6.5), ts=eIn(p(t,b-.4,b));
  tf($(id+'tag'),lerp(-950,x,tg)-ts*1100,y,1,lerp(-7,-2,tg),(t>=a&&t<b)?1:0);typed($(id+'n1'),t1,t,a1,b1);typed($(id+'n2'),t2,t,a2,b2)}
function fondo(id,t,a,d,c1='#3c1872',c2='#0e3a2b'){const u=(t-a)/d;tf($(id+'plate'),lerp(0,-70,u),0,lerp(1.05,1.14,u),0,.4);malla($(id+'mesh'),t,c1,c2,.9)}
// fecha grande: el número cuenta de n0 a n1 entre a y b, y la línea verde se dibuja
function fecha(id,t,rot,n0,n1,a,b,fmt=x=>String(x)){typed($(id+'rot'),rot,t,a-.25,a+.15);const k=1-Math.pow(1-p(t,a,b),3);
  $(id+'num').textContent=t>=a-.05?fmt(Math.round(lerp(n0,n1,k))):'';$(id+'num').style.transform=`scale(${t>b?1+.07*Math.exp(-(t-b)*10):1})`;
  $(id+'num').style.filter=t>b?`drop-shadow(0 0 ${lerp(40,12,p(t,b,b+.6))}px rgba(92,242,154,.45))`:'none'}
function linea(id,t,a,b,x0=460,x1=1460){const l=eInOut(p(t,a,b));$(id+'line').setAttribute('x1',x0);$(id+'d0').setAttribute('cx',x0);$(id+'line').setAttribute('x2',lerp(x0,x1,l));$(id+'dot').setAttribute('cx',lerp(x0,x1,l));
  $(id+'d0').setAttribute('r',t>=a?8:0);$(id+'dot').setAttribute('r',l>0?9:0)}
function sello(el,t,a,x,y,r,s=1){const k=p(t,a-.1,a);el.setAttribute('transform',`translate(${x} ${y}) rotate(${r}) scale(${k<=0?0:lerp(2.3*s,s,eIn(k))})`);el.setAttribute('opacity',k<=0?0:lerp(.2,.92,k))}
function tacha(el,t,a,x0,y0,x1,y1){const q=eOut(p(t,a,a+.16));el.setAttribute('d',`M${x0} ${y0} L${lerp(x0,x1,q)} ${lerp(y0,y1,q)}`);el.setAttribute('opacity',q>0?.95:0)}
function frase(id,t,a1,a2,sale=null,g=.4){$(id+'s').style.opacity=sale===null?eOut(p(t,a1-.3,a1+.2)):eOut(p(t,a1-.3,a1+.2))*(1-p(t,sale,sale+.5));
  $(id+'f').style.opacity=(t>=a1-.1&&(sale===null||t<sale+.5))?1:0;reveal($(id+'f1'),t,a1,g,sale);reveal($(id+'f2'),t,a2,g+.1,sale===null?null:sale+.1)}
let G;
// ESC = [[escena, empieza, fundido de entrada], ...]; R = {escena: función que la dibuja}
async function render(tv){
  const t=aAudio(tv);G={wx:0,wy:0,wr:0,negro:0,ia:true,calido:false,ray:0};let cur=null;
  const vis={};                                      // una misma escena puede salir varias veces en la lista
  for(let i=0;i<ESC.length;i++){const [id,a,f]=ESC[i],nx=ESC[i+1],fin=nx?nx[1]+nx[2]:1e9,on=t>=a&&t<fin;
    if(!(id in vis))vis[id]=null;if(on){vis[id]=f>0?eInOut(p(t,a,a+f)):1;cur=id}}
  for(const id in vis){const el=$(id);el.style.display=vis[id]===null?'none':'block';if(vis[id]!==null){el.style.opacity=vis[id];await R[id](t)}}
  if(typeof EXTRA==='function')EXTRA(t,cur);
  $('recre').style.opacity=G.ia?1:0;
  $('tinte').style.background=G.calido?'linear-gradient(160deg,rgba(214,138,52,.30),rgba(120,36,20,.22))':'linear-gradient(160deg,rgba(112,70,178,.30),rgba(20,60,50,.18))';
  $('world').style.transform=`translate(${G.wx}px,${G.wy}px) rotate(${G.wr}deg)`;
  let hk=0;for(const[h,a]of HITS){if(t>=h&&t<h+.45)hk=Math.max(hk,a*Math.pow(1-(t-h)/.45,2))}
  if(hk>.02){$('caR').setAttribute('dx',(12*hk).toFixed(1));$('caB').setAttribute('dx',(-12*hk).toFixed(1));$('world').style.filter='url(#ca)'}else $('world').style.filter='none';
  $('flash').style.opacity=Math.max(hk*.4,G.ray*.5);$('black').style.opacity=G.negro;
  const q=t*.3,c1=G.calido?'255,176,70':'92,242,154',c2=G.calido?'214,70,30':'176,107,255';
  $('leak').style.background=`radial-gradient(ellipse 700px 900px at ${-6+10*Math.sin(q)}% ${30+20*Math.cos(q*.8)}%,rgba(${c1},${.07+.04*Math.sin(t*.9)+hk*.25}),transparent 65%),radial-gradient(ellipse 800px 700px at ${104-8*Math.cos(q*1.2)}% ${72+14*Math.sin(q)}%,rgba(${c2},${.11+.05*Math.cos(t*.7)+hk*.2}),transparent 65%)`;
  polvo(t);
}
window.render=render;window.LISTO=Promise.resolve();
'''

def pagina(nombre, cuerpo, js, scripts=""):
    html = CAB + '<div id="stage">\n <div id="world" class="abs" style="width:1920px;height:1080px">\n' + cuerpo + "\n </div>" + CAPAS + scripts + "<script>\n" + AYUDA + js + JS + "window.DUR=DUR;window.OFF=0;window.aVideo=aVideo;\n</script>\n</body></html>\n"
    open(nombre, "w").write(html)
