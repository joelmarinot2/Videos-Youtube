"""Arma la página del bloque 5 (El giro): el ADN, los 23, los 14 del Mediterráneo y el año 1800."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from partes import *

lista = lambda i, x, y, n, tam=40: f'<div class="abs" id="{i}" style="left:{x}px;top:{y}px">' + "".join(f'<div style="height:{tam+26}px;white-space:pre"><span style="color:#5cf29a;font-family:TyperB;font-size:{tam}px" id="{i}b{k}"></span><span id="{i}l{k}" style="font-family:TyperB;font-size:{tam}px;letter-spacing:4px;color:#ece5d2;text-shadow:0 2px 10px #000,0 0 30px #000"></span></div>' for k in range(n)) + '</div>'
som = lambda i, d="40deg": f'<div class="abs" id="{i}" style="width:1920px;height:1080px;background:linear-gradient({d},rgba(4,0,10,.9) 0,rgba(4,0,10,.5) 32%,transparent 58%)"></div>'
oscuro = lambda i, src: f'<img class="full" id="{i}bg" src="{src}" style="filter:blur(34px) brightness(.24)"><div class="abs" id="{i}mesh" style="width:1920px;height:1080px;mix-blend-mode:screen"></div>'
grupo = lambda i, x: f'<div class="abs" id="{i}" style="left:{x}px;top:700px;width:520px;text-align:center;opacity:0"><div class="big" id="{i}n" style="font-size:190px"></div><div class="typer" id="{i}t" style="font-size:30px;letter-spacing:6px;color:#ece5d2;margin-top:-6px"></div></div>'

cuerpo = "\n".join([
 f'<div class="scene" id="g1">{fondo("g1")}{fecha("g1")}</div>',
 clip("g2", som("g2s") + lista("g2li", 110, 720, 3, 44) + '<div class="abs" style="width:1920px;height:1080px;background:linear-gradient(200deg,rgba(4,0,10,.8) 0,transparent 45%)" id="g2s2"></div><div class="abs big" id="g2n" style="left:1300px;top:70px;width:500px;text-align:right;font-size:300px"></div><div class="abs typer" id="g2t" style="left:1200px;top:356px;width:600px;text-align:right;color:#5cf29a;font-size:40px;letter-spacing:10px"></div>'),
 clip("g4", frase("g4", "Leer su", "ADN.", "izq", 600, 250)),
 f'''<div class="scene" id="g5">{oscuro("g5", "frames/b503/0150.jpg")}
   <div class="abs pc" id="g5card" style="left:410px;top:230px;width:1100px;height:620px;background:linear-gradient(135deg,#efe7d2,#ddd2b6);border-radius:22px;overflow:hidden">
     <div class="abs" style="left:0;top:0;width:1100px;height:92px;background:#2a1240"></div>
     <div class="abs typer" style="left:44px;top:28px;color:#ece5d2;font-family:TyperB;font-size:34px;letter-spacing:10px" id="g5h"></div>
     <svg class="abs" width="1100" height="620"><g id="g5hel"></g><rect x="40" y="130" width="300" height="450" rx="12" fill="none" stroke="#2a1240" stroke-width="3" opacity=".5"/></svg>
     <div class="abs big" style="left:390px;top:120px;font-size:230px;color:#2a1240">ADN</div>
     <div class="abs typer" id="g5a" style="left:392px;top:352px;line-height:1.35;font-family:TyperB;font-size:34px;letter-spacing:4px;color:#2a1d18"></div>
     <div class="abs typer" id="g5b" style="left:392px;top:462px;font-size:30px;letter-spacing:3px;color:#3a2a22"></div>
     <div class="abs typer" id="g5c" style="left:392px;top:504px;line-height:1.3;font-family:TyperB;font-size:34px;letter-spacing:3px;color:#1f7d4c"></div>
   </div></div>''',
 clip("g6"), clip("g7", tira("g7", 760, 170)), clip("g8"),
 f'''<div class="scene" id="pt">{oscuro("pt", "frames/b503/0150.jpg")}
   <svg class="abs" width="1920" height="1080"><line id="ptax" x1="240" y1="700" x2="240" y2="700" stroke="#ece5d2" stroke-width="3" opacity=".7"/><path id="ptfl" d="M0 0 L-22 -10 L-22 10 Z" fill="#ece5d2" opacity="0"/>
     <g id="ptd"></g><rect id="ptbox" x="0" y="0" width="0" height="0" rx="40" fill="none" stroke="#5cf29a" stroke-width="4" stroke-dasharray="14 12" opacity="0" style="filter:drop-shadow(0 0 8px rgba(92,242,154,.8))"/></svg>
   <div class="abs typer" id="pttm" style="left:1500px;top:724px;font-size:28px;letter-spacing:8px;color:rgba(236,229,210,.8)"></div>
   <div class="abs" id="ptcab" style="left:0;top:120px;width:1920px;text-align:center"><span class="big" id="ptn" style="font-size:230px"></span></div>
   <div class="abs typer" id="ptsub" style="left:0;top:372px;width:1920px;text-align:center;font-size:38px;letter-spacing:8px;color:#5cf29a"></div>
   <div class="abs typer" id="ptsub2" style="left:0;top:880px;width:1920px;text-align:center;font-family:TyperB;font-size:46px;letter-spacing:8px;color:#ece5d2"></div>
   {grupo("ptA", 130)}{grupo("ptB", 760)}{grupo("ptC", 1330)}
   <div class="abs" id="ptfin" style="left:110px;top:130px;opacity:0"><div class="ph" style="font-size:104px"><span class="mask"><span id="ptf1">Pero no explica</span></span></div>
      <div class="phi" style="font-size:230px;margin-top:-46px"><span class="mask" style="padding:0 22px 34px 0"><span id="ptf2">esto.</span></span></div></div></div>''',
 clip("g10a"),
 ficha("g11", sello("g11s1", "RESUELTO") + sello("g11s2", "CASO CERRADO", 640) + '<path id="g11cr" fill="none" stroke="#1a0f0a" stroke-width="9" stroke-linejoin="bevel"/><path id="g11cr2" fill="none" stroke="#1a0f0a" stroke-width="4"/>',
       '<div class="abs" style="width:1920px;height:1080px;background:linear-gradient(90deg,rgba(4,0,10,.8) 0,rgba(4,0,10,.3) 34%,transparent 52%)" id="g11s"></div><div class="abs" id="g11f" style="left:250px;top:560px"><div class="ph" style="font-size:104px"><span class="mask"><span id="g11f1">Primera</span></span></div><div class="phi" style="font-size:230px;margin-top:-46px"><span class="mask" style="padding:0 22px 34px 0"><span id="g11f2">grieta.</span></span></div></div>'),
 f'''<div class="scene" id="gm"><img class="abs" src="{A}/plate_mapa.jpg" style="left:-140px;top:-80px;width:2200px;opacity:.25"><div class="abs" id="gmmesh" style="width:1920px;height:1080px"></div>
   <div class="abs" id="gmtilt" style="width:1920px;height:1080px;transform-origin:50% 60%"><div class="abs" id="gmcam" style="width:1940px;height:1100px;transform-origin:0 0">
     <svg width="1940" height="1100" viewBox="0 0 1940 1100"><defs><filter id="brillo2" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
       <g id="gmtierra"></g><path id="gmindia" fill="#4d2f7d" stroke="#ece5d2" stroke-width="2"/><path id="gmgre" fill="#3b2163" stroke="rgba(236,229,210,.34)" stroke-width="1"/>
       <path id="gmlin" fill="none" stroke="#5cf29a" stroke-width="4" stroke-linecap="round" style="filter:drop-shadow(0 0 6px rgba(92,242,154,.9))"/>
       <g id="gmp1"><circle id="gmp1p" r="10" fill="none" stroke="#5cf29a" stroke-width="1.4"/><circle r="9" fill="rgba(92,242,154,.14)" stroke="#5cf29a" stroke-width="2.2"/><circle r="3" fill="#5cf29a"/></g>
       <g id="gmp2"><circle id="gmp2p" r="10" fill="none" stroke="#5cf29a" stroke-width="1.4"/><circle r="9" fill="rgba(92,242,154,.14)" stroke="#5cf29a" stroke-width="2.2"/><circle r="3" fill="#5cf29a"/></g>
       <text id="gmt1" font-family="TyperB" font-size="15" letter-spacing="3" fill="#5cf29a"></text><text id="gmt2" font-family="TyperB" font-size="13" letter-spacing="3" fill="#5cf29a"></text><text id="gmt3" font-family="TyperB" font-size="15" letter-spacing="3" fill="#5cf29a" text-anchor="end"></text>
       <text id="gmt4" font-family="Typer" font-size="13" letter-spacing="7" fill="rgba(236,229,210,.7)"></text>
     </svg></div></div>
   <div class="abs big" id="gmw1" style="left:0;top:180px;width:1920px;text-align:center;font-size:300px;letter-spacing:14px;opacity:0;text-shadow:0 6px 40px #000">INDIA</div>
   <div class="abs big" id="gmw2" style="left:0;top:520px;width:1920px;text-align:center;font-size:300px;letter-spacing:14px;opacity:0;text-shadow:0 6px 40px #000">ASIA</div>
   <svg class="abs" width="1920" height="1080"><path id="gmx1" fill="none" stroke="#b48cff" stroke-width="22" stroke-linecap="round" filter="url(#gastado)"/><path id="gmx2" fill="none" stroke="#b48cff" stroke-width="22" stroke-linecap="round" filter="url(#gastado)"/></svg>
   <div class="abs" id="gmkm" style="left:0;top:90px;width:1920px;text-align:center;opacity:0"><span class="big" id="gmkmn" style="font-size:230px;text-shadow:0 6px 40px #000"></span><span class="typer" style="font-size:54px;letter-spacing:8px;color:#5cf29a;margin-left:26px;text-shadow:0 2px 12px #000">KM</span></div></div>''',
 f'''<div class="scene" id="g15">{oscuro("g15", "frames/b504/0200.jpg")}
   <div class="abs" style="left:230px;top:250px;font-family:PlayI;font-style:italic;font-size:300px;color:#5cf29a;line-height:1;opacity:.8" id="g15q">“</div>
   <div class="abs" style="left:300px;top:420px;width:1400px"><div class="ph" style="font-size:120px;line-height:1.1"><span class="mask"><span id="g15a">Quedaron</span></span></div>
     <div class="phi" style="font-size:170px;line-height:1.08;margin-top:-10px"><span class="mask" style="padding:0 22px 20px 0"><span id="g15b">extremadamente</span></span></div>
     <div class="phi" style="font-size:170px;line-height:1.08;margin-top:-20px"><span class="mask" style="padding:0 22px 34px 0"><span id="g15c">sorprendidos.</span></span></div></div>
   <svg class="abs" width="1920" height="1080"><line id="g15l" x1="310" y1="250" x2="310" y2="250" stroke="#5cf29a" stroke-width="3"/></svg>
   <div class="abs typer" id="g15t" style="left:310px;top:196px;font-size:30px;letter-spacing:6px;color:#ece5d2"></div></div>''',
 clip("g16", frase("g16", "Y falta", "lo peor.", "izq", 600, 230)),
 clip("g17", tira("g17", 800, 170)),
 f'''<div class="scene" id="g17b">{fondo("g17b", "plate_mapa.jpg")}{fecha("g17b")}
   <svg class="abs" width="1920" height="1080"><path id="g17x" fill="none" stroke="#b48cff" stroke-width="22" stroke-linecap="round" filter="url(#gastado)"/></svg>
   <div class="abs typer" id="g17y1" style="left:360px;top:718px;width:200px;text-align:center;color:#ece5d2;font-size:38px;letter-spacing:4px"></div>
   <div class="abs typer" id="g17y2" style="left:1360px;top:718px;width:200px;text-align:center;color:#5cf29a;font-size:38px;letter-spacing:4px;font-family:TyperB"></div></div>''',
 clip("g18"), clip("g19", tira("g19", 760, 170)), clip("g19b", tira("g19b", 800, 170)),
 clip("g21", '<div class="abs" style="width:1920px;height:1080px;background:rgba(4,0,10,.62)"></div>' + "".join(f'<div class="abs" id="g21c{k}" style="left:{140+k*580}px;top:300px;width:500px;text-align:center;opacity:0"><div class="big" style="font-size:380px;color:{c}">{n}</div><div class="typer" style="font-family:TyperB;font-size:46px;letter-spacing:10px;color:#ece5d2;margin-top:-10px">{w}</div><div class="typer" id="g21e{k}" style="font-size:30px;letter-spacing:6px;color:#5cf29a;margin-top:14px"></div></div>' for k, (n, w, c) in enumerate([("3", "GRUPOS", "#ece5d2"), ("2", "ÉPOCAS", "#ece5d2"), ("1", "LAGO", "#5cf29a")]))),
 clip("g22"),
])
js = r'''
const INI=391.4, FINA=541.4;
const CORTES=[[491.25,495.21]];                         // segunda vez que dice "cuando le ponen fecha a estos 14 esqueletos"
const DUR=FINA-INI-CORTES.reduce((s,c)=>s+c[1]-c[0],0);
function aAudio(tv){let t=tv+INI;for(const[a,b]of CORTES){if(t>=a)t+=b-a}return t}
function aVideo(ta){let d=0;for(const[a,b]of CORTES){if(ta>=b)d+=b-a;else if(ta>a)d+=ta-a}return ta-INI-d}
const ESC=[['g1',391.4,0],['g2',393.6,0],['g4',402.6,0],['g5',405.3,.5],['g6',412.0,0],['g7',418.5,0],['g8',424.5,0],['pt',428.2,0],['g10a',434.6,0],['pt',437.0,0],['g11',448.2,0],['pt',452.7,0],
  ['gm',458.3,0],['g15',476.2,.6],['g16',484.1,0],['g17',487.7,0],['g17b',495.4,0],['g18',503.4,.8],['g19',506.7,.8],['g19b',512.2,0],['pt',518.2,.6],['g21',527.3,0],['g22',533.2,0],['pt',538.0,.5]];
const HITS=[[392.92,.6],[403.32,.8],[448.86,.9],[456.44,1.2],[466.0,.4],[485.14,.7],[498.87,1.2],[521.99,.8],[527.32,.5],[528.75,.5],[530.25,.7],[540.13,.9]];
const LAGO=window.LAGO_DATA;
function lin(id,k,items){items.forEach(([txt,a],i)=>{typed($(id+'l'+i),txt,k,a,a+Math.min(.9,txt.length*.045));$(id+'b'+i).textContent=k>=a?'— ':''})}
// ----- las 38 personas, como puntos -----
const NP=38, RAD=27;
const P_FILA=i=>[960+((i%19)-9)*88,520+Math.floor(i/19)*96];                       // dos filas de 19
const TIEMPO=(()=>{const g=[[9,470],[8,900],[6,1330]],o=[];for(const[n,x]of g)for(let k=0;k<n;k++)o.push([x+((k%3)-1)*62,660-Math.floor(k/3)*62]);return o})();   // tres montones sobre la línea del tiempo
function P_GRUPO(i){if(i<23)return[390+((i%6)-2.5)*66,330+Math.floor(i/6)*66];if(i<37){const k=i-23;return[1020+((k%5)-2)*72,360+Math.floor(k/5)*72]}return[1590,432]}
(function(){let h='';for(let i=0;i<NP;i++)h+=`<circle id="pd${i}" r="${RAD}" fill="none" stroke="rgba(236,229,210,.35)" stroke-width="2.5"/>`;$('ptd').innerHTML=h;
  // mapa de Europa a la India
  let m='';for(const n in MAPA2){if(n==='India'||n==='Greece')continue;m+=`<path d="${MAPA2[n]}" fill="#3b2163" stroke="rgba(236,229,210,.3)" stroke-width="1"/>`}
  $('gmtierra').innerHTML=m;$('gmindia').setAttribute('d',MAPA2['India']);$('gmgre').setAttribute('d',MAPA2['Greece'])})();
const KX2=20*Math.cos(25*Math.PI/180), XY2=(lon,lat)=>[(lon-5)*KX2,(54-lat)*20];
const LG=XY2(79.73,30.26), CR=XY2(24.9,35.2), GR=XY2(22.4,39.4);
$('gmlin').setAttribute('d',`M${CR[0]} ${CR[1]} Q${(CR[0]+LG[0])/2} ${Math.min(CR[1],LG[1])-150} ${LG[0]} ${LG[1]}`);const LL=$('gmlin').getTotalLength();
const CAMM=[[458.3,1290,470,1.75],[464.4,1300,460,1.85],[466.3,430,330,2.5],[472.6,410,335,2.9],[474.4,880,430,1.02],[476.3,880,430,1.06]];
function camm(t){let i=0;while(i<CAMM.length-2&&t>=CAMM[i+1][0])i++;const a=CAMM[i],b=CAMM[i+1],k=eInOut(p(t,a[0],b[0]));return[lerp(a[1],b[1],k),lerp(a[2],b[2],k),lerp(a[3],b[3],k)]}
function punto(i,x,y,estado,brillo=0){const e=$('pd'+i);e.setAttribute('cx',x);e.setAttribute('cy',y);
  const col={v:'none',c:'#ece5d2',g:'#5cf29a',m:'#b48cff',d:'rgba(236,229,210,.32)'}[estado];e.setAttribute('fill',col);
  e.setAttribute('stroke',estado==='v'?'rgba(236,229,210,.35)':estado==='d'?'none':col);e.setAttribute('r',RAD*(1+brillo*.5));
  e.style.filter=(estado==='g'||estado==='m')?`drop-shadow(0 0 ${8+brillo*18}px ${col})`:'none'}
function grp(id,t,a,n,txt,col){const k=p(t,a,a+.3);$(id).style.opacity=k;$(id+'n').textContent=n;$(id+'n').style.color=col;$(id+'n').style.transform=`scale(${t>=a?1+.1*Math.exp(-(t-a)*9):1})`;typed($(id+'t'),txt,t,a+.1,a+.9)}
const R={
 g1:async t=>{G.ia=false;fondo('g1',t,391.4,2.2);fecha('g1',t,'AÑO',2003,2019,392.2,392.92);linea('g1',t,392.1,392.92);G.negro=1-eOut(p(t,391.4,391.9));G.wx-=eInExpo(p(t,393.4,393.6))*900},
 g2:async t=>{await cuadro($('g2i'),'frames/b501',222,t,393.6,0.1);enc($('g2i'),50,50,lerp(1.02,1.1,(t-393.6)/9));G.wx+=(1-eExpo(p(t,393.6,393.9)))*700;
   lin('g2li',t,[['INDIA',394.9],['ESTADOS UNIDOS',395.75],['ALEMANIA',396.7]]);const o=1-p(t,397.6,398.1);$('g2li').style.opacity=o;$('g2s').style.opacity=o*p(t,394.5,394.9);
   const k=1-Math.pow(1-p(t,398.3,399.0),3),o2=p(t,398.1,398.4)*(1-p(t,401.9,402.5));$('g2n').textContent=t>=398.25?Math.round(k*38):'';$('g2n').style.opacity=o2;$('g2s2').style.opacity=o2;
   $('g2n').style.transform=`scale(${t>399?1+.06*Math.exp(-(t-399)*9):1})`;typed($('g2t'),'ESQUELETOS DEL LAGO',t,399.2,400.2);$('g2t').style.opacity=o2},
 g4:async t=>{await cuadro($('g4i'),'frames/b503',240,t,402.6,0.2);enc($('g4i'),50,45,lerp(1.04,1.1,(t-402.6)/2.7));frase('g4',t,402.7,403.3);const a=shake(t,403.32,14,.35);G.wx+=a[0];G.wy+=a[1]},
 g5:async t=>{G.ia=false;malla($('g5mesh'),t,'#2a1052','#0b3024',.6);$('g5bg').style.transform=`scale(${lerp(1.3,1.4,(t-405.3)/6.7)})`;
   const k=spring(p(twos(t),405.6,406.3),2.2,6.2);tf($('g5card'),0,lerp(900,0,k),lerp(.96,1.02,p(t,405.6,412)),lerp(-9,-2,k)+.4*Math.sin(t*.8),k>0?1:0);
   typed($('g5h'),'IDENTIFICACIÓN',t,406.4,407.2);typed($('g5a'),'UNA CÉDULA QUE LLEVAS\nPOR DENTRO',t,407.3,408.9);typed($('g5b'),'DICE:',t,409.68,409.95);typed($('g5c'),'¿DE DÓNDE VENÍAN\nTUS ANTEPASADOS?',t,410.1,411.9);
   let h='',ph=t*1.6;for(let s=0;s<2;s++){let d='';for(let y=0;y<=420;y+=6){const x=190+(s?-1:1)*90*Math.sin(y*.03+ph);d+=(y?'L':'M')+x.toFixed(1)+' '+(145+y)}h+=`<path d="${d}" fill="none" stroke="${s?'#1f7d4c':'#2a1240'}" stroke-width="7" stroke-linecap="round"/>`}
   for(let y=12;y<=420;y+=28){const dx=90*Math.sin(y*.03+ph);h+=`<line x1="${(190-dx).toFixed(1)}" y1="${145+y}" x2="${(190+dx).toFixed(1)}" y2="${145+y}" stroke="#2a1240" stroke-width="3" opacity="${(.25+.55*Math.abs(Math.sin(y*.03+ph))).toFixed(2)}"/>`}
   $('g5hel').innerHTML=h},
 g6:async t=>{await cuadro($('g6i'),'frames/b503',240,t,412.0,3.3);enc($('g6i'),50,45,lerp(1.1,1.2,(t-412)/6.5))},
 g7:async t=>{await cuadro($('g7i'),'frames/b505',155,t,418.5,0.1);enc($('g7i'),45,50,lerp(1.02,1.1,(t-418.5)/6));
   etiqueta('g7',t,418.6,424.3,90,820,'UN SOLO GRUPO','UNA SOLA TORMENTA',418.78,419.8,421.5,422.6)},
 g8:async t=>{await cuadro($('g8i'),'frames/b504',240,t,424.5,0.1);enc($('g8i'),45,40,lerp(1.02,1.1,(t-424.5)/3.7))},
 g10a:async t=>{await cuadro($('g10ai'),'frames/b504',240,t,434.6,3.9);enc($('g10ai'),50,38,lerp(1.25,1.35,(t-434.6)/2.4))},
 pt:async t=>{G.ia=false;malla($('ptmesh'),t,'#2a1052','#0b3024',.6);$('ptbg').style.transform=`scale(${1.3+.04*Math.sin(t*.2)})`;
   const fase=t<434.6?1:t<448.2?2:t<458.3?3:t<527.3?4:5;
   let cab='',sub='',sub2='';$('ptax').setAttribute('opacity',0);$('ptfl').setAttribute('opacity',0);$('pttm').textContent='';$('ptbox').setAttribute('opacity',0);
   for(const g of ['ptA','ptB','ptC'])$(g).style.opacity=0;$('ptfin').style.opacity=0;
   if(fase===1){                                           // 23 personas del sur de Asia
     const n=Math.floor(clamp((t-428.24)/1.0)*23);for(let i=0;i<NP;i++){const[x,y]=P_FILA(i);punto(i,x,y,i<n?'c':'v',i===n-1?1:0);$('pd'+i).setAttribute('opacity',1)}
     cab=t>=428.24?String(n):'';sub=t>=429.3?'PERSONAS':'';typed($('ptsub2'),'ANTEPASADOS DEL SUR DE ASIA',t,429.64,431.2);
   }else if(fase===2){                                     // no murieron al mismo tiempo: la línea del tiempo
     const k=eInOut(p(t,441.3,443.8));const l=eInOut(p(t,437.2,438.6));$('ptax').setAttribute('opacity',.7);$('ptax').setAttribute('x2',lerp(240,1680,l));
     $('ptfl').setAttribute('transform',`translate(${lerp(240,1680,l)+20} 700)`);$('ptfl').setAttribute('opacity',l>0?.8:0);typed($('pttm'),'TIEMPO',t,437.9,438.4);
     const k0=eInOut(p(t,437.0,438.3));
     for(let i=0;i<NP;i++){const f0=P_FILA(i);if(i<23){const a0=[900+((i%4)-1.5)*62,640-Math.floor(i/4)*62],b=TIEMPO[i];
        punto(i,lerp(lerp(f0[0],a0[0],k0),b[0],k),lerp(lerp(f0[1],a0[1],k0),b[1],k),'c',0)}else{punto(i,f0[0],f0[1],'v');$('pd'+i).setAttribute('opacity',1-k0)}}
     cab='';sub='';
     typed($('ptsub2'),t<445?'NO MURIERON AL MISMO TIEMPO':'MURIERON EN MOMENTOS DISTINTOS',t,t<445?441.3:445.06,t<445?443.4:446.9);
   }else{                                                  // los tres grupos
     for(let i=0;i<NP;i++){const[x,y]=P_GRUPO(i);let e='v',b=0;
       if(i<23)e=fase===3?'d':'c';else if(i<37){if(t>=456.42){e='g';b=Math.exp(-(t-456.42)*4)}}else if(t>=521.97){e='m';b=Math.exp(-(t-521.97)*4)}
       if(fase===5&&i>=23)b=.25+.25*Math.sin(t*5);punto(i,x,y,e,b);$('pd'+i).setAttribute('opacity',(fase===5&&i<23)?0:1)}
     if(fase===3){grp('ptA',t,452.7,'23','SUR DE ASIA','rgba(236,229,210,.45)');if(t>=456.42)grp('ptB',t,456.42,'14','PERSONAS','#5cf29a')}
     else if(fase===4){grp('ptA',t,0,'23','SUR DE ASIA','#ece5d2');grp('ptB',t,0,'14','MEDITERRÁNEO','#5cf29a');if(t>=521.97)grp('ptC',t,521.97,'1','SUDESTE DE ASIA','#b48cff')}
     else{grp('ptA',t,0,'23','SUR DE ASIA','rgba(236,229,210,.4)');grp('ptB',t,0,'14','MEDITERRÁNEO','#5cf29a');grp('ptC',t,0,'1','SUDESTE DE ASIA','#b48cff');
       $('ptA').style.opacity=0;const k=eInOut(p(t,539.3,540.1));const bx=$('ptbox');bx.setAttribute('x',800);bx.setAttribute('y',290);bx.setAttribute('width',900);bx.setAttribute('height',300);bx.setAttribute('opacity',k);
       bx.setAttribute('pathLength',1000);bx.setAttribute('stroke-dasharray',`${(k*1000).toFixed(0)} 1000`);
       $('ptfin').style.opacity=1;reveal($('ptf1'),t,538.19,.4);reveal($('ptf2'),t,540.11,.5);G.negro=eIn(p(t,540.9,541.4));const a=shake(t,540.13,14,.35);G.wx+=a[0];G.wy+=a[1]}
     if(fase!==5){const a=shake(t,456.44,22,.5),b2=shake(t,521.99,12,.35);G.wx+=a[0]+b2[0];G.wy+=a[1]+b2[1]}
   }
   $('ptn').textContent=cab;$('ptsub').textContent=sub;if(fase>2){$('ptsub2').textContent=''}},
 g11:async t=>{G.ia=false;const s=lerp(1.14,1.2,(t-448.2)/4.5);$('g11img').style.transform=`scale(${s})`;$('g11over').style.transform=`scale(${s})`;
   $('g11t1').textContent='SEGUNDA RESPUESTA';$('g11t2').textContent='GRANIZO · AÑO 850';
   $('g11s1').setAttribute('transform','translate(880 540) rotate(-8)');$('g11s2').setAttribute('transform','translate(1010 710) rotate(5) scale(1.05)');$('g11s1').setAttribute('opacity',.92);$('g11s2').setAttribute('opacity',.92);
   const pts=[[640,470],[760,520],[820,500],[905,575],[975,560],[1040,650],[1120,640],[1190,730],[1275,735],[1360,830]],k=eOut(p(t,448.84,449.25)),n=k*(pts.length-1);
   let d='';for(let i=0;i<=Math.floor(n)&&i<pts.length;i++)d+=(i?'L':'M')+pts[i].join(' ');if(n<pts.length-1&&n>0){const i=Math.floor(n),f=n-i;d+=`L${lerp(pts[i][0],pts[i+1][0],f)} ${lerp(pts[i][1],pts[i+1][1],f)}`}
   $('g11cr').setAttribute('d',d||'M0 0');$('g11cr').setAttribute('opacity',k>0?.9:0);$('g11cr2').setAttribute('d','M905 575 L930 640 L915 690 M1120 640 L1160 600 L1215 590');$('g11cr2').setAttribute('opacity',k>=1?.8:0);
   reveal($('g11f1'),t,448.3,.4);reveal($('g11f2'),t,448.84,.5);const a=shake(t,448.86,18,.45);G.wx+=a[0];G.wy+=a[1]},
 gm:async t=>{G.ia=false;malla($('gmmesh'),t,'#30115a','#0b2f24',.85);const[fx,fy,z]=camm(t);
   $('gmcam').style.transform=`translate(${960-fx*z}px,${560-fy*z}px) scale(${z})`;$('gmtilt').style.transform=`perspective(1900px) rotateX(${lerp(16,8,p(t,458.3,474.4))}deg)`;
   const w=(el,a,b)=>{el.style.opacity=(t>=a?1:0)*(1-p(t,b,b+.5));el.style.transform=`scale(${t>=a?1+.08*Math.exp(-(t-a)*10):1})`};w($('gmw1'),459.3,463.6);w($('gmw2'),461.1,463.6);
   tacha($('gmx1'),t,459.85,560,360,1360,320);tacha($('gmx2'),t,461.7,600,700,1320,660);for(const e of ['gmx1','gmx2'])$(e).setAttribute('opacity',+$(e).getAttribute('opacity')*(1-p(t,463.6,464.1)));
   const pin=(g,pp,P,a,s)=>{const k=eBack(p(t,a,a+.35));$(g).setAttribute('transform',`translate(${P[0]} ${P[1]}) scale(${k*s})`);const pu=((t-a)%1.1)/1.1;$(pp).setAttribute('r',10+pu*22);$(pp).setAttribute('opacity',t>a?1-pu:0)};
   pin('gmp1','gmp1p',LG,458.4,1);pin('gmp2','gmp2p',CR,471.86,.7);
   const gk=p(t,470.38,470.8);$('gmgre').setAttribute('fill',gk>0?'#5cf29a':'#3b2163');$('gmgre').setAttribute('opacity',gk>0?.55+.45*Math.exp(-(t-470.38)*3):1);$('gmgre').setAttribute('filter',gk>0?'url(#brillo2)':'');
   const t1=$('gmt1');t1.setAttribute('x',GR[0]-8);t1.setAttribute('y',GR[1]-34);t1.setAttribute('text-anchor','middle');typed(t1,'GRECIA',t,470.38,470.9);
   const t2=$('gmt2');t2.setAttribute('x',CR[0]+16);t2.setAttribute('y',CR[1]+22);typed(t2,'CRETA',t,471.86,472.3);
   const t3=$('gmt3');t3.setAttribute('x',LG[0]-18);t3.setAttribute('y',LG[1]-14);typed(t3,'EL LAGO',t,458.6,459.1);
   const t4=$('gmt4');t4.setAttribute('x',70);t4.setAttribute('y',428);typed(t4,'MAR MEDITERRÁNEO',t,465.32,466.6);
   const lk=eInOut(p(t,473.0,475.4));$('gmlin').setAttribute('stroke-dasharray',`${(lk*LL).toFixed(1)} ${LL+20}`);$('gmlin').setAttribute('opacity',lk>0?1:0);
   $('gmkm').style.opacity=p(t,473.3,473.7);$('gmkmn').textContent=Math.round((1-Math.pow(1-p(t,473.5,475.4),3))*5000).toLocaleString('es-CO');
   $('gmkmn').style.transform=`scale(${t>475.4?1+.06*Math.exp(-(t-475.4)*9):1})`;$('gmkmn').style.display='inline-block';
   G.wx+=(1-eExpo(p(t,458.3,458.65)))*900},
 g15:async t=>{G.ia=false;malla($('g15mesh'),t,'#2a1052','#0b3024',.6);$('g15bg').style.transform=`scale(${lerp(1.3,1.4,(t-476.2)/8)})`;$('g15q').style.opacity=.8*p(t,479.9,480.3);
   reveal($('g15a'),t,480.24,.4);reveal($('g15b'),t,480.98,.5);reveal($('g15c'),t,482.12,.5);
   const l=eInOut(p(t,477.2,478.4));$('g15l').setAttribute('x2',lerp(310,1010,l));typed($('g15t'),'LA AUTORA PRINCIPAL DEL ESTUDIO',t,477.2,478.9)},
 g16:async t=>{await cuadro($('g16i'),'frames/b504',240,t,484.1,6.4);enc($('g16i'),55,38,lerp(1.3,1.42,(t-484.1)/3.6));frase('g16',t,484.48,485.12);const a=shake(t,485.14,12,.3);G.wx+=a[0];G.wy+=a[1]},
 g17:async t=>{const tl=aVideo(t)-aVideo(487.7);const i=clamp(Math.floor((tl+5.2)*24)+1,1,241);await pon($('g17i'),`../b4/frames/b409/${String(i).padStart(4,'0')}.jpg`);enc($('g17i'),45,50,lerp(1.06,1.14,tl/3.8));
   const tg=spring(p(tl,.5,1.0),2.4,6.5);tf($('g17tag'),lerp(-950,90,tg),820,1,lerp(-7,-2,tg),tl>=.5?1:0);typed($('g17n1'),'LOS 14 ESQUELETOS',t,488.45,490.3);typed($('g17n2'),'SE LES PONE FECHA',t,490.4,491.2)},
 g17b:async t=>{G.ia=false;fondo('g17b',t,495.4,8);typed($('g17brot'),'AÑO',t,495.5,495.9);
   const k=1-Math.pow(1-p(t,498.35,498.85),3),n=t<498.35?800:Math.round(lerp(800,1800,k));$('g17bnum').textContent=t>=496.33?n.toLocaleString('es-CO').replace('.',''):'';
   $('g17bnum').style.color=t>=498.85?'#5cf29a':'#ece5d2';$('g17bnum').style.transform=`scale(${t>=498.85?1+.09*Math.exp(-(t-498.85)*9):t>=496.33?1+.05*Math.exp(-(t-496.33)*9):1})`;
   $('g17bnum').style.filter=t>=498.85?`drop-shadow(0 0 ${lerp(50,14,p(t,498.85,499.6))}px rgba(92,242,154,.5))`:'none';
   tacha($('g17x'),t,497.05,640,500,1280,450);$('g17x').setAttribute('opacity',+$('g17x').getAttribute('opacity')*(t<498.3?1:0));
   linea('g17b',t,501.0,502.2);typed($('g17y1'),'850',t,501.0,501.3);typed($('g17y2'),'1800',t,502.0,502.3);typed($('g17bsub'),'MIL AÑOS DESPUÉS',t,501.03,502.3);$('g17bsub').style.top='790px';
   const a=shake(t,498.87,24,.5);G.wx+=a[0];G.wy+=a[1];G.wr+=a[2]},
 g18:async t=>{const i=clamp(Math.floor((t-503.4)*24*.8)+1,1,139);await pon($('g18i'),`../b1/frames/b509/${String(i).padStart(4,'0')}.jpg`);enc($('g18i'),50,50,lerp(1.25,1.1,eOut(p(t,503.4,507.4))));$('g18i').style.filter='brightness(.75)'},
 g19:async t=>{await cuadro($('g19i'),'frames/b505',155,t,506.7,0.6);enc($('g19i'),50,50,lerp(1.1,1.02,(t-506.7)/6.3));
   etiqueta('g19',t,508.4,512.1,90,820,'MIL AÑOS ANTES','GENTE DE LA INDIA',508.75,509.9,510.83,511.9)},
 g19b:async t=>{await cuadro($('g19bi'),'frames/b508',155,t,512.2,0.1);enc($('g19bi'),50,55,lerp(1.02,1.1,(t-512.2)/6));
   etiqueta('g19b',t,514.0,518.0,90,820,'AÑO 1800','PERSONAS DEL MEDITERRÁNEO',514.11,514.8,515.15,516.9)},
 g21:async t=>{const i=clamp(Math.floor((t-527.3)*24*.9)+20,1,139);await pon($('g21i'),`../b1/frames/b509/${String(i).padStart(4,'0')}.jpg`);enc($('g21i'),50,50,1.06);
   [527.31,528.73,530.23].forEach((a,k)=>{const e=$('g21c'+k);e.style.opacity=t>=a?1:0;e.style.transform=`scale(${t>=a?1+.14*Math.exp(-(t-a)*9):1})`});
   typed($('g21e2'),'DE 40 METROS',t,530.75,532.0);G.ia=false},
 g22:async t=>{await cuadro($('g22i'),'../b4/frames/b408',192,t,533.2,2.0);enc($('g22i'),50,50,lerp(1.04,1.14,(t-533.2)/4.8));$('g22i').style.filter=`brightness(${lerp(.9,.5,p(t,536.5,538))})`},
};
'''
pagina("bloque5.html", cuerpo, js, '<script src="../b1/lago_b509.js"></script>\n<script src="mapa_ea.js"></script>\n')
print("bloque5.html listo")
