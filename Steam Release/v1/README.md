# Constantinople 1453 — Tabletop Simulator mod (v1)

Second components build. Rules-synced to DESIGN.md / EVENT_DECK.md as of
2026-07-17. Images load via the pre-seeded TTS cache (`b04` bundle) — see
`tts_converter.md` at the repo root for why `file:///` URLs can't work and
how the cache-seeding scheme functions.

## What changed since v0
- **Cards** — Strike the Commander (Round 7+, roll 8+), The Emperor Falls
  (Round 7+), The Fallen Icon (Round 4+, swapped gates with the two
  commander cards), The Stockade at the Breach (+2 Wall Defense).
- **Byzantine player board** — Reserve Pool now carries the "Free repair −1"
  box at the 15th slot: at/below it, Repair capacity drops 3 → 2 actions
  per round (§4.0.8).
- **Ottoman player board** — Mustering Cost table replaced by the
  pool-and-deploy model (§4.0.1); Second Barrage redefined (Attack card →
  extra wall Bombard, 1d10: 1–3 none / 4–10 = 1 HP, never 2; max 1 per
  sector per round); elite surcharge noted; Muster/Diplomacy ops renamed
  Deploy/Blockade with current effects.
- Image URL version bumped `b03` → `b04` so stale cache entries can't
  shadow the new art.

## Load it
`Constantinople_1453.json` is already copied into your TTS Saves folder.
Tabletop Simulator → **Games → Save & Load → Constantinople 1453**.
(Full app restart, not just save reload, if you had v0 open.)

## What's on the table
- **Main map** (locked, centre)
- **3 draw decks** — Byzantine (27), Ottoman (28), Neutral/Event (31); each
  card named, shuffleable, drawable to hand
- **2 player boards** + **Assault Resolution CRT** + a **d10**
- **2 counter decks** — Ottoman (11) and Byzantine (14) unit/leader counters
- **2 hand zones** — White = Byzantine (south), Red = Ottoman (north)

## Assets (`images/`)
- `*_face.png` — deck atlases (7-wide for cards, 5-wide for counters);
  `*_back.png` — card backs
- `*_board.png`, `combat_crt.png`, `main_map.png` — flat tiles
- `b04/` — the staged bundle actually referenced by the save (these are the
  files to upload when moving to real hosting)
- `tokens/tok_*.png` — per-token slices (intermediate; consolidated into the
  counter atlases)

## Sharing with a remote player
Send them `friend_pack/` — 14 pre-cache-named PNGs + install instructions.
Or do real hosting (below) and nobody needs a pack.

## Rebuild
```
py "../build/build_atlases.py"      # card atlases  (WIPES manifest.json —
py "../build/build_extras.py"       # boards/CRT/backs/tokens   always re-run
py "../build/build_token_decks.py"  # counter decks             the full chain)
py "../build/build_save.py"         # assemble + install the .json
```

## Next step (Workshop)
Upload the 14 images in `images/b04/` via TTS **Cloud Manager**, swap the
`url()` helper in `build_save.py` to return the hosted URLs, rebuild, test,
then Modding → Workshop Upload. See `tts_converter.md` §4.

## Known rough edges (carried from v0)
- Object sizes/positions are first-pass estimates — nudge in-game as needed.
- Card backs are generated placeholders (no bespoke back art yet).
- Leader tokens read generically; the name is printed on the token face.
- Charisius card shows 9 Wall HP vs DESIGN.md §3.1's 8 — unreconciled.
