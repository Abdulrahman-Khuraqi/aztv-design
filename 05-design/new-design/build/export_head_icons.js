// Frames of the animated title icons (assets/img/malak/head-*.svg) for the animated WebP fallback.
// Run with the new design served on :8770, from the repo root:
//   node 05-design/new-design/build/export_head_icons.js <frames dir>
//   python3 05-design/new-design/build/make_head_icons.py --webp <frames dir>
// Each icon loops in 3 s, so 90 frames at 30 fps make one seamless loop. Needs Playwright.
const { chromium } = require(process.env.PW || 'playwright');
const OUT = process.argv[2], B = 'http://localhost:8770/assets/img/malak/', FPS = 30, LOOP = 3, SIZE = 384;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: SIZE, height: SIZE } });
  for (const name of ['head-tv', 'head-crown', 'head-renew']) {
    const svg = await (await fetch(B + name + '.svg')).text();
    await p.setContent(`<!doctype html><body style="margin:0;background:transparent">${svg.replace('width="128" height="128"', `width="${SIZE}" height="${SIZE}"`)}</body>`);
    for (let f = 0; f < FPS * LOOP; f++) {
      await p.evaluate(t => document.getAnimations().forEach(a => { a.pause(); a.currentTime = t; }), f * 1000 / FPS);
      await p.locator('svg').screenshot({ path: `${OUT}/${name}-${String(f).padStart(3, '0')}.png`, omitBackground: true });
    }
  }
  await b.close();
})();
