// Renders white platform logos (strip, section 02) from assets/img/logos/ ; then build_page's comment explains the 400x160 canvas step.
const { chromium } = require(process.env.PW || 'playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ deviceScaleFactor: 1 });
  await p.goto('http://localhost:8770/README.md');
  for (const [f, white] of [['bein-white.svg',1],['ssc.svg',0],['mbc.svg',0],['shahid.svg',0],['netflix.svg',0],['osnplus.svg',0],['starzplay-white.png',1],['stctv.svg',0]]) {
    await p.setContent(`<body style="margin:0;background:transparent"><img id=i src="/assets/img/logos/${f}" style="height:120px;display:block;${white ? '' : 'filter:brightness(0) invert(1)'}"></body>`, { waitUntil: 'networkidle' });
    await (await p.$('#i')).screenshot({ path: `${process.argv[2]}/logo-${f.replace(/(-white)?\.(svg|png)$/, '')}.png`, omitBackground: true });
  }
  await b.close(); })();
