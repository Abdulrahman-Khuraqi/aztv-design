# Copies every deliverable into "our workspace.html" (tab «ملفات التسليم»), so the one file holds them all:
# the Salla setup guide, the custom CSS, the image prompts, the logo SVGs, the block images and the project notes.
# Run after any change to those files:  python3 05-design/new-design/build/sync_workspace.py   (needs: pip install markdown)
# The workspace is often opened on its own (as a data: URL), so files are embedded as data URIs, not linked.
import base64, html, json, os, re
import markdown

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
WS = os.path.join(ROOT, 'our workspace.html')
ND = os.path.join(ROOT, '05-design/new-design')

def read(p): return open(os.path.join(ROOT, p), encoding='utf-8').read()
def b64(p): return base64.b64encode(open(os.path.join(ROOT, p), 'rb').read()).decode()
MIME = {'.css': 'text/css', '.md': 'text/markdown', '.html': 'text/html', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.py': 'text/x-python', '.js': 'text/javascript', '.cjs': 'text/javascript', '.json': 'application/json'}
def data_uri(p): return f'data:{MIME[os.path.splitext(p)[1]]};base64,{b64(p)}'
def dl(p, label=None):
    name = os.path.basename(p)
    text = 'تنزيل' if label == '' else 'تنزيل ' + html.escape(label or name)
    return f'<a class="files-btn" download="{name}" href="{data_uri(p)}">{text}</a>'

def md(p):
    out = markdown.markdown(read(p), extensions=['tables', 'fenced_code'])
    # code blocks: left-to-right, with a copy button
    return re.sub(r'<pre><code>(.*?)</code></pre>',
                  lambda m: f'<div class="files-code"><button type="button" class="files-btn files-copy">نسخ</button><pre dir="ltr"><code>{m.group(1)}</code></pre></div>',
                  out, flags=re.S)

css_path = '05-design/new-design/assets/css/malak-custom.css'
css = read(css_path)
img_dir = '05-design/new-design/assets/img/malak'
imgs = sorted(f for f in os.listdir(os.path.join(ROOT, img_dir)) if f.endswith(('.webp', '.png')))
GROUPS = [('أيقونات (التطبيقات والمميزات)', 'icon-'), ('بطاقات beIN', 'bein-'), ('شعارات المنصات بالأبيض', 'logo-'), ('صورة المقارنة', 'compare-')]
gallery = ''
for title, pre in GROUPS:
    items = ''.join(f'''<figure class="files-img"><img src="{data_uri(f'{img_dir}/{f}')}" alt="{f}">
<figcaption><code>{f}</code> {dl(f'{img_dir}/{f}', '')}</figcaption></figure>''' for f in imgs if f.startswith(pre))
    gallery += f'<h3>{title}</h3><div class="files-grid">{items}</div>'

bg_dir = '05-design/shared/subscription-backgrounds/export'
BACKGROUNDS = [('bg-aztv.webp', 'الخيار B · AZ TV بالأبيض'), ('bg-aztv-plus.webp', 'الخيار B · AZ TV Plus بالذهبي'),
               ('option-e-aztv.webp', 'الخيار E · AZ TV بالأبيض'), ('option-e-aztv-plus.webp', 'الخيار E · AZ TV Plus بالذهبي')]
backgrounds = ''.join(f'''<figure class="files-img"><img src="{data_uri(f'{bg_dir}/{f}')}" alt="{t}">
<figcaption><b>{t}</b><code>{f}</code> {dl(f'{bg_dir}/{f}', '')}</figcaption></figure>''' for f, t in BACKGROUNDS)

card_dir = '05-design/shared/subscription-cards/bg'
CARD_BGS = [('card-bg-aztv.webp', 'خلفية البطاقة · AZ TV بالأبيض والأسود'), ('card-bg-aztv-plus.webp', 'خلفية البطاقة · AZ TV Plus بالذهبي')]
card_bgs = ''.join(f'''<figure class="files-img"><img src="{data_uri(f'{card_dir}/{f}')}" alt="{t}">
<figcaption><b>{t}</b><code>{f}</code> {dl(f'{card_dir}/{f}', '')}</figcaption></figure>''' for f, t in CARD_BGS)

subscription_cards_dir = '05-design/shared/subscription-cards'
accepted_card = f'{subscription_cards_dir}/new/aztv-3m.png'
all_cards_sheet = f'{subscription_cards_dir}/new/all-cards.jpg'
product_sheet_b = f'{subscription_cards_dir}/product-images/overview-b.jpg'
product_sheet_e = f'{subscription_cards_dir}/product-images/overview-e.jpg'
subscription_card_source = f'{subscription_cards_dir}/card.html'
subscription_card_renderer = f'{subscription_cards_dir}/render-cards.cjs'

card_photos_dir = '05-design/shared/subscription-cards/photos/originals'
card_photo_files = sorted(f for f in os.listdir(os.path.join(ROOT, card_photos_dir)) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')))
card_photos = ''.join(f'''<figure class="files-img files-card-photo"><img src="{data_uri(f'{card_photos_dir}/{f}')}" alt="{f}" loading="lazy">
<figcaption><code>{f}</code> {dl(f'{card_photos_dir}/{f}', '')}</figcaption></figure>''' for f in card_photo_files)

transparent_portraits_dir = '05-design/shared/subscription-cards/stars/latest-roles/vertical/transparent'
transparent_portrait_files = sorted(
    f for f in os.listdir(os.path.join(ROOT, transparent_portraits_dir))
    if re.match(r'^\d{2}-.*\.png$', f, re.I)
)
transparent_portrait_count = len(transparent_portrait_files)
transparent_portraits = ''.join(f'''<figure class="files-img files-card-photo files-transparent-photo"><img src="{data_uri(f'{transparent_portraits_dir}/{f}')}" alt="{f}" loading="lazy">
<figcaption><code>{f}</code> {dl(f'{transparent_portraits_dir}/{f}', '')}</figcaption></figure>''' for f in transparent_portrait_files)
comparison_sheet = f'{transparent_portraits_dir}/contact-sheet-with-white-background-images.jpg'
cillian_white_portrait = '05-design/shared/subscription-cards/stars/latest-roles/vertical/03-cillian-murphy-white-background.png'

# who appears on the subscription cards (05-design/shared/subscription-cards/card-stars.json)
stars_path = '05-design/shared/subscription-cards/card-stars.json'
SD = json.load(open(os.path.join(ROOT, stars_path), encoding='utf-8'))
E = html.escape
player_cards = ''.join(f'<article class="star"><b class="n">{i}</b><h3>{E(p["ar"])}</h3><small class="ltr">{E(p["name"])}</small><p>{E(p["why"])}</p></article>'
                       for i, p in enumerate(SD['players'], 1))
star_cards = ''.join(f'<article class="star"><b class="n">{i}</b><h3>{E(s["ar_title"])}</h3><small class="ltr">{E(s["title"])}</small>'
                     f'<p class="who">{E(s["ar"])}<br><span class="ltr">{E(s["name"])}</span></p><p>{E(s["why"])}</p></article>'
                     for i, s in enumerate(SD['stars'], 1))
pair_rows = ''.join(f'<tr><td><span class="chip {"wait" if q["tier"] == "plus" else ""}">{"Plus" if q["tier"] == "plus" else "AZ TV"}</span> {E(q["card"])}</td>'
                    f'<td class="ltr">{E(q["player"])}</td><td class="ltr">{E(q["star"])}</td></tr>' for q in SD['pairs'])

logo_dir = '05-design/new-design/assets/img/logo'
logos = ''.join(f'''<figure class="files-img files-logo"><img src="{data_uri(f'{logo_dir}/{f}')}" alt="{f}">
<figcaption><code>{f}</code> {dl(f'{logo_dir}/{f}', '')}</figcaption></figure>''' for f in ('aztv-logo-stroke.svg', 'aztv-logo-shine.svg', 'aztv-logo-loop.svg', 'aztv-logo-animated.svg', 'aztv-logo.svg'))

PANEL = f'''<!-- FILES:START (generated by 05-design/new-design/build/sync_workspace.py; edit the source files, not this block) -->
<section class="panel" id="files" role="tabpanel">
  <header class="block">
    <p class="eyebrow">ملفات التسليم</p>
    <h1>كل ملفات التنفيذ في مكان واحد</h1>
    <p class="lead">نسخة من كل ملف نحتاجه لتنفيذ التصميم على سلة، محفوظة داخل هذا الملف نفسه: دليل التنفيذ، ملف الـ CSS، الشعار، الصور، ونصوص توليد الصور. كل ملف له زر تنزيل. المصدر في مجلد المشروع وفي GitHub، وهذه نسخة احتياطية تُحدَّث مع كل تعديل.</p>
    <p class="files-jump">
      <button type="button" class="linkbtn" data-jump="f-review">المراجعة والتعديلات التالية</button> ·
      <button type="button" class="linkbtn" data-jump="f-setup">دليل التنفيذ</button> ·
      <button type="button" class="linkbtn" data-jump="f-css">ملف الـ CSS</button> ·
      <button type="button" class="linkbtn" data-jump="f-logo">الشعار</button> ·
      <button type="button" class="linkbtn" data-jump="f-images">صور البلوكات</button> ·
      <button type="button" class="linkbtn" data-jump="f-subcards">بطاقات الاشتراك المعتمدة</button> ·
      <button type="button" class="linkbtn" data-jump="f-subbg">خلفيات بطاقات الاشتراك</button> ·
      <button type="button" class="linkbtn" data-jump="f-cardphotos">صور بطاقات الاشتراك</button> ·
      <button type="button" class="linkbtn" data-jump="f-stars">نجوم البطاقات</button> ·
      <button type="button" class="linkbtn" data-jump="f-prompts">نصوص الصور</button> ·
      <button type="button" class="linkbtn" data-jump="f-project">ملاحظات المشروع</button>
    </p>
  </header>

  <div class="block files-sec" id="f-review">
    <div class="files-head"><h2>المراجعة: التعديل التالي لكل قسم</h2>{dl('05-design/REVIEW.md')}</div>
    <p class="note"><code>05-design/REVIEW.md</code> · لقطات كل قسم في تبويب «لوحة التصميم».</p>
    <div class="files-doc">{md('05-design/REVIEW.md')}</div>
  </div>

  <div class="block files-sec" id="f-setup">
    <div class="files-head"><h2>دليل التنفيذ على سلة</h2>{dl('05-design/SALLA-SETUP.md')}</div>
    <p class="note"><code>05-design/SALLA-SETUP.md</code></p>
    <div class="files-doc">{md('05-design/SALLA-SETUP.md')}</div>
  </div>

  <div class="block files-sec" id="f-css">
    <div class="files-head"><h2>ملف الـ CSS للمتجر</h2>{dl(css_path)}</div>
    <p class="note"><code>{css_path}</code> · يُلصق كاملًا في خانة الـ CSS المخصص في سلة.</p>
    <div class="files-code"><button type="button" class="files-btn files-copy">نسخ الملف كاملًا</button><pre dir="ltr" class="files-tall"><code>{html.escape(css)}</code></pre></div>
  </div>

  <div class="block files-sec" id="f-logo">
    <div class="files-head"><h2>الشعار SVG</h2></div>
    <p class="note"><code>{logo_dir}/</code> · نسخة الإطار (stroke) في الهيدر، والنسخ الأخرى بدائل، والثابت لأي مكان آخر.</p>
    <div class="files-grid">{logos}</div>
  </div>

  <div class="block files-sec" id="f-images">
    <div class="files-head"><h2>صور البلوكات</h2></div>
    <p class="note"><code>{img_dir}/</code> · تُرفع في حقول البلوكات حسب دليل التنفيذ. صور الأقسام الأخرى (الـ Hero والتصنيفات) في <code>05-design/new-design/assets/img/</code>.</p>
    {gallery}
  </div>

  <div class="block files-sec" id="f-subcards">
    <div class="files-head"><h2>بطاقات الاشتراك · التصميم المعتمد</h2>{dl(f'{subscription_cards_dir}/README.md')}</div>
    <p class="note">كل ما نعمل عليه الآن في مكان واحد: البطاقة المعتمدة، البطاقات التسع، ملف التصميم، وأداة التصدير. الشكل المعتمد لكل البطاقات هو بطاقة «اشتراك ٣ شهور». البطاقات الثماني التي فيها وجوه كلها بالصور الآن: البطاقة ٥ (بلس سنة) بالصورتين 017 و018، والبطاقة ٧ (بلس ٦ شهور) بالصورتين 020 و014، والبطاقة ٨ بالصورة 016. كلها بانتظار المراجعة.</p>
    <div class="files-grid files-subscription-cards">
      <figure class="files-img files-subscription-card" id="f-subcards-accepted">
        <span class="files-status is-accepted">✓ البطاقة المعتمدة</span>
        <img src="{data_uri(accepted_card)}" alt="البطاقة المعتمدة: اشتراك AZ TV لمدة 3 شهور" loading="lazy">
        <figcaption><b>اشتراك AZ TV · ٣ شهور</b><code>new/aztv-3m.png</code>{dl(accepted_card, '')}</figcaption>
      </figure>
    </div>
    <h3>البطاقات التسع · بانتظار المراجعة</h3>
    <p class="note"><code>new/all-cards.jpg</code> · كل بطاقة برقمها كما في README.md (البطاقة ١ محذوفة). تُبنى من جديد بـ <code>node render-cards.cjs</code> ثم <code>python3 contact-sheet.py</code>.</p>
    <figure class="files-img files-all-cards" id="f-subcards-all">
      <img src="{data_uri(all_cards_sheet)}" alt="البطاقات التسع" loading="lazy" style="width:100%;height:auto">
      <figcaption><code>new/all-cards.jpg</code> {dl(all_cards_sheet, '')}</figcaption>
    </figure>
    <h3>صور المنتجات · البطاقات على الخلفية المعتمدة</h3>
    <p class="note"><code>{subscription_cards_dir}/product-images/</code> · البطاقات التسع كلها معتمدة، وكل واحدة موضوعة على خلفية المنتج المعتمدة (أبيض لـ AZ TV وذهبي للبلس)، 2000 × 2000 جاهزة لرفعها كصورة منتج في سلة. الخلفية B (الشعاع الأسود) هي المستخدمة في الموقع، والخلفية E (التقسيم المائل) بديل.</p>
    <figure class="files-img files-all-cards" id="f-subcards-products-b">
      <img src="{data_uri(product_sheet_b)}" alt="صور المنتجات على الخلفية B" loading="lazy" style="width:100%;height:auto">
      <figcaption><b>الخلفية B (في الموقع)</b><code>product-images/overview-b.jpg</code> {dl(product_sheet_b, '')}</figcaption>
    </figure>
    <figure class="files-img files-all-cards" id="f-subcards-products-e">
      <img src="{data_uri(product_sheet_e)}" alt="صور المنتجات على الخلفية E" loading="lazy" style="width:100%;height:auto">
      <figcaption><b>الخلفية E (بديل)</b><code>product-images/overview-e.jpg</code> {dl(product_sheet_e, '')}</figcaption>
    </figure>
    <div class="files-source-box" id="f-subcards-source">
      <div><h3>ملف تصميم البطاقة</h3><p class="note"><code>{subscription_card_source}</code> · يحتوي قالب البطاقة وتعريف كل منتج.</p></div>
      <div class="files-source-actions">{dl(subscription_card_source, 'card.html')}{dl(subscription_card_renderer, 'أداة التصدير render-cards.cjs')}</div>
    </div>
  </div>

  <div class="block files-sec" id="f-subbg">
    <div class="files-head"><h2>خلفيات بطاقات الاشتراك</h2></div>
    <p class="note"><code>{bg_dir}/</code> · خلفيتان معتمدتان (B و E)، لكل منهما نسخة AZ TV بالأبيض ونسخة AZ TV Plus بالذهبي. 2000 × 2000، والبطاقة توضع في المساحة 760 × 1296 في المنتصف (x 620، y 408). نسخ PNG في نفس المجلد، والمصدر <code>05-design/shared/subscription-backgrounds/backgrounds.html</code>.</p>
    <div class="files-grid">{backgrounds}</div>
    <h3>خلفية البطاقة نفسها</h3>
    <p class="note"><code>{card_dir}/</code> · ما تشترك فيه كل بطاقات الباقة قبل العنوان والصور والمدة. 760 × 1296 بزوايا وفتحة تعليق شفافة، توضع مباشرة في مساحة البطاقة على الخلفيتين. نسخ PNG ودليل أماكن المحتوى (<code>*-guide.png</code>) في نفس المجلد، والمصدر <code>05-design/shared/subscription-cards/card-background.html</code>.</p>
    <div class="files-grid">{card_bgs}</div>
  </div>

  <div class="block files-sec" id="f-cardphotos">
    <div class="files-head"><h2>صور بطاقات الاشتراك · الخلفية البيضاء</h2>{dl('05-design/shared/subscription-cards/photos/README.md')}</div>
    <p class="note">المجموعة الآن تضم {transparent_portrait_count} قصاصات شخصيات شفافة، وصورة كيليان مورفي بخلفية بيضاء، إضافة إلى {len(card_photo_files)} صورة أصلية للمقارنة والرجوع إليها.</p>
    <h3>الصور الجديدة بعد إزالة الخلفية</h3>
    <p class="note"><code>{transparent_portraits_dir}/</code> · {transparent_portrait_count} صور عمودية 1200 × 1500 بنسبة 4:5. تعرض الصفحة خلفها أرضية بيضاء فقط للمعاينة؛ الملفات نفسها PNG بخلفية شفافة. الصور المرفوضة لا تظهر هنا حتى تصل بدائل أفضل.</p>
    <div class="files-grid files-card-photos">{transparent_portraits}</div>
    <h3>كيليان مورفي · الخلفية البيضاء</h3>
    <p class="note">نسخة معدّلة من الصورة التي أرسلها العميل: أُزيلت خلفية الشارع والشخص الآخر، مع إبقاء الشخصية الرئيسية على أرضية بيضاء.</p>
    <div class="files-grid files-card-photos">
      <figure class="files-img files-card-photo"><img src="{data_uri(cillian_white_portrait)}" alt="كيليان مورفي على خلفية بيضاء" loading="lazy">
        <figcaption><b>Cillian Murphy</b><code>03-cillian-murphy-white-background.png</code> {dl(cillian_white_portrait, '')}</figcaption></figure>
    </div>
    <h3>مقارنة الصور الشفافة مع مجموعة الخلفية البيضاء</h3>
    <figure class="files-img files-comparison"><img src="{data_uri(comparison_sheet)}" alt="مقارنة صور الشخصيات الشفافة مع صور الخلفية البيضاء" loading="lazy">
      <figcaption><code>contact-sheet-with-white-background-images.jpg</code> {dl(comparison_sheet, '')}</figcaption>
    </figure>
    <h3>الصور الأصلية ذات الخلفية البيضاء</h3>
    <p class="note"><code>{card_photos_dir}/</code> · الصور الأصلية الإحدى عشرة كما وصلت، محفوظة دون تعديل.</p>
    <div class="files-grid files-card-photos">{card_photos}</div>
  </div>

  <div class="block files-sec" id="f-stars">
    <div class="files-head"><h2>نجوم البطاقات: أفضل ١٠ لاعبين و ١٠ نجوم</h2>{dl(stars_path)}</div>
    <p class="note"><code>{stars_path}</code> · الأشهر والأقوى جمهورًا، مختارون لجمهور سعودي وعربي يتابع الكرة والمسلسلات. ليس ترتيبًا مباشرًا: نتحقق من الأندية والمستوى الحالي قبل النشر.</p>
    <h3>أفضل ١٠ لاعبين</h3>
    <div class="stars">{player_cards}</div>
    <h3>أفضل ١٠ نجوم مسلسلات وأفلام</h3>
    <div class="stars">{star_cards}</div>
    <h3>اقتراح التوزيع على البطاقات</h3>
    <p class="note">{E(SD["pairs_note"])}</p>
    <div class="tablewrap"><table><thead><tr><th>البطاقة</th><th>اللاعب</th><th>النجم</th></tr></thead><tbody>{pair_rows}</tbody></table></div>
    <p class="note">{E(SD["reserve"])}</p>
    <p class="note">{E(SD["rights"])}</p>
  </div>

  <div class="block files-sec" id="f-prompts">
    <div class="files-head"><h2>نصوص توليد الصور</h2>{dl('05-design/IMAGE-PROMPTS.md')}</div>
    <p class="note"><code>05-design/IMAGE-PROMPTS.md</code> · لـ Gemini و ChatGPT.</p>
    <div class="files-doc" dir="ltr">{md('05-design/IMAGE-PROMPTS.md')}</div>
  </div>

  <div class="block files-sec" id="f-project">
    <details><summary><h2 style="display:inline">ملاحظات المشروع (PROJECT.md)</h2></summary>
      <div class="files-head" style="margin-top:12px">{dl('PROJECT.md')}</div>
      <div class="files-doc" dir="ltr">{md('PROJECT.md')}</div>
    </details>
  </div>
  <script>
  /* copy buttons: clipboard where allowed, otherwise select the text so Ctrl+C works */
  document.querySelectorAll("#files .files-copy").forEach(function (b) {{
    b.addEventListener("click", function () {{
      var code = b.parentElement.querySelector("code"), text = code.textContent;
      function done(t) {{ var o = b.textContent; b.textContent = t; setTimeout(function () {{ b.textContent = o; }}, 1500); }}
      function select() {{ var r = document.createRange(); r.selectNodeContents(code); var s = getSelection(); s.removeAllRanges(); s.addRange(r); done("محدد، اضغط Ctrl+C"); }}
      try {{ navigator.clipboard.writeText(text).then(function () {{ done("تم النسخ"); }}, select); }} catch (e) {{ select(); }}
    }});
  }});
  </script>
</section>
<!-- FILES:END -->
'''

STYLE = '''/* FILES-STYLE:START */
.files-jump { margin-top: 10px; color: var(--muted); }
.files-sec { margin-top: 34px; padding-top: 26px; border-top: 1px solid var(--line); }
.files-head { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px 16px; }
.files-head h2 { margin: 0; }
.files-btn { display: inline-flex; align-items: center; gap: 6px; padding: 6px 14px; border-radius: 999px; border: 1px solid rgba(234, 207, 105, .5);
  background: none; color: var(--gold); font: 500 14px/1.4 var(--body); text-decoration: none; cursor: pointer; white-space: nowrap; }
.files-btn:hover { background: var(--gold); color: var(--ink); }
.files-code { position: relative; margin: 12px 0; }
.files-code .files-copy { position: absolute; top: 10px; inset-inline-end: 10px; background: var(--ink); }
.files-code pre { margin: 0; padding: 46px 16px 16px; border-radius: 10px; background: var(--surface); border: 1px solid var(--line);
  overflow: auto; font: 400 13px/1.6 var(--mono); color: var(--text); white-space: pre-wrap; word-break: break-word; }
.files-tall { max-height: 560px; }
.files-doc { margin-top: 12px; overflow-x: auto; }
.files-doc table { margin: 10px 0; }
.files-doc td, .files-doc th { vertical-align: top; }
.files-doc h1 { font-size: 26px; } .files-doc h2 { font-size: 20px; margin-top: 26px; } .files-doc h3 { font-size: 17px; margin-top: 18px; }
.files-doc blockquote { margin: 12px 0; padding: 10px 16px; border-inline-start: 3px solid var(--gold); background: var(--gold-wash); border-radius: 8px; }
.files-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 12px; margin: 12px 0 18px; }
.files-img { margin: 0; padding: 10px; border-radius: 12px; background: var(--surface); border: 1px solid var(--line); display: flex; flex-direction: column; gap: 8px; }
.files-img img { width: 100%; aspect-ratio: 1; object-fit: contain; border-radius: 8px; background: #0D0D0D; }
.files-logo img { padding: 12px; }
.files-card-photos { grid-template-columns: repeat(auto-fill, minmax(185px, 1fr)); }
.files-card-photo img { aspect-ratio: 4 / 5; object-fit: contain; background: #fff; }
.files-transparent-photo img { background: linear-gradient(135deg, #fff 0 50%, #f2f2f2 50% 100%); background-size: 20px 20px; }
.files-comparison { max-width: 1120px; }
.files-comparison img { aspect-ratio: auto; object-fit: contain; background: #fff; }
.files-subscription-cards { grid-template-columns: repeat(auto-fit, minmax(250px, 360px)); }
.files-subscription-card { position: relative; }
.files-subscription-card img { aspect-ratio: 760 / 1296; object-fit: contain; background: transparent; }
.files-status { align-self: flex-start; padding: 5px 10px; border: 1px solid var(--line); border-radius: 999px; color: var(--muted); font-size: 12px; }
.files-status.is-accepted { border-color: rgba(134, 201, 160, .55); background: rgba(134, 201, 160, .1); color: var(--ok); font-weight: 700; }
.files-source-box { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px; padding: 18px; border: 1px solid rgba(234, 207, 105, .3); border-radius: 12px; background: var(--gold-wash); }
.files-source-box h3, .files-source-box p { margin: 0; }
.files-source-actions { display: flex; flex-wrap: wrap; gap: 8px; }
.files-img figcaption { display: flex; flex-direction: column; gap: 6px; align-items: flex-start; font-size: 12px; }
.files-img figcaption code { word-break: break-all; }
#files details > summary { cursor: pointer; }
.stars { display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 14px; margin: 12px 0 22px; }
.star { position: relative; display: flex; flex-direction: column; gap: 4px; padding: 18px 18px 16px; border-radius: 14px; background: var(--surface); border: 1px solid var(--line); min-width: 0; }
.star .n { font: 700 14px/1 var(--mono); color: var(--gold); direction: ltr; }
.star h3 { margin: 6px 0 0; font-size: 19px; }
.star small { color: var(--muted); font-size: 13px; }
.star .who { margin-top: 6px; color: var(--text); font-size: 15px; font-weight: 500; }
.star p { max-width: none; color: var(--muted); font-size: 14px; line-height: 1.7; }
.star .who { color: var(--gold); }
/* FILES-STYLE:END */
'''

t = open(WS, encoding='utf-8').read()
# panel: replace the generated block, or add it before the log tab panel the first time
if '<!-- FILES:START' in t:
    t = re.sub(r'<!-- FILES:START.*?<!-- FILES:END -->\n', lambda m: PANEL, t, flags=re.S)
else:
    anchor = '<!-- ============ السجل'
    i = t.find(anchor) if anchor in t else t.find('<section class="panel" id="log"')
    t = t[:i] + PANEL + '\n' + t[i:]
# styles
if '/* FILES-STYLE:START */' in t:
    t = re.sub(r'/\* FILES-STYLE:START \*/.*?/\* FILES-STYLE:END \*/\n', lambda m: STYLE, t, flags=re.S)
else:
    t = t.replace('</style>', STYLE + '</style>', 1)
# tab button
if 'data-go="files"' not in t.split('</nav>')[0]:
    t = t.replace('    <button type="button" class="tab" role="tab" data-go="log">السجل</button>',
                  '    <button type="button" class="tab" role="tab" data-go="files">ملفات التسليم</button>\n    <button type="button" class="tab" role="tab" data-go="log">السجل</button>', 1)
# «قائمة المهام» tab from 05-design/todo.json (also writes 05-design/TODO.md); placed right after the overview tab
import sys
sys.path.insert(0, os.path.dirname(__file__))
import todo_panel
TODO_PANEL, TODO_STYLE = todo_panel.build(ROOT)
if '<!-- TODO:START' in t:
    t = re.sub(r'<!-- TODO:START.*?<!-- TODO:END -->\n', lambda m: TODO_PANEL, t, flags=re.S)
else:
    i = t.find('<section class="panel" id="plan"')
    j = t.rfind('<!--', 0, i)
    t = t[:j] + TODO_PANEL + '\n' + t[j:]
if '/* TODO-STYLE:START */' in t:
    t = re.sub(r'/\* TODO-STYLE:START \*/.*?/\* TODO-STYLE:END \*/\n', lambda m: TODO_STYLE, t, flags=re.S)
else:
    t = t.replace('</style>', TODO_STYLE + '</style>', 1)
if 'data-go="todo"' not in t.split('</nav>')[0]:
    t = t.replace('    <button type="button" class="tab" role="tab" data-go="plan">الخطة</button>',
                  '    <button type="button" class="tab" role="tab" data-go="todo">قائمة المهام</button>\n    <button type="button" class="tab" role="tab" data-go="plan">الخطة</button>', 1)
open(WS, 'w', encoding='utf-8').write(t)
print('workspace', len(t) // 1024, 'KB')
