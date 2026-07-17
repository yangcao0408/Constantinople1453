# -*- coding: utf-8 -*-
"""Assemble the Tabletop Simulator save (.json) from the rendered assets.

Components-only, local build: every image is referenced by an absolute
file:/// URL, so the save loads immediately on this machine. Swap the URLs
for hosted ones later to make it Workshop-shareable.
"""
import json, os, random, re, shutil, sys
from urllib.parse import quote
from PIL import Image

MAXDIM = 4000          # TTS/Unity texture limit is 4096; stay safely under

ROOT = r"C:\Users\CAO YANG\Desktop\Constantinople 1453"
VDIR = os.path.join(ROOT, "Steam Release", "v1")
IMG = os.path.join(VDIR, "images")
ART = os.path.join(ROOT, "artifacts")
SAVES = r"C:\Users\CAO YANG\Documents\My Games\Tabletop Simulator\Saves"

rng = random.Random(1453)
_guids = set()
def guid():
    while True:
        g = "".join(rng.choice("0123456789abcdef") for _ in range(6))
        if g not in _guids:
            _guids.add(g); return g

# This TTS build fetches every image URL via curl, which mangles file:///
# paths into https://localhost connections (Player.log: "Curl error 7 ...
# localhost port 443") — local file URLs can never load. Workaround: give the
# save fake http:// URLs and PRE-SEED TTS's image cache (Mods/Images). TTS
# checks the cache before fetching, so the images load without any network.
# Cache filename rule (verified against existing mods): the URL stripped of
# all non-alphanumeric characters, plus the real image extension.
VERSION = 4
STAGE = os.path.join(IMG, "b%02d" % VERSION)   # bundle for later real hosting
TTS_CACHE = r"C:\Users\CAO YANG\Documents\My Games\Tabletop Simulator\Mods\Images"

def url(path):
    """Stage the image, seed it into the TTS cache, return its fake URL."""
    os.makedirs(STAGE, exist_ok=True)
    dst = os.path.join(STAGE, os.path.basename(path))
    if os.path.abspath(path) != os.path.abspath(dst):
        shutil.copy(path, dst)
    stem = os.path.splitext(os.path.basename(path))[0]
    fake = "http://c1453.local/b%02d/%s" % (VERSION, stem)
    cache_name = re.sub(r"[^A-Za-z0-9]", "", fake) + ".png"
    shutil.copy(path, os.path.join(TTS_CACHE, cache_name))
    return fake

CARD_FILES = {"byzantine": "byzantine_cards.html",
              "ottoman": "ottoman_cards.html",
              "neutral": "neutral_cards.html"}

def card_titles(deck):
    """Pull each card's title text (in grid order) for nicknames."""
    html = open(os.path.join(ART, CARD_FILES[deck]), encoding="utf-8").read()
    titles = []
    for m in re.finditer(r'<div class="card-title">(.*?)</div>', html, re.S):
        t = re.sub(r"<[^>]+>", "", m.group(1))
        t = (t.replace("&mdash;", "—").replace("&amp;", "&")
             .replace("&minus;", "-").replace("&#9766;", "").replace("&middot;", "·"))
        titles.append(t.strip())
    return titles

def base(name, nick, pos, scale, rot=(0, 180, 0), locked=False):
    return {
        "GUID": guid(), "Name": name,
        "Transform": {"posX": pos[0], "posY": pos[1], "posZ": pos[2],
                      "rotX": rot[0], "rotY": rot[1], "rotZ": rot[2],
                      "scaleX": scale[0], "scaleY": scale[1], "scaleZ": scale[2]},
        "Nickname": nick, "Description": "", "GMNotes": "",
        "AltLookAngle": {"x": 0, "y": 0, "z": 0},
        "ColorDiffuse": {"r": 1, "g": 1, "b": 1},
        "LayoutGroupSortIndex": 0, "Value": 0, "Locked": locked,
        "Grid": True, "Snap": True, "IgnoreFoW": False, "MeasureMovement": False,
        "DragSelectable": True, "Autoraise": True, "Sticky": True, "Tooltip": True,
        "GridProjection": False, "HideWhenFaceDown": False, "Hands": False,
        "LuaScript": "", "LuaScriptState": "", "XmlUI": "",
    }

def tile(nick, img_path, pos, base_scale, locked=False):
    """Flat Custom_Tile with UNIFORM X/Z scale. TTS auto-sizes a Custom_Tile's
    mesh to the image's aspect ratio on its own; the old scaleZ*=h/w correction
    applied the aspect a second time, flattening every tile by an extra h/w
    (the long-standing 'boards look stretched' bug, present since v0)."""
    o = base("Custom_Tile", nick, pos,
             (base_scale, 1.0, base_scale), locked=locked)
    o["CustomImage"] = {
        "ImageURL": url(img_path), "ImageSecondaryURL": "",
        "ImageScalar": 1.0, "WidthScale": 0.0,
        "CustomTile": {"Type": 0, "Thickness": 0.1, "Stackable": False, "Stretch": True},
    }
    return o

def make_deck(deck, meta, pos):
    key = {"byzantine": "1", "ottoman": "2", "neutral": "3"}[deck]
    n, cols, rows = meta["count"], meta["cols"], meta["rows"]
    face = url(os.path.join(IMG, meta["face"]))
    back = url(os.path.join(IMG, deck + "_back.png"))
    cd = {key: {"FaceURL": face, "BackURL": back, "NumWidth": cols,
                "NumHeight": rows, "BackIsHidden": True, "UniqueBack": False,
                "Type": 0}}
    titles = card_titles(deck)
    ids, contained = [], []
    for i in range(n):
        cid = int(key) * 100 + i
        ids.append(cid)
        card = base("CardCustom", titles[i] if i < len(titles) else "",
                    (pos[0], pos[1] + 0.1 + i * 0.02, pos[2]), (1, 1, 1),
                    rot=(0, 180, 180))
        card["CardID"] = cid
        card["SidewaysCard"] = False
        card["CustomDeck"] = cd
        contained.append(card)
    d = base("Deck", {"byzantine": "Byzantine Pile", "ottoman": "Ottoman Pile",
                       "neutral": "Neutral / Event Pile"}[deck],
             pos, (1, 1, 1), rot=(0, 180, 180))
    d["SidewaysCard"] = False
    d["DeckIDs"] = ids
    d["CustomDeck"] = cd
    d["ContainedObjects"] = contained
    return d

def make_token_deck(side, info, pos, scale):
    """A deck of counters (units + leaders) built from one atlas image."""
    key = {"ott": "4", "byz": "5"}[side]
    n, cols, rows = info["count"], info["cols"], info["rows"]
    face = url(os.path.join(IMG, info["face"]))
    back = url(os.path.join(IMG, info["back"]))
    # UniqueBack: the back is an atlas aligned cell-for-cell with the face, so
    # each counter flips to its OWN back (reduced-strength side for multi-step
    # units, faction emblem for the rest) instead of one shared deck back.
    cd = {key: {"FaceURL": face, "BackURL": back, "NumWidth": cols,
                "NumHeight": rows, "BackIsHidden": True,
                "UniqueBack": bool(info.get("unique_back")),
                "Type": 0}}
    labels = info["labels"]
    ids, contained = [], []
    for i in range(n):
        cid = int(key) * 100 + i
        ids.append(cid)
        card = base("CardCustom", labels[i] if i < len(labels) else "",
                    (pos[0], pos[1] + 0.1 + i * 0.02, pos[2]),
                    (scale, scale, scale), rot=(0, 180, 0))
        card["CardID"] = cid
        card["SidewaysCard"] = False
        card["CustomDeck"] = cd
        contained.append(card)
    d = base("Deck", {"ott": "Ottoman Counters", "byz": "Byzantine Counters"}[side],
             pos, (scale, scale, scale), rot=(0, 180, 0))
    d["SidewaysCard"] = False
    d["DeckIDs"] = ids
    d["CustomDeck"] = cd
    d["ContainedObjects"] = contained
    return d

FRIEND_README = u"""Constantinople 1453 — image pack for joining the playtest (v1)
================================================================

These {n} PNG files are pre-cached artwork for the Tabletop Simulator save.
Without them the table loads blank (the save points at placeholder URLs that
only resolve from this cache).

NOTE: this is the v1 pack (filenames contain "b{ver:02d}"). It replaces any
older pack — you can delete those; they don't conflict.

INSTALL (2 minutes):
1. Close Tabletop Simulator if it's running.
2. Copy all {n} .png files (NOT this txt) into this folder on your machine:

   Documents\\My Games\\Tabletop Simulator\\Mods\\Images

   (Full path is usually:
    C:\\Users\\<you>\\Documents\\My Games\\Tabletop Simulator\\Mods\\Images)

3. IMPORTANT: do not rename the files — the weird names are how TTS finds them.
4. Start TTS. Menu -> Configuration -> make sure "Mod Caching" is ON.
5. Join the host's game. All boards, cards and counters should now render.

If anything is still blank after joining, leave and rejoin once.
"""

def build_friend_pack():
    """Regenerate the shareable friend pack: every image the save references,
    copied under its TTS cache-mangled name (same rule as url()), plus a readme.
    Derives from the b04 staging bundle populated during this build, so it can
    never fall out of sync with the save again."""
    fp = os.path.join(VDIR, "friend_pack")
    os.makedirs(fp, exist_ok=True)
    for old in os.listdir(fp):                       # clear stale files first
        if old.lower().endswith(".png"):
            os.remove(os.path.join(fp, old))
    pngs = sorted(f for f in os.listdir(STAGE) if f.endswith(".png"))
    for f in pngs:
        stem = os.path.splitext(f)[0]
        fake = "http://c1453.local/b%02d/%s" % (VERSION, stem)
        cache_name = re.sub(r"[^A-Za-z0-9]", "", fake) + ".png"
        shutil.copy(os.path.join(STAGE, f), os.path.join(fp, cache_name))
    open(os.path.join(fp, "READ_ME_FIRST.txt"), "w", encoding="utf-8").write(
        FRIEND_README.format(n=len(pngs), ver=VERSION))
    print("friend_pack:", len(pngs), "images ->", fp)

def main():
    man = json.load(open(os.path.join(IMG, "manifest.json")))
    # keep the map with the rest of the bundle, capped to the TTS texture limit
    mp = Image.open(os.path.join(ROOT, "Main_board", "Main Map.png"))
    if max(mp.size) > MAXDIM:
        r = MAXDIM / float(max(mp.size))
        mp = mp.resize((int(mp.size[0] * r), int(mp.size[1] * r)), Image.LANCZOS)
    mp.save(os.path.join(IMG, "main_map.png"))
    man["main_board"] = {"w": mp.size[0], "h": mp.size[1]}
    objs = []

    # --- map (locked, centred) ---
    objs.append(tile("Constantinople 1453 — Map", os.path.join(IMG, "main_map.png"),
                     (0, 1, 0), 15.65, locked=True))

    # --- decks (front edge) ---
    objs.append(make_deck("byzantine", man["byzantine"], (-8, 1.5, -14)))
    objs.append(make_deck("neutral", man["neutral"], (0, 1.5, -14)))
    objs.append(make_deck("ottoman", man["ottoman"], (8, 1.5, -14)))

    # --- player boards + CRT ---
    # Board scales are user-tuned on the table against the unit tokens:
    # Ottoman confirmed right at 5.9; Byzantine tuned upward stepwise
    # (5.9 -> 6.24 at "1.35" -> 6.61 at "1.43"). Tune these by eye on-table,
    # not by pixel math - the boards' cell artwork differs per board.
    b = man["boards"]
    objs.append(tile("Byzantine Player Board", os.path.join(IMG, b["byzantine"]["file"]),
                     (-26, 1, 0), 6.61))
    objs.append(tile("Ottoman Player Board", os.path.join(IMG, b["ottoman"]["file"]),
                     (26, 1, 0), 5.9))
    objs.append(tile("Assault Resolution — CRT", os.path.join(IMG, b["crt"]["file"]),
                     (22, 1, 16), 9.5))

    # --- Siege Clock round track (turn counter) + its marker ---
    rt = man.get("round_track")
    if rt:
        objs.append(tile("Siege Clock — Round Track", os.path.join(IMG, rt["file"]),
                         (0, 1, 21), 5.0, locked=True))
        marker = base("Checker_red", "Round Marker", (-4.1, 2, 21), (0.9, 0.9, 0.9))
        objs.append(marker)

    # --- unit/leader counters: one consolidated deck per side ---
    td = man["token_decks"]
    objs.append(make_token_deck("ott", td["ott"], (-12, 1.5, 10), 0.55))
    objs.append(make_token_deck("byz", td["byz"], (12, 1.5, 10), 0.55))

    # --- a d10 for the CRT ---
    objs.append(base("Die_10", "d10", (14, 1.5, 16), (1, 1, 1)))

    # --- two player hand zones: Byzantine = White (south), Ottoman = Red (north) ---
    for color, pos, roty in (("White", (0, 2.76, -34.75), 0),
                             ("Red", (0, 2.76, 34.75), 180)):
        hz = base("HandTrigger", "", pos, (26.0, 5.17, 5.4),
                  rot=(0, roty, 0), locked=True)
        hz["ColorDiffuse"] = {"r": 0.192, "g": 0.701, "b": 0.168, "a": 0.0}
        hz["Grid"] = False
        hz["FogColor"] = color
        objs.append(hz)

    # --- global layout scale ---
    # Built-in tables are fixed meshes (Custom_Square is the largest), so to
    # gain table room we shrink the whole layout uniformly instead. Every
    # position and scale shares one factor, so relative sizing (token = board
    # cell) is untouched. Raise/lower this one knob to taste.
    LAYOUT_SCALE = 0.75
    def shrink(o):
        t = o["Transform"]
        t["posX"] *= LAYOUT_SCALE; t["posZ"] *= LAYOUT_SCALE
        t["scaleX"] *= LAYOUT_SCALE; t["scaleY"] *= LAYOUT_SCALE; t["scaleZ"] *= LAYOUT_SCALE
        for c in o.get("ContainedObjects", []):
            shrink(c)
    for o in objs:
        shrink(o)

    save = {
        "SaveName": "Constantinople 1453", "EpochTime": 0, "Date": "",
        "VersionNumber": "v14.2.1", "GameMode": "Constantinople 1453",
        "GameType": "", "GameComplexity": "", "Tags": [], "Gravity": 0.5,
        # Table_Custom_Square is the largest built-in table (Table_RPG was too
        # small for the full layout; the flex-table merge was reverted).
        "PlayArea": 0.5, "Table": "Table_Custom_Square", "TableURL": "",
        "Sky": "Sky_Museum", "SkyURL": "", "Note": "",
        "TabStates": {}, "MusicPlayer": {},
        "Grid": {"Type": 0, "Lines": False, "Color": {"r": 0.5, "g": 0.5, "b": 0.5},
                 "Opacity": 0.75, "ThickLines": False, "Snapping": False, "Offset": False,
                 "BothSnapping": False, "xSize": 2, "ySize": 2, "PosOffset": {"x": 0, "y": 1, "z": 0}},
        "Lighting": {"LightIntensity": 0.54, "LightColor": {"r": 1.0, "g": 0.9804, "b": 0.8902},
                     "AmbientIntensity": 1.3, "AmbientType": 0,
                     "AmbientColor": {"r": 0.5, "g": 0.5, "b": 0.5},
                     "AmbientColorTop": {"r": 0.5, "g": 0.5, "b": 0.5},
                     "AmbientColorBottom": {"r": 0.5, "g": 0.5, "b": 0.5},
                     "ReflectionIntensity": 1.0, "LutIndex": 0, "LutContribution": 1.0,
                     "LutURL": ""},
        "Hands": {"Enable": True, "DisableUnused": False, "Hiding": 0},
        "ComponentTags": {"labels": []},
        "Turns": {"Enable": False, "Type": 0, "TurnOrder": [], "Reverse": False,
                  "SkipEmpty": False, "DisableInteractions": False,
                  "PassTurns": True, "TurnColor": ""},
        "DecalPallet": [], "LuaScript": "", "LuaScriptState": "", "XmlUI": "",
        "ObjectStates": objs,
    }

    out_local = os.path.join(VDIR, "Constantinople_1453.json")
    json.dump(save, open(out_local, "w", encoding="utf-8"), indent=2)
    print("wrote", out_local, "(%d objects)" % len(objs))
    # also drop into the TTS Saves folder if present
    if os.path.isdir(SAVES):
        dst = os.path.join(SAVES, "Constantinople_1453.json")
        shutil.copy(out_local, dst)
        print("installed to TTS Saves:", dst)
    # regenerate the shareable friend pack from the same bundle this save uses
    build_friend_pack()

if __name__ == "__main__":
    main()
