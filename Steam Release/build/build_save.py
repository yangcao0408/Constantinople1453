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
V0 = os.path.join(ROOT, "Steam Release", "v0")
IMG = os.path.join(V0, "images")
ART = os.path.join(ROOT, "artifacts")
SAVES = r"C:\Users\CAO YANG\Documents\My Games\Tabletop Simulator\Saves"

rng = random.Random(1453)
_guids = set()
def guid():
    while True:
        g = "".join(rng.choice("0123456789abcdef") for _ in range(6))
        if g not in _guids:
            _guids.add(g); return g

def url(path):
    """Absolute file:/// URL with spaces percent-encoded."""
    p = os.path.abspath(path).replace("\\", "/")
    return "file:///" + quote(p, safe="/:")   # keep C:/ intact, only encode spaces

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

def tile(nick, img_path, w, h, pos, base_scale, locked=False):
    """Flat Custom_Tile; scaleZ set from image aspect so nothing distorts."""
    o = base("Custom_Tile", nick, pos,
             (base_scale, 1.0, base_scale * (h / float(w))), locked=locked)
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
    cd = {key: {"FaceURL": face, "BackURL": back, "NumWidth": cols,
                "NumHeight": rows, "BackIsHidden": True, "UniqueBack": False,
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
                     man["main_board"]["w"], man["main_board"]["h"],
                     (0, 1, 0), 15.65, locked=True))

    # --- decks (front edge) ---
    objs.append(make_deck("byzantine", man["byzantine"], (-8, 1.5, -14)))
    objs.append(make_deck("neutral", man["neutral"], (0, 1.5, -14)))
    objs.append(make_deck("ottoman", man["ottoman"], (8, 1.5, -14)))

    # --- player boards + CRT ---
    b = man["boards"]
    objs.append(tile("Byzantine Player Board", os.path.join(IMG, b["byzantine"]["file"]),
                     b["byzantine"]["w"], b["byzantine"]["h"], (-26, 1, 0), 9.0))
    objs.append(tile("Ottoman Player Board", os.path.join(IMG, b["ottoman"]["file"]),
                     b["ottoman"]["w"], b["ottoman"]["h"], (26, 1, 0), 9.0))
    objs.append(tile("Assault Resolution — CRT", os.path.join(IMG, b["crt"]["file"]),
                     b["crt"]["w"], b["crt"]["h"], (20, 1, 16), 5.5))

    # --- unit/leader counters: one consolidated deck per side ---
    td = man["token_decks"]
    objs.append(make_token_deck("ott", td["ott"], (-12, 1.5, 10), 0.55))
    objs.append(make_token_deck("byz", td["byz"], (12, 1.5, 10), 0.55))

    # --- a d10 for the CRT ---
    objs.append(base("Die_10", "d10", (14, 1.5, 16), (1, 1, 1)))

    save = {
        "SaveName": "Constantinople 1453", "EpochTime": 0, "Date": "",
        "VersionNumber": "v14.2.1", "GameMode": "Constantinople 1453",
        "GameType": "", "GameComplexity": "", "Tags": [], "Gravity": 0.5,
        "PlayArea": 0.5, "Table": "Table_RPG", "TableURL": "",
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

    out_local = os.path.join(V0, "Constantinople_1453.json")
    json.dump(save, open(out_local, "w", encoding="utf-8"), indent=2)
    print("wrote", out_local, "(%d objects)" % len(objs))
    # also drop into the TTS Saves folder if present
    if os.path.isdir(SAVES):
        dst = os.path.join(SAVES, "Constantinople_1453.json")
        shutil.copy(out_local, dst)
        print("installed to TTS Saves:", dst)

if __name__ == "__main__":
    main()
