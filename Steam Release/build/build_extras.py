# -*- coding: utf-8 -*-
"""Render the non-card TTS assets: player boards, combat CRT, card backs, unit tokens."""
import json, math, os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = r"C:\Users\CAO YANG\Desktop\Constantinople 1453"
ART = os.path.join(ROOT, "artifacts")
OUT = os.path.join(ROOT, "Steam Release", "v0", "images")
TOKOUT = os.path.join(OUT, "tokens")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SCALE = 1.5
MAXDIM = 4000          # TTS/Unity texture limit is 4096; stay safely under

os.makedirs(TOKOUT, exist_ok=True)

def cap(im):
    """Downscale so neither dimension exceeds MAXDIM (TTS can't load bigger)."""
    w, h = im.size
    if max(w, h) <= MAXDIM:
        return im
    r = MAXDIM / float(max(w, h))
    return im.resize((max(1, int(w * r)), max(1, int(h * r))), Image.LANCZOS)

# ---- palette ----
PORPHYRY_DEEP = (44, 19, 57)
OTTOMAN_DEEP = (24, 46, 30)
NEUTRAL_BG = (42, 32, 21)
GOLD = (169, 132, 60)
GOLD_BRIGHT = (216, 180, 101)
PARCH = (230, 217, 174)

def font(sz, bold=True):
    for f in ([r"C:\Windows\Fonts\georgiab.ttf"] if bold else []) + \
             [r"C:\Windows\Fonts\georgia.ttf", r"C:\Windows\Fonts\constan.ttf"]:
        if os.path.exists(f):
            return ImageFont.truetype(f, sz)
    return ImageFont.load_default()

def balanced_div(html, start):
    """Full <div ...>...</div> string beginning at index `start`."""
    depth = 0
    for t in re.finditer(r'<div\b|</div>', html[start:]):
        if t.group(0) == '</div>':
            depth -= 1
            if depth == 0:
                return html[start:start + t.end()]
        else:
            depth += 1
    return html[start:]

def extract_style(html):
    m = re.search(r"<style>.*?</style>", html, re.S)
    return m.group(0) if m else ""

def chrome_shot(html_path, png_path, w, h):
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
           "--default-background-color=00000000",
           "--force-device-scale-factor=%s" % SCALE,
           "--window-size=%d,%d" % (w, h),
           "--screenshot=" + png_path, "file:///" + html_path.replace("\\", "/")]
    subprocess.run(cmd, capture_output=True, text=True)
    if not os.path.exists(png_path):
        print("FAILED", png_path); sys.exit(1)

HEAD = (u'<!doctype html><html data-theme="light"><head><meta charset="utf-8">'
        u'<style>html,body{margin:0!important;padding:0!important;'
        u'background:transparent!important;}'
        u'header p,.notes{display:none!important;}%s</style></head>'
        u'<body>%s%s</body></html>')

MEASURE_JS = (u'<script>window.addEventListener("load",function(){var b='
              u'document.querySelector(".board");document.documentElement'
              u'.setAttribute("data-bw",b?Math.ceil(b.scrollWidth):0);});</script>')

def measure_board(html_path):
    """Board's natural content width, measured with the original wrapping."""
    r = subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                        "--virtual-time-budget=4000", "--dump-dom",
                        "file:///" + html_path.replace("\\", "/")],
                       capture_output=True, text=True)
    m = re.search(r'data-bw="(\d+)"', r.stdout)
    return int(m.group(1)) if m else 0

def render_sheet(src, name, width=None):
    html = open(os.path.join(ART, src), encoding="utf-8").read()
    # pass 1: measure the board at its natural (wrapped) layout width
    mp = os.path.join(OUT, name + "_measure.html")
    open(mp, "w", encoding="utf-8").write(HEAD % ("", html, MEASURE_JS))
    bw = measure_board(mp)
    win_w = (bw + 80) if bw else (width or 2000)
    # pass 2: unclip the board and render at exactly its content width
    over = (u'.wrap{max-width:none!important;}'
            u'.board{overflow:visible!important;}')
    page = HEAD % (over, html, "")
    hp = os.path.join(OUT, name + "_src.html")
    open(hp, "w", encoding="utf-8").write(page)
    raw = os.path.join(OUT, name + "_raw.png")
    chrome_shot(hp, raw, win_w, 4000)
    im = Image.open(raw).convert("RGBA")
    # threshold alpha so faint box-shadow halos don't defeat the autocrop
    mask = im.split()[-1].point(lambda a: 255 if a > 30 else 0)
    bbox = mask.getbbox()
    pad = 12
    bbox = (max(0, bbox[0] - pad), max(0, bbox[1] - pad),
            min(im.size[0], bbox[2] + pad), min(im.size[1], bbox[3] + pad))
    im = cap(im.crop(bbox))
    out = os.path.join(OUT, name + ".png")
    im.save(out)
    os.remove(raw)
    print("sheet", name, im.size, "->", os.path.basename(out))
    return {"file": name + ".png", "w": im.size[0], "h": im.size[1]}

# ---------- card backs ----------
def star(draw, cx, cy, r, fill):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    draw.polygon(pts, fill=fill)

def make_back(name, bg, emblem):
    W, H = 600, 840
    im = Image.new("RGBA", (W, H), bg + (255,))
    d = ImageDraw.Draw(im)
    d.rectangle([26, 26, W - 26, H - 26], outline=GOLD, width=4)
    d.rectangle([40, 40, W - 40, H - 40], outline=GOLD_BRIGHT, width=1)
    cx, cy = W // 2, H // 2 - 20
    if emblem == "cross":                      # Byzantine
        t = 40
        d.rectangle([cx - t, cy - 150, cx + t, cy + 150], fill=GOLD_BRIGHT)
        d.rectangle([cx - 110, cy - t, cx + 110, cy + t], fill=GOLD_BRIGHT)
        for dx in (-110, 110):
            d.rectangle([cx + dx - 8, cy - 90, cx + dx + 8, cy + 90], fill=GOLD_BRIGHT)
    elif emblem == "crescent":                 # Ottoman
        r = 150
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD_BRIGHT)
        off = 55
        d.ellipse([cx - r + off, cy - r, cx + r + off, cy + r], fill=bg + (255,))
        star(d, cx + r + 40, cy, 60, GOLD_BRIGHT)
    else:                                      # Neutral diamond
        r = 150
        d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)],
                  outline=GOLD_BRIGHT, width=6)
        star(d, cx, cy, 70, GOLD_BRIGHT)
    ft = font(46); fb = font(30, bold=False)
    def ctext(y, s, f, col):
        w = d.textbbox((0, 0), s, font=f)[2]
        d.text(((W - w) / 2, y), s, font=f, fill=col)
    ctext(90, u"CONSTANTINOPLE", font(34), GOLD_BRIGHT)
    ctext(H - 150, u"1453", ft, GOLD_BRIGHT)
    ctext(H - 92, name.upper(), fb, GOLD)
    out = os.path.join(OUT, name + "_back.png")
    im.save(out)
    print("back", name, "->", os.path.basename(out))
    return name + "_back.png"

# ---------- unit tokens ----------
def render_tokens():
    html = open(os.path.join(ART, "unit_token_template.html"), encoding="utf-8").read()
    style = extract_style(html)
    groups = []
    for m in re.finditer(r'<div class="token-group"', html):
        grp = balanced_div(html, m.start())
        lm = re.search(r'tg-label">([^<]*)<', grp)
        label = re.sub(r"&amp;", "&", lm.group(1)).strip() if lm else "unit"
        cm = re.search(r'<div class="(?:counter|leader) ', grp)
        if not cm:
            continue
        counter = balanced_div(grp, cm.start())
        head = counter.split(">", 1)[0]
        side = "byz" if "byz" in head else "ott"
        groups.append((label, counter, side))
    cols = 6
    cell = 230
    rows = (len(groups) + cols - 1) // cols
    cells = "\n".join('<div class="cell">%s</div>' % c for _, c, _ in groups)
    page = (u'<!doctype html><html data-theme="light"><head><meta charset="utf-8">%s'
            u'<style>html,body{margin:0;padding:0;background:transparent;}'
            u'.tgrid{display:grid;grid-template-columns:repeat(%d,%dpx);grid-auto-rows:%dpx;}'
            u'.cell{display:flex;align-items:center;justify-content:center;}'
            u'</style></head><body><div class="tgrid">%s</div></body></html>'
            % (style, cols, cell, cell, cells))
    hp = os.path.join(OUT, "tokens_src.html")
    open(hp, "w", encoding="utf-8").write(page)
    raw = os.path.join(OUT, "tokens_atlas.png")
    chrome_shot(hp, raw, cols * cell, rows * cell)
    im = Image.open(raw).convert("RGBA")
    s = SCALE
    toks = []
    for i, (label, _, side) in enumerate(groups):
        r, c = divmod(i, cols)
        box = (int(c * cell * s), int(r * cell * s), int((c + 1) * cell * s), int((r + 1) * cell * s))
        sub = im.crop(box)
        bb = sub.split()[-1].getbbox()
        if not bb:
            continue
        sub = sub.crop(bb)
        slug = re.sub(r"[^a-z0-9]+", "_", label.lower()).strip("_")
        fn = "tok_%02d_%s.png" % (i, slug)
        sub.save(os.path.join(TOKOUT, fn))
        toks.append({"file": "tokens/" + fn, "label": label, "side": side, "size": sub.size})
    os.remove(raw)
    print("tokens:", len(toks))
    return toks

def main():
    man = json.load(open(os.path.join(OUT, "manifest.json")))
    man["boards"] = {
        "byzantine": render_sheet("byzantine_player_board.html", "byzantine_board", 3200),
        "ottoman": render_sheet("ottoman_player_board.html", "ottoman_board", 3200),
        "crt": render_sheet("combat_crt.html", "combat_crt", 2800),
    }
    man["backs"] = {
        "byzantine": make_back("byzantine", PORPHYRY_DEEP, "cross"),
        "ottoman": make_back("ottoman", OTTOMAN_DEEP, "crescent"),
        "neutral": make_back("neutral", NEUTRAL_BG, "diamond"),
    }
    man["tokens"] = render_tokens()
    # main board is already a PNG
    board_png = os.path.join(ROOT, "Main_board", "Main Map.png")
    bim = Image.open(board_png)
    man["main_board"] = {"file": "../../../Main_board/Main Map.png", "w": bim.size[0], "h": bim.size[1]}
    json.dump(man, open(os.path.join(OUT, "manifest.json"), "w"), indent=2)
    print("done. main board", bim.size)

if __name__ == "__main__":
    main()
