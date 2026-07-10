# Constantinople 1453 — Design Document (Draft v0.1)

A 2-player, card-driven wargame (GMT COIN/CDG-adjacent) simulating the siege of
Constantinople, April–May 1453. One player is the Ottoman besieger, the other
the Byzantine defender.

## 1. High-Concept

- **Length:** 9–10 rounds, each round = one week of the historical 53-day siege.
- **Ottoman goal:** Breach the walls and take the city before Morale runs
  out (§4.0.4, the sole hard-loss track) — while their card economy
  (§4.0) steadily throttles what they can afford to do each round.
- **Byzantine goal:** Prevent any wall sector from being breached until the
  Ottoman player is forced to withdraw (a track hits zero) or the round track
  is exhausted (game ends turn 9/10 — Byzantine automatic win, since the
  historical relief-fleet clock is what the Ottomans are racing).
- **Core tension:** Ottomans have overwhelming force but a shrinking clock
  (political capital + army will to fight); Byzantines have almost no
  reserves and must allocate a razor-thin garrison across a long wall.

## 2. Turn Structure — Card-Driven

Each round (= one week, one "day" of action in game terms — the two are the
same beat, "day" is just the flavor name for the round's action sequence)
runs in two phases:

### 2.1 Phase A — Bombardment

- The Ottoman player bombards **3–4 sectors**, gated by cannon placement
  (i.e. which sectors currently have artillery sited against them — this is
  the spatial/logistics lever, not a free choice of any 3–4 sectors every
  round).
- **Concentration bonus:** if the Ottoman player commits 2 cannon
  units/cards against the *same* sector in the same round, that counts as
  a second hit — enough to also trigger an immediate Assault on that
  sector this round, without waiting for the Card Phase.
- This is a real trade-off, not an exploit: doubling up on one sector to
  chain Bombard→Assault uses 2 of the 3–4 total bombard slots, so it comes
  directly out of pressure the Ottoman player could otherwise be applying
  to other sectors. Concentration wins a sector faster; spreading keeps
  every Byzantine sector under pressure. Exact slot counts (3 vs 4, cost
  of doubling) to be tuned in playtesting.
- **Each Bombard action removes 1 Wall HP** from its target sector
  (§3.1) — the baseline damage rate behind the "several rounds of
  grinding" tempo the whole game is built around.
- **Second Barrage** (added 2026-07-10): once per round, **discard 2
  cards** for one additional Bombard action beyond the normal 3-4 slots.
  Same 1 HP damage as a normal shot, but it never counts toward the
  Concentration Bonus above — full details and reasoning in §4.0.3.

### 2.2 Phase B — Card Phase

- A single shared **Event Deck** (target ~35–45 cards for a 9–10 round
  game). Each round, both players are dealt a hand of **8–9 cards**.
- Players alternate playing cards for up to **7 mini-turns**, ending early
  if either side runs out of cards. Each card is usable for **either**:
  - its **Event** text (one-shot historical effect — weather, disease,
    Genoese blockade-runners, Hungarian envoy, janissary unrest, Orban's
    cannon arriving, the Golden Horn Manoeuvre, Coco's Raid, etc.), or
  - its **Ops value** (spend as generic points on the actions below).
- Ops actions (spendable by either side, gated by role):
  - **Ottoman:** Assault a wall sector (also usable here outside the
    concentration-bonus trigger in Phase A), Sap/mine, Muster
    reinforcements, Diplomacy (pressure Genoese/Venetians to stay
    neutral). Bombard itself is a Phase A action, not a Card Phase Ops
    action.
  - **Byzantine:** Repair a wall sector, Reinforce a sector (spend Reserve
    Pool tokens, §4.1), Sortie (raid to disrupt/destroy Ottoman cannon —
    steps the Ottoman Draw Track down, §4.0), Sue for aid (attempt to
    trigger relief-fleet event chances), Fire-ship raid (Coco's Raid —
    contest an unlocked Golden Horn, and on success also steps the
    Ottoman Draw Track down for ships lost/damaged, same logic as Sortie
    — Byzantine naval/raid actions should generally cut into the Ottoman
    card economy when they succeed, not just move Byzantine-side tracks).
- End-of-round bookkeeping: track adjustments, reserve/resource upkeep.
- **Each Ops action costs 2 Ops points** to perform (Assault, Repair,
  Reinforce, Sortie, Sap/Mine, Sue for Aid, Diplomacy, Muster
  Reinforcements — every entry in the lists above).
- **Pressure to Attack (added 2026-07-10):** starting **round 2**, if the
  Ottoman player makes zero Assault attempts this round (Phase A
  concentration-bonus assault or Phase B Ops), Morale **-1** — the
  Sultan's court and army expect visible progress, and a round of pure
  bombardment with no follow-through reads as hesitation. This exists to
  rule out a degenerate "bombard forever, never risk an assault"
  strategy. It works even this early, before the walls are properly
  softened (§3.1, real damage doesn't usually start until round 3-4),
  because the rebalanced CRT (§6.5) makes a cheap, disposable "probing"
  assault — a single Bashi-bazouk thrown at bad odds — genuinely low-risk
  for the attacker and low-cost for the defender. The rational response
  to this rule most rounds should be exactly that: a token assault to
  avoid the Morale penalty, not a real commitment, which is itself decent
  siege flavor (constant skirmishing pressure alongside the main
  bombardment).

### 2.3 Generic Action Cards

Most of the shared Neutral-pool draw each round (4–5 of it) isn't the
named Event Deck material built out in EVENT_DECK.md — it's plain,
single-use **generic action cards**, each worth exactly **1 Ops point**.
(This is a clarification of what fills the existing "5–6 from the Neutral
pile" draw from §2.2 above, not an additional draw on top of the 8–9/round
total — confirm this reading if it doesn't match what you had in mind.)

There are **four** generic card types (revised 2026-07-11, added a
fourth after the original three left Sap/Mine and Sue for Aid with no
efficient funding path at all — worth having *some* cheap route to them
even if rarer, rather than making them permanently reliant on named
cards), each **typed to match specific Ops actions**:

| Type | Ottoman match | Byzantine match |
|---|---|---|
| **Attack** | Assault | Sortie, Fire-ship raid |
| **Supplies** | Diplomacy | Repair |
| **Move** | Muster Reinforcements | Reinforce |
| **Guile** | Sap/Mine | Sue for Aid |

Fire-ship raid moved under Attack rather than staying unmatched — it's a
genuinely aggressive strike action, the same category as a Sortie, not a
diplomatic or logistics action.

- **On-purpose use**: a card contributes its full 1 Ops toward its
  matching action. Two matching cards = exactly the 2 Ops an action
  costs — clean and efficient.
- **Off-purpose use**: any 2 generic cards, discarded together
  (regardless of type), convert to 1 Ops toward *any* action — a flat
  2-for-1 penalty. Funding a 2-Ops action entirely off-purpose costs 4
  generic cards instead of 2.
- **Guile is deliberately the rarer type** (fewer copies in the pool,
  see EVENT_DECK.md) — Sap/Mine and Sue for Aid should still feel like
  more deliberate, less routine actions than the "big three," just not
  permanently locked out of an efficient path entirely.
- **Named Event Deck cards are exempt from type-matching** — their Ops
  value (see below) already works toward any action, unchanged from the
  original design. The generic-card typing system is additional texture
  layered under the named deck, not a replacement for it.

This creates the intended tension directly: draw the right generic card
for what you want to do, and it's efficient; draw the wrong mix, and you
either wait, spend a named card's Ops value instead, or burn cards 2-for-1
to force it through.

### 2.4 Ops Value Scale (revised)

Generic action cards (§2.3) are always exactly **1 Ops**. Named Event
Deck cards range **2–5 Ops**, scaled by how significant the Event is —
this widens the original 1–3 scale specifically so a genuinely pivotal
card (Golden Horn Manoeuvre, The Emperor Falls, Terms of Surrender) feels
meaningfully heavier than two generic cards stapled together, not just
marginally better:

| Ops | Tier | Guidance |
|---|---|---|
| 2 | Minor | Situational, narrow-effect Events |
| 3 | Moderate | The deck's default — most named cards land here |
| 4 | Major | Strong, often round-gated or unique Events |
| 5 | Pivotal | Reserved for the small handful of story-defining beats |

*Open question:* only a representative pass of the most obviously
"pivotal" cards has been rescaled into this range so far (see
EVENT_DECK.md) — the full deck needs a rebalancing pass against this new
1–5 scale rather than the original 1–3 guidance.

## 3. The Wall — Segmented Map

### 3.1 Land Wall Sectors (5, north to south)

| # | Sector | Gate | Wall HP | Notes |
|---|---|---|---|---|
| 1 | **Blachernae** | Caligaria/Kynegos Gate | 7 | Single wall (not triple), historically weaker construction, but flanked by terrain |
| 2 | **Charisius** | Charisius (Adrianople) Gate | 8 | High ground, standard triple wall — historically quieter |
| 3 | **Mesoteichion** | St. Romanus Gate | 6 | The historical breach point — lowest ground, weakest position, where the great cannon focused |
| 4 | **Gate of the Spring** | Pege (Selymbria) Gate | 8 | Higher ground, secondary pressure point |
| 5 | **Golden Gate** | Golden Gate | 8 | Southernmost, saw the least assault pressure historically |

Each land sector tracks:
- **Wall Integrity (HP)**, reduced by Bombard, restored by Repair — can't
  repair past a "rubble" cap once heavily battered.
- **Garrison strength present** (Byzantine's scarce resource, moved via
  Reinforce, drawn from the Reserve Pool — §4.1).

**Assault is always legal, at any HP** — there's no hard breach gate. What
changes with HP is the **Wall Defense** value it contributes to the
defender's total strength in the Assault check (§6):

| HP remaining | State | Wall Defense |
|---|---|---|
| > 1/2 max | Intact | **6** — close to historically un-stormable; only rational once softened |
| ≤ 1/2 max | **Contested** | **3** — a real, if risky, attack option |
| ≤ 1/3 max | **Breached** | **1** — wall proper is gone, but rubble/improvised stockade (as Giustiniani built at Mesoteichion) still gives a token defense — never 0 |

This avoids a turtle-lock where a well-repaired sector becomes
mathematically safe forever; it also means Repair is a genuine
round-to-round race against Bombard rather than a one-time fix. The
1,000-year historical dominance of these walls before gunpowder siege
artillery is the justification for a full-health wall being worth as much
as, or more than, an entire committed unit stack (§6) — direct assault on
an intact wall should be close to irrational, which is accurate: no
attacker ever took these walls by frontal assault before 1453.

**Wall Defense is a combat modifier, not a second health pool** (made
explicit 2026-07-11, §6.5) — it never runs out on its own the way
Garrison Strength does. Its only job is shaping the Assault ratio, which
in turn shapes how much Garrison damage a hit deals. A sector falls only
when its Garrison Strength hits 0, regardless of remaining Wall HP — an
intact but empty wall offers no one to actually stop the Ottomans.

### 3.2 Sea Wall — Golden Horn (the only mechanical sea sector)

The Marmara sea wall and the Acropolis Point are **not tracked as sectors**
— strong currents made them historically unassailable, so they're map
flavor only, not playable space.

The **Golden Horn** is the one sea sector, and it works differently from
the land sectors:

- **Dormant at game start.** It isn't assaultable or garrisoned until the
  Ottoman player plays the **"Golden Horn Manoeuvre" (旱地行舟)** event —
  the historical overland portage of ships past the chain. Playing that
  event unlocks the sector; it doesn't itself resolve any combat.
- **No Bombard action.** Historically no siege artillery could be brought
  to bear on it (that would require a battery on the neutral Genoese
  Galata shore), and ship-mounted guns of the era couldn't breach masonry.
  Its Integrity is never worn down — the Ottoman player goes straight to
  Assault.
- **Permanent naval defense value.** No Wall Defense from HP (there is no
  HP track here), but the sector still contributes a flat **Naval Defense
  of 3** to the defender's total in every Assault check — representing
  the inherent difficulty of a shipborne escalade regardless of
  garrison, roughly equivalent to a permanently-Contested land wall. This
  never improves or degrades; it's a constant, not a track.
- **Garrison strength still matters directly**, same as any land sector —
  it's the main lever the Byzantine player has to push the odds further
  against the Ottomans. Byzantines have no reserves, so any garrison
  posted here is diverted from a land sector.
- **A Byzantine counter-event, "Coco's Raid" (fire ships)**, should exist
  as the historical answer — a Byzantine Ops/event action that can
  neutralize or roll back the unlocked Golden Horn threat, at real risk
  of failure (historically, the raid failed after being betrayed and
  Coco was killed).

Leaving the Golden Horn completely ungarrisoned is a real, recurring
gamble once it's unlocked, not a free action — see §5.

Breaching a sector (land or sea) doesn't auto-end the game — the Ottoman
player still has to win an **Assault** (a resolved combat check pitting
attacking Ops/troops committed that round against defending garrison in
that sector), and specifically grind that sector's **Garrison Strength**
to 0 in the process (§6.5), to actually take it. This is the single most
important design lever for difficulty tuning.

## 4. Ottoman Tracks

**Restructured 2026-07-11.** Formerly two numeric countdown tracks
(Resources 35 + Morale), which felt redundant — both were big numbers
ticking toward the same "hits zero → you lose." The fix: **Resources is
no longer a numeric counter at all. The Ottoman card economy IS their
resource.** This leaves Morale as the single hard-loss track (kept for
flavor), and makes the two systems distinct *in kind* — Morale is the
doom clock, card-draw is the economic throttle — rather than two
identical doom bars.

### 4.0 Resources = the Ottoman Card Economy

Ottoman material strength (gunpowder, cannon, gold, logistics) is
represented not by a point pool but by **how many cards the Ottoman
player draws each round** and can then spend.

- **Draw Track:** a small track setting the Ottoman player's per-round
  Neutral-pile draw. **Starts at 6** (placeholder), range **2–8**. The
  Byzantine player draws a flat baseline from the Neutral pile (say 5);
  the Ottoman player draws equal to their current Draw Track level —
  starting *above* the Byzantine baseline, reflecting their real material
  superiority, and grindable up or down over the game.
- **Two distinct ways Resources actually move in play** (clarified
  2026-07-11, once the Event Deck card-text conversion pass — see
  EVENT_DECK.md — made the split concrete):
  - **Persistent Draw Track shifts** — reserved for genuinely
    multi-round, structural effects: a recalled commander sitting out
    2 rounds (The Karamanid Rising, Skanderbeg's Revolt), Double Pay
    Proclaimed's sustained morale-of-the-army boost. These change the
    *baseline* going forward.
    - **"Spending resources"** on the expensive capabilities below is
    also paid this way, but as an immediate discard rather than a track
    shift — see next bullet.
  - **Immediate one-shot draw/discard** — this is what almost all
    individual Event Deck cards actually use now: "Ottoman draws N extra
    cards" or "Ottoman discards N cards," resolved once, not a change to
    next round's baseline. Powder Shipment Arrives, Plague in the Camp,
    Tribute Demand, mustering costs, Second Barrage, Combined Arms — all
    of these are immediate hand-size effects, not Draw Track edits. This
    is the far more common case; treat Draw Track shifts as the
    exception reserved for effects that are explicitly about a
    sustained, multi-round change in capability.
- Either way, a card-starved Ottoman hand (whether from a lowered Draw
  Track or a run of discard-heavy cards) has both fewer actions *and*
  fewer cards to burn on Second Barrages or elite musters — the intended
  strangulation, expressed entirely through the card engine.
- **No independent hard-loss condition.** Unlike the old Resources track,
  the Draw Track bottoming out at 2 doesn't end the game — it just
  starves the Ottoman of options, which indirectly costs them the siege
  (can't sustain enough assault pressure before Morale/time runs out).
  Morale (§4.0.4) is now the *only* track whose zero = immediate
  Byzantine win.

*Interpretation flag:* this reads "spend resources" as "discard cards"
and "resource level" as "cards drawn per round." If you meant spending to
work differently (e.g. paying costs by drawing-and-discarding from the
shared pile), say so — the rest of the model holds either way.

#### 4.0.1 Mustering Cost (per unit fielded, §6.1)

Paid in **discarded cards** now, not Resource points, but the same tiered
escalation — cheap irregulars barely dent your hand, elite troops are a
real spend of your options:

| Unit | Cost |
|---|---|
| Bashi-bazouk | Free (unpaid volunteers) |
| Azap | 4 units per 1 card |
| New Levy Janissary | 2 units per 1 card |
| Janissary | 1 card per unit |
| Solak | 2 cards per unit |

Placeholder ratios — and note card-costs and old point-costs aren't the
same scale, so these need re-tuning against how big a typical hand is
(Draw Track ~6), not just carried over 1:1 from the old Resource numbers.

#### 4.0.2 Mehmed's Combined Arms

Combined Arms (§6.2, +2 Attack when leading an Assault at a cannon-sited
sector) now **costs 1 discarded card to activate** — a real spend of your
hand each time, not a free passive.

#### 4.0.3 Second Barrage

A Phase A option (§2.1): once per round, the Ottoman player may **discard
2 cards** (placeholder) for **one additional Bombard action** beyond the
normal 3-4 slots. This extra shot deals the same Wall HP damage as a
normal Bombard (§3.1: **1 Bombard action removes 1 Wall HP**), but **does
not count toward the Concentration Bonus** (§2.1) — it can't be the shot
that unlocks a same-round Assault. That's the "half effectiveness": not
half damage (fractional HP is awkward), but half the strategic value.
One extra shot per round max.

#### 4.0.4 Morale (revised this session — track size and gain/loss sources)

- **Morale** (janissary/army will to fight + Sultan's political capital to
  keep the siege going against court opposition).
- **Morale gain is capped at exactly two named cards in the whole deck**
  (EVENT_DECK.md, revised this session): **The Hadith of Conquest (+1,
  round 1-2)** and **The War Council (+1, round 7+)** — max **+2** across
  a full game. No other source of Morale gain exists. (Previously
  Baltaoğlu's Punishment also granted +1; that's been cut — a public
  scapegoating doesn't actually put fight back in the army, so it's now a
  pure card-draw effect instead.)
- **Morale loss**, current confirmed sources: named/event cards (The Four
  Ships -2, Halil Pasha's Doubt -1 optional) and the Pressure-to-Attack
  rule (§2.2, -1/round from round 2+ if the Ottoman makes zero Assault
  attempts).
- **Morale hitting zero → the Ottoman army withdraws → immediate
  Byzantine win.** This is the sole hard-loss track for the Ottoman side.
  Note this isn't the *only* way Byzantine wins — reaching round 9/10
  with no sector lost is an automatic Byzantine win regardless of Morale
  (§5) — so Morale running out under sustained pressure late in the game
  is a legitimate, expected outcome, not a sign the track is broken.

**Open design thread, this session (2026-07-10) — not yet decided:**
two structural drains under discussion to supplement the named-card
swings above, replacing the old vague "elapsed time" / "failed assaults"
language from the pre-rewrite version of this section:

1. **Time decay** — Morale -1 every 2 rounds (e.g. end of rounds 2, 4, 6,
   8), unconditional. Thematically strong: it's the mechanical expression
   of the real historical pressure to abandon the siege before autumn/
   politics forced a withdrawal, and it means the Ottoman player faces
   real urgency even in a round where nothing else went wrong — matching
   the "shrinking clock" framing in §1's High-Concept. Over a 9-10 round
   game this alone contributes roughly **-4 to -5**, which is most of a
   7-8 level track by itself — that's intentional pressure, not a bug,
   given the auto-win-at-round-9/10 rule above, but it means the two
   Morale-gain cards (+2 total) need to matter as real, felt offsets, not
   token bonuses.
2. **Elite Casualty threshold** — Morale -1 once cumulative Janissary/
   Solak steps lost (across the whole game, not per-Assault) crosses some
   threshold (e.g. every 3 elite steps). This would replace the old
   "Elite Casualty Morale Surcharge" language in §6.3, which doubled a
   per-Assault "small Morale hit" that no longer exists now that Morale
   is decoupled from the automatic per-roll Attacker-steps-lost trigger
   (§6.5) — that trigger fired on literally every Assault under the
   rescaled CRT, which was never the intent. A cumulative threshold
   instead makes elite losses a real, trackable cost of committing
   Janissaries/Solaks, consistent with the Mustering Cost/Force
   Commitment Cap tension already built around those units (§6.3).

Track size still pending a final number — 7-8 levels is the leading
candidate (see conversation), sized against the two above drains plus
the +2 max from named cards, rather than picked first and backed into.
§6.3's Elite Casualty Morale Surcharge text still needs updating to match
whichever way this resolves.

### 4.1 Byzantine Track — Reserve Pool

Resolves the open question above: Byzantines get one shared track, the
**Reserve Pool**, sized **20-30 tokens** (revised this session, up from
a flat 20 — see the survivability check below for why).

- Per-sector Garrison Strength (§3.1) is where troops actually sit and
  fight; the Reserve Pool is the finite well that feeds it. Every time the
  Byzantine player Reinforces a sector or fields new units (via Ops or
  event), a token comes off the Reserve Pool — mirroring Ottoman
  Resources as the "can we even afford this action" constraint.
- As the pool depletes, penalty bands kick in (same graduated-band logic
  as wall HP, §3.1 — exact thresholds TBD, likely mirroring 1/2 and 1/3).
- At **zero**, the Byzantine player can no longer Reinforce or field new
  units at all — existing garrisons keep fighting where they stand, but
  there's no way to backfill losses. Like the Ottoman Draw Track
  bottoming out (§4.0), this doesn't itself end the game — an empty
  Reserve Pool just means every remaining sector has to hold with what
  it's already got. (Both sides now have a soft-strangulation resource —
  Reserve Pool for Byzantines, Draw Track for Ottomans — and one hard
  loss condition each: a won Assault against the Byzantines, Morale zero
  against the Ottomans.)
- 20-30 tokens is still a placeholder scale — needs playtesting against
  how many tokens a typical Reinforce action costs and how many rounds
  the siege runs (9–10).

**Survivability check, new session (2026-07-10):** the target driving
both this Reserve Pool range and the CRT rescale in §6.5 is explicit
now, rather than backed into: Byzantine should field **~12-15 Garrison
HP at game start (Initial Garrison, below) plus 20-30 more via
Reinforce**, for **~32-45 total capacity**, against an expected
**20-25 Assaults over the full game** — enough that the Byzantine
player can hold off **at least 20** of them and still call the game a
real challenge rather than a rout in either direction. With the CRT
halved (§6.5, avg Defender loss now 0.5-3.6 per Assault depending on
column, versus the old 0.5-6.7), 20 Assaults at a blended average of
~2 Garrison steps each lands around **40 total steps lost** — squarely
inside the 32-45 capacity range, and comfortably below it if the
Byzantine player is actively repairing walls to keep ratios out of the
worst columns (§3.1, §6.4). This is still a rough Fermi pass, not a
simulation — real per-round assault frequency, which sectors get
targeted, and how aggressively the Byzantine player repairs vs.
reinforces will all move the actual number — but the two halves (CRT
output, Garrison capacity) are now sized against each other on purpose
instead of the CRT being tuned first and the capacity backed in after.

**Initial Garrison** (present at each sector from round 1, entirely
separate from the Reserve Pool, which represents *replacement* troops
only): **12-15 total**, e.g. **2 Roman militia pre-deployed at each of
the 5 land sectors (10 total)**, plus **Giustiniani's Genoese Company
and 1-2 Venetian Marine units** deployed at their historical starting
positions (Mesoteichion/mobile reserve for Giustiniani, spread along the
wall for the Venetians) — roughly 2-5 additional units on top of the 10
militia, landing in the 12-15 target range. Still a placeholder pending
a real playtest to confirm the ~32-45 total capacity / 20-Assault
target above actually holds up in play.

## 5. Win/Loss Summary

- **Ottoman wins:** Grind any one of the 6 sectors' (5 land + Golden Horn)
  **Garrison Strength to 0** via a won Assault (§6.5) — legal any time,
  but realistically only likely once a land sector is Contested/Breached
  (§3.1) or the Golden Horn is under-garrisoned, since that's what keeps
  per-hit Garrison damage low or high — before **Morale** hits 0 (§4.0.4,
  their sole hard-loss track). No sector-count threshold — a real breach
  anywhere was historically fatal, since the city had no second line of
  urban defense once the walls were penetrated. This is why the Golden
  Horn matters even though it can never be bombarded: an under-garrisoned
  Golden Horn is a live, low-odds-but-real path to an Ottoman win, not
  just a nuisance sector.
- **Byzantine wins:** Survive to the end of round 9/10 without losing an
  Assault in any sector, OR drive Ottoman **Morale** to 0 earlier. (The
  Ottoman Draw Track, §4.0, is not a loss condition — grinding it down
  only strangles the Ottoman player toward one of those two outcomes.)

## 6. Assault Resolution

Paths of Glory-style odds-ratio Combat Results Table (CRT). Chosen over a
flat point differential specifically because the stakes are absolute — a
single won Assault ends the game (§5) — so the die roll needs to preserve
real risk even at good odds, matching the historical pattern of repeated
failed Ottoman assaults even against battered walls, right up until the
one that finally succeeded.

### 6.1 Unit Combat Values (draft)

Each side's defenders/attackers are drawn from historically distinct
national contingents rather than a single generic troop type — the siege
really was fought by a patchwork of separate factions on the defending
side, and a tiered irregular-to-elite structure on the Ottoman side.

| Unit | Side | Attack | Defense | Steps | Notes |
|---|---|---|---|---|---|
| Bashi-bazouk | Ottoman | 1 | — | 1 (removed on hit) | Unpaid, loot-driven volunteers, historically thrown in as the expendable first wave to draw and exhaust defensive fire. **Free of the Elite Casualty Morale Surcharge** (§6.3) — losing them costs Mehmed nothing politically |
| Azap | Ottoman | 2 | — | 1 (removed on hit) | Paid irregular infantry, the second wave — disciplined enough to hit harder than Bashi-bazouks, but still not a standing corps |
| New Levy Janissary | Ottoman | 2 | — | **2** | Recently-conscripted Janissaries, not yet campaign-hardened — tougher than any irregular (part of the standing corps' training pipeline) but not yet worth the full political weight of a veteran; **exempt from the Elite Casualty Morale Surcharge** (§6.3) |
| Janissary | Ottoman | 3 | — | **2** | Elite standing corps, held back for the decisive wave — full Elite Casualty Morale Surcharge and Mustering Cost apply (§6.3) |
| Solak | Ottoman | 4 | — | **2** | The Sultan's own personal bodyguard archers — small token cap (2), the single best Ottoman unit; full Elite Casualty Morale Surcharge and Mustering Cost apply (§6.3) |
| Roman militia | Byzantine | 1 | 1 | 1 (removed on hit) | Native levies; scarcity handled by quantity via the Reserve Pool (§4.1), not by a stronger stat |
| Genoese Company (Giustiniani's) | Byzantine | 2 | 3 | **2** | Giustiniani's own professional condottieri (~400-700 men historically) — small token pool, the best troops in the city |
| Venetian Marines | Byzantine | 1 | 2 | 1 | Crews/soldiers off Minotto's ships — semi-professional, a mid-tier option between militia and the elite companies |
| Cretan Sailors | Byzantine | 1 | 2 | **2** | Small elite pool (1 token) — historically fought on for days after the city itself had fallen |
| Isidore's Legation | Byzantine | 1 | 3 | 1 (removed on hit) | Cardinal Isidore of Kiev's ~200-man papal legation — a small, symbolic Western-Church contingent fighting alongside the defenders; single token, no step reduction (too small a company for a meaningful "reduced" state) |

Multi-step units (New Levy Janissary, Janissary, Solak, Genoese Company,
Cretan Sailors) take a hit, flip to a reduced/spent face, and are only
removed on a second hit — the mechanic is identical on both sides (per
your steer: symmetric rule, asymmetric quantity is where the real
imbalance should live). The actual difficulty gap between the two armies
should come from how many tokens of each type exist in the pools (a large
pool of standard Janissary and Azap tokens for the bulk of the army; only
2-3 Genoese Company tokens, a single Cretan token, and a capped Solak
pool of 2 reflecting how genuinely small those elite contingents were) —
exact pool sizes TBD, §7.

The Ottoman roster now mirrors the Byzantine one's shape: a free/expendable
base tier (Bashi-bazouk ~ Roman militia), a paid-professional middle tier
(Azap ~ Venetian Marines), and elite tiers where overcommitting carries
real political or logistical risk (Janissary/Solak ~ Genoese Company),
which is the same tension on both sides of the table by design.

### 6.2 Leaders

Leaders add flat strength to their side's total, added before the ratio
is computed (this is how Paths of Glory itself models leaders, keeping it
consistent with how Wall Defense and Naval Defense already contribute as
flat points rather than column shifts):

**Byzantine:**

- **Constantine XI (the Emperor)**: **+2 Defense** (his charismatic
  presence rallying troops in person), *plus* his unique Command
  Coordination ability, §6.2.1 — the only leader who adds both a combat
  stat and a structural ability. A single, unique, irreplaceable token:
  he can only be in one sector at a time, a real logistical puzzle every
  round (which sector needs unified command most?). Historically he died
  in the final assault, and organized resistance collapsed almost
  immediately after — losing him should carry weight beyond just "one
  more leader gone," exact consequence still TBD (§7).
- **Giustiniani**: +2 Defense. Commands the Genoese Company only.
  Historically he commanded the mobile professional reserve, redeployed
  to reinforce whichever sector was under the heaviest pressure — his
  removal/wounding at Mesoteichion in the final assault, which triggered
  a defensive collapse, is a strong candidate for a mid/late-game event.
  **First Strike:** when Giustiniani leads a Defense that includes the
  Genoese Company, inflict one automatic step loss on the attacking force
  *before* the CRT roll is made — Genoese crossbow companies were among
  the most renowned mercenary archers in Europe, and this reflects
  disciplined volley fire breaking up an assault before it makes contact,
  rather than just another flat stat.
- **Girolamo Minotto**: +1 Defense. Commands Venetian Marines only.
- **Loukas Notaras**: **+2 Defense.** Megas Doux — the empire's highest
  naval office, historically the supreme commander of the Byzantine
  fleet. **Naval Command:** he is the natural leader for defending the
  Golden Horn sector, and — unique among the foreign-contingent leaders —
  is not restricted to a single national contingent's troops there; he
  may command whatever mix of units (militia, any present foreign
  contingent) is garrisoned at the Golden Horn without needing
  Constantine present, the one exception to the multi-contingent rule in
  §6.2.1. This gives the Byzantine side a Golden Horn specialist
  mirroring Zaganos Pasha on the Ottoman side. He was also a genuinely
  controversial, politically complicated figure (later accused of
  favoring Ottoman rule over union with the Latin church) — good
  additional material for a loyalty-themed Event Deck card, distinct from
  his battlefield role.
- **Cretan Sailors have no dedicated named leader** in the sources — by
  design, they can only be committed alongside Constantine (§6.2.1), not
  under any of the above.
- *Not statted as a combat leader, but strong Event Deck material:*
  **George Sphrantzes** (Constantine's close advisor/chronicler, natural
  flavor for the "Sue for aid" Ops action, §2.2).

**Ottoman:**

- **Mehmed II (the Sultan)**: **+1 Attack** personally — a deliberately
  modest combat stat, reflecting his mixed reputation as a close-in
  tactician relative to his real strategic brilliance (his own senior
  vizier, Halil Pasha, opposed the siege outright, and Mehmed's early
  push for a premature assault had to be reined in by his commanders).
  **Combined Arms:** if Mehmed leads an Assault at a sector that
  currently has cannon sited against it (this round's Bombard targets,
  §2.1), he adds a further **+2 Attack** for **1 discarded card** (§4.0.2)
  — representing coordinated artillery fire support timed to the infantry
  assault, which is exactly what happened in the historical final
  assault on May 29. A real spend each time, not a standing passive. No
  command
  restriction — Mehmed (or any Ottoman leader) may command any Ottoman
  unit type freely. Unlike the Byzantine side's fractious alliance of
  independent contingents, the Ottoman army was under genuinely unified
  sultanic command, and that structural contrast is worth keeping visible
  in the rules rather than symmetrizing away.
- **Zaganos Pasha**: **+1 Attack.** Historically oversaw the Golden Horn
  ship portage and directed the Serbian sapper corps (notably countered
  on the Byzantine side by a Scottish/German engineer, John Grant — good
  flavor for a future defensive counter-sapper card). **Engineering:**
  when present, the Sap/Mine Ops action costs 1 less Ops (one fewer card
  to fund it); he is also the natural leader for Assaults on the Golden
  Horn sector, reflecting his actual area of command.
- **Karaca Pasha**: **+1 Attack.** Beylerbey of Rumelia, commanded the
  European/Balkan troops, historically positioned toward the **northern**
  end of the line. **Northern Command:** +1 further Attack when leading
  an Assault on Blachernae or Charisius. He was killed during the siege
  by defensive fire from the walls — a strong candidate for a mid-game
  "Karaca Pasha Killed" event (a Morale hit, mirroring Giustiniani's
  wounding as a symmetric narrative beat on the Ottoman side).
- **Ishak Pasha**: **+1 Attack.** Beylerbey of Anatolia, commanded the
  Anatolian troops, historically positioned toward the **southern** end
  of the line. **Southern Command:** +1 further Attack when leading an
  Assault on Gate of the Spring or Golden Gate. Unlike Karaca Pasha, he
  survived the siege and went on to become Grand Vizier later in
  Mehmed's reign — a stable, enduring figure rather than one built around
  a death event.
- Between the four of them, every zone of the wall now has its own
  historical commander: Karaca Pasha (north), Mehmed (center, following
  the cannon), Ishak Pasha (south), Zaganos Pasha (Golden Horn) — closely
  matching the real Ottoman deployment around the city.
- *Not statted as a combat leader, but strong Event Deck material:*
  **Halil Pasha** (Grand Vizier, led the internal faction opposed to the
  siege — good source for a Morale-draining "court dissent" event) and
  **Baltaoğlu Süleyman Pasha** (the admiral who failed to stop Christian
  relief ships early in the siege and was subsequently punished by
  Mehmed — good source for a Golden Horn-flavored naval-failure event).

#### 6.2.1 Command Coordination

The defending side is a patchwork of rival national factions, not one
army — Genoese and Venetian contingents in particular were historically
prone to friction and distrust. This is modeled directly as a
restriction on which units can be committed together to the same Assault
defense:

- **Roman militia never needs a leader** — always includable, the
  baseline home-army defenders.
- **Each foreign contingent (Genoese, Venetian) requires its own matching
  leader present in that sector** to be committed at all — no leader
  present, no access to that contingent's troops there.
- **A single Defense may combine militia with *one* foreign contingent**
  (whichever single foreign leader is present) without any special
  requirement.
- **Combining two or more different foreign contingents in the same
  Defense requires Constantine XI present in that sector.** Only the
  Emperor has the standing to coordinate rival factions together — no
  other leader can.
- **Exception: Notaras at the Golden Horn.** As Megas Doux he may command
  any mix of units present at that specific sector without needing
  Constantine — the one deliberate crack in an otherwise strict rule,
  reflecting his real naval authority there (§6.2).
- Cretan Sailors, having no leader of their own, can *only* ever be
  fielded as part of a Constantine-coordinated Defense.

This makes Constantine the answer to "how do I mount my strongest
possible defense at the sector under real pressure this round," while
also making him a single point of failure the Byzantine player has to
risk moving toward danger — exactly the tension his historical role
carried.

### 6.3 Force Commitment Caps

Frontage, not point-budget, is the limiting factor — a breach or wall
section is only so many meters wide, so the cap is on **number of units**,
not total strength. A stronger unit takes up the same "slot" as a weaker
one; the cost of committing your strongest units shows up elsewhere (see
below), not in the cap itself.

- **Attacker cap: 5 units per Assault** (any mix of Ottoman troops).
- **Defender cap: 4 garrison units committed per Assault.** Wall Defense
  and Naval Defense (§3.1/§3.2) aren't "units" and don't count against
  this — they're the fortification's own contribution, stacked on top of
  whatever garrison units are committed. (Matches the shape of your own
  example: rubble +1, a Genoese unit, and up to 3 militia units stacking
  alongside it.)
- Both caps are placeholders pending playtesting, but the asymmetry
  (5 attacker slots vs 4 defender slots) is intentional — Ottomans should
  be able to slightly out-mass the defenders at the point of contact even
  though the defenders get the fortification bonus the attacker never
  does.

**Committing elite troops is a deliberate, costly choice, not the default
play** — this is what actually keeps a 5-Janissary stack rare rather than
routine, doing the job a flat point-cap would otherwise have done:

- **Elite Casualty Morale Surcharge:** whenever this Assault's resolution
  (§6.5) deals the Attacker **1 or more steps lost**, if one or more
  **Janissary or Solak** units were among the committed attackers, the
  Morale hit is doubled. Bashi-bazouks, Azaps, and New Levy Janissaries
  are exempt (§6.1) — Janissaries and Solaks were expensive, prized, and
  politically sensitive to lose in numbers, and taking real casualties
  among veteran troops should hurt the Ottoman player far more than
  losing irregulars or green recruits, mirroring the real political risk
  Mehmed carried every time he fed his best troops into a failed assault.
- **Mustering cost:** committing a 3rd or more **Janissary or Solak** unit
  (New Levy exempt) to the same Assault costs **1 discarded card per unit
  beyond the second** (so a 5-veteran all-in assault costs 3 extra
  discarded cards on top of the normal Assault Ops cost). This represents
  the logistical and political effort of concentrating elite troops at a
  single point, and directly answers "it shouldn't be easy to commit five
  Janissary units at one go" — it's possible, but it's a deliberate all-in
  spend a player will only reach for when the odds already look good, not
  a routine opener. (Consistent with the card-economy model, §4.0 — elite
  concentration burns hand, i.e. your options, not an abstract point
  pool.)

### 6.4 Combat Calculation

- **Attacker Strength** = sum of committed attacking units' Attack values
  (max 5 units, §6.3) + any Ottoman leader bonus + event modifiers.
- **Defender Strength** = sum of committed garrison units' Defense values
  (max 4 units, §6.3) + Wall Defense (§3.1 band) or Naval Defense (§3.2,
  Golden Horn only) + Giustiniani bonus if present + event modifiers.
- Compute **Attacker : Defender**, rounded down to the nearest standard
  column: 1:2 (or worse), **3:4**, 1:1, 3:2, 2:1, 3:1, 4:1+. (Added the
  3:4 column 2026-07-11 — the jump straight from 1:2 to 1:1 was the
  single biggest gap in the ladder, and it's exactly the range a
  partially-softened wall spends a lot of time in.)
- Roll **1d10** against the column on the CRT below. A single die, not a
  sum of two — summing dice (2d6/2d10) produces a bell curve that
  clusters results around the average and smooths out extreme outcomes,
  which would work against the whole point of using a CRT here: even
  good odds should still carry real risk (§6). A single d10 keeps the
  same flat, every-face-equally-likely character as the d6 it replaces —
  it's just finer-grained, letting the bands below hit precise
  percentages instead of being locked to sixths.

### 6.5 Combat Results Table — Mutual Damage (revised 2026-07-11)

Every Assault resolves as a **paired outcome**: how many steps the
Attacker loses, and how many steps the Defender loses, off the same
single roll — every cell is a real number for both sides now, no
exceptions. Read each cell as **Atk-x / Def-y**: the Attacker loses *x*
committed unit steps, the Defender loses *y* Garrison steps.

**Sector Falls is no longer a CRT category.** Previously it was a
separate lucky-roll result bolted onto the top-right corner of the
table, gated to never appear below 2:1. That's gone. Instead:

- **Wall Defense is purely a combat modifier now** — it shapes the ratio
  (via Bombard grinding it down, §3.1), which shapes how much Garrison
  damage lands per Assault. It is *not* a second, independent health pool
  the sector can survive on even with no defenders left.
- **Garrison Strength is the sector's actual life total.** A sector
  falls the instant its Garrison Strength is reduced to **0** by
  accumulated Defender steps lost from a won Assault — full stop,
  regardless of the roll, the ratio, or the wall's remaining HP band. An
  empty wall cannot repel anyone, no matter how intact the masonry.
- This means there's no more artificial floor protecting a sector below
  2:1 odds. The real protection is exactly what it should be: keep Wall
  Defense high (via Repair) so Garrison damage per hit stays low, and
  keep Garrison Strength topped up (via Reinforce) so there's a deep
  pool to grind through. Nothing is hard-coded safe anymore; everything
  has to be actually defended.
- A sector with 0 Garrison Strength that simply hasn't been assaulted
  yet doesn't auto-lose — the fall triggers only when the Ottoman player
  actually wins an Assault there and the resulting Defender steps lost
  brings the total to 0 or below. This still gives the Byzantine player
  a window to Reinforce before the axe falls.

**Numbers halved back down, new session (2026-07-10)** — the 2026-07-11
doubling overshot. Working backward from an actual survivability target
instead of a "does this feel weighty" gut check: the plan calls for
Byzantine to field roughly **12-15 Garrison HP at game start plus 20-30
more via Reinforce** (§4.1, ~32-45 total capacity) across an expected
**20-25 Assaults over the full game**, and to be a real but winnable
challenge the Byzantine player should be able to hold off **at least
20** of those. That means average Garrison damage per Assault needs to
land around **1.5-2.5**, not the 0.5-6.7 range the doubled table
produced — a single roll in the 4:1+ column was averaging 6.7 Defender
steps lost, enough to gut an entire sector's committed defense (capped
at 4 units, §6.3 — realistically 5-8 steps total even fully loaded with
multi-step units) in one hit. That's also out of scale with the
committed-force sizes implied by the caps themselves: a maxed attacker
commitment (5 units, mostly 1-2 steps each) tops out around **10
steps**, a maxed defender commitment (4 units) around **5-8** — the
CRT's per-roll output should read as chipping into forces that size, not
erasing them outright.

The fix: every cell below is **half the 2026-07-11 table**, rounded,
with Attacker loss floored at 1 (a won assault roll should always cost
the attacker something) and Defender loss allowed down to 0 at bad
ratios. This preserves the exact same shape — bad ratio still punishes
the attacker hardest, good ratio still punishes the defender hardest —
just at a scale where a sector can actually absorb several Assaults
before Garrison Strength runs out, rather than dying to one or two lucky
rolls at high ratio.

| Roll | 1:2 or worse | 3:4 | 1:1 | 3:2 | 2:1 | 3:1 | 4:1+ |
|---|---|---|---|---|---|---|---|
| 1 | Atk-2/Def-0 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 |
| 2 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 |
| 3 | Atk-2/Def-0 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 |
| 4 | Atk-2/Def-0 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 |
| 5 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 |
| 6 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-4 |
| 7 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-4 |
| 8 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-4 | Atk-1/Def-4 |
| 9 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-4 | Atk-1/Def-4 | Atk-1/Def-5 |
| 10 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-4 | Atk-1/Def-5 | Atk-1/Def-5 |

Whenever Attacker steps lost ≥ 1 (every roll): Ottoman Draw Track steps
down (§4.0, wasted materiel = fewer cards next round), small Morale hit
(doubled per the Elite Casualty Morale Surcharge, §6.3). Whenever
Defender steps lost ≥ 1: Garrison Strength drops accordingly, and check
for Sector Falls per the rule above.

Average steps lost per roll, this table:

| Column | Avg Atk | Avg Def |
|---|---|---|
| 1:2 or worse | 1.5 | 0.5 |
| 3:4 | 1.2 | 1.1 |
| 1:1 | 1.1 | 1.4 |
| 3:2 | 1.0 | 1.9 |
| 2:1 | 1.0 | 2.6 |
| 3:1 | 1.0 | 3.1 |
| 4:1+ | 1.0 | 3.6 |

Same shape as before — bad ratio still punishes the attacker hardest,
good ratio still punishes the defender hardest, and it should still take
several rounds of Bombard grinding a sector from Intact (Wall Defense 6)
to Contested (3) to Breached (1) before Assault odds are actually worth
taking. The top end (4:1+, best roll) now caps at Def-5 instead of
Def-10 — still enough to meaningfully hurt an under-garrisoned sector,
but no longer able to erase one outright in a single blow, which was the
core "dying too fast" problem this pass fixes. Against a 12-15 initial +
20-30 reinforced Garrison pool (§4.1) and an expected 20-25 Assaults
across the game, a defender who keeps Wall Defense maintained (via
Repair, keeping ratios out of the 3:1/4:1+ columns as long as possible)
should clear the "hold off at least 20 Assaults" bar comfortably; a
defender who lets a sector go untended into repeated high-ratio Assaults
will still lose it, which is the intended risk/reward. All values are a
first-draft placeholder pending playtesting, and this interacts directly
with whatever Initial Garrison and Reserve Pool numbers end up being
(§4.1) — those need tuning together, not independently.

## 7. Next Steps (pending your input)

1. Event Deck card list — [EVENT_DECK.md](EVENT_DECK.md): Ottoman pile
   currently 29 cards, Byzantine 28, Neutral 27 (including 17 dual-use
   alt-history cards) — deliberately over-provisioned; user intends to
   skim down to a clean per-round draw number — no fixed target for now
   per user direction (2026-07-10); trim to a clean per-round draw number
   later if desired. A pile-alignment bug was fixed this pass: a
   designated-pile card is dead weight if its Event only ever hurts its
   own owner (a rational player would never choose it over Ops) — cards
   were re-sorted by who benefits, not by whose historical agency
   triggered them. Ops values resolved too (1-3, weighted toward 2) —
   closes the open question from §2.2. Note: §2.2 specifies 3-4
   designated draws/round, not a flat 3 — needs either a flat-3 draw
   rule or a reshuffle fallback once pile sizes are finalized, flagged in
   EVENT_DECK.md's Open Questions. A new [Forced] tag (11 cards so far)
   marks fixed historical beats that must be played as Event the moment
   they're drawn, rather than optional Event-or-Ops choices — the
   mechanical interaction with Phase B's alternating mini-turn sequence
   (§2.2) still needs to be nailed down, see EVENT_DECK.md's Open
   Questions.
2. ~~Decide the specific mechanical consequence of losing Constantine XI~~
   — resolved by "The Emperor Falls" in EVENT_DECK.md (Ottoman pile):
   losing him costs -1 Wall Defense at every sector for the rest of the
   game. Still needs playtesting to confirm that malus is the right size.
3. Playtest interaction of Giustiniani's First Strike and Mehmed's
   Combined Arms with the CRT (§6.2) — both are new modifiers layered on
   top of an already-tuned table and could shift the odds more than
   intended.
4. **Sue for Aid, Reserve Pool cap, and Reinforce conversion rate were
   proposed in conversation but not yet written into this file** —
   pending confirmation: Sue for Aid costs 2 Ops, roll 1d10, 8+ (lowered
   by relevant bonus cards, floor 5+) grants Reserve Pool +1, auto-fails
   if negated by an Ottoman card; Reserve Pool hard-capped at its
   starting value (now **20-30**, §4.1, up from the old flat 20 — overflow
   wasted) to fix the "too generous" cumulative-bonus-card problem
   identified 2026-07-10; 1 Reserve Pool token = 1 militia-equivalent unit
   fielded via Reinforce (1-for-1).
6. Tune placeholder numbers via playtesting: bombard slot count (3 vs 4)
   and doubling cost, Reserve Pool size (20-30) and per-action token
   cost, HP-band thresholds, force commitment caps (5/4, §6.3), the
   mutual-damage CRT (§6.5), and unit token pool sizes (§6.1 — large
   pools for Bashi-bazouk/Azap/Janissary, small capped pools for Genoese
   Company (2-3), Cretan Sailor (1), and Solak (2)).
7. Full Ops-value rebalancing pass against the new 1-5 scale (§2.4) —
   only a representative sample of pivotal cards has been rescaled so
   far, see EVENT_DECK.md's Open Questions.
8. Generic action cards now have actual card content in EVENT_DECK.md —
   4 types now (Attack, Supplies, Move, Guile — added §2.3), 30 cards
   total. Still open: the draw mechanism doesn't yet guarantee the
   intended "mostly generic" split per round from a single shuffled
   pool — needs either two sub-decks or a higher generic:named ratio,
   flagged in EVENT_DECK.md's Open Questions.
9. Nail down [Forced] card timing relative to Phase B's alternating
   mini-turn sequence, and the [Forced] + [Requires: X] interaction —
   both flagged in EVENT_DECK.md's Open Questions.
10. **Initial Garrison (added 2026-07-10, §4.1)** — proposed but not
    confirmed: **12-15 total** (2 Roman militia per land sector = 10,
    plus Giustiniani's Genoese Company + 1-2 Venetian Marines), deployed
    at game start and entirely separate from the 20-30-token Reserve
    Pool. This was the missing number behind the "is the Reserve Pool
    enough" question — needs confirming, then a real playtest to
    validate the ~32-45 total capacity / 20-Assault-survival target it's
    meant to cover (§4.1, resized alongside the CRT halving in this same
    session's pass, §6.5).
11. Confirm the "Pressure to Attack" rule (§2.2, Morale -1 if the Ottoman
    player makes zero Assault attempts from round 2 onward) plays well in
    practice — in particular whether "send one cheap unit at bad odds"
    becomes a rote, un-interesting ritual rather than a real decision.
12. ~~Ottoman Resources as a 35-point numeric track~~ — **superseded
    2026-07-11.** The numeric Resources track was removed entirely and
    replaced by the card economy (§4.0): a Draw Track sets Ottoman cards
    drawn per round, costs are paid by discarding cards, drains step the
    Draw Track down, and Morale is now the sole hard-loss track. This
    resolved the Resources/Morale overlap the user flagged. **Pending
    conversion work this created:** every EVENT_DECK.md card that
    references "Ottoman Resources ±N" (Plague in the Camp, Tribute Demand,
    Powder Shipment Arrives, Coco's Raid, The Chain Holds, The Four Ships,
    Orban's Offer, Hunyadi's Truce, Whispers of Betrayal, etc.) needs
    re-pointing to Draw Track steps up/down — a mechanical find-and-fix
    pass, not a redesign, but not yet done.
13. **Draw Track numbers to pin down** (§4.0): starting value (placeholder
    6), range (2-8), Byzantine flat Neutral draw (placeholder 5), and the
    re-tuned card-discard costs in §4.0.1-4.0.3 (which aren't 1:1 with the
    old Resource-point numbers). Also decide whether a naval raid / failed
    assault steps the Draw Track down by 1 or more.
14. Dual-Use cards in EVENT_DECK.md now tagged [Historical] /
    [Unhistorical] / [Generic] per branch — see EVENT_DECK.md's Open
    Questions for the full breakdown and the Galata's Choice edge case
    (both branches unhistorical, since the real outcome was neutrality
    holding and nothing happening).
15. **CRT rebuilt again 2026-07-11 — bigger numbers, Sector Falls
    restructured.** Roughly doubled every step-loss value (§6.5) — the
    old table, spread across ~20 assaults/game, landed only 20-30 total
    damage, too little for both sides. Also **removed Sector Falls as a
    CRT category entirely** — it's now a derived state: Wall Defense is
    purely a combat modifier (shapes the ratio via Bombard), and a
    sector falls the instant its Garrison Strength hits 0 from
    accumulated Assault damage, regardless of roll or wall HP band. This
    removes the old "impossible below 2:1" hard-coded floor — the only
    protection now is genuinely keeping Wall Defense and Garrison
    Strength maintained. **This interacts directly with Initial Garrison
    and Reserve Pool sizing (§4.1, still placeholder)** — the bigger CRT
    numbers mean a thinly-garrisoned sector can now fall in very few
    hits, so those numbers need tuning together, not independently, once
    real playtesting starts. ~~Superseded by item 16.~~
16. **CRT halved back down, new session (2026-07-10) — item 15's
    doubling overshot.** Explicit survivability target this time instead
    of a gut check: Byzantine Initial Garrison + Reserve Pool sized to
    **~32-45 total** (§4.1, now 12-15 + 20-30), expected **20-25
    Assaults** over the game, Byzantine should hold off **at least 20**.
    Every CRT cell (§6.5) is now half of item 15's table, floored so a
    won Assault always costs the Attacker at least 1 step. Top-end
    Defender loss dropped from 9-10 (could one-shot a sector's entire
    committed defense) to 4-5. Sector-Falls-as-derived-state from item
    15 is unchanged, just operating on smaller per-hit numbers now.
    Still first-draft/placeholder pending real playtesting, but the CRT
    and the Garrison capacity numbers are now sized against each other on
    purpose (see the survivability check in §4.1 and the rationale in
    §6.5) rather than one being tuned first and the other backed in.
