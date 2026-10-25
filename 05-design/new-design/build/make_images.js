// Renders the block images in assets/img/malak/ (icons, beIN tiles, comparison).
// Run with the new design served on :8770, from the repo root:  node 05-design/new-design/build/make_images.js 05-design/new-design/build/out
// then convert the PNGs to WebP into assets/img/malak/. Needs Playwright.
const { chromium } = require(process.env.PW || 'playwright');
const OUT = process.argv[2], B = 'http://localhost:8770/assets/';
const HEAD = `<base href="${B}"><link rel="stylesheet" href="css/pingarlt-2194a8e3.css"><link rel="stylesheet" href="css/hugeicons-font.min-d8a04d24.css"><link rel="stylesheet" href="css/sallaicons-51125e7e.css">
<style>*{box-sizing:border-box}body{margin:0;font-family:PingARLT,sans-serif;direction:rtl;background:transparent}</style>`;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ deviceScaleFactor: 1 });
  await p.goto('http://localhost:8770/README.md');
  async function shot(html, w, h, file, transparent) {
    await p.setViewportSize({ width: w, height: h });
    await p.setContent(`<!doctype html><html><head>${HEAD}</head><body>${html}</body></html>`, { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(200);
    const el = await p.$('body > div'); await el.screenshot({ path: `${OUT}/${file}`, omitBackground: !!transparent });
  }
  // gold line icons on transparent ground (the tile colour comes from the theme)
  const icons = { 'icon-apple': 'apple', 'icon-android-phone': 'smart-phone-01', 'icon-android-tv': 'tv-smart', 'icon-smart-tv': 'tv-01',
    'icon-fast': 'zap', 'icon-support': 'customer-support', 'icon-payment': 'credit-card', 'icon-devices': 'laptop-phone-sync', 'icon-renew': 'refresh',
    'icon-tv': 'tv-02', 'icon-crown': 'crown' };
  for (const [f, ic] of Object.entries(icons))
    await shot(`<div style="width:400px;height:400px;display:grid;place-items:center"><i class="hgi-stroke hgi-${ic}" style="font-size:190px;color:#EACF69"></i></div>`, 400, 400, f + '.png', true);
  // beIN package tiles
  const tile = (inner) => `<div style="width:600px;height:600px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px;
     background:radial-gradient(120% 90% at 50% 0%,#2A2615 0%,#1A1A1A 45%,#0D0D0D 100%)">${inner}</div>`;
  for (const [f, name, tier] of [['bein-qimma-arabi','قمة','عربي'],['bein-qimma-khaleeji','قمة','خليجي'],['bein-tamayoz-arabi','تميز','عربي'],['bein-tamayoz-khaleeji','تميز','خليجي']])
    await shot(tile(`<img src="img/logos/bein-white.svg" style="width:330px"><div style="font-size:78px;font-weight:800;color:#EACF69;line-height:1">${name} <span style="color:#F3F0E6">${tier}</span></div>`), 600, 600, f + '.png');
  await shot(tile(`<i class="hgi-stroke hgi-refresh" style="font-size:190px;color:#EACF69"></i><div style="font-size:64px;font-weight:800;color:#F3F0E6;line-height:1">تجديد <span style="color:#EACF69">beIN</span></div>`), 600, 600, 'bein-renew.png');
  // comparison image, desktop and phone
  const Y = '<i class="hgi-stroke hgi-checkmark-circle-02" style="color:#EACF69;font-size:1.5em"></i>', N = '<span style="color:rgba(243,240,230,.3)">—</span>', R = '<i class="sicon-sar"></i>';
  const rows = [['أقل سعر لسنة', `سنة + ٣ شهور بـ ٩٦ ${R}`, `سنة بـ ١٩٦ ${R}`], ['مدد الاشتراك', 'من شهر إلى سنة + ٣ شهور', 'من ٣ شهور إلى سنة'],
    ['جودة المشاهدة', 'عالية', 'الأعلى'], ['اشتراك لجهازين', N, Y], ['أبل وأندرويد والشاشات الذكية', Y, Y], ['سنة مجانًا مع AZ TV Box', N, Y], ['تجديد بسعر أقل', Y, Y]];
  const table = (fs, pad, lw) => `<table style="width:100%;border-collapse:separate;border-spacing:0;font-size:${fs}px;color:#F3F0E6">
    <thead><tr><td style="width:${lw}%"></td><th style="padding:${pad}px;font-size:1.35em">AZ TV<div style="font-size:.6em;font-weight:500;color:#B9B4A6">الباقة العادية</div></th>
    <th style="padding:${pad * 1.6}px ${pad}px ${pad}px;font-size:1.35em;background:rgba(234,207,105,.1);border-radius:24px 24px 0 0;position:relative">
      <span style="position:absolute;top:-.9em;inset-inline:0;margin:auto;width:max-content;padding:.25em .9em;border-radius:99px;background:#EACF69;color:#0D0D0D;font-size:.5em">الأفضل تجربة</span>AZ TV Plus<div style="font-size:.6em;font-weight:500;color:#B9B4A6">باقة البلس</div></th></tr></thead>
    <tbody>${rows.map((r, i) => `<tr><th style="text-align:start;font-weight:600;color:#B9B4A6;padding:${pad}px;border-top:1px solid rgba(243,240,230,.1)">${r[0]}</th>
      <td style="text-align:center;padding:${pad}px;border-top:1px solid rgba(243,240,230,.1)">${r[1]}</td>
      <td style="text-align:center;padding:${pad}px;border-top:1px solid rgba(243,240,230,.1);background:rgba(234,207,105,.1);${i === rows.length - 1 ? 'border-radius:0 0 24px 24px' : ''}">${r[2]}</td></tr>`).join('')}</tbody></table>`;
  await shot(`<div style="width:1200px;padding:44px 60px;background:#0D0D0D">${table(26, 18, 36)}</div>`, 1200, 640, 'compare-desktop.png');
  await shot(`<div style="width:780px;padding:60px 24px 30px;background:#0D0D0D">${table(30, 22, 34)}</div>`, 780, 1060, 'compare-phone.png');
  await b.close();
})();
