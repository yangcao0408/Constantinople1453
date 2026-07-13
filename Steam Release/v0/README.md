# Constantinople 1453 — Tabletop Simulator mod (v0, local test build)

Components-only build. All art is referenced by absolute `file:///` paths, so this
loads immediately on **this PC only**. See "Sharing" below to make it Workshop-ready.

## Load it
`Constantinople_1453.json` is already copied into your TTS Saves folder.
Tabletop Simulator → **Games → Save & Load → Constantinople 1453**.

## What's on the table
- **Main map** (locked, centre)
- **3 draw decks** — Byzantine (27), Ottoman (28), Neutral/Event (31); each card is
  named, shuffleable, drawable to hand
- **2 player boards** (left/right) + **Assault Resolution CRT** + a **d10**
- **Unit tokens**: 14 unit types as *infinite bags* (pull unlimited copies),
  11 leaders as single loose tiles

## Assets (`images/`)
- `*_face.png` — deck atlases (7-wide grids); `*_back.png` — card backs
- `*_board.png`, `combat_crt.png`, `main_map.png` — flat tiles
- `tokens/tok_*.png` — one image per unit/leader counter

## Rebuild
```
py "../build/build_atlases.py"   # render card deck atlases from artifacts/*.html
py "../build/build_extras.py"    # boards, CRT, card backs, unit tokens
py "../build/build_save.py"      # assemble + install the .json
```

## Sharing (Workshop)
`file:///` paths only work here. To share: upload everything in `images/` to hosted
URLs (TTS in-game **Cloud Manager** is easiest), then re-run `build_save.py` with the
image URLs swapped for the hosted ones.

## Known rough edges (v0)
- Object sizes/positions are first-pass estimates — nudge in-game as needed.
- Card backs are generated placeholders (no bespoke back art yet).
- Leader token tooltips read generically ("Leader §6.2 — …"); the name is printed on
  the token face itself.
