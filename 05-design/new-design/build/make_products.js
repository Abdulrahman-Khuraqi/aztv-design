// Composes the product card images (1000x1000) from the section 03 3D renders, with the duration in Arabic in the store font.
// Regular AZ TV = black and white, Plus = gold. Output: assets/img/products/prod-*.png (to upload in Salla) and .webp (for the page).
// Run with the new design served on :8770, from the repo root:  node 05-design/new-design/build/make_products.js
const { chromium } = require(process.env.PW || 'playwright');
const path = require('path');
const OUT = path.join(__dirname, '../assets/img/products');

const BW = { art: 'cat-aztv-3d-bw.png', glow: 'rgba(255,255,255,.13)', ink: '#F3F0E6', tag: 'AZ TV', accent: '#D9D6CE' };
const GOLD = { art: 'cat-aztv-plus-3d.png', glow: 'rgba(234,207,105,.26)', ink: '#EACF69', tag: 'AZ TV PLUS', accent: '#EACF69', k4: true };
const PRODUCTS = [
  ['prod-aztv-15m', BW, 'سنة + ٣ شهور', 'اشتراك AZ TV'],
  ['prod-aztv-6m', BW, '٦ شهور', 'اشتراك AZ TV'],
  ['prod-aztv-3m', BW, '٣ شهور', 'اشتراك AZ TV'],
  ['prod-aztv-1m', BW, 'شهر', 'اشتراك AZ TV'],
  ['prod-plus-12m', GOLD, 'سنة', 'اشتراك AZ TV Plus'],
  ['prod-plus-12m-2dev', GOLD, 'سنة لجهازين', 'اشتراك AZ TV Plus'],
  ['prod-plus-6m', GOLD, '٦ شهور', 'اشتراك AZ TV Plus'],
  ['prod-plus-3m', GOLD, '٣ شهور', 'اشتراك AZ TV Plus'],
  ['prod-renew-aztv', { ...BW, art: 'cat-renewal-3d-bw.png' }, 'تجديد', 'اشتراك AZ TV'],
  ['prod-renew-plus', { ...GOLD, art: 'cat-renewal-3d.png' }, 'تجديد', 'اشتراك AZ TV Plus'],
];

const card = (s, big, sub) => `
<div id="c" style="position:relative;width:1000px;height:1000px;overflow:hidden;direction:rtl;font-family:PingARLT,sans-serif;
  background:radial-gradient(70% 55% at 50% 40%, ${s.glow}, transparent 72%), #0D0D0D">
  <div style="position:absolute;inset:28px;border:1.5px solid ${s.accent}2E;border-radius:40px"></div>
  <div style="position:absolute;top:62px;right:72px;font:700 30px/1 PingARLT;letter-spacing:.24em;color:${s.accent};direction:ltr">${s.tag}</div>
  ${s.k4 /* 4K under the package name, clear of Salla's discount badge on the left */ ? `<div style="position:absolute;top:110px;right:66px;padding:10px 20px;border-radius:14px;background:#EACF69;color:#0D0D0D;font:800 34px/1 PingARLT">4K</div>` : ''}
  <img src="/assets/img/${s.art}" style="position:absolute;top:104px;left:50%;width:590px;transform:translateX(-50%);filter:drop-shadow(0 28px 30px rgba(0,0,0,.65))">
  <div style="position:absolute;bottom:92px;inset-inline:0;text-align:center">
    <div style="font:800 ${big.length > 8 ? 96 : 120}px/1.1 PingARLT;color:${s.ink}">${big}</div>
    <div style="margin-top:14px;font:500 36px/1.3 PingARLT;color:#B9B4A6">${sub}</div>
  </div>
</div>`;

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1000, height: 1000 } });
  await p.goto('http://localhost:8770/README.md');   // same origin, so the fonts load
  for (const [name, style, big, sub] of PRODUCTS) {
    await p.setContent(`<!doctype html><html><head><link rel="stylesheet" href="/assets/css/pingarlt-2194a8e3.css">
      <style>body{margin:0}</style></head><body>${card(style, big, sub)}</body></html>`, { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await (await p.$('#c')).screenshot({ path: path.join(OUT, name + '.png') });
    console.log(name);
  }
  await b.close();
})();
