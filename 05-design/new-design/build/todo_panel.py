# Builds the «قائمة المهام» workspace tab (and 05-design/TODO.md) from 05-design/todo.json.
# Called by sync_workspace.py; edit todo.json, not the generated HTML.
import base64, html, io, json, os
from PIL import Image

WHO = {'me': ('Claude يركّبها', 'me'), 'you': ('أنت: توليد صورة', 'you'), 'client': ('من العميل', 'client')}
STATUS = {'todo': 'لم يبدأ', 'doing': 'قيد العمل', 'done': 'تم'}


def thumb(path, size=180):
    """small WebP data URI of the image in use today (first frame for GIFs)"""
    try:
        im = Image.open(path)
        im.seek(0)
        im = im.convert('RGBA')
    except Exception:
        return ''
    im.thumbnail((size, size))
    bg = Image.new('RGBA', im.size, (13, 13, 13, 255))
    bg.alpha_composite(im)
    buf = io.BytesIO()
    bg.convert('RGB').save(buf, 'WEBP', quality=72)
    return 'data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode()


def build(root):
    data = json.load(open(os.path.join(root, '05-design/todo.json'), encoding='utf-8'))
    imgdir = os.path.join(root, '05-design/new-design/assets/img')
    items = [i for g in data['groups'] for i in g['items']]
    total, done = len(items), sum(1 for i in items if i['status'] == 'done')

    groups_html, md = '', ['# قائمة المهام: الصور التي تُعاد', '',
                           f'مولّدة من `05-design/todo.json` (لا تُعدَّل هنا). تم {done} من {total}.', '',
                           'طريقة التوليد: أرفق مع كل نص صورة المرجع `05-design/new-design/assets/img/cat-aztv-3d.png` '
                           '(أو `cat-aztv-plus-3d.png`)، واحفظ الناتج باسم «الملف الجديد».', '']
    for g in data['groups']:
        md += [f"## {g['title']}", '', f"- **أين:** {g['where']}", f"- **لماذا:** {g['why']}", f"- **كيف:** {g['how']}", '']
        cards = ''
        for it in g['items']:
            who_t, who_c = WHO[it['who']]
            prompt = ''
            if it.get('prompt'):
                full = it['prompt']
                if it['who'] == 'you' and not it.get('refs'):   # items with their own references carry their own style text
                    full += '\n\n' + data['style'].replace('{EDGE}', it.get('edge', 'gold'))
                prompt = ('<details class="todo-prompt"><summary>نص التوليد (Prompt)</summary><div class="files-code">'
                          '<button type="button" class="files-btn files-copy">نسخ</button>'
                          f'<pre dir="ltr"><code>{html.escape(full)}</code></pre></div></details>')
            # "now" is a file in new-design/assets/img/, or a repo path starting with 05-design/
            now = it.get('now', '')
            now = os.path.join(root if now.startswith('05-design/') else imgdir, now) if now else ''
            img = thumb(now, 720 if g.get('closeup') else 180) if now else ''
            img_html = f'<img src="{img}" alt="الصورة الحالية">' if img else ''
            # a finished item also shows its new image (first file found by its new name)
            new_img = ''
            if it['status'] == 'done':
                for cand in (os.path.join(imgdir, 'products', it['new']), os.path.join(imgdir, it['new'])):
                    if os.path.exists(cand):
                        new_img = thumb(cand)
                        break
            chips = f'<span class="chip todo-who-{who_c}">{who_t}</span><span class="chip">{STATUS[it["status"]]}</span>'
            if it.get('priority'):
                chips += f'<span class="chip wait">{html.escape(it["priority"])}</span>'
            meta = f'<dt>الرابط</dt><dd><code>{html.escape(it["link"])}</code></dd>' if it.get('link') else ''
            refs = ''
            for r in it.get('refs', []):   # reference images to attach when generating: thumbnail + download
                rp = os.path.join(root, r)
                if os.path.exists(rp):
                    # embedded as a 1024px WebP to keep the workspace light; the full PNG is at the path shown
                    im = Image.open(rp).convert('RGBA'); im.thumbnail((1024, 1024)); buf = io.BytesIO(); im.save(buf, 'WEBP', quality=90)
                    name = os.path.splitext(os.path.basename(r))[0] + '.webp'
                    refs += (f'<a class="todo-ref" download="{name}" title="{r}" href="data:image/webp;base64,{base64.b64encode(buf.getvalue()).decode()}">'
                             f'<img src="{thumb(rp)}" alt=""><span>{os.path.basename(r)}</span></a>')
            if refs:
                prompt = f'<div class="todo-refs"><b>صور المرجع (أرفقها مع النص، اضغط للتنزيل)</b><div>{refs}</div></div>' + prompt
            meta += f'<dt>الملف الجديد</dt><dd><code>{html.escape(it["new"])}</code></dd><dt>المواصفات</dt><dd>{html.escape(it["spec"])}</dd>'
            cards += (f'<article class="todo-item{" todo-closeup" if g.get("closeup") else ""}" data-id="{it["id"]}" data-status="{it["status"]}">'
                      f'<label class="todo-check"><input type="checkbox"{" checked" if it["status"] == "done" else ""}><span>تم</span></label>'
                      f'<figure class="todo-now">{img_html}<figcaption>{"القديمة" if new_img else "الحالية"}</figcaption>'
                      f'{f"<img class={chr(34)}todo-new{chr(34)} src={chr(34)}{new_img}{chr(34)} alt=\"\"><figcaption>الجديدة</figcaption>" if new_img else ""}</figure>'
                      f'<div class="todo-body"><h4>{html.escape(it["title"])}</h4><p class="todo-chips">{chips}</p>'
                      f'<dl class="todo-meta">{meta}</dl>{prompt}</div></article>\n')
            md.append(f"- [{'x' if it['status'] == 'done' else ' '}] **{it['title']}** · {who_t}"
                      f"{' · ' + it['priority'] if it.get('priority') else ''} · الآن: `{it.get('now', '')}` ← الجديد: `{it['new']}` · {it['spec']}")
        md.append('')
        groups_html += (f'<div class="block todo-group" id="todo-{g["id"]}">\n'
                        f'  <h2>{g["title"]} <span class="chip">{len(g["items"])}</span></h2>\n'
                        f'  <dl class="todo-why"><dt>أين</dt><dd>{g["where"]}</dd><dt>لماذا</dt><dd>{g["why"]}</dd><dt>كيف</dt><dd>{g["how"]}</dd></dl>\n'
                        f'  <div class="todo-list">\n{cards}  </div>\n</div>\n')

    open(os.path.join(root, '05-design/TODO.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')

    jump = ' · '.join(f'<button type="button" class="linkbtn" data-jump="todo-{g["id"]}">{g["title"]}</button>' for g in data['groups'])
    panel = (
        '<!-- TODO:START (generated by 05-design/new-design/build/todo_panel.py from 05-design/todo.json) -->\n'
        '<section class="panel" id="todo" role="tabpanel">\n'
        '  <header class="block">\n'
        '    <p class="eyebrow">قائمة المهام</p>\n'
        '    <h1>الصور التي تُعاد</h1>\n'
        '    <p class="lead">كل صورة قديمة ما زالت في التصميم الجديد، مرتبة حسب القسم. لكل صورة: شكلها اليوم، والملف الجديد، ومن يصنعه، '
        'ونص التوليد جاهزًا للنسخ. علامة «تم» هنا للمتابعة على جهازك، والحالة الرسمية في <code>05-design/todo.json</code>.</p>\n'
        f'    <div class="todo-progress"><div class="todo-bar"><span style="width:{round(100 * done / total)}%"></span></div>'
        f'<p><b id="todo-count">{done}</b> من {total} تم</p></div>\n'
        '    <p class="note">طريقة التوليد: أرفق مع كل نص صورة المرجع <code>05-design/new-design/assets/img/cat-aztv-3d.png</code> '
        '(أو <code>cat-aztv-plus-3d.png</code>) حتى تخرج كل الصور بنفس أسلوب القسم 03، واحفظ الناتج باسم «الملف الجديد» وارفعه لي.</p>\n'
        f'    <p class="files-jump">{jump}</p>\n'
        '  </header>\n'
        f'{groups_html}'
        '  <script>\n'
        '  /* local tick marks (per viewer); the shared status lives in 05-design/todo.json */\n'
        '  (function () {\n'
        '    var KEY = "aztv-todo-checks", saved = {};\n'
        '    try { saved = JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) {}\n'
        '    var items = document.querySelectorAll("#todo .todo-item"), count = document.getElementById("todo-count");\n'
        '    function refresh() { var n = 0; items.forEach(function (it) { var c = it.querySelector("input"); it.classList.toggle("is-done", c.checked); if (c.checked) n++; }); count.textContent = n; }\n'
        '    items.forEach(function (it) {\n'
        '      var c = it.querySelector("input"), id = it.dataset.id;\n'
        '      if (it.dataset.status !== "done" && saved[id]) c.checked = true;\n'
        '      c.addEventListener("change", function () { saved[id] = c.checked; try { localStorage.setItem(KEY, JSON.stringify(saved)); } catch (e) {} refresh(); });\n'
        '    });\n'
        '    refresh();\n'
        '  })();\n'
        '  </script>\n'
        '</section>\n'
        '<!-- TODO:END -->\n')
    return panel, STYLE


STYLE = '''/* TODO-STYLE:START */
.todo-progress { display: flex; align-items: center; gap: 14px; margin-top: 14px; }
.todo-bar { flex: 1; max-width: 360px; height: 8px; border-radius: 99px; background: var(--surface); overflow: hidden; border: 1px solid var(--line); }
.todo-bar span { display: block; height: 100%; background: var(--gold); }
.todo-progress p { margin: 0; color: var(--muted); }
.todo-group { margin-top: 30px; padding-top: 24px; border-top: 1px solid var(--line); }
.todo-group h2 { display: flex; align-items: center; gap: 10px; }
.todo-why { display: grid; grid-template-columns: auto 1fr; gap: 4px 14px; margin: 8px 0 14px; font-size: 15px; }
.todo-why dt { color: var(--gold); }
.todo-why dd { margin: 0; color: var(--muted); }
.todo-list { display: grid; gap: 12px; }
.todo-item { display: grid; grid-template-columns: auto 110px 1fr; gap: 14px; align-items: start; padding: 14px; border-radius: 12px; background: var(--surface); border: 1px solid var(--line); }
.todo-item.is-done { opacity: .55; }
.todo-item.is-done h4 { text-decoration: line-through; }
.todo-check { display: flex; flex-direction: column; align-items: center; gap: 4px; font-size: 12px; color: var(--muted); cursor: pointer; }
.todo-check input { width: 22px; height: 22px; accent-color: #EACF69; cursor: pointer; }
.todo-now { margin: 0; text-align: center; }
.todo-now img { width: 110px; height: 110px; object-fit: contain; border-radius: 8px; background: #0D0D0D; border: 1px solid var(--line); }
.todo-now figcaption { font-size: 12px; color: var(--muted); }
.todo-item.todo-closeup { grid-template-columns: auto 260px 1fr; }
.todo-closeup .todo-now img { width: 260px; height: auto; border: 0; background: none; }
.todo-now img.todo-new { margin-top: 8px; border-color: rgba(234, 207, 105, .5); }
.todo-item.is-done .todo-now { opacity: 1; }
.todo-body { min-width: 0; }
.todo-body h4 { margin: 0 0 6px; font-size: 16px; }
.todo-chips { display: flex; flex-wrap: wrap; gap: 6px; margin: 0 0 8px; }
.todo-who-me { color: var(--ok); border-color: rgba(134, 201, 160, .4); }
.todo-who-you { color: var(--gold); border-color: rgba(234, 207, 105, .45); }
.todo-who-client { color: var(--new); border-color: rgba(146, 185, 230, .45); }
.todo-meta { display: grid; grid-template-columns: auto 1fr; gap: 2px 12px; margin: 0; font-size: 14px; }
.todo-meta dt { color: var(--muted); }
.todo-meta dd { margin: 0; min-width: 0; word-break: break-word; }
.todo-prompt { margin-top: 8px; }
.todo-refs { margin-top: 10px; font-size: 14px; }
.todo-refs > div { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 6px; }
.todo-ref { display: flex; flex-direction: column; align-items: center; gap: 4px; width: 120px; color: var(--gold); font-size: 11.5px; text-decoration: none; text-align: center; word-break: break-all; }
.todo-ref img { width: 120px; height: 90px; object-fit: contain; border-radius: 8px; background: #0D0D0D; border: 1px solid var(--line); }
.todo-ref:hover img { border-color: var(--gold); }
.todo-prompt summary { cursor: pointer; color: var(--gold); font-size: 14px; }
@media (max-width: 640px) { .todo-item { grid-template-columns: auto 1fr; } .todo-body { grid-column: 1 / -1; } }
/* TODO-STYLE:END */
'''
