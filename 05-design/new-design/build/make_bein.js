// Composes the three beIN world cards (section 04): 4K receiver, PVR receiver, official renewal. 1000x1000, same system as the product cards.
// Each card uses the 3D render from assets/img/bein/ when it exists (bein-4k-3d.png, bein-pvr-3d.png, bein-renew-3d.png),
// otherwise the temporary art (device cut out of the old banner, or the gold renewal render).
// Run with the new design served on :8770, from the repo root:  node 05-design/new-design/build/make_bein.js
const { chromium } = require(process.env.PW || 'playwright');
const fs = require('fs');
const path = require('path');
const IMG = path.join(__dirname, '../assets/img');
const OUT = path.join(IMG, 'bein');

const pick = (render, fallback) => fs.existsSync(path.join(IMG, 'bein', render)) ? `bein/${render}` : fallback;
const CARDS = [
  ['bein-card-4k', pick('bein-4k-3d.png', 'bein/ref-bein-4k-device.png'), 'رسيفر 4K', 'beIN TV 4K'],
  ['bein-card-pvr', pick('bein-pvr-3d.png', 'bein/ref-bein-pvr-device.png'), 'رسيفر PVR', 'beIN PVR HD'],
  ['bein-card-renew', pick('bein-renew-3d.png', 'cat-renewal-3d.png'), 'تجديد الاشتراك', 'اشتراك beIN الرسمي'],
];

const card = (art, big, sub) => `
<div id="c" style="position:relative;width:1000px;height:1000px;overflow:hidden;direction:rtl;font-family:PingARLT,sans-serif;
  background:radial-gradient(60% 45% at 50% 42%, rgba(234,207,105,.20), transparent 72%),
             radial-gradient(80% 40% at 50% 100%, rgba(91,42,134,.35), transparent 70%), #0D0D0D">
  <div style="position:absolute;inset:28px;border:1.5px solid rgba(234,207,105,.18);border-radius:40px"></div>
  <img src="/assets/img/logos/bein-white.svg" style="position:absolute;top:60px;right:72px;height:44px">
  <div style="position:absolute;top:150px;bottom:300px;inset-inline:90px;display:grid;place-items:center">
    <img src="/assets/img/${art}" style="max-width:820px;max-height:520px;object-fit:contain;filter:drop-shadow(0 30px 30px rgba(0,0,0,.7))">
  </div>
  <div style="position:absolute;bottom:96px;inset-inline:0;text-align:center">
    <div style="font:800 ${big.length > 9 ? 100 : 118}px/1.1 PingARLT;color:#F3F0E6">${big}</div>
    <div style="margin-top:14px;font:600 38px/1.3 PingARLT;color:#EACF69;direction:${/[a-z]/i.test(sub) && !/[؀-ۿ]/.test(sub) ? 'ltr' : 'rtl'}">${sub}</div>
  </div>
</div>`;

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1000, height: 1000 } });
  await p.goto('http://localhost:8770/README.md');   // same origin, so the fonts load
  for (const [name, art, big, sub] of CARDS) {
    await p.setContent(`<!doctype html><html><head><link rel="stylesheet" href="/assets/css/pingarlt-2194a8e3.css">
      <style>body{margin:0}</style></head><body>${card(art, big, sub)}</body></html>`, { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await (await p.$('#c')).screenshot({ path: path.join(OUT, name + '.png') });
    console.log(name, '←', art);
  }
  await b.close();
})();
