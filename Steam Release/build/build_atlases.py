# -*- coding: utf-8 -*-
"""Render Constantinople 1453 card HTML sheets into TTS deck atlases.

For each source HTML (byzantine/ottoman/neutral card sheets) we:
  1. pull out the <style> block and every top-level `.card` div,
  2. re-lay them in a rigid, edge-to-edge CSS grid (no gaps/shadows/rounding),
  3. render the whole grid with headless Chrome -> one atlas PNG,
  4. record card count + grid dims in a manifest for the save-file builder.
"""
import json, os, re, subprocess, sys, tempfile

ROOT = r"C:\Users\CAO YANG\Desktop\Constantinople 1453"
ART = os.path.join(ROOT, "artifacts")
OUT = os.path.join(ROOT, "Steam Release", "v0", "images")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
COLS = 7            # atlas columns (TTS max 10)
SCALE = 1.5         # device pixel ratio for the render
CARD_W, CARD_H = 300, 420

DECKS = [
    ("byzantine", "byzantine_cards.html"),
    ("ottoman",   "ottoman_cards.html"),
    ("neutral",   "neutral_cards.html"),
]

def extract_style(html):
    m = re.search(r"<style>.*?</style>", html, re.S)
    return m.group(0) if m else ""

def extract_cards(html):
    """Return a list of full `<div class="card ...">...</div>` strings via a
    balanced-div scan (regex can't match nested divs)."""
    cards = []
    for m in re.finditer(r'<div class="card ', html):
        i = m.start()
        depth = 0
        j = i
        # walk tags from here, tracking div nesting depth
        for t in re.finditer(r'<div\b|</div>', html[i:]):
            if t.group(0) == '</div>':
                depth -= 1
                if depth == 0:
                    j = i + t.end()
                    break
            else:
                depth += 1
        cards.append(html[i:j])
    return cards

ATLAS_TMPL = u"""<!doctype html><html{darkattr}><head><meta charset="utf-8">
{style}
<style>
  html,body{{margin:0;padding:0;background:transparent;}}
  .atlas{{display:grid;grid-template-columns:repeat({cols},{cw}px);
         grid-auto-rows:{ch}px;width:{w}px;}}
  .atlas .card{{width:{cw}px!important;height:{ch}px!important;margin:0!important;
         border-radius:0!important;box-shadow:none!important;}}
  .atlas .card::before{{border-radius:0!important;}}
</style></head><body><div class="atlas">
{cards}
</div></body></html>"""

def build():
    os.makedirs(OUT, exist_ok=True)
    manifest = {}
    for name, fn in DECKS:
        html = open(os.path.join(ART, fn), encoding="utf-8").read()
        style = extract_style(html)
        cards = extract_cards(html)
        n = len(cards)
        rows = (n + COLS - 1) // COLS
        w, h = COLS * CARD_W, rows * CARD_H
        page = ATLAS_TMPL.format(
            darkattr=' data-theme="light"', style=style, cols=COLS,
            cw=CARD_W, ch=CARD_H, w=w, cards="\n".join(cards))
        atlas_html = os.path.join(OUT, name + "_atlas.html")
        with open(atlas_html, "w", encoding="utf-8") as f:
            f.write(page)
        png = os.path.join(OUT, name + "_face.png")
        cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
               "--default-background-color=00000000",
               "--force-device-scale-factor=%s" % SCALE,
               "--window-size=%d,%d" % (w, h),
               "--screenshot=" + png, "file:///" + atlas_html.replace("\\", "/")]
        print("rendering", name, "%dx%d cards, grid %dx%d, page %dx%d" % (n, 1, COLS, rows, w, h))
        r = subprocess.run(cmd, capture_output=True, text=True)
        if not os.path.exists(png):
            print("FAILED", name, r.stderr[-800:]); sys.exit(1)
        manifest[name] = {"count": n, "cols": COLS, "rows": rows,
                          "face": os.path.basename(png)}
        print("  ->", png, os.path.getsize(png) // 1024, "KB")
    with open(os.path.join(OUT, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)
    print("manifest:", json.dumps(manifest, indent=2))

if __name__ == "__main__":
    build()
