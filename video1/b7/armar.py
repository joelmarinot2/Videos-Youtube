"""Arma la página del bloque 7 (El cierre): el puerto, la espera, de vuelta al lago, el anuncio del archivo 002 y el logo."""
import sys, os, glob
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from partes import *
oscuro = lambda i, src: f'<img class="full" id="{i}bg" src="{src}" style="filter:blur(34px) brightness(.24)"><div class="abs" id="{i}mesh" style="width:1920px;height:1080px;mix-blend-mode:screen"></div>'
fila = lambda k, y: f'<div class="abs" id="c7r{k}" style="left:330px;top:{y}px;opacity:0"><svg width="90" height="90" style="position:absolute;left:0;top:6px"><rect x="6" y="6" width="74" height="74" rx="10" fill="none" stroke="#ece5d2" stroke-width="4" opacity=".7"/><path id="c7k{k}" d="M22 46 L40 64 L72 22" fill="none" stroke="#5cf29a" stroke-width="10" stroke-linecap="round" stroke-linejoin="round" pathLength="100" stroke-dasharray="0 100" style="filter:drop-shadow(0 0 8px rgba(92,242,154,.8))"/></svg><div class="big" id="c7t{k}" style="position:absolute;left:130px;top:0;font-size:104px;letter-spacing:6px;white-space:pre"></div></div>'

cuerpo = "\n".join([
 clip("c1"), clip("c2"), clip("c2b"), clip("c3"), clip("c3b"),
 clip("c4", '<svg class="abs" width="1920" height="1080"><line id="c4alt" x1="1740" y1="900" x2="1740" y2="900" stroke="#5cf29a" stroke-width="3" style="filter:drop-shadow(0 0 6px #5cf29a)"/><g id="c4tk"></g></svg><div class="abs big" id="c4num" style="left:1000px;top:250px;width:690px;text-align:right;font-size:210px;text-shadow:0 0 30px rgba(10,4,20,.7)"></div><div class="abs typer" id="c4m" style="left:1000px;top:462px;width:690px;text-align:right;color:#5cf29a;font-size:32px;letter-spacing:12px;text-shadow:0 1px 8px rgba(0,0,0,.9)"></div>'),
 clip("c4b"),
 clip("c4c", '<svg class="abs" width="1920" height="1080"><ellipse id="c4ring" fill="none" stroke="#5cf29a" stroke-width="5" stroke-linecap="round" pathLength="1000" style="filter:drop-shadow(0 0 8px rgba(92,242,154,.9))"/></svg>' + frase("c4c", "En el mismo", "sitio.", "izq", 620, 220)),
 clip("c5", tira("c5", 420, 150)), clip("c5b"), clip("c5c"), clip("c6"),
 f'<div class="scene" id="c7">{oscuro("c7", "../b5/frames/b503/0150.jpg")}<div class="abs typer" id="c7h" style="left:330px;top:150px;font-size:34px;letter-spacing:10px;color:#5cf29a"></div>{fila(0, 230)}{fila(1, 400)}{fila(2, 570)}'
 + '<div class="abs" id="c7r3" style="left:330px;top:760px;opacity:0"><svg width="90" height="90" style="position:absolute;left:0;top:6px"><rect id="c7box" x="6" y="6" width="74" height="74" rx="10" fill="none" stroke="#b48cff" stroke-width="5"/></svg><div class="big" id="c7t3" style="position:absolute;left:130px;top:0;font-size:104px;letter-spacing:6px;color:#b48cff;white-space:pre"></div></div></div>',
 f'''<div class="scene" id="c9"><img class="abs" src="{A}/plate_mapa.jpg" style="left:-140px;top:-80px;width:2200px;opacity:.25"><div class="abs" id="c9mesh" style="width:1920px;height:1080px"></div>
   <div class="abs" id="c9tilt" style="width:1920px;height:1080px;transform-origin:50% 60%"><div class="abs" id="c9cam" style="width:1940px;height:1100px;transform-origin:0 0">
     <svg width="1940" height="1100" viewBox="0 0 1940 1100"><g id="c9tierra"></g>
       <path id="c9lin" fill="none" stroke="#5cf29a" stroke-width="4" stroke-linecap="round" style="filter:drop-shadow(0 0 6px rgba(92,242,154,.9))"/>
       <g id="c9p1"><circle r="9" fill="rgba(92,242,154,.14)" stroke="#5cf29a" stroke-width="2.2"/><circle r="3" fill="#5cf29a"/></g>
       <g id="c9p2"><circle id="c9p2p" r="10" fill="none" stroke="#5cf29a" stroke-width="1.4"/><circle r="9" fill="rgba(92,242,154,.14)" stroke="#5cf29a" stroke-width="2.2"/><circle r="3" fill="#5cf29a"/></g>
     </svg></div></div></div>''',
 clip("c9b"),
 clip("c10", '<div class="abs" style="width:1920px;height:1080px;background:rgba(4,0,10,.6)"></div><div class="abs" style="left:0;top:270px;width:1920px;text-align:center"><div class="ph" style="font-size:110px"><span class="mask" style="padding:0 0 14px 0"><span id="c10a">¿Tienes una</span></span></div><div class="phi" style="font-size:260px;margin-top:-50px"><span class="mask" style="padding:0 30px 50px 30px"><span id="c10b">teoría?</span></span></div></div><div class="abs typer" id="c10t" style="left:0;top:760px;width:1920px;text-align:center;font-family:TyperB;font-size:46px;letter-spacing:8px;color:#ece5d2"></div><div class="abs typer" id="c10t2" style="left:0;top:836px;width:1920px;text-align:center;font-size:34px;letter-spacing:8px;color:#5cf29a"></div>'),
 f'''<div class="scene" id="c11">{fondo("c11")}
   <div class="abs typer" id="c11h" style="left:0;top:150px;width:1920px;text-align:center;font-size:44px;letter-spacing:18px;color:#5cf29a"></div>
   <div class="abs typer" id="c11a" style="left:0;top:330px;width:1920px;text-align:center;font-size:36px;letter-spacing:12px;color:#ece5d2"></div>
   <div class="abs big" id="c11w1" style="left:0;top:370px;width:1920px;text-align:center;font-size:230px;letter-spacing:10px;opacity:0">UN LAGO</div>
   <div class="abs big" id="c11w2" style="left:0;top:630px;width:1920px;text-align:center;font-size:230px;letter-spacing:10px;opacity:0">UNOS HUESOS</div>
   <svg class="abs" width="1920" height="1080"><path id="c11x1" fill="none" stroke="#b48cff" stroke-width="22" stroke-linecap="round" filter="url(#gastado)"/><path id="c11x2" fill="none" stroke="#b48cff" stroke-width="22" stroke-linecap="round" filter="url(#gastado)"/></svg></div>''',
 clip("c11b", '<div class="abs" style="width:1920px;height:1080px;background:linear-gradient(0deg,rgba(4,0,10,.9) 0,rgba(4,0,10,.45) 30%,transparent 52%)"></div><div class="abs typer" id="c11bt" style="left:0;top:800px;width:1920px;text-align:center;font-size:34px;letter-spacing:12px;color:#ece5d2"></div><svg class="abs" width="1920" height="1080"><g id="c11bm" fill="#5cf29a" style="filter:drop-shadow(0 0 8px rgba(92,242,154,.8))"></g></svg>'),
 clip("c11c", tira("c11c", 760, 170)),
 f'''<div class="scene" id="c12"><img class="full" id="c12img" src="../b1/img/lago_lejos.jpg" style="filter:blur(26px) brightness(.34) saturate(.8)"><div class="abs" id="c12mesh" style="width:1920px;height:1080px;mix-blend-mode:screen"></div>
    <svg class="abs" width="1920" height="1080"><g id="c12sim" transform="translate(960 300)">
        <circle id="c12c" r="34" fill="none" stroke="#5cf29a" stroke-width="3" stroke-dasharray="214" stroke-dashoffset="214" transform="rotate(-90)" style="filter:drop-shadow(0 0 8px rgba(92,242,154,.8))"/><circle id="c12p" r="0" fill="#5cf29a"/>
        <g id="c12cruz" stroke="#5cf29a" stroke-width="2"><line x1="-56" y1="0" x2="-42" y2="0"/><line x1="42" y1="0" x2="56" y2="0"/><line x1="0" y1="-56" x2="0" y2="-42"/><line x1="0" y1="42" x2="0" y2="56"/></g></g>
      <line id="c12line" x1="960" y1="690" x2="960" y2="690" stroke="#5cf29a" stroke-width="3" style="filter:drop-shadow(0 0 8px rgba(92,242,154,.8))"/></svg>
    <div class="abs" id="c12w1" style="left:0;top:356px;width:1920px;text-align:center;font-family:Play;font-weight:600;font-size:64px;letter-spacing:38px;color:#ece5d2;padding-left:34px;box-sizing:border-box"></div>
    <div class="abs" id="c12w2" style="left:0;top:430px;width:1920px;text-align:center;font-family:Play;font-weight:800;font-size:196px;letter-spacing:8px;color:#ece5d2;white-space:nowrap"></div>
    <div class="abs" id="c12w3" style="left:0;top:736px;width:1920px;text-align:center;font-family:Typer;font-size:50px;letter-spacing:12px;color:#5cf29a;white-space:pre"></div>
    <div class="abs" id="c12w4" style="left:0;top:850px;width:1920px;text-align:center;font-family:Typer;font-size:30px;letter-spacing:8px;color:rgba(236,229,210,.85);white-space:pre"></div></div>''',
])
js = r'''
const INI=630.0, FINA=727.0, DUR=FINA-INI;
const aAudio=tv=>tv+INI, aVideo=ta=>ta-INI;
const ESC=[['c1',630.0,0],['c2',633.6,1.0],['c2b',636.1,.8],['c3',637.9,.9],['c3b',643.7,1.0],['c4',646.6,1.0],['c4b',652.6,.9],['c4c',656.3,.8],['c5',659.3,1.0],['c5b',661.7,.9],['c5c',665.6,.9],
  ['c6',668.9,.9],['c7',677.2,.8],['c9',688.7,.8],['c9b',693.9,1.2],['c10',697.8,1.0],['c11',703.9,.6],['c11b',709.7,0],['c11c',713.4,0],['c12',718.4,.6]];
const HITS=[[658.0,.4],[710.7,.5],[721.3,.6]];
const LAGO=window.LAGO_DATA;
(function(){let h='';for(let i=0;i<=10;i++){const y=900-i*56;h+=`<line x1="1740" y1="${y}" x2="${i%5?1756:1772}" y2="${y}" stroke="#5cf29a" stroke-width="2" class="tk" data-i="${i}" opacity="0"/>`}$('c4tk').innerHTML=h;
  let m='';for(const n in MAPA2){m+=`<path d="${MAPA2[n]}" fill="${n==='India'?'#4d2f7d':n==='Greece'?'#2f7a57':'#3b2163'}" stroke="rgba(236,229,210,.3)" stroke-width="1"/>`}$('c9tierra').innerHTML=m;
  $('c12w2').innerHTML=[...'INEXPLICABLES'].map(c=>`<span style="display:inline-block">${c}</span>`).join('');
  // clave morse: puntos y rayas (sin letras)
  const cod=['...','-','.','-.','-..','.','-.-.'];let x=0,g='',n=0;const els=[];
  for(const letra of cod){for(const s of letra){const w=s==='.'?26:78;els.push([x,w,n++]);x+=w+22}x+=46}
  const off=960-(x-68)/2;for(const[ex,w,k]of els)g+=`<rect class="mo" data-k="${k}" x="${off+ex}" y="900" width="${w}" height="26" rx="13" opacity="0"/>`;$('c11bm').innerHTML=g;window.NMORSE=n})();
const KX2=20*Math.cos(25*Math.PI/180), XY2=(lon,lat)=>[(lon-5)*KX2,(54-lat)*20];
const LG=XY2(79.73,30.26), CR=XY2(24.9,35.2);
$('c9lin').setAttribute('d',`M${CR[0]} ${CR[1]} Q${(CR[0]+LG[0])/2} ${Math.min(CR[1],LG[1])-150} ${LG[0]} ${LG[1]}`);const LL=$('c9lin').getTotalLength();
const R={
 c1:async t=>{await cuadro($('c1i'),'frames/b507',N507,t,630.0,0.1);enc($('c1i'),45,50,lerp(1.02,1.1,(t-630)/4.6));G.negro=1-eOut(p(t,630.0,631.6))},
 c2:async t=>{await cuadro($('c2i'),'frames/b701',N701,t,633.6,0.1);enc($('c2i'),50,50,lerp(1.02,1.08,(t-633.6)/3.5))},
 c2b:async t=>{await cuadro($('c2bi'),'frames/b506',N506,t,636.1,0.6);enc($('c2bi'),50,50,lerp(1.02,1.08,(t-636.1)/2.8))},
 c3:async t=>{await cuadro($('c3i'),'frames/b702',N702,t,637.9,0.1);enc($('c3i'),50,48,lerp(1.02,1.14,(t-637.9)/6.8))},
 c3b:async t=>{await cuadro($('c3bi'),'frames/b703',241,t,643.7,5.4);enc($('c3bi'),58,58,lerp(1.25,1.1,eOut(p(t,643.7,647.6))))},
 c4:async t=>{await cuadro($('c4i'),'frames/b706',241,t,646.6,0.2);enc($('c4i'),50,50,lerp(1.1,1.02,(t-646.6)/7));
   const a=1-Math.pow(1-p(t,648.75,649.6),3),sale=p(t,651.4,652.0);$('c4alt').setAttribute('y2',900-a*560);$('c4alt').setAttribute('opacity',(t>=648.7?1:0)*(1-sale));
   document.querySelectorAll('#c4tk .tk').forEach(e=>e.setAttribute('opacity',(a*10>=+e.dataset.i&&t>=648.7?1:0)*(1-sale)));
   $('c4num').textContent=t>=648.7?Math.round(a*5000).toLocaleString('es-CO'):'';$('c4num').style.opacity=1-sale;typed($('c4m'),'METROS',t,649.47,649.9);$('c4m').style.opacity=1-sale},
 c4b:async t=>{await cuadro($('c4bi'),'../b1/frames/b108',241,t,652.6,1.0);enc($('c4bi'),40,70,lerp(1.02,1.12,(t-652.6)/4.6))},
 c4c:async t=>{const i=clamp(Math.floor((t-656.3)*24*.9)+10,1,139);await pon($('c4ci'),`../b1/frames/b509/${String(i).padStart(4,'0')}.jpg`);$('c4ci').style.filter='brightness(.85)';
   const L=LAGO[i-1],k=eInOut(p(t,656.6,658.0));const e=$('c4ring');e.setAttribute('cx',L[0]);e.setAttribute('cy',L[1]);e.setAttribute('rx',L[2]*1.13);e.setAttribute('ry',L[3]*1.13);
   e.setAttribute('stroke-dasharray',`${(k*1000).toFixed(0)} 1000`);e.setAttribute('opacity',k>0?1:0);frase('c4c',t,656.37,657.81)},
 c5:async t=>{await cuadro($('c5i'),'frames/b704',241,t,659.3,0.3);enc($('c5i'),50,55,lerp(1.02,1.08,(t-659.3)/3.3));
   etiqueta('c5',t,659.3,662.4,90,840,'HOY','',659.35,659.7,999,999)},
 c5b:async t=>{await cuadro($('c5bi'),'../b1/frames/b104',230,t,661.7,4.6);enc($('c5bi'),50,50,lerp(1.02,1.08,(t-661.7)/4.8))},
 c5c:async t=>{await cuadro($('c5ci'),'../b1/frames/b107',451,t,665.6,3.0);enc($('c5ci'),30,50,lerp(1.1,1.3,eInOut(p(t,665.6,669.8))))},
 c6:async t=>{await cuadro($('c6i'),'frames/b705',241,t,668.9,0.6);enc($('c6i'),55,55,lerp(1.02,1.12,(t-668.9)/9.2))},
 c7:async t=>{G.ia=false;malla($('c7mesh'),t,'#2a1052','#0b3024',.6);$('c7bg').style.transform=`scale(${lerp(1.3,1.42,(t-677.2)/11.5)})`;typed($('c7h'),'LO QUE LA CIENCIA LOGRÓ DECIRNOS',t,677.27,678.8);
   [['QUIÉNES ERAN',678.87],['DE DÓNDE VENÍAN',679.83],['QUÉ COMÍAN',681.93]].forEach(([tx,a],k)=>{$('c7r'+k).style.opacity=p(t,a-.1,a+.1);typed($('c7t'+k),tx,t,a,a+.5);
     const c=eOut(p(t,a+.45,a+.75));$('c7k'+k).setAttribute('stroke-dasharray',`${(c*100).toFixed(0)} 100`)});
   $('c7r3').style.opacity=p(t,685.6,685.9);typed($('c7t3'),'¿POR QUÉ?',t,686.1,687.2);$('c7box').setAttribute('opacity',.5+.5*Math.sin(t*5))},
 c9:async t=>{G.ia=false;malla($('c9mesh'),t,'#30115a','#0b2f24',.85);const z=lerp(1.02,1.1,p(t,688.7,695));
   $('c9cam').style.transform=`translate(${960-880*z}px,${560-430*z}px) scale(${z})`;$('c9tilt').style.transform='perspective(1900px) rotateX(10deg)';
   $('c9p1').setAttribute('transform',`translate(${CR[0]} ${CR[1]})`);$('c9p2').setAttribute('transform',`translate(${LG[0]} ${LG[1]})`);
   const lk=eInOut(p(t,691.0,693.6));$('c9lin').setAttribute('stroke-dasharray',`${(lk*LL).toFixed(1)} ${LL+20}`);$('c9lin').setAttribute('opacity',lk>0?1:0);
   const pu=((t-688.7)%1.2)/1.2;$('c9p2p').setAttribute('r',10+pu*26);$('c9p2p').setAttribute('opacity',1-pu)},
 c9b:async t=>{await cuadro($('c9bi'),'frames/b706',241,t,693.9,3.5,.9);enc($('c9bi'),50,50,lerp(1.02,1.12,(t-693.9)/5))},
 c10:async t=>{const i=clamp(170-Math.floor((t-697.8)*24*.9),1,180);await pon($('c10i'),`../b1/frames/b103/${String(i).padStart(4,'0')}.jpg`);enc($('c10i'),50,50,lerp(1.1,1.0,(t-697.8)/6.8));
   reveal($('c10a'),t,698.0,.45);reveal($('c10b'),t,698.61,.5);typed($('c10t'),'DÉJAMELA EN LOS COMENTARIOS',t,699.85,701.1);typed($('c10t2'),'LAS LEO TODAS',t,701.91,702.8);G.ia=false},
 c11:async t=>{G.ia=false;fondo('c11',t,703.9,5.8);typed($('c11h'),'PRÓXIMO ARCHIVO',t,704.37,705.3);typed($('c11a'),'LA PISTA NO ES',t,705.87,706.7);
   const w=(el,a)=>{el.style.opacity=t>=a?1:0;el.style.transform=`scale(${t>=a?1+.08*Math.exp(-(t-a)*10):1})`;el.style.color=t>=a+.5?'rgba(236,229,210,.5)':'#ece5d2'};
   w($('c11w1'),706.81);w($('c11w2'),708.03);tacha($('c11x1'),t,707.3,560,520,1360,480);tacha($('c11x2'),t,708.75,380,780,1540,740)},
 c11b:async t=>{await cuadro($('c11bi'),'frames/b708',241,t,709.7,0.5);enc($('c11bi'),42,48,lerp(1.04,1.14,(t-709.7)/3.7));typed($('c11bt'),'UNA SOLA PALABRA · EN CLAVE MORSE',t,710.07,712.9);
   const n=Math.floor(clamp((t-710.7)/2.5)*NMORSE);document.querySelectorAll('#c11bm .mo').forEach(e=>e.setAttribute('opacity',+e.dataset.k<n?1:0))},
 c11c:async t=>{await cuadro($('c11ci'),'frames/b707',241,t,713.4,0.3,1.3);enc($('c11ci'),50,52,lerp(1.03,1.1,(t-713.4)/5));
   etiqueta('c11c',t,713.6,718.2,90,820,'ARCHIVO N.º 002','UN AVIÓN · LOS ANDES',713.77,714.7,715.45,716.6);G.negro=eIn(p(t,717.6,718.4))*.7},
 c12:async t=>{G.ia=false;const u=(t-718.4)/8.6;$('c12img').style.transform=`scale(${lerp(1.3,1.42,u)})`;malla($('c12mesh'),t,'#2a1052','#0b3024',.55);
   $('c12c').setAttribute('stroke-dashoffset',214*(1-eInOut(p(t,718.5,719.2))));$('c12p').setAttribute('r',6*eBack(p(t,719.1,719.45)));
   $('c12cruz').setAttribute('opacity',p(t,719.0,719.5));$('c12sim').setAttribute('transform',`translate(960 262) rotate(${(t-718.4)*6}) scale(1.15)`);
   const k1=eExpo(p(t,720.6,721.3));$('c12w1').textContent='ARCHIVOS';$('c12w1').style.opacity=k1;$('c12w1').style.transform=`translateY(${(1-k1)*26}px)`;$('c12w1').style.filter=`blur(${(1-k1)*10}px)`;
   [...$('c12w2').children].forEach((sp,i)=>{const a=721.3+i*.035,k=eExpo(p(t,a,a+.55));sp.style.transform=`translateY(${(1-k)*50}px)`;sp.style.opacity=k;sp.style.filter=`blur(${(1-k)*14}px)`});
   const l=eInOut(p(t,722.0,722.9));$('c12line').setAttribute('x1',960-l*745);$('c12line').setAttribute('x2',960+l*745);
   typed($('c12w3'),'FIN DEL ARCHIVO N.º 001',t,723.4,724.5);typed($('c12w4'),'NARRACIÓN · JOEL MARINO',t,724.6,725.4);$('c12sim').setAttribute('opacity',1);
   $('c12w2').style.textShadow=t>722?`0 0 ${lerp(60,18,p(t,722,723.2))}px rgba(92,242,154,.28)`:'none';G.negro=Math.max(G.negro,eIn(p(t,725.8,726.9)))},
};
'''
for k in ("b507", "b701", "b506", "b702"): js = js.replace("N" + k[1:], str(len(glob.glob(f"frames/{k}/*.jpg"))))
pagina("bloque7.html", cuerpo, js, '<script src="../b1/lago_b509.js"></script>\n<script src="mapa_ea.js"></script>\n')
print("bloque7.html listo")
