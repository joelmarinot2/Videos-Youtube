"""Arma la página del bloque 4 (La segunda respuesta): la expedición de 2003, las fracturas y el granizo."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from partes import *
from PIL import Image
CW, CH = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "craneo.png")).size
FX, FY, KX, KY = 0.61, 0.34, 0.50, 0.66          # dónde están la fractura y la cara dentro del recorte del cráneo
H1 = 800; W1 = round(H1 * CW / CH); X1 = 960 - W1 // 2; Y1 = 150      # cráneo completo
fx, fy = X1 + W1 * FX, Y1 + H1 * FY; kx, ky = X1 + W1 * KX, Y1 + H1 * KY
H2 = 1700; W2 = round(H2 * CW / CH); X2 = round(960 - W2 * FX); Y2 = round(700 - H2 * FY)   # cráneo muy cerca: la fractura queda en (960,700)

lista = lambda i, x, y, n, tam=40: f'<div class="abs" id="{i}" style="left:{x}px;top:{y}px">' + "".join(f'<div style="height:{tam+26}px;white-space:pre"><span style="color:#5cf29a;font-family:TyperB;font-size:{tam}px" id="{i}b{k}"></span><span id="{i}l{k}" style="font-family:TyperB;font-size:{tam}px;letter-spacing:4px;color:#ece5d2;text-shadow:0 2px 10px #000,0 0 30px #000"></span></div>' for k in range(n)) + '</div>'
som = lambda i, d="90deg": f'<div class="abs" id="{i}" style="width:1920px;height:1080px;background:linear-gradient({d},rgba(4,0,10,.88) 0,rgba(4,0,10,.5) 36%,transparent 62%)"></div>'

cuerpo = "\n".join([
 f'<div class="scene" id="m1">{fondo("m1")}{fecha("m1")}</div>',
 clip("m2", tira("m2", 980, 170)), clip("m3"), clip("m4"),
 clip("m5"), clip("m6"),
 clip("m9", '<div class="abs" style="width:1920px;height:1080px;background:linear-gradient(200deg,rgba(4,0,10,.8) 0,transparent 45%)" id="m9s"></div><div class="abs big" id="m9n" style="left:1300px;top:70px;width:500px;text-align:right;font-size:300px"></div><div class="abs typer" id="m9t" style="left:1300px;top:356px;width:500px;text-align:right;color:#5cf29a;font-size:40px;letter-spacing:10px"></div>'),
 f'''<div class="scene" id="m10"><img class="full" id="m10bg" src="frames/b406/0100.jpg" style="filter:blur(34px) brightness(.28)"><div class="abs" id="m10mesh" style="width:1920px;height:1080px;mix-blend-mode:screen"></div>
   <div class="abs" id="m10cam" style="width:1920px;height:1080px">
     <img class="abs" id="m10sk" src="craneo.png" style="left:{X1}px;top:{Y1}px;width:{W1}px;height:{H1}px;filter:drop-shadow(0 30px 50px rgba(0,0,0,.8))">
     <svg class="abs" width="1920" height="1080">
       <path id="m10l1" fill="none" stroke="#5cf29a" stroke-width="2.5"/><path id="m10l2" fill="none" stroke="#5cf29a" stroke-width="2.5"/>
       <path id="m10x1" fill="none" stroke="#b48cff" stroke-width="13" stroke-linecap="round" filter="url(#gastado)"/><path id="m10x2" fill="none" stroke="#b48cff" stroke-width="13" stroke-linecap="round" filter="url(#gastado)"/>
       <circle id="m10c" cx="{fx:.0f}" cy="{fy:.0f}" r="84" fill="none" stroke="#5cf29a" stroke-width="4" pathLength="1000" transform="rotate(-90 {fx:.0f} {fy:.0f})" style="filter:drop-shadow(0 0 8px rgba(92,242,154,.9))"/>
       <path id="m10l3" fill="none" stroke="#5cf29a" stroke-width="2"/>
     </svg>
     <div class="abs typer" id="m10t1" style="left:1340px;top:{ky-30:.0f}px;color:#ece5d2;font-family:TyperB;font-size:44px;letter-spacing:5px"></div>
     <div class="abs typer" id="m10t2" style="left:150px;top:880px;color:#ece5d2;font-family:TyperB;font-size:44px;letter-spacing:5px"></div>
     <div class="abs typer" id="m10t3" style="left:{fx+190:.0f}px;top:{fy-70:.0f}px;color:#5cf29a;font-family:TyperB;font-size:30px;letter-spacing:5px"></div>
     <div class="abs typer" id="m10t4" style="left:{fx+190:.0f}px;top:{fy-28:.0f}px;color:#ece5d2;font-size:19px;letter-spacing:3px"></div>
   </div>{tira("m10", 900, 150)}</div>''',
 clip("m12", som("m12s", "270deg") + '<div class="abs" id="m12w" style="left:1180px;top:330px;width:640px;text-align:right">' + "".join(f'<div class="big" id="m12w{k}" style="font-size:150px;letter-spacing:6px;opacity:0;text-shadow:0 4px 30px #000">{w}</div>' for k, w in enumerate(["CORTOS", "PROFUNDOS", "REDONDOS"])) + '</div>'),
 f'''<div class="scene" id="m12b"><img class="full" src="frames/b406/0100.jpg" style="filter:blur(34px) brightness(.22)"><div class="abs" id="m12bmesh" style="width:1920px;height:1080px;mix-blend-mode:screen"></div>
   <img class="abs" id="m12bsk" src="craneo.png" style="left:{X2}px;top:{Y2}px;width:{W2}px;height:{H2}px">
   <div class="abs" style="width:1920px;height:1080px;background:linear-gradient(180deg,rgba(4,0,10,.92) 0,rgba(4,0,10,.6) 30%,transparent 55%)"></div>
   <svg class="abs" width="1920" height="1080">
     <line id="m12bd" x1="960" y1="60" x2="960" y2="700" stroke="#5cf29a" stroke-width="2" stroke-dasharray="6 12" opacity=".7"/>
     <circle id="m12bo" cx="960" cy="700" r="0" fill="none" stroke="#5cf29a" stroke-width="3"/>
     <circle id="m12bc" cx="960" cy="150" r="96" fill="rgba(92,242,154,.10)" stroke="#5cf29a" stroke-width="5" style="filter:drop-shadow(0 0 12px rgba(92,242,154,.9))"/>
     <path id="m12bl" fill="none" stroke="#5cf29a" stroke-width="2.5"/>
   </svg>
   <div class="abs typer" id="m12bt1" style="left:1260px;top:150px;color:#5cf29a;font-size:30px;letter-spacing:8px"></div>
   <div class="abs typer" id="m12bt2" style="left:1260px;top:196px;color:#ece5d2;font-family:TyperB;font-size:46px;letter-spacing:5px"></div></div>''',
 f'''<div class="scene" id="m13"><img class="full" src="frames/b406/0100.jpg" style="filter:blur(34px) brightness(.22)" id="m13bg"><div class="abs" id="m13mesh" style="width:1920px;height:1080px;mix-blend-mode:screen"></div>
   <div class="abs typer" id="m13a" style="left:0;top:150px;width:1920px;text-align:center;color:#ece5d2;font-size:38px;letter-spacing:14px"></div>
   <div class="abs big" id="m13w1" style="left:0;top:200px;width:1920px;text-align:center;font-size:290px;letter-spacing:10px;opacity:0">AVALANCHA</div>
   <div class="abs typer" id="m13b" style="left:0;top:570px;width:1920px;text-align:center;color:#ece5d2;font-size:38px;letter-spacing:14px"></div>
   <div class="abs big" id="m13w2" style="left:0;top:620px;width:1920px;text-align:center;font-size:290px;letter-spacing:10px;opacity:0">BATALLA</div>
   <svg class="abs" width="1920" height="1080"><path id="m13x1" fill="none" stroke="#b48cff" stroke-width="22" stroke-linecap="round" filter="url(#gastado)"/><path id="m13x2" fill="none" stroke="#b48cff" stroke-width="22" stroke-linecap="round" filter="url(#gastado)"/></svg></div>''',
 clip("m14", som("m14s") + '<svg class="abs" width="1920" height="1080"><ellipse id="m14ring" fill="none" stroke="#5cf29a" stroke-width="5" stroke-linecap="round" pathLength="1000" style="filter:drop-shadow(0 0 8px rgba(92,242,154,.9))"/></svg>' + lista("m14li", 120, 420, 3, 52)),
 clip("m14b", '<svg class="abs" width="1920" height="1080"><line id="m14alt" x1="1740" y1="900" x2="1740" y2="900" stroke="#5cf29a" stroke-width="3" style="filter:drop-shadow(0 0 6px #5cf29a)"/><g id="m14tk"></g></svg><div class="abs big" id="m14num" style="left:1000px;top:250px;width:690px;text-align:right;font-size:210px;text-shadow:0 0 30px rgba(10,4,20,.7)"></div><div class="abs typer" id="m14m" style="left:1000px;top:462px;width:690px;text-align:right;color:#5cf29a;font-size:32px;letter-spacing:12px;text-shadow:0 1px 8px rgba(0,0,0,.9)"></div>'),
 clip("m15", '<div class="abs" id="m15s" style="width:1920px;height:1080px;background:radial-gradient(ellipse at 50% 55%,rgba(4,0,10,.6) 0,transparent 60%)"></div><div class="abs phi" style="left:0;top:330px;width:1920px;text-align:center;font-size:360px"><span class="mask" style="padding:0 30px 70px 30px"><span id="m15g">Granizo.</span></span></div>'),
 clip("m16", tira("m16", 900, 170)),
 f'<div class="scene" id="m16b">{fondo("m16b", "plate_mapa.jpg")}{fecha("m16b")}</div>',
 clip("m17", frase("m17", "La canción", "tenía razón.", "izq", 620, 190)),
 clip("m18"), clip("m18b"),
 clip("m19", '<div class="abs" style="width:1920px;height:1080px;background:repeating-linear-gradient(0deg,rgba(0,0,0,.28) 0,rgba(0,0,0,.28) 2px,transparent 2px,transparent 5px);mix-blend-mode:multiply"></div><div class="abs" style="width:1920px;height:1080px;box-shadow:inset 0 0 260px 90px rgba(0,0,0,.85);border-radius:90px"></div>'),
 ficha("m19b", sello("m19s1", "RESUELTO") + sello("m19s2", "CASO CERRADO", 640)),
 f'<div class="scene" id="m20"><img class="full" src="../b1/img/ficha.jpg" style="filter:blur(30px) brightness(.3)">{fondo("m20")}{fecha("m20")}</div>',
 clip("m20b"),
 '<div class="abs" id="lis" style="left:0;top:0;width:1920px;height:1080px;opacity:0"><div class="abs" style="width:1920px;height:1080px;background:linear-gradient(40deg,rgba(4,0,10,.9) 0,rgba(4,0,10,.5) 30%,transparent 55%)"></div>' + lista("lisl", 110, 660, 4, 46) + '</div>',
])
js = r'''
const INI=271.0, FINA=391.4, DUR=FINA-INI;
const aAudio=tv=>tv+INI, aVideo=ta=>ta-INI;
const ESC=[['m1',271.0,0],['m2',273.0,0],['m3',280.0,0],['m4',284.8,0],['m5',289.9,0],['m6',292.2,0],['m9',298.4,0],['m10',304.6,.5],['m12',320.7,0],['m12b',327.0,.5],['m13',332.2,0],
  ['m14',338.2,.5],['m14b',342.6,0],['m15',348.6,0],['m16',352.0,0],['m16b',356.6,0],['m17',361.3,.6],['m18',364.4,.8],['m18b',369.3,1.4],['m19',373.0,0],['m19b',375.4,0],['m20',383.0,.6],['m20b',386.5,0]];
const HITS=[[271.92,.6],[299.92,.4],[331.76,1.0],[334.27,.6],[336.32,.6],[348.8,1.2],[357.1,.8],[378.3,.7],[380.05,1.0],[384.82,.5]];
const FXX=__FX__, FYY=__FY__, KXX=__KX__, KYY=__KY__;
const LAGO=window.LAGO_DATA;
(function(){let h='';for(let i=0;i<=10;i++){const y=900-i*56;h+=`<line x1="1740" y1="${y}" x2="${i%5?1756:1772}" y2="${y}" stroke="#5cf29a" stroke-width="2" class="tk" data-i="${i}" opacity="0"/>`}$('m14tk').innerHTML=h})();
function lin(id,k,items){items.forEach(([txt,a],i)=>{typed($(id+'l'+i),txt,k,a,a+Math.min(.9,txt.length*.045));$(id+'b'+i).textContent=k>=a?'— ':''})}
function guia(el,t,a,x0,y0,x1,y1,x2){const k=eExpo(p(t,a,a+.45)),mx=lerp(x0,x1,Math.min(1,k*2)),my=lerp(y0,y1,Math.min(1,k*2));
  el.setAttribute('d',`M${x0} ${y0} L${mx} ${my}`+(k>.5?` L${lerp(x1,x2,(k-.5)*2)} ${y1}`:''));el.setAttribute('opacity',k>0?1:0)}
const R={
 m1:async t=>{G.ia=false;fondo('m1',t,271,2);fecha('m1',t,'AÑO',1942,2003,271.2,271.92);linea('m1',t,271.1,271.92);
   G.negro=1-eOut(p(t,271.0,271.35));G.wx-=eInExpo(p(t,272.8,273.0))*900},
 m2:async t=>{await cuadro($('m2i'),'frames/b401',187,t,273.0,0.1);enc($('m2i'),50,50,lerp(1.02,1.1,(t-273)/7));G.wx+=(1-eExpo(p(t,273.0,273.3)))*700;
   etiqueta('m2',t,274.5,279.7,90,820,'EXPEDICIÓN · AÑO 2003','CÁMARAS DE NATIONAL GEOGRAPHIC',274.8,276.0,276.7,278.2)},
 m3:async t=>{await cuadro($('m3i'),'frames/b402',241,t,280.0,0.6);enc($('m3i'),28,62,lerp(1.02,1.16,eInOut(p(t,280,284.8))))},
 m4:async t=>{await cuadro($('m4i'),'frames/b403',137,t,284.8,0.2);enc($('m4i'),50,50,lerp(1.02,1.08,(t-284.8)/5.1))},
 m5:async t=>{await cuadro($('m5i'),'frames/b404',120,t,289.9,0.6);enc($('m5i'),45,58,lerp(1.05,1.12,(t-289.9)/2.3))},
 m6:async t=>{await cuadro($('m6i'),'frames/b405',241,t,292.2,1.4,1.2);enc($('m6i'),50,55,lerp(1.04,1.1,(t-292.2)/6.2))},
 m9:async t=>{await cuadro($('m9i'),'frames/b406',161,t,298.4,0.1);enc($('m9i'),50,55,lerp(1.02,1.08,(t-298.4)/6.2));
   const k=1-Math.pow(1-p(t,299.2,299.9),3),o=1-p(t,302.6,303.2);$('m9n').textContent=t>=299.15?Math.round(k*30):'';$('m9n').style.opacity=o;$('m9s').style.opacity=o*p(t,298.9,299.3);
   $('m9n').style.transform=`scale(${t>299.9?1+.06*Math.exp(-(t-299.9)*9):1})`;typed($('m9t'),'ESQUELETOS',t,299.7,300.3);$('m9t').style.opacity=o},
 m10:async t=>{G.ia=t<305.1;malla($('m10mesh'),t,'#2a1052','#0b3024',.6);
   const z=eInOut(p(t,313.3,316.4)),s=lerp(1,1.75,z)*lerp(1,1.05,p(t,304.6,320.7));
   $('m10cam').style.transformOrigin=`${FXX}px ${FYY+60}px`;$('m10cam').style.transform=`scale(${s}) translate(${lerp(0,960-FXX,z)/s}px,${lerp(0,90,z)/s}px)`;
   $('m10sk').style.transformOrigin='50% 50%';$('m10sk').style.transform=`rotate(${1.2*Math.sin(t*.5)}deg)`;
   etiqueta('m10',t,306.5,313.2,90,90,'ALGUNOS TIENEN FRACTURAS','',306.7,307.9,999,999);
   const o=1-p(t,313.0,313.5);
   guia($('m10l1'),t,308.7,KXX+70,KYY,1250,KYY-12,1330);typed($('m10t1'),'EN LA CARA',t,309.0,309.5);tacha($('m10x1'),t,309.75,1320,KYY+2,1640,KYY-14);
   guia($('m10l2'),t,310.0,KXX-110,KYY+150,560,908,520);typed($('m10t2'),'EN LOS BRAZOS',t,310.2,310.8);tacha($('m10x2'),t,311.1,135,912,530,896);
   for(const e of ['m10l1','m10l2','m10x1','m10x2'])$(e).setAttribute('opacity',+$(e).getAttribute('opacity')*o);$('m10t1').style.opacity=o;$('m10t2').style.opacity=o;
   const c=eInOut(p(t,316.7,317.4));$('m10c').setAttribute('stroke-dasharray',`${(c*1000).toFixed(0)} 1000`);$('m10c').setAttribute('opacity',c>0?1:0);
   guia($('m10l3'),t,317.1,FXX+62,FYY-58,FXX+140,FYY-40,FXX+180);typed($('m10t3'),'ARRIBA',t,317.3,317.7);typed($('m10t4'),'EN LO MÁS ALTO\nDE LA CABEZA',t,318.0,319.5)},
 m12:async t=>{await cuadro($('m12i'),'frames/b407',192,t,320.7,0.1);enc($('m12i'),40,50,lerp(1.02,1.1,(t-320.7)/6.3));
   [321.42,322.26,323.34].forEach((a,i)=>{const e=$('m12w'+i),k=eExpo(p(t,a,a+.3));e.style.opacity=k;e.style.transform=`translateX(${(1-k)*120}px)`;e.style.color=i===2&&t>=a?'#5cf29a':'#ece5d2'});
   $('m12s').style.opacity=p(t,321.2,321.6)},
 m12b:async t=>{G.ia=false;malla($('m12bmesh'),t,'#2a1052','#0b3024',.5);const s=lerp(1,1.06,p(t,327,332.2));$('m12bsk').style.transformOrigin=`${960}px ${700}px`;
   const k=eIn(p(t,329.9,331.74)),y=lerp(150,700,k),r=lerp(96,84,k);$('m12bc').setAttribute('cy',y);$('m12bc').setAttribute('r',r);$('m12bc').setAttribute('opacity',p(t,327.3,327.7));
   $('m12bd').setAttribute('opacity',.7*p(t,329.0,329.6)*(1-p(t,331.74,332.0)));
   const w=p(t,331.74,332.2);$('m12bo').setAttribute('r',w>0?84+w*320:0);$('m12bo').setAttribute('opacity',w>0?1-w:0);
   guia($('m12bl'),t,327.6,1060,150,1180,170,1250);$('m12bl').setAttribute('opacity',+$('m12bl').getAttribute('opacity')*(1-p(t,329.7,330)));
   typed($('m12bt1'),'DEL TAMAÑO DE',t,327.7,328.3);typed($('m12bt2'),'UNA PELOTA DE BÉISBOL',t,328.3,329.4);$('m12bt1').style.opacity=$('m12bt2').style.opacity=1-p(t,329.7,330);
   const a=shake(t,331.76,22,.45);G.wx+=a[0];G.wy+=a[1];G.wr+=a[2]},
 m13:async t=>{G.ia=false;malla($('m13mesh'),t,'#2a1052','#0b3024',.6);$('m13bg').style.transform=`scale(${lerp(1.3,1.4,(t-332.2)/6)})`;
   typed($('m13a'),'NO ES UNA',t,333.26,333.8);typed($('m13b'),'NO ES UNA',t,335.24,335.9);
   const w=(el,a)=>{el.style.opacity=t>=a?1:0;el.style.transform=`scale(${t>=a?1+.08*Math.exp(-(t-a)*10):1})`;el.style.color=t>=a+.45?'rgba(236,229,210,.5)':'#ece5d2'};
   w($('m13w1'),333.88);w($('m13w2'),335.96);tacha($('m13x1'),t,334.25,330,380,1590,340);tacha($('m13x2'),t,336.3,470,800,1450,760)},
 m14:async t=>{const i=clamp(Math.floor((t-338.2)*24*.9)+1,1,139);await pon($('m14i'),`../b1/frames/b509/${String(i).padStart(4,'0')}.jpg`);$('m14i').style.filter='brightness(.8)';
   const L=LAGO[i-1],k=eInOut(p(t,338.85,339.9));const e=$('m14ring');e.setAttribute('cx',L[0]);e.setAttribute('cy',L[1]);e.setAttribute('rx',L[2]*1.13);e.setAttribute('ry',L[3]*1.13);
   e.setAttribute('stroke-dasharray',`${(k*1000).toFixed(0)} 1000`);e.setAttribute('opacity',k>0?1:0);
   lin('m14li',t,[['ALGO REDONDO',338.88],['ALGO DURO',340.06],['QUE CAE DEL CIELO',341.08]]);$('m14s').style.opacity=p(t,338.5,339)},
 m14b:async t=>{const i=clamp(160-Math.floor((t-342.6)*24),1,180);await pon($('m14bi'),`../b1/frames/b103/${String(i).padStart(4,'0')}.jpg`);enc($('m14bi'),50,50,lerp(1.1,1.0,(t-342.6)/6));
   $('m14bi').style.filter=`brightness(${lerp(1,.6,p(t,345.5,348.6))})`;
   const a=1-Math.pow(1-p(t,342.65,343.6),3),sale=p(t,346.6,347.2);$('m14alt').setAttribute('y2',900-a*560);$('m14alt').setAttribute('opacity',1-sale);
   document.querySelectorAll('#m14tk .tk').forEach(e=>e.setAttribute('opacity',(a*10>=+e.dataset.i?1:0)*(1-sale)));
   $('m14num').textContent=Math.round(a*5000).toLocaleString('es-CO');$('m14num').style.opacity=1-sale;typed($('m14m'),'METROS',t,343.3,343.7);$('m14m').style.opacity=1-sale;
   G.negro=eIn(p(t,347.6,348.5))*.9},
 m15:async t=>{await cuadro($('m15i'),'frames/b408',192,t,348.6,0.5);enc($('m15i'),50,50,lerp(1.04,1.14,(t-348.6)/3.4));
   reveal($('m15g'),t,348.78,.45);$('m15s').style.opacity=p(t,348.7,348.9);G.negro=t<348.76?1:0;const a=shake(t,348.8,28,.55);G.wx+=a[0];G.wy+=a[1];G.wr+=a[2];
   for(const r of [349.5,350.7]){if(t>=r&&t<r+.2)G.ray=Math.max(G.ray,(1-(t-r)/.2)*.7)}},
 m16:async t=>{await cuadro($('m16i'),'frames/b409',241,t,352.0,1.2);enc($('m16i'),45,50,lerp(1.02,1.1,(t-352)/4.6));
   etiqueta('m16',t,354.0,356.6,90,820,'UNIVERSIDAD DE OXFORD','SE LES PONE FECHA A LOS HUESOS',354.2,355.4,355.5,356.3)},
 m16b:async t=>{G.ia=false;fondo('m16b',t,356.6,4.7,'#30115a','#0f3a2c');fecha('m16b',t,'AÑO',2003,850,356.7,357.1);linea('m16b',t,359.0,360.2);
   typed($('m16bsub'),'HACE MÁS DE MIL AÑOS',t,359.04,360.2);const a=shake(t,357.1,12,.3);G.wx+=a[0];G.wy+=a[1]},
 m17:async t=>{G.calido=t<364.8;await cuadro($('m17i'),'../b3/frames/b301',187,t,361.3,1.5);enc($('m17i'),55,45,lerp(1.08,1.14,(t-361.3)/3.5));frase('m17',t,361.62,362.24)},
 m18:async t=>{G.calido=t<369.8;await cuadro($('m18i'),'../b3/frames/b306',230,t,364.4,1.0);enc($('m18i'),42,58,lerp(1.16,1.26,(t-364.4)/6.3))},
 m18b:async t=>{await cuadro($('m18bi'),'frames/b408',192,t,369.3,4.2);enc($('m18bi'),50,50,lerp(1.04,1.12,(t-369.3)/3.7))},
 m19:async t=>{await cuadro($('m19i'),'frames/b402',241,t,373.0,5.5);enc($('m19i'),50,50,1.06);$('m19i').style.filter='saturate(.7) contrast(1.15) brightness(1.05)';
   $('m19').style.filter=`brightness(${1+.05*Math.sin(t*40)})`},
 m19b:async t=>{G.ia=false;const s=lerp(1.04,1.14,(t-375.4)/7.6);$('m19bimg').style.transform=`scale(${s})`;$('m19bover').style.transform=`scale(${s})`;
   typed($('m19bt1'),'SEGUNDA RESPUESTA',t,375.5,376.2);typed($('m19bt2'),'GRANIZO · AÑO 850',t,376.3,377.0);
   sello($('m19s1'),t,378.3,880,540,-8);sello($('m19s2'),t,380.05,1010,710,5,1.05);
   let a=shake(t,378.3,12,.3),b=shake(t,380.05,20,.45);G.wx+=a[0]+b[0];G.wy+=a[1]+b[1]},
 m20:async t=>{G.ia=false;fondo('m20',t,383,3.5);fecha('m20',t,'ASÍ SE QUEDÓ',0,15,383.9,384.82);linea('m20',t,383.6,384.82);typed($('m20sub'),'AÑOS',t,384.85,385.3)},
 m20b:async t=>{await cuadro($('m20bi'),'frames/b502',241,t,386.5,0.3);enc($('m20bi'),50,50,lerp(1.04,1.14,(t-386.5)/4.9));G.negro=eIn(p(t,390.3,391.2))},
};
function EXTRA(t,cur){const on=t>=290.2&&t<298.4;$('lis').style.opacity=on?(1-p(t,297.9,298.4))*p(t,290.2,290.5):0;
  lin('lisl',t,[['SANDALIAS DE CUERO',290.5],['ANILLOS',292.3],['OBJETOS DE MADERA',293.58],['PUNTAS DE LANZA DE HIERRO',295.24]])}
'''.replace("__FX__", f"{fx:.1f}").replace("__FY__", f"{fy:.1f}").replace("__KX__", f"{kx:.1f}").replace("__KY__", f"{ky:.1f}")
pagina("bloque4.html", cuerpo, js, '<script src="../b1/lago_b509.js"></script>\n')
print("bloque4.html listo; cráneo", CW, CH, "fractura en", round(fx), round(fy))
