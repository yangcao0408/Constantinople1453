# TTS Converter — techniques & pitfalls from the v0 build

How we turned this repo's HTML card sheets / boards / token templates into a
working Tabletop Simulator mod, and every trap hit along the way. Read this
before building v1.

---

## 1. What a TTS mod actually is

- **One save `.json`** (drop into `Documents\My Games\Tabletop Simulator\Saves`)
  plus **images referenced by URL**. No art is embedded in the save.
- Cards live in **deck atlases**: one big grid image per deck (max 10×7 per
  sheet), plus one back image. `CustomDeck` entry gives `FaceURL`, `BackURL`,
  `NumWidth` (cols), `NumHeight` (rows).
- `CardID = deckKey * 100 + cellIndex` (cell index is row-major from top-left).
  Each deck needs a unique numeric `deckKey` ("1", "2", …).
- Boards/maps/aids are `Custom_Tile` objects (`Stretch: true`, square base —
  set `scaleZ = scaleX * h/w` to keep the image's aspect ratio).
- Counters work best as **counter decks** (same atlas mechanic as cards) —
  they lie flat, drag, stack, flip. Ctrl+C/V duplicates when more copies are
  needed. (Infinite bags + 25 loose token images = image-count bloat; avoid.)
- Hand zones are `HandTrigger` objects with `FogColor` = seat color
  ("White", "Red", …). One per player; cards dragged in are hidden.

**Don't guess the schema** — open an existing working save from the same TTS
version (we cribbed from the Here I Stand autosave, `VersionNumber v14.2.1`)
and copy its object shapes field-for-field.

## 2. The pipeline (scripts in `Steam Release/build/`)

| Script | Does |
|---|---|
| `build_atlases.py` | Extracts each `.card` div from the HTML sheets, re-lays them in a rigid edge-to-edge CSS grid, screenshots with headless Chrome → one face atlas per deck + `manifest.json` |
| `build_extras.py` | Player boards + CRT (two-pass measure → render → alpha-threshold autocrop), generated card backs (Pillow), unit-token atlas → sliced per-token PNGs |
| `build_token_decks.py` | Consolidates the sliced tokens into 2 counter-deck atlases (one per side) + backs |
| `build_save.py` | Assembles the save JSON (decks, tiles, counter decks, d10, hand zones), stages images, **seeds the TTS image cache**, installs the save |

Rebuild order: `build_atlases.py` → `build_extras.py` → `build_token_decks.py`
→ `build_save.py` (all with `py`, i.e. Python 3 — plain `python` here is 2.7!).

### Rendering HTML → PNG (headless Chrome)
```
chrome --headless=new --disable-gpu --hide-scrollbars
       --default-background-color=00000000        # transparent bg for autocrop
       --force-device-scale-factor=1.5            # crispness
       --window-size=WxH --screenshot=out.png file:///page.html
```

Techniques that mattered:
- **Balanced-div extraction**: regex can't match nested divs. Scan for the
  opening tag, then walk `<div`/`</div>` tokens counting depth.
  Pitfall: `class="card\b` also matched `card-inner`/`card-top` (162 "cards"
  instead of 27) — match `class="card "` (trailing space) exactly.
- **Atlas layout**: strip the page chrome (header/notes), force cards into
  `display:grid` with exact cell size, kill border-radius/box-shadow/margins.
  Unused trailing cells can stay transparent — TTS ignores them.
- **Two-pass measure for overflow content**: the player boards use
  `overflow-x:auto` and clip at the wrap width; `width:fit-content` /
  `inline-flex` do NOT reliably unclip (text max-content explodes). Instead:
  pass 1 loads the page with a JS snippet writing `board.scrollWidth` into a
  DOM attribute, read it via `--dump-dom`; pass 2 renders at exactly that
  window width with `overflow:visible`.
- **Autocrop with thresholded alpha**: box-shadows bleed faint alpha to the
  window edge and defeat `getbbox()`. Threshold first
  (`alpha.point(a>30)`), then crop, then pad ~12px.

## 3. The pitfalls, in the order they bit us

1. **URL-encoding the drive colon** — `quote()` turned `C:` into `C%3A`;
   TTS: "Cannot connect to destination host". Encode with `safe="/:"`
   (only spaces become `%20`). *(Moot now — see #4.)*
2. **4096px texture ceiling** — any image over 4096 on a side fails as
   `unsupported format: UNKNOWN` (misleading!). The files were valid PNGs;
   only their dimensions were wrong. Cap everything at 4000px (`MAXDIM`).
3. **Too many separate images** — 35 local images = flaky tail failures, and
   generally more to host/load. Consolidate: counters into per-side atlas
   decks. Final count: 14 images for the whole mod.
4. **THE BIG ONE — `file:///` URLs do not work at all in current TTS.**
   `Player.log` (at `AppData\LocalLow\Berserk Games\Tabletop Simulator\`)
   showed every fetch as `Curl error 7: Failed to connect to localhost port
   443` — TTS routes image loads through curl, which mangles `file://` into
   an HTTPS request to localhost. All earlier "partial successes" were cache
   accidents. **Never debug blind: read Player.log first.** Every in-game
   error we chased (cannot connect / unknown format / blanks) was downstream
   of this.
5. **Workaround: pre-seed the TTS image cache.** TTS checks
   `Documents\My Games\Tabletop Simulator\Mods\Images` *before* fetching.
   Cache filename = URL stripped of ALL non-alphanumerics + real extension
   (verified against existing mods). So: put fake-but-stable URLs in the save
   (`http://c1453.local/b03/<name>`, no extension → tidy cache names) and
   copy each PNG to `Mods/Images/httpc1453localb03<name>.png`. Requires
   "Mod Caching" ON (default). Bump the `b03` version segment to bust stale
   entries — same filename never re-reads from disk.
6. **Remote players see blanks** — the cache seed is per-machine. Either send
   them the seeded cache files (`friend_pack` zip → their `Mods/Images`) or do
   real hosting. Save data streams host→client, but every client fetches
   images itself.
7. **Full app restart, not save reload**, after changing images — TTS holds
   failed-load state in memory.
8. **Windows/tooling traps**: `python` = 2.7 on this machine, use `py`;
   PowerShell 5.1 has no `&&`; Chrome screenshot writes nothing on failure —
   always check the file exists.

## 4. The v1 recipe (do it in this order)

1. **Host images FIRST.** In TTS: Modding → **Cloud Manager** → Upload the
   images (from `Steam Release/v0/images/b03/`), right-click → Copy URL each.
   Real `steamusercontent` URLs make every problem in §3 #4–7 vanish —
   no cache seeding, no friend packs, loads work for everyone.
   (Keep the cache-seed path as the offline/rapid-iteration fallback.)
2. Re-render whatever art changed (`build_atlases.py` / `build_extras.py` /
   `build_token_decks.py`). Keep every output ≤4000px.
3. Point `build_save.py`'s `url()` at the hosted URLs (a simple
   `name → URL` dict) and rebuild. Validate before loading:
   JSON parses, every URL resolves, deck counts match `DeckIDs`,
   no image over 4096, card nicknames present.
4. Test locally, then with a second machine.
5. Workshop publish (when ready): load the save in TTS → Modding →
   **Workshop Upload**. Thumbnail, description, done.

## 5. Current state (end of v0)

- Save: `Steam Release/v0/Constantinople_1453.json` (also installed in Saves).
  12 objects: map tile, 3 card decks (27/28/31 named cards), 2 player boards,
  CRT, 2 counter decks (11 Ottoman / 14 Byzantine), d10, 2 hand zones
  (White=Byzantine south, Red=Ottoman north).
- Images: 14 total in `Steam Release/v0/images/b03/`, seeded into the local
  TTS cache. Friend pack zip for remote players in `Steam Release/v0/`.
- Not yet done: real hosting (Cloud Manager), Workshop publish, any Lua
  scripting/snap points, bespoke card-back art, leader-token real-name
  tooltips, in-game layout tuning.
