# -*- coding: utf-8 -*-
"""Consolidate the 25 unit/leader token PNGs into two counter-deck atlases
(Ottoman + Byzantine). One image per side instead of 25 loose files -> far
fewer simultaneous local-file loads for TTS to choke on."""
import json, math, os
from PIL import Image, ImageDraw, ImageFont

ROOT = r"C:\Users\CAO YANG\Desktop\Constantinople 1453"
IMG = os.path.join(ROOT, "Steam Release", "v1", "images")
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

def star(d, cx, cy, r, fill):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    d.polygon(pts, fill=fill)

def emblem_cell(side, sz=200):
    """Generic faction-emblem back tile for tokens that do NOT flip."""
    im = Image.new("RGBA", (sz, sz), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([4, 4, sz - 4, sz - 4], radius=16,
                        fill=SIDE_BG[side] + (255,), outline=GOLD_BRIGHT, width=3)
    cx, cy = sz // 2, sz // 2
    if side == "byz":                        # Orthodox cross
        t = 7
        d.rectangle([cx - t, cy - 72, cx + t, cy + 78], fill=GOLD_BRIGHT)          # upright
        d.rectangle([cx - 20, cy - 56, cx + 20, cy - 45], fill=GOLD_BRIGHT)        # titulus
        d.rectangle([cx - 48, cy - 25, cx + 48, cy - 11], fill=GOLD_BRIGHT)        # main bar
        d.polygon([(cx - 26, cy + 40), (cx - 26, cy + 50),                          # footrest
                   (cx + 26, cy + 28), (cx + 26, cy + 18)], fill=GOLD_BRIGHT)
    else:                                    # centred star-and-crescent
        r = 58
        ccx = cx + 5
        d.ellipse([ccx - r, cy - r, ccx + r, cy + r], fill=GOLD_BRIGHT)
        off = 33                             # rounder crescent (~210°), matches the card back
        d.ellipse([ccx - r + off, cy - r, ccx + r + off, cy + r], fill=SIDE_BG[side] + (255,))
        star(d, ccx + 26, cy, 20, GOLD_BRIGHT)
    return im

def make_back(side, toks):
    """Back atlas aligned cell-for-cell with the face atlas: flippable units get
    their rendered reduced-strength side; everything else gets the faction emblem."""
    n = len(toks)
    rows = (n + COLS - 1) // COLS
    atlas = Image.new("RGBA", (COLS * CELL, rows * CELL), (0, 0, 0, 0))
    emblem = emblem_cell(side)
    for i, t in enumerate(toks):
        r, c = divmod(i, COLS)
        if t.get("back_file"):
            im = Image.open(os.path.join(IMG, t["back_file"])).convert("RGBA")
        else:
            im = emblem
        x = c * CELL + (CELL - im.size[0]) // 2
        y = r * CELL + (CELL - im.size[1]) // 2
        atlas.paste(im, (x, y), im)
    out = os.path.join(IMG, side + "_counters_back.png")
    atlas.save(out)
    return os.path.basename(out)

def main():
    man = json.load(open(os.path.join(IMG, "manifest.json")))
    toks = man["tokens"]
    decks = {}
    for side in ("ott", "byz"):
        side_toks = [t for t in toks if t["side"] == side]
        info = make_atlas(side, side_toks)
        info["back"] = make_back(side, side_toks)
        info["unique_back"] = True
        decks[side] = info
        flips = sum(1 for t in side_toks if t.get("flip"))
        print(side, "counter deck:", info["count"], "counters",
              "%dx%d" % (info["cols"], info["rows"]), "-", flips, "flippable")
    man["token_decks"] = decks
    json.dump(man, open(os.path.join(IMG, "manifest.json"), "w"), indent=2)

if __name__ == "__main__":
    main()
