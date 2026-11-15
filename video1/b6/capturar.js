// Saca los cuadros del montaje. Uso:
//   node capturar.js ver 4.5,12,31      -> capturas sueltas (tiempos del AUDIO) en revisar/
//   node capturar.js tramo <ini> <fin> <salida.mp4>   -> tramo en tiempo de VIDEO, a 24 cuadros/s
const { chromium } = require('playwright'); const { spawn } = require('child_process'); const path = require('path');
const FPS = 24, PAG = process.env.PAG || 'bloque6.html';
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await pg.goto('file://' + path.join(__dirname, PAG));
  await pg.evaluate(async () => { await document.fonts.ready; await window.LISTO; });
  await pg.waitForTimeout(500);
  const off = await pg.evaluate(() => OFF);
  if (process.argv[2] === 'ver') {
    for (const ta of process.argv[3].split(',').map(Number)) {
      await pg.evaluate(async t => { await render(window.aVideo ? aVideo(t) : t); }, ta);
      await pg.screenshot({ path: path.join(__dirname, 'revisar', `a${ta.toFixed(2).padStart(6, '0')}.jpg`), type: 'jpeg', quality: 82 });
    }
    await b.close(); return;
  }
  const ini = +process.argv[3], fin = +process.argv[4], out = process.argv[5];
  const f0 = Math.round(ini * FPS), f1 = Math.round(fin * FPS);
  const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '13', '-pix_fmt', 'yuv420p', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let f = f0; f < f1; f++) {
    await pg.evaluate(async t => { await render(t); }, f / FPS);
    const buf = await pg.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if ((f - f0) % 120 === 0) console.log(`${out}: cuadro ${f - f0}/${f1 - f0}`);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close(); console.log(out + ' listo');
})();
