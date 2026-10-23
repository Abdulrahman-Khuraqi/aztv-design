// Renders every background to export/ (2000 x 2000) and the mock-ups with the old 6-month cards to mockups/.
// Run from this folder: node render.cjs (needs the playwright package)
const { chromium } = require("playwright");
const { pathToFileURL } = require("node:url");
const { resolve } = require("node:path");

(async () => {
const page_ = pathToFileURL(resolve("backgrounds.html")).href;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1100, height: 1100 }, deviceScaleFactor: 2 });

const jobs = [];
for (const opt of ["a", "b"]) for (const tier of ["regular", "plus"]) {
  jobs.push({ q: `opt=${opt}&tier=${tier}`, out: `export/option-${opt}-${tier}.png` });
  jobs.push({ q: `opt=${opt}&tier=${tier}&guide=1`, out: `export/option-${opt}-${tier}-guide.jpg` });
  jobs.push({ q: `opt=${opt}&tier=${tier}&card=src/old-card-${tier}-6m.png`, out: `mockups/option-${opt}-${tier}-6m.jpg` });
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
