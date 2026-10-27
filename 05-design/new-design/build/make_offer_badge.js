// The gold seal of section 06 «عروض بداية الموسم»: «خصم حتى 60٪» in the store font, used as the title block's icon image
// (a normal field of the theme's title block, so nothing custom on Salla). 480 x 480 PNG with transparency, shown at about 120 px.
// Change the number in BADGE below if the offer changes. Run from the repo root:  node 05-design/new-design/build/make_offer_badge.js
const { chromium } = require(process.env.PW || 'playwright');
const path = require('path');
const BADGE = { top: 'خصم حتى', big: '60', unit: '٪' };
const OUT = path.join(__dirname, '../assets/img/malak/offer-badge.png');
const FONT = (w) => 'file://' + path.join(__dirname, `../assets/fonts/${w}`);

// a seal: 28-point burst edge in gold, a black disc with a thin gold ring, the text in gold
const N = 28, R1 = 236, R2 = 214;
const burst = Array.from({ length: N * 2 }, (_, i) => {
  const a = (i / (N * 2)) * Math.PI * 2 - Math.PI / 2, r = i % 2 ? R2 : R1;
  return `${(240 + Math.cos(a) * r).toFixed(1)},${(240 + Math.sin(a) * r).toFixed(1)}`;
}).join(' ');
const html = `<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>
  @font-face { font-family: P; src: url("${FONT('PingARLT-Bold-7c5bdf53.woff2')}"); font-weight: 700; }
  @font-face { font-family: P; src: url("${FONT('PingARLT-Black-7a45930b.woff2')}"); font-weight: 900; }
  html, body { margin: 0; background: transparent; }
  #b { position: relative; width: 480px; height: 480px; font-family: P, sans-serif; }
  #b svg { position: absolute; inset: 0; }
  .t { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }
  .top { font-size: 50px; font-weight: 700; color: #F3F0E6; line-height: 1; margin-bottom: 4px; }
  .big { direction: ltr; display: flex; align-items: flex-start; font-weight: 900; line-height: .9;
    background: linear-gradient(180deg, #FFF3C4 0%, #EACF69 45%, #B8983F 100%); -webkit-background-clip: text; background-clip: text; color: transparent; }
  .big b { font-size: 170px; }
  .big i { font-style: normal; font-size: 82px; margin-top: 18px; margin-inline-start: 4px; }
</style></head><body><div id="b">
  <svg viewBox="0 0 480 480"><defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFF0B0"/><stop offset=".45" stop-color="#EACF69"/><stop offset="1" stop-color="#9C7B2C"/></linearGradient>
    <radialGradient id="k" cx=".5" cy=".35" r=".7"><stop offset="0" stop-color="#26241F"/><stop offset="1" stop-color="#0D0D0D"/></radialGradient></defs>
    <polygon points="${burst}" fill="url(#g)"/>
    <circle cx="240" cy="240" r="192" fill="url(#k)"/>
    <circle cx="240" cy="240" r="176" fill="none" stroke="url(#g)" stroke-width="3"/>
    <circle cx="240" cy="240" r="168" fill="none" stroke="#EACF69" stroke-opacity=".35" stroke-width="1" stroke-dasharray="2 7"/>
  </svg>
  <div class="t"><div class="top">${BADGE.top}</div><div class="big"><b>${BADGE.big}</b><i>${BADGE.unit}</i></div></div>
</div></body></html>`;

(async () => {
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 480, height: 480 } });
  await p.setContent(html, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await p.locator('#b').screenshot({ path: OUT, omitBackground: true });
  await b.close();
  console.log(OUT);
})();
