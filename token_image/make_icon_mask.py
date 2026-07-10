#!/usr/bin/env python3
"""
Turn reference icon PNGs (transparent background, any single line-art color)
into CSS mask rules, so they render pixel-exact but recolored to match
whichever faction/ink color a card or token needs.

Usage:
    python make_icon_mask.py                          # process every .png in this folder
    python make_icon_mask.py some_icon.png             # process just one file
    python make_icon_mask.py some_icon.png -c my-class # override the CSS class name

Output:
    Writes/updates icon_masks.css in this folder, one rule per icon:

        .icon-raster.<class-name>{
          -webkit-mask-image:url("data:image/png;base64,....");
          mask-image:url("data:image/png;base64,....");
        }

    Re-running is safe — each icon's rule is replaced in place by filename,
    not appended, so this can be run after adding/updating any PNG without
    producing duplicate or stale rules.

Markup pattern to use each rule (paste into the card/token HTML):

    <div class="icon-wrap">
      <div class="icon-raster <class-name>"></div>
    </div>

That relies on these base classes already being defined in the card/token
stylesheet:

    .icon-wrap{ width:42px; height:42px; position:relative; }
    .icon-raster{
      width:100%; height:100%;
      background-color:var(--cream);
      -webkit-mask-size:contain; mask-size:contain;
      -webkit-mask-repeat:no-repeat; mask-repeat:no-repeat;
      -webkit-mask-position:center; mask-position:center;
      filter:drop-shadow(0 1px 1px rgba(0,0,0,.35));
    }

Swap background-color on a per-card basis (e.g. var(--ottoman) or
var(--porphyry)) to recolor the same traced icon for a different faction.
"""

import argparse
import base64
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSS_OUT = HERE / "icon_masks.css"

RULE_RE_TEMPLATE = r"/\* icon:{name} \*/\n\.icon-raster\.[a-zA-Z0-9_-]+\{{[^}}]*\}}\n"


def slugify(stem: str) -> str:
    slug = stem.lower()
    slug = re.sub(r"^icon_(unit_)?", "", slug)
    slug = slug.replace("_", "-")
    slug = re.sub(r"[^a-z0-9-]", "", slug)
    return slug


PAD_FRACTION = 0.08  # margin added around the trimmed artwork, as a fraction of its larger dimension


def crop_to_content(png_bytes: bytes, path: Path) -> bytes:
    """
    Trim to the alpha-channel bounding box, then pad back out to a square
    with a uniform margin. Without this, two icons with identical on-canvas
    artwork size but different amounts of empty transparent margin around
    them render at different visual sizes under mask-size:contain — this
    normalizes every icon to fill the same proportion of its box regardless
    of how the source PNG was originally cropped/exported.
    """
    try:
        from PIL import Image
        import io
    except ImportError:
        print(f"  warning: Pillow not installed — {path.name} embedded as-is, not auto-cropped", file=sys.stderr)
        return png_bytes

    im = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
    alpha = im.split()[-1]
    bbox = alpha.getbbox()
    if bbox is None:
        print(f"  warning: {path.name} is fully transparent — skipping crop", file=sys.stderr)
        return png_bytes

    trimmed = im.crop(bbox)
    w, h = trimmed.size
    side = max(w, h)
    pad = round(side * PAD_FRACTION)
    canvas_size = side + pad * 2
    canvas = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
    canvas.paste(trimmed, ((canvas_size - w) // 2, (canvas_size - h) // 2), trimmed)

    out = io.BytesIO()
    canvas.save(out, format="PNG")
    return out.getvalue()


def check_alpha(png_bytes: bytes, path: Path) -> None:
    try:
        from PIL import Image
        import io
        im = Image.open(io.BytesIO(png_bytes))
        if im.mode not in ("RGBA", "LA") and "transparency" not in im.info:
            print(f"  warning: {path.name} has no alpha channel — mask will render as a solid block", file=sys.stderr)
    except ImportError:
        pass  # Pillow not installed; skip the check rather than fail the run


def build_rule(png_path: Path, class_name: str) -> str:
    data = png_path.read_bytes()
    check_alpha(data, png_path)
    data = crop_to_content(data, png_path)
    b64 = base64.b64encode(data).decode("ascii")
    uri = f'url("data:image/png;base64,{b64}")'
    return (
        f"/* icon:{png_path.name} */\n"
        f".icon-raster.{class_name}{{\n"
        f"  -webkit-mask-image:{uri};\n"
        f"  mask-image:{uri};\n"
        f"}}\n"
    )


def upsert_rule(css_text: str, png_name: str, rule: str) -> str:
    pattern = RULE_RE_TEMPLATE.format(name=re.escape(png_name))
    if re.search(pattern, css_text):
        return re.sub(pattern, rule, css_text)
    sep = "\n" if css_text and not css_text.endswith("\n\n") else ""
    return css_text + sep + rule + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("png", nargs="?", help="single PNG to process (omit to process every .png in this folder)")
    ap.add_argument("-c", "--class-name", help="CSS class name (default: derived from filename)")
    ap.add_argument("-o", "--out", default=str(CSS_OUT), help=f"output CSS file (default: {CSS_OUT.name})")
    args = ap.parse_args()

    targets = [Path(args.png)] if args.png else sorted(HERE.glob("*.png"))
    if not targets:
        print("No PNG files found.", file=sys.stderr)
        sys.exit(1)

    out_path = Path(args.out)
    css_text = out_path.read_text(encoding="utf-8") if out_path.exists() else ""

    for png_path in targets:
        if not png_path.exists():
            print(f"skip: {png_path} not found", file=sys.stderr)
            continue
        class_name = args.class_name or slugify(png_path.stem)
        rule = build_rule(png_path, class_name)
        css_text = upsert_rule(css_text, png_path.name, rule)
        print(f"{png_path.name} -> .icon-raster.{class_name}")

    out_path.write_text(css_text, encoding="utf-8")
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
