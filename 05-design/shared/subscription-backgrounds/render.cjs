// Renders both backgrounds to export/ (2000 x 2000) and the mock-ups with the old 6-month cards to mockups/.
// Run from this folder: node render.cjs (needs the playwright package)
const { chromium } = require("playwright");
const { pathToFileURL } = require("node:url");
const { resolve } = require("node:path");

(async () => {
const page_ = pathToFileURL(resolve("backgrounds.html")).href;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1100, height: 1100 }, deviceScaleFactor: 2 });

const jobs = [];
for (const [tier, name] of [["regular", "aztv"], ["plus", "aztv-plus"]]) {
  jobs.push({ q: `tier=${tier}`, out: `export/bg-${name}.png` });
  jobs.push({ q: `tier=${tier}&guide=1`, out: `export/bg-${name}-guide.jpg` });
  jobs.push({ q: `tier=${tier}&card=src/old-card-${tier}-6m.png`, out: `mockups/bg-${name}-6m.jpg` });
}
for (const j of jobs) {
  await page.goto(`${page_}?${j.q}`);
  await page.waitForSelector("body[data-ready]");
  await page.waitForFunction(() => [...document.images].every(i => !i.src || i.complete));
  await page.locator("#bg").screenshot(j.out.endsWith(".jpg") ? { path: j.out, quality: 88 } : { path: j.out });
  console.log(j.out);
}
await browser.close();
})();
