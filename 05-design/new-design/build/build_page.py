# Run: python3 05-design/new-design/build/build_page.py   (needs: pip install beautifulsoup4 pillow)
# Builds 05-design/new-design/index.html from the saved live page (old-design) using only ملاك (ANGEL) blocks:
# the theme's own markup, reordered and refilled the way the merchant would in Salla's theme customizer.
import copy, re, sys
from bs4 import BeautifulSoup

import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')) + '/'
SRC = ROOT + '03-current-site/old-design/index.html'
OUT = ROOT + '05-design/new-design/index.html'
S = 'https://aztvstore.com/ar'
def c(cid): return f'{S}/-/c{cid}'
def page(pid): return f'{S}/redirect/pages/{pid}'

html = open(SRC, encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')
def frag(s): return BeautifulSoup(s, 'html.parser')
def block(cid): return copy.copy(soup.find('section', attrs={'component-id': cid}))

# ---------- theme settings (colours + dark mode), applied the way Salla prints them ----------
style = soup.find('style', string=re.compile(r'--dark-bg-main'))
style.string = re.sub(r':root \{.*?\}', ''':root {
        --font-main:  'PingARLT' ;
        --font-secondary:  'PingARLT' ;
        --color-primary: #EACF69;
        --color-primary-dark: #B8983F;
        --color-primary-light: #F3DE8E;
        --color-primary-reverse: #0D0D0D;
        --dark-bg-main: #0D0D0D;
        --dark-text-main: #F3F0E6;
        --dark-text-sec: #B9B4A6;
        --dark-grey: #1A1A1A;
        --text-btn: #0D0D0D;
        --bg-color: #0D0D0D;
        --header-bg: #0D0D0D;
        --menu-bg: #0D0D0D;
        --footer-bg: #0D0D0D;
    }''', style.string, count=1, flags=re.S)
soup.html['class'] = ['dark', 'theme-dark', 'angel-theme', 'hydrated']
soup.body['class'] = [x.replace('color-mode-light', 'color-mode-dark') for x in soup.body['class']]
soup.html['style'] = soup.html['style'].replace('--theme-primary-color: #000000', '--theme-primary-color: #EACF69').replace('--store-color: #000000', '--store-color: #EACF69')

# our one custom CSS (goes into Salla), then the local-only preview fixes
theme_css = soup.find('link', href='assets/css/app-400a6c5f.css')
theme_css.insert_after(frag('\n<link rel="stylesheet" href="assets/css/preview-only.css"><!-- local preview only: stands in for Salla\'s scripts -->'))
last_style = soup.head.find_all(['style', 'link'])[-1]
last_style.insert_after(frag('\n<link rel="stylesheet" href="assets/css/malak-custom.css"><!-- THE custom CSS for Salla: paste this file into the store\'s custom CSS -->\n'))

# remove browser-extension leftovers from the capture
for sel in ['#claude-agent-glow-border', '#claude-phantom-cursor', '#claude-agent-animation-styles']:
    for el in soup.select(sel): el.decompose()
for st in soup.find_all('style'):
    if st.string and 'imageye-selected' in st.string: st.decompose()

# ---------- logo: animated SVG in the header, static SVG in the footer ----------
hl = soup.select_one('header img.logo-light')
# header: the STROKE version (slow 10 s loop: gold stroke draws the logo, it fills, a shine passes, it fades, repeat)
hl['src'] = 'assets/img/logo/aztv-logo-stroke.svg'; hl['width'] = '909'; hl['height'] = '814'; hl['style'] = 'width: auto; height:2.85rem'
# in dark mode ملاك hides .logo-light in a dark header and shows .logo-dark (the theme's dark-mode logo field), so the logo goes there too
dl = copy.copy(hl); dl['class'] = ['logo-dark']; hl.insert_after(dl)
fl = soup.select_one('footer img.logo-light')
fl['src'] = 'assets/img/logo/aztv-logo.svg'; fl['width'] = '885'; fl['height'] = '790'; fl['style'] = 'width:auto; height:2.5rem'

# ---------- main menu (Salla: «القوائم» → القائمة الرئيسية) ----------
# Fixes from the plan: no empty card (the menu banner slide had no image), no empty image circles, beIN grouped
# devices / packages / renewal, AZ TV Box, renewal and offers added, activation in one place. Items carry no images.
MENU = [
  ('باقات الاشتراك', c(1765121197), [('الباقة العادية AZ TV', c(971844871)), ('باقة البلس AZ TV Plus', c(921887589))]),
  ('تجديد الاشتراك', c(183760688), None),
  ('عالم beIN', c(1461115041), [('أجهزة beIN 4K', c(757128774)), ('أجهزة beIN PVR', c(1398521669)), ('قمة عربي', c(1147218769)),
                                ('قمة خليجي', c(415231319)), ('تميز عربي', c(374229586)), ('تميز خليجي', c(1787038800)),
                                ('تجديد اشتراك beIN الرسمي', c(899162953))]),
  ('AZ TV Box', f'{S}/-/p1152326425', None),
  ('العروض', c(1510593888), None),
  ('تفعيل الاشتراك', page(1920849311), [('تفعيل AZ TV', page(1920849311)), ('تفعيل AZ TV Plus', page(389705163))]),
]
def menu_li(name, href, children):
    a = f'<a aria-label="{name}" class="sidemenu-link text-gray-500{" has-max" if children else ""}" href="{href}" target="_self"><div class="menu_title font-primary">{name}</div></a>'
    if not children:
        return f'<li class="text-sm font-bold md:text-lg">{a}</li>'
    subs = f'<li><a aria-label="{name}" class="sidemenu-link display-all-category text-gray-500" href="{href}" target="_self"><div class="font-primary">عرض الكل</div></a></li>'
    subs += ''.join(f'<li class="text-sm font-bold md:text-lg"><a aria-label="{n}" class="sidemenu-link text-gray-500" href="{h}" target="_self"><div class="menu_title font-primary">{n}</div></a></li>' for n, h in children)
    return f'<li class="text-sm font-bold md:text-lg">{a}<ul>{subs}</ul></li>'
mm = soup.select_one('#mobile-menu ul.main-menu')
for li in mm.find_all('li', recursive=False):
    cls = li.get('class') or []
    if 'links' in cls or 'social' in cls: continue   # «روابط تهمك» and «خدمة العملاء» come from the theme, kept
    li.decompose()                                    # includes the empty menu-banner slide
first_fixed = mm.find('li', recursive=False)
for name, href, children in MENU:
    first_fixed.insert_before(frag(menu_li(name, href, children)))

# ---------- block factories ----------
def divider(cid, title, sub=None, button=None, icon=None, countdown=False, xl=False, base='1319788990'):
    d = block(base); d['component-id'] = cid
    d['class'] = ['s-block', 's-angel--divider'] + (['xl-title'] if xl else []) + ['merge-bottom', 'centered-title']
    d.select_one('.divider-title h2').string = title
    p = d.select_one('.divider-title p')
    if sub: p.string = sub
    elif p: p.decompose()
    ic = d.select_one('.divider-icon')
    if ic and icon: ic.img['src'] = ic.img['data-src'] = icon
    elif ic: ic.decompose()
    cd = d.select_one('.divider-countdown')
    if cd and not countdown: cd.decompose()
    a = d.select_one('a.divider-url')
    if button: a.string = button[0]; a['href'] = button[1]; a['aria-label'] = button[0]
    else: a.decompose()
    return d

CAT_SLIDE = None
def categories(cid, items, base='2109940184'):
    global CAT_SLIDE
    b = block(base); b['component-id'] = cid
    wrap = b.select_one('.swiper-wrapper')
    slides = wrap.select('.swiper-slide')
    tpl = copy.copy(slides[0])
    for s in slides: s.decompose()
    for i, (name, href, img) in enumerate(items, 1):
        s = copy.copy(tpl)
        s['aria-label'] = f'{i} / {len(items)}'; s['class'] = ['swiper-slide', 'swiper-width-control']; s.attrs.pop('style', None)
        a = s.select_one('a'); a['href'] = href; a['aria-label'] = name
        bg = s.select_one('.lazy__bg'); bg['data-bg'] = img; bg['style'] = f'background-image: url("{img}");'
        s.select_one('span').string = name
        wrap.append(s)
    return b

def banners(cid, items, cols):
    b = block('668296755'); b['component-id'] = cid
    grid = b.select_one('.square-grid')
    grid['class'] = [x for x in grid['class'] if not x.startswith('grid-cols-')] + [f'grid-cols-{cols}']
    tiles = grid.select('.banner-square'); tpl = copy.copy(tiles[0])
    for t in tiles: t.decompose()
    for href, img in items:
        t = copy.copy(tpl); t.a['href'] = href; t.img['src'] = t.img['data-src'] = img
        grid.append(t)
    return b

def hero(cid, href, desktop, phone=None, alt='Az TV | عز تي في'):
    b = block('1800638171'); b['component-id'] = cid
    slides = b.select('.swiper-slide'); [s.decompose() for s in slides[1:]]
    s = slides[0]; a = s.a; a['href'] = href; a.attrs.pop('data-ak-original-href', None)
    pic = a.picture; src = pic.source; img = pic.img
    if phone: src['srcset'] = src['data-srcset'] = phone
    else: src.decompose()
    img['src'] = img['data-src'] = desktop; img['alt'] = alt
    b.select_one('salla-slider').attrs.pop('data-ak-hero-override', None)
    return b

def hero_video(cid, href, mp4, mp4_phone, poster, poster_phone, alt='Az TV | عز تي في'):
    """ملاك hero slider with one video slide (the theme styles .responsive-video / .video-swiper).
    Markup rebuilt from the theme CSS: check it against a real video slide once the video is set in the customizer."""
    b = hero(cid, href, poster, poster_phone, alt)
    b['class'] = b['class'] + ['responsive-video']
    a = b.select_one('.swiper-slide a')
    a.clear()
    a.append(frag(f'''<div class="video-swiper"><video class="w-full" autoplay muted loop playsinline preload="auto" poster="{poster}" aria-hidden="true">
<source media="(max-width: 767px)" src="{mp4_phone}" type="video/mp4"><source media="(max-width: 767px)" src="{mp4_phone[:-4]}.webm" type="video/webm">
<source src="{mp4}" type="video/mp4"><source src="{mp4[:-4]}.webm" type="video/webm"></video></div>'''))
    return b

def raw(s): return frag(s)

# ---------- 02: moving strip (ANGEL "angel-ad"), rebuilt from the theme CSS: confirm against the real block ----------
# white logos on one 400x160 canvas each, optical size baked in, so the strip gives them all the same height
LOGOS = [('bein', 'beIN SPORTS'), ('ssc', 'SSC'), ('mbc', 'MBC'), ('shahid', 'Shahid'), ('netflix', 'Netflix'),
         ('osnplus', 'OSN+'), ('starzplay', 'STARZPLAY'), ('stctv', 'stc tv')]
items = ''.join(f'<span class="angel-ad__item"><img class="angel-ad__img" src="assets/img/malak/logo-{f}.png" alt="{n}"></span>' for f, n in LOGOS)
STRIP = raw(f'''<section class="s-block s-block--angel-ad" component-id="new-02-strip">
<!-- ملاك moving strip (angel-ad). Markup rebuilt from the theme CSS (angel-ad__container/__slider/__item/__img): check it against the real block. -->
<div class="angel-ad"><div class="angel-ad__container"><div class="angel-ad__slider">{items}{items}</div></div></div>
</section>''')

# ---------- 16: FAQ (ANGEL "s-block--faqs"), rebuilt from the theme CSS ----------
FAQ = [
  ('متى يوصلني الاشتراك بعد الدفع؟', 'يوصلك الاشتراك بعد الدفع مباشرة، وتقدر تبدأ التفعيل على جهازك فورًا.'),
  ('وش الفرق بين باقة AZ TV وباقة AZ TV Plus؟', 'AZ TV هي الباقة العادية بمدد تبدأ من شهر. AZ TV Plus تعطيك أعلى جودة مشاهدة وخيار اشتراك لجهازين.'),
  ('على أي أجهزة يشتغل الاشتراك؟', 'على أجهزة أبل، جوالات وشاشات أندرويد، وشاشات سامسونق وLG، وعلى جهاز AZ TV Box.'),
  ('كيف أفعّل اشتراكي؟', 'من قسم التطبيقات والأجهزة: اختر جهازك واتبع خطوات تفعيل AZ TV أو AZ TV Plus.'),
  ('وش طرق الدفع المتاحة؟', 'مدى، Apple Pay، البطاقات الائتمانية، والتقسيط مع تابي وتمارا.'),
  ('كيف أجدد اشتراكي؟', 'من قسم تجديد الاشتراك: اختر باقتك والمدة، والتجديد بسعر أقل لعملائنا.'),
  ('واجهتني مشكلة، كيف أتواصل معكم؟', 'كلمنا على واتساب أو اتصل على 0509130883، أو راسلنا على تيليجرام.'),
]
faq_items = ''.join(f'''<div class="faq-entry"><input type="checkbox" id="faq-{i}" class="hidden"{' checked' if i == 1 else ''}>
<div class="faq-box border rounded-md da-brdr"><label for="faq-{i}" class="faq-question flex items-center justify-between gap-4 cursor-pointer font-primary">{q}<span class="open-badge"></span></label>
<div class="faq-answer"><p class="da-ts">{a}</p></div></div></div>''' for i, (q, a) in enumerate(FAQ, 1))
FAQS = raw(f'''<section class="s-block s-block--faqs" component-id="new-16-faq">
<!-- ملاك FAQ block (s-block--faqs). Markup rebuilt from the theme CSS (faqs-list, input:checked + div, open-badge, faq-answer): check it against the real block. Answers are drafts for the client. -->
<div class="container"><div class="s-block__title"><div class="flex flex-col w-full"><h2 class="w-full da-cp text-center">الأسئلة الشائعة</h2>
<p class="w-full text-center !p-0 text-gray-400 da-ts">إجابات سريعة قبل ما تطلب</p></div></div>
<div class="faqs-list flex flex-col gap-3">{faq_items}</div></div>
</section>''')

IMG = 'assets/img/'
M = IMG + 'malak/'
B = []
# 01 Hero: slider (poster now, video slide later) + title block pulled over it by the CSS
# 01 Hero: the black-and-white video (assets/video/, phone version cropped 3:4), its first frame as the poster
VID = 'assets/video/'
B += [hero_video('new-01-hero', c(1765121197), VID + 'hero.mp4', VID + 'hero-phone.mp4', VID + 'hero-poster.webp', VID + 'hero-poster-phone.webp'),
      divider('new-01-title', 'المباريات والمسلسلات في اشتراك واحد',
              'كل ما تحتاجه للمشاهدة والترفيه، من اشتراكات عز تي في إلى أجهزة beIN، على كل أجهزتك.', ('تصفح الباقات', c(1765121197)), xl=True)]
# 02 Logos
B += [divider('new-02-title', 'كل منصاتك وقنواتك في مكان واحد', 'رياضة، مسلسلات، أفلام وبرامج من أشهر المنصات'), STRIP]
# 03 Main categories
B += [divider('new-03-title', 'تسوّق حسب القسم', 'وصول سريع إلى الباقات والتجديد وأجهزة beIN'),
      categories('new-03-cats', [('تجديد الاشتراك', c(183760688), IMG + 'cat-renewal-3d.webp'), ('AZ TV', c(971844871), IMG + 'cat-aztv-3d-bw.webp'),
                                 ('AZ TV Plus', c(921887589), IMG + 'cat-aztv-plus-3d.webp'), ('beIN Sports', c(899162953), IMG + 'cat-bein-3d.webp'),
                                 ('AZ TV Box', f'{S}/-/p1152326425', IMG + 'cat-aztv-box-3d.webp')])]
# 04 beIN world: title + three balanced cards in one banners block (4K receiver, PVR receiver, official renewal).
# The five package tiles were removed (packages stay reachable from the menu and «تصفح عروض beIN»). Cards: build/make_bein.js
B += [divider('1319788990', 'عالم beIN', 'أجهزة واشتراكات وتجديدات beIN الرسمية', ('تصفح عروض beIN', c(1461115041))),
      banners('668296755', [(c(757128774), IMG + 'bein/bein-card-4k.webp'), (c(1398521669), IMG + 'bein/bein-card-pvr.webp'),
                            (c(899162953), IMG + 'bein/bein-card-renew.webp')], 3)]
# 05 AZ TV Box: featured product. Block image = the box on dark (wide, product on the left, empty right half for the text; the CSS lays the text over it).
# Subtitle (block field) leads with the free Plus year, the strongest reason to buy, instead of leaving it in the fifth tab.
b5 = block('1551497783')
im5 = b5.select_one('.p_image img'); im5['src'] = im5['data-src'] = IMG + 'aztv-box-dark.webp'; im5['width'] = '1600'; im5['height'] = '893'
b5.select_one('h2 + p').string = 'جهاز أندرويد بدقة 4K، ومعه اشتراك AZ TV Plus سنة كاملة مجانًا'
B += [b5]
# 06 Season offers: title with countdown and button + products grid
B += [divider('43834166', 'عروض بداية الموسم', 'خصم حتى 60٪ على باقات عز تي في وعز تي في بلس', ('كل العروض', c(1510593888)), countdown=True), block('817347637')]
# 07 AZ TV packages
d7 = block('427126746'); d7.select_one('.divider-title h2').string = 'اشتراكات AZ TV'; d7.select_one('.divider-title p').string = 'الباقة العادية: نقلة نوعية لجهازك'
B += [d7, block('353140267')]
# 08 AZ TV apps
B += [divider('1336426713', 'تطبيقات وأجهزة AZ TV', 'اختر جهازك واتبع خطوات التفعيل', ('تفعيل AZ TV', page(1920849311))),
      categories('2109940184', [('أجهزة أبل', page(1090910122), M + 'icon-apple.webp'), ('جوالات أندرويد', page(750360850), M + 'icon-android-phone.webp'),
                                ('شاشات أندرويد', page(192097435), M + 'icon-android-tv.webp'), ('شاشات سامسونق وLG', page(60771101), M + 'icon-smart-tv.webp')])]
# 09 Why us: store features
f9 = block('602276575'); f9.select_one('.s-block__title h2').string = 'ليش تختار عز تي في؟'; f9.select_one('.s-block__title p').string = 'كل اللي تحتاجه عشان تبدأ المشاهدة بدون تعقيد'
for feat, (t1, t2, ic) in zip(f9.select('.angel-feature'), [('تفعيل سريع', 'طلبك يوصلك بعد الدفع مباشرة', 'icon-fast'), ('دعم يرد عليك', 'واتساب وتيليجرام والاتصال', 'icon-support'),
                                                              ('طرق دفع متعددة', 'مدى، Apple Pay، تابي وتمارا', 'icon-payment'), ('يعمل على كل أجهزتك', 'أبل وأندرويد والشاشات الذكية', 'icon-devices')]):
    bg = feat.select_one('.lazy__bg'); bg['data-bg'] = M + ic + '.webp'; bg['style'] = f'background-image: url("{M}{ic}.webp");'
    ps = feat.select('p'); ps[0].string = t1; ps[1].string = t2
    for k in ('data-prefix', 'data-suffix', 'data-to'): ps[0].attrs.pop(k, None)
    ps[0]['class'] = [x for x in ps[0]['class'] if x != 'has-num']
B += [f9]
# 10 Testimonials (the block prints its own title)
B += [block('1444537310')]
# 11 Plus packages
d11 = block('1161342244'); d11.select_one('.divider-title h2').string = 'اشتراكات AZ TV Plus'; d11.select_one('.divider-title p').string = 'أعلى جودة مشاهدة، مع خيار اشتراك لجهازين'
B += [d11, block('1726651700')]
# 12 Plus apps
B += [divider('852429351', 'تطبيقات وأجهزة AZ TV Plus', 'بعد الشراء، اختر جهازك وفعّل البلس في دقائق', ('تفعيل AZ TV Plus', page(389705163))),
      categories('1625484070', [('أجهزة أبل', page(316806827), M + 'icon-apple.webp'), ('جوالات أندرويد', page(750360850), M + 'icon-android-phone.webp'),
                                ('شاشات أندرويد', page(2122758163), M + 'icon-android-tv.webp'), ('شاشات سامسونق وLG', page(1220412517), M + 'icon-smart-tv.webp')])]
# 13 Comparison: no ملاك block, so a designed image in a hero slider (desktop + phone image)
B += [divider('new-13-title', 'AZ TV أو AZ TV Plus؟', 'مقارنة سريعة تساعدك تختار الباقة الأنسب', ('تصفح الباقات', c(1765121197))),
      hero('new-13-compare', c(1765121197), M + 'compare-desktop.webp', M + 'compare-phone.webp', alt='مقارنة بين AZ TV و AZ TV Plus')]
# 14 Second store
d14 = divider('569291821', '2 والثالث مجانًا', 'أضف ثلاث تيشرتات للسلة ويتفعّل العرض', ('تسوّق التيشرتات', 'https://azshirtsstore.com/'), xl=True, base='569291821')
B += [d14, block('1409389868')]
# 15 Loyal customers
d15 = block('1584482337'); h = d15.select_one('.divider-title h2'); h.string = 'لعملائنا الأوفياء'
if not d15.select_one('.divider-title p'):
    h.insert_after(frag('<p class="w-full mt-1 px-1 !p-0 !m-0 text-gray-400 da-ts whitespace-nowrap">جدّد اشتراكك بسعر أقل</p>'))
B += [d15, block('677271330')]
# 16 FAQ
B += [FAQS]
# 17 Final CTA
B += [divider('new-17-cta', 'جاهز تبدأ المشاهدة؟', 'اختر باقتك اليوم، أو جدّد اشتراكك وكمّل من حيث وقفت.', ('تصفح الباقات', c(1765121197)), xl=True)]

# products blocks: the dividers already title them, so the blocks' own titles are left empty (block setting)
for blk in B:
    for el in blk.select('[block-title]'):
        if blk.select_one('custom-salla-product-card'): el['block-title'] = ''
    if blk.select_one('custom-salla-product-card'):
        for h2 in blk.select('.s-slider-block__title-right h2, .s-block__title .right-side h2'): h2.string = ''
    lst = blk.select_one('salla-products-list[style]')
    if lst and blk.get('component-id') == '817347637': lst['style'] = '--mob-products-cols:2;--products-cols:2'

# replace the old block run (first hero .. last products slider) with the new order
app = soup.select_one('.app-inner')
old = [s for s in app.find_all('section', recursive=False) if s.get('component-id') not in (None, '')]
anchor = old[0]
marker = soup.new_tag('i'); anchor.insert_before(marker)
for s in old: s.decompose()
for blk in B:
    marker.insert_before(blk); marker.insert_before('\n')
marker.decompose()

# ---------- product images: the finished subscription cards on the approved background ----------
# 05-design/shared/subscription-cards/product-images/b/<name>.jpg (2000 x 2000, made by render-products.cjs) -> assets/img/products/<name>.webp (1000 x 1000)
# and every product card of these ten products shows it instead of the store's old image (needs Pillow)
from PIL import Image
PRODUCT_CARDS = {  # Salla product id -> card file
    '1133679038': 'aztv-6m', '527896233': 'aztv-3m', '264351896': 'aztv-1m',
    '331255752': 'plus-12m', '1669484767': 'plus-12m-2dev', '1879371242': 'plus-6m', '1024479901': 'plus-3m',
    '777133688': 'renew-aztv', '287657453': 'renew-plus',
    '930436127': 'offer-week'}  # the offer of the week (سنة + ٣ شهور, 96 SAR): two finished cards on the stage
PRODUCT_SRC = ROOT + '05-design/shared/subscription-cards/product-images/'   # background F (f/, straight split, chosen by the client 2026-10-25) for all; PRODUCT_BG=b or e picks another
PRODUCT_OUT = ROOT + '05-design/new-design/assets/img/products/'
os.makedirs(PRODUCT_OUT, exist_ok=True)
for card in PRODUCT_CARDS.values():
    Image.open(PRODUCT_SRC + os.environ.get('PRODUCT_BG', 'f') + '/' + card + '.jpg').convert('RGB').resize((1000, 1000), Image.LANCZOS).save(PRODUCT_OUT + card + '.webp', quality=88, method=6)
swapped = 0
for a in soup.select('a[href]'):
    m = re.search(r'/p(\d+)$', a['href'])
    img = a.find('img', class_='s-product-card-image-contain')
    if m and img and m.group(1) in PRODUCT_CARDS:
        img['src'] = img['data-src'] = f'assets/img/products/{PRODUCT_CARDS[m.group(1)]}.webp'
        swapped += 1
print('product images swapped', swapped)

out = str(soup)
out = out.replace('<!-- ANGEL Theme by AfterAds', '<!-- NEW DESIGN built only from the store theme ملاك (ANGEL) blocks + assets/css/malak-custom.css. Generated by the build script; see 05-design/SALLA-SETUP.md. -->\n<!-- ANGEL Theme by AfterAds', 1)
open(OUT, 'w', encoding='utf-8').write(out)
print('blocks', len(B), 'bytes', len(out))
