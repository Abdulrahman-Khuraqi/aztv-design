# Writes the animated section-title icons (07 TV, 11 crown, 15 renew) to assets/img/malak/head-*.svg.
# Run:  python3 05-design/new-design/build/make_head_icons.py
# Each icon is one SVG with its motion inside (CSS), like the animated logo, so it runs as a plain uploaded image.
# Every animation repeats on the same 3 s loop, so export_head_icons.js can turn them into seamless animated WebP files
# (fallback for Salla if the title block's icon field does not take SVG): then run this script with --webp <frames dir>.
import math, os, sys

ND = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ND, 'assets/img/malak')

# shared look: the logo's gold, a dark glossy body, a breathing glow behind; still for reduced motion
DEFS = '''
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#FBEBA8"/><stop offset=".45" stop-color="#ECD169"/><stop offset="1" stop-color="#B38D36"/>
    </linearGradient>
    <linearGradient id="body" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2E2E2E"/><stop offset="1" stop-color="#101010"/>
    </linearGradient>
    <radialGradient id="glow">
      <stop offset="0" stop-color="#EACF69" stop-opacity=".42"/><stop offset="1" stop-color="#EACF69" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#FFF" stop-opacity="0"/><stop offset=".5" stop-color="#FFF8DC" stop-opacity=".55"/><stop offset="1" stop-color="#FFF" stop-opacity="0"/>
    </linearGradient>'''
CSS = '''
    #glow { animation: breathe 3s ease-in-out infinite; transform-box: view-box; transform-origin: 64px 68px; }
    #float { animation: float 3s ease-in-out infinite; }
    .shine { animation: shine 3s cubic-bezier(.45, 0, .2, 1) infinite; }
    @keyframes breathe { 0%, 100% { opacity: .55; transform: scale(.92); } 50% { opacity: 1; transform: scale(1.04); } }
    @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-3px); } }
    @keyframes shine { 0%, 15% { transform: translateX(-70px) skewX(-20deg); } 55%, 100% { transform: translateX(150px) skewX(-20deg); } }'''
STILL = '\n    @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }'


def svg(name, label, comment, defs, css, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128" role="img" aria-label="{label}">
  <!-- {comment}
       Made by build/make_head_icons.py (edit there). One 3 s loop; still for reduced motion. -->
  <defs>{DEFS}{defs}
  </defs>
  <style>{CSS}{css}{STILL}
  </style>
  <circle id="glow" cx="64" cy="68" r="58" fill="url(#glow)"/>
{body}
</svg>
'''


def tv():
    defs = '''
    <radialGradient id="screen" cx=".5" cy=".3" r=".85">
      <stop offset="0" stop-color="#3A3016"/><stop offset=".55" stop-color="#151410"/><stop offset="1" stop-color="#0A0A0A"/>
    </radialGradient>
    <clipPath id="screen-clip"><rect x="28" y="50" width="72" height="44" rx="8"/></clipPath>'''
    css = '''
    #ant { animation: wiggle 3s ease-in-out infinite; transform-box: view-box; transform-origin: 64px 42px; }
    #waves { transform: translate(84px, 22px); }
    .wave { fill: none; stroke: #ECD169; stroke-width: 3; stroke-linecap: round; opacity: 0;
            transform-box: view-box; transform-origin: 0 0; animation: wave 1.5s ease-out infinite; }
    .wave.w2 { animation-delay: .35s; }
    #play { transform-box: fill-box; transform-origin: 40% 50%; animation: pulse 1.5s ease-in-out infinite; }
    #led { animation: blink 1.5s steps(1, end) infinite; }
    @keyframes wiggle { 0%, 100% { transform: rotate(0); } 25% { transform: rotate(-7deg); } 75% { transform: rotate(7deg); } }
    @keyframes wave { 0% { opacity: 0; transform: scale(.7); } 30% { opacity: 1; } 100% { opacity: 0; transform: scale(1.12); } }
    @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.14); } }
    @keyframes blink { 0% { fill: #ECD169; } 50% { fill: #3A3016; } }'''
    body = '''  <g id="float">
    <g id="ant" fill="none" stroke="url(#gold)" stroke-width="3.5" stroke-linecap="round">
      <path d="M64 42 48 25"/><path d="M64 42 84 22"/>
      <circle cx="48" cy="25" r="3.8" fill="url(#gold)" stroke="none"/><circle cx="84" cy="22" r="3.8" fill="url(#gold)" stroke="none"/>
      <g id="waves">{WAVES}</g>
    </g>
    <path d="M40 103 34 114M88 103 94 114" stroke="url(#gold)" stroke-width="4" stroke-linecap="round"/>
    <rect x="16" y="40" width="96" height="64" rx="16" fill="url(#body)" stroke="url(#gold)" stroke-width="3.5"/>
    <rect x="28" y="50" width="72" height="44" rx="8" fill="url(#screen)" stroke="#ECD169" stroke-opacity=".35" stroke-width="1.5"/>
    <g clip-path="url(#screen-clip)"><rect class="shine" x="10" y="40" width="26" height="64" fill="url(#shine)"/></g>
    <path id="play" d="M58 63.5v17a2 2 0 0 0 3 1.7l14.5-8.5a2 2 0 0 0 0-3.4L61 61.8a2 2 0 0 0-3 1.7z" fill="url(#gold)"/>
    <path d="M30 99h14" stroke="#ECD169" stroke-opacity=".35" stroke-width="2" stroke-linecap="round"/>
    <circle id="led" cx="98" cy="99" r="2" fill="#ECD169"/>
  </g>'''
    def wave(rr, cls):   # arc around the right antenna tip, up and to the right
        a0, a1 = math.radians(-80), math.radians(5)
        return (f'<path class="{cls}" d="M{rr * math.cos(a0):.1f} {rr * math.sin(a0):.1f}'
                f'A{rr} {rr} 0 0 1 {rr * math.cos(a1):.1f} {rr * math.sin(a1):.1f}"/>')
    body = body.replace('{WAVES}', wave(8, 'wave') + wave(14, 'wave w2'))
    return svg('tv', 'AZ TV', 'Section 07 title icon: a TV whose antennas wiggle and send signal waves, a pulsing gold play button, a shine across the screen.', defs, css, body)


def crown():
    crown_path = 'M25 84 19 45 44 63 64 31 84 63 109 45 103 84Z'
    defs = f'''
    <clipPath id="crown-clip"><path d="{crown_path}"/><rect x="22" y="83" width="84" height="19" rx="5"/></clipPath>
    <path id="spark" d="M0-8C1-1.5 1.5-1 8 0 1.5 1 1 1.5 0 8-1 1.5-1.5 1-8 0-1.5-1-1-1.5 0-8Z"/>'''
    css = '''
    #crown { animation: rock 3s ease-in-out infinite; transform-box: view-box; transform-origin: 64px 102px; }
    .spark { fill: #FFF6D6; opacity: 0; transform-box: fill-box; transform-origin: center; animation: twinkle 1.5s ease-in-out infinite; }
    .spark.s2 { animation-delay: .5s; } .spark.s3 { animation-delay: 1s; }
    #gem { animation: gem 1.5s ease-in-out infinite; }
    @keyframes rock { 0%, 100% { transform: rotate(-3deg); } 50% { transform: rotate(3deg); } }
    @keyframes twinkle { 0%, 100% { opacity: 0; transform: scale(.2) rotate(0); } 45% { opacity: 1; transform: scale(1) rotate(45deg); } 70% { opacity: 0; transform: scale(.4) rotate(90deg); } }
    @keyframes gem { 0%, 100% { fill: #FBEBA8; } 50% { fill: #FFFFFF; } }'''
    body = f'''  <g id="float"><g id="crown">
    <path d="{crown_path}" fill="url(#gold)" stroke="url(#gold)" stroke-width="4" stroke-linejoin="round"/>
    <path d="M30 79 26 54 44 67 64 39 84 67 102 54 98 79" fill="none" stroke="#FFF4C8" stroke-opacity=".45" stroke-width="1.5" stroke-linejoin="round"/>
    <circle cx="19" cy="45" r="5.5" fill="url(#gold)"/><circle cx="64" cy="30" r="6.5" fill="url(#gold)"/><circle cx="109" cy="45" r="5.5" fill="url(#gold)"/>
    <path d="M64 55 71.5 66 64 77 56.5 66Z" fill="url(#body)" stroke="#B38D36" stroke-width="2" stroke-linejoin="round"/>
    <rect x="22" y="83" width="84" height="19" rx="5" fill="url(#body)" stroke="url(#gold)" stroke-width="3"/>
    <path id="gem" d="M64 86.5 70 92.5 64 98.5 58 92.5Z" fill="#FBEBA8"/>
    <circle cx="41" cy="92.5" r="3.6" fill="url(#gold)"/><circle cx="87" cy="92.5" r="3.6" fill="url(#gold)"/>
    <g clip-path="url(#crown-clip)"><rect class="shine" x="0" y="20" width="28" height="90" fill="url(#shine)"/></g>
  </g></g>
  <g transform="translate(106 20)"><use href="#spark" class="spark"/></g>
  <g transform="translate(20 23) scale(.75)"><use href="#spark" class="spark s2"/></g>
  <g transform="translate(117 74) scale(.6)"><use href="#spark" class="spark s3"/></g>'''
    return svg('crown', 'AZ TV Plus', 'Section 11 title icon: a gold crown with a black enamel band and jewels; it rocks gently, a shine sweeps across, sparkles twinkle.', defs, css, body)


def renew():
    cx, cy, r = 64, 64, 46
    def pt(a, rr=r): return cx + rr * math.cos(math.radians(a)), cy + rr * math.sin(math.radians(a))
    def arc(a0, a1):
        (x0, y0), (x1, y1) = pt(a0), pt(a1)
        return f'M{x0:.1f} {y0:.1f}A{r} {r} 0 0 1 {x1:.1f} {y1:.1f}'
    def head(a):   # arrowhead at angle a, pointing clockwise (SVG angles grow clockwise)
        tip = pt(a + 9)
        o, i = pt(a - 3, r + 9), pt(a - 3, r - 9)
        return f'M{tip[0]:.1f} {tip[1]:.1f}L{o[0]:.1f} {o[1]:.1f}L{i[0]:.1f} {i[1]:.1f}Z'
    css = '''
    #ring { animation: spin 3s cubic-bezier(.65, 0, .35, 1) infinite; transform-box: view-box; transform-origin: 64px 64px; }
    #badge { transform-box: fill-box; transform-origin: center; animation: pop 3s ease-out infinite; }
    #tick { stroke-dasharray: 16; animation: tick 3s ease-out infinite; }
    #card { animation: tilt 3s ease-in-out infinite; transform-box: view-box; transform-origin: 64px 63px; }
    @keyframes spin { 0% { transform: rotate(0); } 60%, 100% { transform: rotate(360deg); } }
    @keyframes pop { 0%, 55% { transform: scale(0); } 68% { transform: scale(1.18); } 76%, 92% { transform: scale(1); } 100% { transform: scale(0); } }
    @keyframes tick { 0%, 62% { stroke-dashoffset: 16; } 76%, 100% { stroke-dashoffset: 0; } }
    @keyframes tilt { 0%, 100% { transform: rotate(-6deg); } 60% { transform: rotate(4deg); } }'''
    defs = '''
    <clipPath id="card-clip"><rect x="38" y="45" width="52" height="36" rx="6"/></clipPath>'''
    body = f'''  <circle cx="64" cy="64" r="46" fill="none" stroke="#ECD169" stroke-opacity=".16" stroke-width="2" stroke-dasharray="3 6"/>
  <g id="float">
    <g id="ring" fill="url(#gold)">
      <path d="{arc(200, 330)}" fill="none" stroke="url(#gold)" stroke-width="6.5" stroke-linecap="round"/>
      <path d="{arc(20, 150)}" fill="none" stroke="url(#gold)" stroke-width="6.5" stroke-linecap="round"/>
      <path d="{head(330)}" stroke="url(#gold)" stroke-width="2" stroke-linejoin="round"/>
      <path d="{head(150)}" stroke="url(#gold)" stroke-width="2" stroke-linejoin="round"/>
    </g>
    <g id="card">
      <rect x="38" y="45" width="52" height="36" rx="6" fill="url(#body)" stroke="url(#gold)" stroke-width="2.5"/>
      <rect x="45" y="52" width="11" height="9" rx="2" fill="url(#gold)"/>
      <path d="M45 70h24M45 75h14" stroke="#ECD169" stroke-opacity=".55" stroke-width="2.4" stroke-linecap="round"/>
      <text x="83" y="60" text-anchor="end" font-family="Arial, sans-serif" font-size="9" font-weight="700" fill="#ECD169">AZ</text>
      <g clip-path="url(#card-clip)"><rect class="shine" x="10" y="35" width="18" height="56" fill="url(#shine)"/></g>
    </g>
    <g id="badge">
      <circle cx="86" cy="80" r="11" fill="url(#gold)" stroke="#0D0D0D" stroke-width="2.5"/>
      <path id="tick" d="M80.5 80.5l3.8 3.8 7-7.6" fill="none" stroke="#0D0D0D" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
  </g>'''
    return svg('renew', 'تجديد', 'Section 15 title icon: two gold arrows spin once around a subscription card, then a check badge pops on; a shine crosses the card.', defs, css, body)


ICONS = {'head-tv': tv, 'head-crown': crown, 'head-renew': renew}


def webp(frames_dir, step=2, size=160):
    """animated WebP from the 30 fps frames export_head_icons.js wrote (<name>-000.png ...), one seamless loop.
    Every 2nd frame (15 fps) at 160 px keeps each file at 170-300 KB, lighter than the GIFs they replace."""
    from PIL import Image
    for name in ICONS:
        files = sorted(f for f in os.listdir(frames_dir) if f.startswith(name + '-') and f.endswith('.png'))[::step]
        frames = [Image.open(os.path.join(frames_dir, f)).convert('RGBA').resize((size, size), Image.LANCZOS) for f in files]
        out = os.path.join(OUT, name + '.webp')
        frames[0].save(out, save_all=True, append_images=frames[1:], duration=round(1000 * step / 30), loop=0,
                       quality=70, method=6, minimize_size=True, allow_mixed=True)
        print(out, len(frames), os.path.getsize(out) // 1024, 'KB')


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == '--webp':
        webp(sys.argv[2])
    else:
        for name, make in ICONS.items():
            p = os.path.join(OUT, name + '.svg'); open(p, 'w', encoding='utf-8').write(make())
            print(p, os.path.getsize(p), 'bytes')
