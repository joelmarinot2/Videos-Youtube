// Abre la página animada y saca cada cuadro. Uso: node capturar.js [cuadros|"ver" t1,t2,...]
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');
const FPS = +(process.env.FPS||60);
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await pg.goto('file://' + path.join(__dirname, 'muestra2.html'));
  await pg.evaluate(() => document.fonts.ready);
  await pg.waitForTimeout(500);
  if (process.argv[2] === 'ver') {               // capturas sueltas para revisar
    for (const t of process.argv[3].split(',').map(Number)) {
      await pg.evaluate(t => render(t), t);
      await pg.screenshot({ path: path.join(__dirname, 'revisar2', `t${t.toFixed(2)}.jpg`), type: 'jpeg', quality: 80 });
    }
    await b.close(); return;
  }
  const dur = await pg.evaluate(() => DUR), n = Math.round(dur * FPS);
  const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '14', '-pix_fmt', 'yuv420p', path.join(__dirname, 'video_mudo2.mp4')], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let f = 0; f < n; f++) {
    await pg.evaluate(t => render(t), f / FPS);
    const buf = await pg.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 60 === 0) console.log(`cuadro ${f}/${n}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await b.close();
  console.log('listo');
})();
