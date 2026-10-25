// Composes the section 14 banner («2 والثالث مجانًا», the shirts store): the Gemini artwork with the Arabic text, the button and the
// AZ Shirts logo laid over it in the site font, desktop and phone. The text is added here, not by the AI, so the Arabic stays correct.
// Artwork: 05-design/sections/14-second-store/second-store-gemini.jpg (three shirts across the frame, gift box in the centre).
// Run with the new design served on :8770, from the repo root:  node 05-design/new-design/build/make_second_store.js
// It writes the WebP files (via python3 + Pillow) into assets/img/second-store/: desktop 1600 wide, phone 800 wide.
const { chromium } = require(process.env.PW || 'playwright');
const path = require('path');
const os = require('os');
const { execFileSync } = require('child_process');
const ROOT = path.join(__dirname, '../../..');
const fs = require('fs');
const dataUri = (f, type) => `data:${type};base64,` + fs.readFileSync(path.join(ROOT, f)).toString('base64');
const ART = dataUri('05-design/sections/14-second-store/second-store-gemini.jpg', 'image/jpeg');
const LOGO = dataUri('05-design/sections/14-second-store/logo-az-shirts.png', 'image/png');
const OUT = path.join(__dirname, '../assets/img/second-store');
const SITE = (process.env.SITE_URL || 'http://localhost:8770').replace(/\/$/, '');

const TITLE = '2 والثالث <em>مجانًا</em>';
const LINE = 'أضف ثلاث تيشرتات للسلة ويتفعّل العرض';
const BUTTON = 'تسوّق التيشرتات';

const css = `
  *{box-sizing:border-box} body{margin:0;background:#0D0D0D}
  #c{position:relative;overflow:hidden;direction:rtl;font-family:PingARLT,sans-serif;background:#0D0D0D;color:#F3F0E6}
  .art{position:absolute;left:50%;transform:translateX(-50%);display:block;
       -webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 var(--fade-top),#000 calc(100% - var(--fade-bottom)),transparent 100%);}
  .head{position:absolute;inset-inline:0;top:var(--head-top);display:flex;flex-direction:column;align-items:center;text-align:center}
  .logo{height:var(--logo);display:block}
  h1{margin:var(--title-gap) 0 0;font:800 var(--title)/1.15 PingARLT;color:#F3F0E6;letter-spacing:0}
  h1 em{font-style:normal;color:#EACF69}
  p{margin:var(--line-gap) 0 0;font:500 var(--line)/1.5 PingARLT;color:#D9D4C5;max-width:var(--line-max)}
  .btn{position:absolute;left:50%;transform:translateX(-50%);bottom:var(--btn-bottom);display:inline-flex;align-items:center;gap:.5em;
       padding:0 1.6em;height:var(--btn-h);border-radius:999px;background:#EACF69;color:#0D0D0D;font:700 var(--btn)/1 PingARLT;
       box-shadow:0 12px 40px -10px rgba(234,207,105,.55)}
  .btn i{font-style:normal;font-size:1.1em}`;

const banner = (v) => `
<div id="c" style="width:${v.w}px;height:${v.h}px;--head-top:${v.headTop}px;--logo:${v.logo}px;--title-gap:${v.titleGap}px;--title:${v.title}px;
  --line-gap:${v.lineGap}px;--line:${v.line}px;--line-max:${v.lineMax}px;--btn:${v.btn}px;--btn-h:${v.btnH}px;--btn-bottom:${v.btnBottom}px;
  --fade-top:${v.fadeTop}px;--fade-bottom:${v.fadeBottom}px">
  <div style="position:absolute;inset:0;overflow:hidden">
    <img class="art" src="${ART}" style="top:${v.artTop}px;width:${v.artW}px;${v.artX ? `left:${v.artX}px;transform:none;` : ''}">
  </div>
  <div class="head"><img class="logo" src="${LOGO}" alt=""><h1>${TITLE}</h1><p>${LINE}</p></div>
  <div class="btn">${BUTTON}<i>←</i></div>
</div>`;

// desktop: the artwork at full width under a text band; the button sits on the floor under the gift box
const DESKTOP = { name: 'second-store-desktop', w: 2000, h: 1330, artTop: 214, artW: 2000, fadeTop: 230, fadeBottom: 60,
  headTop: 54, logo: 66, titleGap: 22, title: 104, lineGap: 10, line: 36, lineMax: 1200, btn: 34, btnH: 84, btnBottom: 40 };
// phone: the gift box and the white shirt in the middle, the green and yellow shirts cut by the edges
const PHONE = { name: 'second-store-phone', w: 1000, h: 1350, artTop: 262, artW: 1840, artX: -420, fadeTop: 200, fadeBottom: 80,
  headTop: 54, logo: 60, titleGap: 18, title: 92, lineGap: 8, line: 34, lineMax: 820, btn: 34, btnH: 84, btnBottom: 44 };

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 2000, height: 1400 } });
  await p.goto(`${SITE}/README.md`);   // same origin, so the site fonts load
  for (const v of [DESKTOP, PHONE]) {
    await p.setContent(`<!doctype html><html><head><link rel="stylesheet" href="${SITE}/assets/css/pingarlt-2194a8e3.css">
      <style>${css}</style></head><body>${banner(v)}</body></html>`, { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    const png = path.join(os.tmpdir(), v.name + '.png');   // full-size render; only the WebP goes into the site
    await (await p.$('#c')).screenshot({ path: png });
    console.log(v.name, v.w + 'x' + v.h);
  }
  await b.close();
  // web versions: desktop 1600 wide, phone 800 wide
  execFileSync('python3', ['-c', `
from PIL import Image
for n, w in (('second-store-desktop', 1600), ('second-store-phone', 800)):
    im = Image.open('${os.tmpdir()}/' + n + '.png').convert('RGB')
    im.resize((w, round(w * im.height / im.width)), Image.LANCZOS).save('${OUT}/' + n + '.webp', quality=86, method=6)
`]);
})();
