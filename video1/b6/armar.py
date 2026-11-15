"""Arma la página del bloque 6 (Lo que se descartó): una ficha por cada posibilidad y un sello por cada descarte."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from partes import *
lista = lambda i, x, y, n, tam=40: f'<div class="abs" id="{i}" style="left:{x}px;top:{y}px">' + "".join(f'<div style="height:{tam+26}px;white-space:pre"><span style="color:#5cf29a;font-family:TyperB;font-size:{tam}px" id="{i}b{k}"></span><span id="{i}l{k}" style="font-family:TyperB;font-size:{tam}px;letter-spacing:4px;color:#ece5d2;text-shadow:0 2px 10px #000,0 0 30px #000"></span></div>' for k in range(n)) + '</div>'
som = lambda i, d="40deg": f'<div class="abs" id="{i}" style="width:1920px;height:1080px;background:linear-gradient({d},rgba(4,0,10,.9) 0,rgba(4,0,10,.5) 32%,transparent 58%)"></div>'
oscuro = lambda i, src: f'<img class="full" id="{i}bg" src="{src}" style="filter:blur(34px) brightness(.24)"><div class="abs" id="{i}mesh" style="width:1920px;height:1080px;mix-blend-mode:screen"></div>'
def st(i, txt, w, col): return f'''<g id="{i}" filter="url(#gastado)"><rect x="{-w/2}" y="-62" width="{w}" height="124" rx="10" fill="none" stroke="{col}" stroke-width="9"/><rect x="{-w/2+16}" y="-46" width="{w-32}" height="92" rx="5" fill="none" stroke="{col}" stroke-width="3"/>
          <text y="33" text-anchor="middle" font-family="Bebas" font-size="100" letter-spacing="10" fill="{col}">{txt}</text></g>'''

cuerpo = "\n".join([
 clip("h0", frase("h0", "Empezar a", "descartar.", "izq", 600, 210)),
 f'''<div class="scene" id="fi"><img class="full" id="fiimg" src="../b1/img/ficha.jpg">
    <div class="abs" id="fiover" style="width:1920px;height:1080px;transform-origin:center center">
      <div class="abs" id="fit0" style="left:800px;top:288px;font-family:Typer;font-size:26px;letter-spacing:8px;color:#5a4636;white-space:pre"></div>
      <div class="abs" id="fit1" style="left:796px;top:336px;font-family:TyperB;font-size:36px;line-height:1.32;letter-spacing:3px;color:#2a1d18;opacity:.88;white-space:pre"></div>
      <div class="abs" id="fit2" style="left:796px;top:486px;font-family:Typer;font-size:31px;letter-spacing:3px;color:#3a2a22;opacity:.85;white-space:pre"></div>
      <svg class="abs" width="1920" height="1080" style="mix-blend-mode:multiply">{st("fis", "DESCARTADO", 560, "#4a1f7e")}{st("fid", "DATO", 300, "#1f7d4c")}</svg></div></div>''',
 clip("h1b", som("h1bs") + lista("h1bl", 110, 690, 3, 44)),
 clip("h1c", frase("h1c", "Eran", "forasteros.", "izq", 600, 210)),
 clip("h4m"),
 clip("h5", tira("h5", 700, 150)),
 f'<div class="scene" id="h5b"><img class="full" id="h5bi" src="diario.jpg">{som("h5bg2", "90deg")}{lista("h5bl", 120, 300, 3, 56)}' + frase("h5b", "No aparece", "en ninguna.", "izq", 560, 200) + '</div>',
 f'''<div class="scene" id="h6">{oscuro("h6", "../b5/frames/b503/0150.jpg")}
   <svg class="abs" width="1920" height="1080"><line id="h6l" x1="310" y1="250" x2="310" y2="250" stroke="#5cf29a" stroke-width="3"/></svg>
   <div class="abs typer" id="h6t" style="left:310px;top:170px;font-family:TyperB;font-size:38px;letter-spacing:6px;color:#ece5d2"></div>
   <div class="abs typer" id="h6t2" style="left:310px;top:270px;font-size:26px;letter-spacing:6px;color:#5cf29a"></div>
   <div class="abs" style="left:230px;top:300px;font-family:PlayI;font-style:italic;font-size:300px;color:#5cf29a;line-height:1" id="h6q">“</div>
   <div class="abs" style="left:300px;top:470px;width:1500px"><div class="ph" style="font-size:96px;line-height:1.12"><span class="mask"><span id="h6a">Todavía no está claro</span></span></div>
     <div class="ph" style="font-size:96px;line-height:1.12"><span class="mask"><span id="h6b">qué los llevó hasta el lago</span></span></div>
     <div class="phi" style="font-size:150px;line-height:1.1;margin-top:-6px"><span class="mask" style="padding:0 22px 34px 0"><span id="h6c">ni cómo murieron.</span></span></div></div></div>''',
 clip("h8", '<div class="abs" style="width:1920px;height:1080px;background:rgba(4,0,10,.72)"></div><div class="abs typer" id="h8t" style="left:0;top:300px;width:1920px;text-align:center;font-size:36px;letter-spacing:10px;color:#ece5d2"></div><div class="abs phi" style="left:0;top:380px;width:1920px;text-align:center;font-size:320px"><span class="mask" style="padding:0 40px 70px 40px"><span id="h8q">¿Por qué?</span></span></div>'),
])
js = r'''
const INI=541.4, FINA=630.0, DUR=FINA-INI;
const aAudio=tv=>tv+INI, aVideo=ta=>ta-INI;
const ESC=[['h0',541.4,0],['fi',550.1,0],['h1b',557.9,0],['h1c',567.6,0],['fi',570.9,0],['h4m',584.1,0],['fi',587.6,0],['h5',590.1,0],['h5b',597.9,0],['h6',607.2,.6],['fi',617.7,0],['h8',624.1,.6]];
// fichas: [desde, hasta, encabezado, pregunta, la escribe de..a, razón, de..a, momento del sello, entra deslizando]
const FICHAS=[
 [550.1,557.9,'POSIBILIDAD 1','¿DESCENDIENTES DE GRIEGOS\nQUE VIVÍAN EN LA INDIA?',550.5,555.9,'',0,0,556.9,1],
 [570.9,576.4,'POSIBILIDAD 2','¿UNA FAMILIA?',571.3,572.4,'NO ERAN PARIENTES ENTRE SÍ',573.95,575.2,573.0,1],
 [576.4,582.3,'POSIBILIDAD 3','¿UN EJÉRCITO?',576.5,577.9,'HABÍA HOMBRES Y MUJERES',578.25,580.7,580.95,1],
 [582.3,584.1,'POSIBILIDAD 4','¿UNA EPIDEMIA?',582.3,583.7,'',0,0,999,1],
 [587.6,590.1,'POSIBILIDAD 4','¿UNA EPIDEMIA?',0,0,'NO ENCONTRARON NADA',587.67,588.55,588.75,0],
 [617.7,624.1,'ESTO ES DATO','14 PERSONAS DEL MEDITERRÁNEO\nMURIERON EN ESE LAGO\nHACE UNOS 200 AÑOS',619.0,623.3,'',0,0,618.45,1]];
const HITS=[[546.8,.6],[556.9,.9],[573.0,.9],[580.95,.9],[588.75,.9],[604.6,.8],[618.45,.6],[627.87,1.2]];
function lin(id,k,items){items.forEach(([txt,a],i)=>{typed($(id+'l'+i),txt,k,a,a+Math.min(.9,txt.length*.045));$(id+'b'+i).textContent=k>=a?'— ':''})}
const R={
 h0:async t=>{await cuadro($('h0i'),'frames/b601',NB601,t,541.4,0.1);enc($('h0i'),50,50,lerp(1.02,1.12,(t-541.4)/8.7));frase('h0',t,546.23,546.77);
   G.negro=1-eOut(p(t,541.4,542.2));const a=shake(t,546.8,12,.3);G.wx+=a[0];G.wy+=a[1]},
 fi:async t=>{G.ia=false;const F=FICHAS.find(f=>t>=f[0]&&t<f[1])||FICHAS[0];const [a,b,cab,q,qa,qb,r,ra,rb,ts,des]=F;
   const s=lerp(1.08,1.16,(t-a)/(b-a));$('fiimg').style.transform=`scale(${s})`;$('fiover').style.transform=`scale(${s})`;
   $('fit0').textContent=cab;if(qb>0)typed($('fit1'),q,t,qa,qb);else $('fit1').textContent=q;
   const esDato=cab==='ESTO ES DATO';$('fit1').style.fontSize=esDato?'31px':'36px';$('fit2').style.top=(q.includes('\n')?486:420)+'px';
   if(rb>0)typed($('fit2'),r,t,ra,rb);else $('fit2').textContent='';
   const k=p(t,ts-.1,ts);const el=$(esDato?'fid':'fis'),otro=$(esDato?'fis':'fid');otro.setAttribute('opacity',0);
   el.setAttribute('transform',esDato?`translate(1150 700) rotate(6) scale(${k<=0?0:lerp(2.2,1.1,eIn(k))})`:`translate(1010 690) rotate(-7) scale(${k<=0?0:lerp(2.3,1.1,eIn(k))})`);el.setAttribute('opacity',k<=0?0:lerp(.2,.92,k));
   if(des)G.wx+=(1-eExpo(p(t,a,a+.28)))*1100;const sh=shake(t,ts,esDato?10:18,.4);G.wx+=sh[0];G.wy+=sh[1]},
 h1b:async t=>{await cuadro($('h1bi'),'frames/b603',241,t,557.9,0.1);enc($('h1bi'),55,45,lerp(1.02,1.12,(t-557.9)/9.7));
   lin('h1bl',t,[['ADN SIN MEZCLA CON LA REGIÓN',558.73],['CASI NO COMÍAN MIJO',562.99],['(EL CEREAL DE ESAS MONTAÑAS)',564.61]]);$('h1bs').style.opacity=p(t,558.3,558.7)},
 h1c:async t=>{await cuadro($('h1ci'),'../b5/frames/b508',155,t,567.6,2.6);enc($('h1ci'),50,55,lerp(1.1,1.18,(t-567.6)/3.3));frase('h1c',t,568.21,568.51)},
 h4m:async t=>{await cuadro($('h4mi'),'frames/b603',241,t,584.1,6.2);enc($('h4mi'),38,50,lerp(1.5,1.62,(t-584.1)/3.5))},
 h5:async t=>{await cuadro($('h5i'),'frames/b604',NB604,t,590.1,0.1);enc($('h5i'),50,50,lerp(1.02,1.14,(t-590.1)/7.8));
   etiqueta('h5',t,590.1,597.6,90,840,'¿Y LOS ARCHIVOS?','',590.3,591.2,999,999)},
 h5b:async t=>{const u=p(t,597.9,607.2);enc($('h5bi'),38,48,lerp(1.05,1.5,eInOut(u)));
   lin('h5bl',t,[['UNA CARTA',598.03],['UN PERMISO',598.81],['UN DIARIO',600.45]]);const o=1-p(t,602.4,602.9);$('h5bl').style.opacity=o;
   $('h5bg2').style.opacity=o;if(t<602.9){$('h5bs').style.opacity=0;$('h5bf').style.opacity=0}else frase('h5b',t,604.03,604.57);
   const a=shake(t,604.6,14,.35);G.wx+=a[0];G.wy+=a[1]},
 h6:async t=>{G.ia=false;malla($('h6mesh'),t,'#2a1052','#0b3024',.6);$('h6bg').style.transform=`scale(${lerp(1.3,1.4,(t-607.2)/10.5)})`;
   typed($('h6t'),'NIRAJ RAI',t,609.75,610.6);const l=eInOut(p(t,609.0,610.2));$('h6l').setAttribute('y1',232);$('h6l').setAttribute('y2',232);$('h6l').setAttribute('x2',lerp(310,1010,l));
   typed($('h6t2'),'GENETISTA · AUTOR DEL ESTUDIO',t,608.2,609.6);$('h6t2').style.top='250px';$('h6q').style.opacity=.8*p(t,612.5,612.9);
   reveal($('h6a'),t,612.83,.4);reveal($('h6b'),t,614.19,.4);reveal($('h6c'),t,616.39,.5)},
 h8:async t=>{const i=clamp(Math.floor((t-624.1)*24*.7)+1,1,139);await pon($('h8i'),`../b1/frames/b509/${String(i).padStart(4,'0')}.jpg`);enc($('h8i'),50,50,lerp(1.3,1.1,eOut(p(t,624.1,630))));
   typed($('h8t'),'LO QUE NADIE PUEDE CONTESTAR',t,624.41,626.6);reveal($('h8q'),t,627.85,.5);
   G.ia=false;const a=shake(t,627.87,24,.5);G.wx+=a[0];G.wy+=a[1];G.wr+=a[2];G.negro=eIn(p(t,629.2,629.95))},
};
'''
import glob
n1 = len(glob.glob("frames/b601/*.jpg")); n4 = len(glob.glob("frames/b604/*.jpg"))
js = js.replace("NB601", str(n1)).replace("NB604", str(n4))
pagina("bloque6.html", cuerpo, js, '<script src="../b1/lago_b509.js"></script>\n')
print("bloque6.html listo", n1, n4)
