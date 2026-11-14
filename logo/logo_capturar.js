const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  for (const v of process.argv.slice(2)) {
    await pg.goto('file://' + path.join(__dirname, 'logo.html') + '#' + v); await pg.reload();
    await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(400);
    await pg.screenshot({ path: path.join(__dirname, 'logo', `logo-${v}.png`), omitBackground: v.includes('transparente') });
  }
  await b.close();
})();
