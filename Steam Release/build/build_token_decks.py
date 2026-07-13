# -*- coding: utf-8 -*-
"""Consolidate the 25 unit/leader token PNGs into two counter-deck atlases
(Ottoman + Byzantine). One image per side instead of 25 loose files -> far
fewer simultaneous local-file loads for TTS to choke on."""
import json, math, os
from PIL import Image, ImageDraw, ImageFont

ROOT = r"C:\Users\CAO YANG\Desktop\Constantinople 1453"
IMG = os.path.join(ROOT, "Steam Release", "v0", "images")
CELL = 360          # uniform atlas cell (tokens are ~325-345, padded)
COLS = 5

GOLD_BRIGHT = (216, 180, 101)
SIDE_BG = {"ott": (24, 46, 30), "byz": (44, 19, 57)}
SIDE_NAME = {"ott": "OTTOMAN", "byz": "BYZANTINE"}

def font(sz):
    for f in (r"C:\Windows\Fonts\georgiab.ttf", r"C:\Windows\Fonts\georgia.ttf"):
        if os.path.exists(f):
            return ImageFont.truetype(f, sz)
    return ImageFont.load_default()

def make_atlas(side, toks):
    n = len(toks)
    rows = (n + COLS - 1) // COLS
    atlas = Image.new("RGBA", (COLS * CELL, rows * CELL), (0, 0, 0, 0))
    for i, t in enumerate(toks):
        r, c = divmod(i, COLS)
        im = Image.open(os.path.join(IMG, t["file"])).convert("RGBA")
        x = c * CELL + (CELL - im.size[0]) // 2
        y = r * CELL + (CELL - im.size[1]) // 2
        atlas.paste(im, (x, y), im)
    out = os.path.join(IMG, side + "_counters_face.png")
    atlas.save(out)
    return {"count": n, "cols": COLS, "rows": rows,
            "face": os.path.basename(out), "labels": [t["label"] for t in toks]}

def make_back(side):
    im = Image.new("RGBA", (CELL, CELL), SIDE_BG[side] + (255,))
    d = ImageDraw.Draw(im)
    d.rectangle([10, 10, CELL - 10, CELL - 10], outline=GOLD_BRIGHT, width=3)
    cx, cy = CELL // 2, CELL // 2 - 10
    if side == "byz":                       # cross
        d.rectangle([cx - 16, cy - 70, cx + 16, cy + 70], fill=GOLD_BRIGHT)
        d.rectangle([cx - 52, cy - 16, cx + 52, cy + 16], fill=GOLD_BRIGHT)
    else:                                   # crescent
        r = 62
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD_BRIGHT)
        d.ellipse([cx - r + 26, cy - r, cx + r + 26, cy + r], fill=SIDE_BG[side] + (255,))
    f = font(30)
    w = d.textbbox((0, 0), SIDE_NAME[side], font=f)[2]
    d.text(((CELL - w) / 2, CELL - 66), SIDE_NAME[side], font=f, fill=GOLD_BRIGHT)
    out = os.path.join(IMG, side + "_counters_back.png")
    im.save(out)
    return os.path.basename(out)

def main():
    man = json.load(open(os.path.join(IMG, "manifest.json")))
    toks = man["tokens"]
    decks = {}
    for side in ("ott", "byz"):
        side_toks = [t for t in toks if t["side"] == side]
        info = make_atlas(side, side_toks)
        info["back"] = make_back(side)
        decks[side] = info
        print(side, "counter deck:", info["count"], "counters",
              "%dx%d" % (info["cols"], info["rows"]))
    man["token_decks"] = decks
    json.dump(man, open(os.path.join(IMG, "manifest.json"), "w"), indent=2)

if __name__ == "__main__":
    main()
