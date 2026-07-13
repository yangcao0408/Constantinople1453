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
  game). Each round, players are dealt a hand of **10-11 cards (Ottoman)
  / 9 cards (Byzantine)** — revised this session, up from the earlier
  8-9 placeholder; full breakdown and rationale in §4.0.
- Players alternate playing cards for up to **7 mini-turns**, ending early
  if either side runs out of cards. Each card is usable for **either**:
  - its **Event** text (one-shot historical effect — weather, disease,
    Genoese blockade-runners, Hungarian envoy, janissary unrest, Orban's
    cannon arriving, the Golden Horn Manoeuvre, Coco's Raid, etc.), or
  - its **Ops value** (spend as generic points on the actions below).
- **Card Carryover (new this session):** hands are no longer strictly
  use-it-or-lose-it. At end of round, each player may **keep up to 3
  unused cards**, carried into next round's hand on top of that round's
  normal draw (§4.0); anything beyond 3 is discarded as before. This lets
  a player deliberately bank toward something specific — holding back
  for a pivotal 5-Ops card's Ops value, stockpiling before a Second
  Barrage or an all-in elite Assault — rather than being forced to spend
  or lose everything every single round. The cap (3) is deliberately
  small relative to the new hand sizes (10-11 / 9) so it enables genuine
  planning without letting either side stockpile a war chest that trivializes
  a later round; applies symmetrically to both sides.
- **Reshuffle Rule (new this session — resolves the open "how does
  reshuffling actually work" question):** applies to all three piles
  (Ottoman, Byzantine, Neutral), standard CDG convention:
  - **A named/Event card whose Event text is triggered is removed from
    the game permanently** — it never returns to its pile, reshuffled or
    otherwise. This matches how the deck already treats most pivotal
    cards ("unique," "Forced") and generalizes it: a historical beat that
    actually happened shouldn't be drawable and re-triggered a second
    time, whether or not it happened to be tagged unique.
  - **Everything else discarded — a card spent for its Ops value, a
    named card never played as its Event, or a generic Attack/Supplies/
    Move/Guile card (§2.3) spent on any Ops action — goes to that pile's
    discard stack, which reshuffles back into the draw pile once it's
    exhausted.** Generic cards in particular have no Event text to use
    up, so they always cycle this way — a fixed pool of ~30 that
    recirculates all game, exactly as intended (EVENT_DECK.md's Generic
    Action Cards section).
  - Net effect: each pile's *named* card count only ever shrinks over the
    game (as Events get triggered and permanently removed), while the
    *generic* cards remain a stable, renewable resource throughout — so
    a late-game hand skews harder toward whatever named cards are left
    unplayed plus a steady generic-card floor, rather than a pile that
    either runs dry or keeps re-offering already-resolved history.
- Ops actions (spendable by either side, gated by role):
  - **Ottoman:** Assault a wall sector (also usable here outside the
    concentration-bonus trigger in Phase A), Sap/mine, Muster
    reinforcements, Diplomacy (pressure Genoese/Venetians to stay
    neutral). Bombard itself is a Phase A action, not a Card Phase Ops
    action.
  - **Byzantine:** Repair a wall sector, Reinforce a sector (spend Reserve
    Pool tokens, §4.1), Sortie (raid to disrupt/destroy Ottoman cannon —
    steps the Ottoman Draw Track down, §4.0), Sue for Aid (advance the
    Powers Stirring track — the West's stirring forces the Ottoman to
    hedge; filling it permanently steps the Draw Track down and forces
    the Sultan toward a rushed assault, §4.0.5), Fire-ship raid (Coco's Raid —
    contest an unlocked Golden Horn, and on success also steps the
    Ottoman Draw Track down for ships lost/damaged, same logic as Sortie
    — Byzantine naval/raid actions should generally cut into the Ottoman
    card economy when they succeed, not just move Byzantine-side tracks).
- End-of-round bookkeeping: track adjustments, reserve/resource upkeep.
- **Each Ops action costs 2 Ops points** to perform (Assault, Repair,
  Reinforce, Sortie, Sap/Mine, Sue for Aid, Diplomacy, Muster
  Reinforcements — every entry in the lists above).
- **Pressure to Attack (added 2026-07-10):** starting **round 2**, if the
  Ottoman player makes fewer than the **required number of Assault
  attempts** this round (Phase A concentration-bonus assault or Phase B
  Ops) — **base requirement: 1** — Morale **-1** — the Sultan's court and
  army expect visible progress, and a round of pure bombardment with no
  follow-through reads as hesitation. This exists to rule out a degenerate
  "bombard forever, never risk an assault" strategy. It works even this
  early, before the walls are properly softened (§3.1, real damage
  doesn't usually start until round 3-4), because the rebalanced CRT
  (§6.5) makes a cheap, disposable "probing" assault — a single
  Bashi-bazouk thrown at bad odds — genuinely low-risk for the attacker
  and low-cost for the defender. The rational response to this rule most
  rounds should be exactly that: a token assault to avoid the Morale
  penalty, not a real commitment, which is itself decent siege flavor
  (constant skirmishing pressure alongside the main bombardment).
  - **Halil Pasha's Doubt** (EVENT_DECK.md, Byzantine pile, revised this
    session) deals an immediate **Morale -1**, and permanently raises
    this requirement by **+1**, starting the round after it's played, for
    the rest of the game — turning the "one token assault is enough"
    baseline into "two real Assault attempts required," which costs the
    Ottoman more committed troops (and, via the Elite Casualty pool
    §4.0.4, more exposure to Morale loss from it) than a single cheap
    probe would. One of the strongest Byzantine cards in the deck for
    exactly this reason — a direct hit plus a permanent structural
    squeeze. Played early, the requirement change compounds over more
    remaining rounds, which is the intended incentive to play it early
    rather than bank it.

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
| ≤ 1/2 max | **Battered** | **3** — a real, if risky, attack option |
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
  garrison, roughly equivalent to a permanently-Battered land wall. This
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

- **Draw Track (rebased this session — buffed):** a small track setting
  the Ottoman player's per-round Neutral-pile draw. **Starts at 7**
  (placeholder, up from 6), range **3-10** (up from 2-8, same
  ±proportional spread around the new baseline). Combined with a flat
  **3 cards/round from the Ottoman designated pile** (down slightly from
  the earlier 3-4 fuzz, for clean math), total Ottoman hand is
  **10-11 cards/round** — matching the Draw Track's normal 7-8 range
  plus 3, not counting event-driven spikes either direction.
- **Byzantine draw (rebased this session):** flat **6 cards/round from
  the Neutral pile** (up from the earlier placeholder of 5) plus a flat
  **3 cards/round from the Byzantine designated pile**, for a **flat 9
  cards/round total** — no Draw-Track-equivalent fluctuation on the
  Byzantine side, since their resource constraint is the Reserve Pool
  (§4.1), not card supply.
- **Why buff the draw rate now:** this session tightened Ottoman
  spending substantially — Mustering Cost retuned tighter across every
  tier (§4.0.1), Janissary/Solak muster removed entirely in favor of a
  mandatory New Levy pipeline, the Elite Casualty pool and Halil Pasha's
  Doubt both push toward committing (and losing) more troops. Raising
  the *draw* side loosens the faucet enough that the Ottoman player has
  something to spend on all that new friction, rather than compounding a
  tighter economy on both ends of the same round. The Ottoman:Byzantine
  gap (10-11 vs 9) is intentionally modest — still reflects real material
  superiority (§1's High-Concept) without making raw card count itself
  the deciding factor.
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

#### 4.0.5 Sue for Aid & the Powers Stirring Track (revised 2026-07-13)

The Byzantine **Sue for Aid** Ops action — the city's appeals to Venice,
Genoa, the Pope, Hungary, and the Karamanids — feeds a single persistent
**Powers Stirring track** (0 → 4 steps) rather than granting an immediate
resource. This is the defender's mirror of the Ottoman-side persistent
Draw Track shifts described in §4.0: it is the **only** tool by which the
Byzantine player can force a *permanent* change in the Ottoman baseline,
and it is deliberately slow and contestable.

- **The action:** Sue for Aid costs **2 Ops** (§2.2). Roll **1d10**:
  - **6+** — advance the Powers Stirring marker **1 step** (a strong
    result of **9–10** advances **2 steps**).
  - **5 or less** — no progress this attempt.
  - Modifiers from event cards (below) add or subtract from the roll, or
    move the marker directly.
- **Filling the track (marker reaches 4) — "The Powers Stir":** a
  one-time swing that resolves immediately, then the marker **resets to 0**
  and can be built again:
  - **Permanent Draw Track −1** for the rest of the game (a pasha and his
    corps are detached to watch the frontier — the same fiction the
    Karamanid Rising / Skanderbeg's Revolt recall cards deliver, but
    player-driven). This is a genuine persistent shift per §4.0, not a
    one-shot discard.
  - **Pressure to Attack requirement +1** (§2.2) — fear that relief is
    finally coming forces the Sultan to force the pace and throw more
    weight at the walls sooner, exactly as Mehmed did historically. This
    stacks with Halil Pasha's Doubt if both land.
- **Why a track, not a dice-roll-for-a-token:** the earlier proposal
  (2 Ops → 8+ → Reserve Pool +1) was strictly dominated by Reinforce
  (same cost, guaranteed board presence) and paid in the scarce Guile
  type — no rational player took it. Routing it into a persistent Draw
  Track squeeze makes it the defender's only proactive win-race clock,
  distinct *in kind* from the one-shot Draw Track hits of Sortie/Fire-ship
  (§2.2), and it gives the Ottoman blockade cards a real objective to
  contest instead of a marginal action to swat.
- **Cards that interact with the track** (full text in EVENT_DECK.md):
  - *Boosters:* Hungarian Envoy (+1 to the advance roll this round), The
    Winds Shift / Byzantine branch (+1), Rumors of a Relief Fleet
    (advance the marker 1 step directly).
  - *Suppressors:* Rumeli Fort, the Throat-Cutter (−1 to every advance
    roll for the rest of the game), Hunyadi's Truce / Ottoman branch and
    Intercepted Dispatch / Ottoman branch (each knocks the marker **back
    1 step** — the two stacking is now fine: it costs the Byzantine tempo
    rather than bricking the action outright).
  - *Finality:* The Scout Ship's Return (Byzantine, Round 7+, Forced)
    **freezes the marker permanently** where it stands — no further
    advances, hope of relief is dead — alongside its Reserve Pool +1.

#### 4.0.1 Mustering Cost (per unit fielded, §6.1)

Paid in **discarded cards** now, not Resource points, but the same tiered
escalation — cheap irregulars barely dent your hand, elite troops are a
real spend of your options:

| Unit | Cost | Change |
|---|---|---|
| Bashi-bazouk | 3 units per 1 card | was Free — closes the "literally unlimited free units" case |
| Azap | 1 unit per 1 card | was 4 units per 1 card |
| New Levy Janissary | 1 unit per 1 card | was 2 units per 1 card |
| New Levy Janissary → Janissary (upgrade) | 1 card per unit upgraded | the *only* way to field a Janissary now |
| Janissary (fresh muster) | **removed** | no longer musterable directly — must be upgraded from New Levy |
| Solak | **removed** | no longer musterable at all — see note below |
| **Replenish** (Janissary or Solak, new) | 1 card per unit restored | restores a *flipped* (damaged, not destroyed) Janissary or Solak back to full step count |

**Replenish, added this session:** without this, a Janissary or Solak
that's taken one hit (flipped to its reduced face, per §6.1's multi-step
rule) just sits there permanently weakened for the rest of the game —
there was no way back to full strength short of losing the unit outright
and re-earning a replacement through the upgrade pipeline from scratch.
Replenish fixes that: pay 1 discarded card (via Muster Reinforcements,
§2.2) to restore a flipped Janissary or Solak to full step count,
representing reinforcement drafts backfilling a bloodied but intact
formation rather than raising a fresh one. Deliberately cheaper than the
New Levy → Janissary upgrade path would cost from scratch (1 card here
vs. 1 card to muster New Levy + 1 more to upgrade) — repairing a unit
you already have should be more efficient than replacing it.

**Retuned this session, second pass** (previous ratios were an
unre-tuned placeholder carried over 1:1 from the old Resource-point
numbers, never actually checked against typical hand size). Every tier
is tighter than the original draft — Bashi-bazouk stops being a literal
zero-cost unlimited resource, Azap drops from 4-per-card to 1-per-card
(a 4x tightening), New Levy Janissary is now 1-per-card (was 2) — and,
this pass, **Janissary can no longer be mustered fresh at all**. The
training pipeline is now mandatory, not just cheaper: muster New Levy
(1 card/unit) first, then spend 1 more card to upgrade a fielded New
Levy into a full Janissary. No more paying a premium to skip the queue —
there is no queue-skip anymore, which makes the New Levy stage a real
bottleneck the Ottoman player has to plan around rather than an optional
discount path.

**Solak has no mustering path at all (removed this pass)** — resolves
the price-compression flag from last pass by removing the comparison
entirely rather than re-pricing it. Given the flavor already on record
(§6.1: "the Sultan's own personal bodyguard," a hard-capped pool of 2),
it makes more sense for Solak not to be a wartime recruit in the first
place: **both Solak tokens should be available to the Ottoman player
from game start** (or via a specific named Event card, if you'd rather
gate them behind something drawn mid-game) rather than something raised
mid-siege through the same card economy as everyone else. This still
needs a decision — pre-deployed at start, or event-gated — but either
way it's no longer part of this table. Flagging this choice in §7.

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
  keep the siege going against court opposition) — **track runs 0-7,
  starting at 7 (full strength), hard-capped at 7 (overflow from gain
  cards is wasted).**
- **Morale gain now comes from a single named card in the whole deck**
  (EVENT_DECK.md, revised this session): **The Hadith of Conquest (+1,
  round 1-2)** — max **+1** across a full game. No other source of Morale
  gain exists. (The War Council previously granted the second +1; that was
  removed when the card was repurposed to a permanent Force Commitment Cap
  boost, §6.3. Baltaoğlu's Punishment had earlier been cut from the gain
  list too — a public scapegoating doesn't actually put fight back in the
  army, so it's now a pure card-draw effect instead.)
- **Morale loss**, current confirmed sources:
  - Named/event cards: **The Four Ships (-2, unique, round-limited)**,
    **Halil Pasha's Doubt (-1, immediate, one-time)**.
  - **The Pressure to Attack rule** (§2.2): -1/round from round 2+ if the
    Ottoman makes fewer than the required number of Assault attempts
    (base requirement 1, permanently raised to 2 for the rest of the game
    by **Halil Pasha's Doubt**, on top of its immediate -1 above — see
    §2.2). That card is deliberately one of the strongest in the
    Byzantine pile for combining both: a direct Morale hit now, plus a
    structural squeeze that forces more Assault commitments (and more
    exposure to the Elite Casualty pool below) for the rest of the game.
  - **The Elite Casualty pool (confirmed this session, replaces the old
    per-Assault "small Morale hit" and the §6.3 Elite Casualty Morale
    Surcharge language):** track a running total of Attack value from
    **New Levy Janissary, Janissary, and Solak units fully destroyed**
    (matching the exemption list in §6.3 — only Bashi-bazouk and Azap
    never contribute, win or lose). New Levy Janissary destroyed = +2 to
    the pool, Janissary destroyed = +3, Solak destroyed = +4. Cumulative for the whole game, never
    resets. **Morale -1 every time the running total crosses another
    multiple of 5** (i.e., total Morale lost from this source at any
    point = floor(pool / 5)). Only works as a real pressure because of
    **§6.3.1**: the Byzantine player, not the Ottoman, chooses which
    committed Ottoman unit absorbs each lost step, so elites can't be
    routinely shielded behind cheap troops. Threshold lowered from an
    earlier draft of 10 once that fix made the pool fill up under
    realistic play — see the estimate below.
- **Morale hitting 0 → the Ottoman army lifts the siege → immediate
  Byzantine win.** This is the sole hard-loss track for the Ottoman side.
  Note this isn't the *only* way Byzantine wins — reaching round 9/10
  with no sector lost is an automatic Byzantine win regardless of Morale
  (§5) — so Morale running out under sustained pressure late in the game
  is a legitimate, expected outcome, not a sign the track is broken.

**Morale bands (graduated debuffs, added 2026-07-13):** below full
strength the army's flagging will shows up as *fewer options*, never as a
direct combat nerf — deliberately. Because Morale can no longer be
regained mid-game (gain is Hadith-only, round 1-2, §4.0.4 above) and its
main drain is combat losses, a debuff that weakened Assaults directly
would create a death spiral (weaker Assault → more elite casualties →
lower Morale → weaker Assault still) with no way back out, and would also
awkwardly cancel The War Council's permanent Force Commitment Cap boost
(§6.3). The bands throttle the card economy instead, which the Ottoman
player can absorb and play around:

| Morale | Debuff | Flavor |
|---|---|---|
| **5–7** | none | army confident |
| **3–4** | draw **1 fewer** card from the Neutral pile each round while Morale sits in this band | war effort flags, fewer options |
| **1–2** | draw **2 fewer** cards from the Neutral pile each round while Morale sits in this band | the push is faltering |
| **0** | siege lifted → immediate Byzantine win | Halil's faction prevails |

These are *conditional hand-size reductions applied while Morale is in the
band* (the "immediate hand-size effect" case of §4.0), **not** permanent
Draw Track step-downs — so they lift again if Morale climbs back into a
higher band, and they don't compound destructively with the Draw Track's
own value or its combat attrition (§6.5). At the normal Draw Track of 7–8,
−1 / −2 trims total hand (including the flat 3 from the designated pile)
from ~10–11 down to ~9–10 / ~8–9 — a real pinch, not a crippling one. The
hard 0-loss is what actually carries the tension; these two soft bands are
texture, sized gently on purpose since the track is a one-way ratchet
after round 2.

**Design rationale, decided this session (2026-07-10):** the Elite
Casualty pool is now Morale's primary drain, in place of the flat
time-decay idea considered earlier (Morale -1 every 2 rounds,
unconditional). Reasoning: the round-limit auto-win at round 9/10 above
already supplies the "hurry up, clock's ticking" pressure on the Ottoman
player, so a second, unconditional Morale timer stacked on top would
have been redundant. The casualty pool does different, more specific
work instead — it ties Morale directly to *how hard the Ottoman commits
real troops*, which is exactly the lever Halil Pasha's Doubt now pushes
on by forcing more Assault attempts per round. A passive Ottoman who
mostly probes with exempt cheap troops barely touches this pool, but
that Ottoman also isn't threatening any sector and will lose to the
round limit anyway (§5) — so nothing is exploitable, it's just a
narrower, more particular role for Morale than pure time-decay would
have given it: not a doom clock in its own right, but a real, felt cost
for leaning on Janissaries and Solaks to press the attack.

**Track size confirmed this session: 0-7, starting at 7.** Against the
+1 max from a named card (Hadith of Conquest) and the
drains above (Four Ships -2, Halil Pasha's Doubt -1 plus its structural
squeeze, the Elite Casualty pool's -1-per-5 ticks, and occasional
Pressure to Attack penalties), a full 7-point swing is crossable but not
trivial over 9-10 rounds — still first-draft pending playtesting, but no
longer an open question.

**Elite Casualty pool sizing estimate (this session):** with §6.3.1's
defender-assigns-losses fix in place, elites can no longer be reliably
shielded, so a full-game pool of roughly **14-21 Attack-value points**
(a handful of Janissary/Solak kills across the back-half of the game, at
3-4 points each) is a realistic estimate for an Ottoman player who
commits elites when they actually need the damage. **New Levy Janissary
kills now also feed the pool at +2 each (added this session)**, which
pushes the realistic total somewhat above this range and warrants a
re-estimate in playtesting. At the **new
threshold of 5** (lowered from an earlier draft of 10), that's **2-4
Morale ticks from this source alone** — a meaningful fraction of the
7-point track, not just a footnote, which was the point of lowering it.
§6.3's Elite Casualty Morale Surcharge text has been updated to match
this (the pool above replaces that old per-Assault doubling mechanic
entirely).

### 4.1 Byzantine Track — Reserve Pool

Resolves the open question above: Byzantines get one shared track, the
**Reserve Pool**, sized **20-30 tokens** (revised this session, up from
a flat 20 — see the survivability check below for why).

- Per-sector Garrison Strength (§3.1) is where troops actually sit and
  fight; the Reserve Pool is the finite well that feeds it. Every time the
  Byzantine player Reinforces a sector or fields new units (via Ops or
  event), a token comes off the Reserve Pool — mirroring Ottoman
  Resources as the "can we even afford this action" constraint.
- The pool has **no graduated depletion penalties** — considered and set
  aside for now (2026-07-13). Running low simply means fewer tokens on
  hand to spend; there are no debuff bands layered on top of that. The
  only hard threshold is empty (below). (The Ottoman Morale track, by
  contrast, *does* keep its graduated bands, §4.0.4 — that track is a hard
  loss condition, so texturing its decline earns its keep; the Reserve
  Pool isn't a loss track, so plain depletion is pressure enough.)
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
  but realistically only likely once a land sector is Battered/Breached
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

| Unit | Side | Attack | Defense | Steps | Pool | Notes |
|---|---|---|---|---|---|---|
| Bashi-bazouk | Ottoman | 1 | — | 1 (removed on hit) | large | Unpaid, loot-driven volunteers, historically thrown in as the expendable first wave to draw and exhaust defensive fire. **Free of the Elite Casualty Morale Surcharge** (§6.3) — losing them costs Mehmed nothing politically |
| Azap | Ottoman | 2 | — | 1 (removed on hit) | large | Paid irregular infantry, the second wave — disciplined enough to hit harder than Bashi-bazouks, but still not a standing corps |
| New Levy Janissary | Ottoman | 2 | — | **2** | muster pool | Recently-conscripted Janissaries, not yet campaign-hardened — tougher than any irregular (part of the standing corps' training pipeline) but not yet worth the full political weight of a veteran; **contributes +2 (its Attack value) to the Elite Casualty pool when fully destroyed** (§6.3, §4.0.4) |
| Janissary | Ottoman | 3 | — | **2** | large (via upgrade) | Elite standing corps, held back for the decisive wave — full Elite Casualty Morale Surcharge and Mustering Cost apply (§6.3) |
| Solak | Ottoman | 4 | — | **2** | **2 (cap)** | The Sultan's own personal bodyguard archers — small token cap (2), the single best Ottoman unit; full Elite Casualty Morale Surcharge and Mustering Cost apply (§6.3) |
| Imperial Guard | Byzantine | 2 | 2 | 1 (removed on hit) | **2** | Constantine's small household / professional Greek core — the best *native* troops left, but too few to form a standing elite corps (no native elite survived to 1453); punchy but fragile at 1-step |
| Roman militia | Byzantine | 1 | 1 | 1 (removed on hit) | 20–30 (Reserve Pool) | Native levies; scarcity handled by quantity via the Reserve Pool (§4.1), not by a stronger stat |
| Clergy Levy | Byzantine | 0 | 1 | 1 (removed on hit) | **2** | Monks, clergy and civilians pressed to the walls — no offensive/sortie capability (Atk 0), just a defending body on the rampart |
| Genoese Company (Giustiniani's) | Byzantine | 2 | 3 | **2** | **2** | Giustiniani's own professional condottieri (~700 men historically) — the best troops in the city; irreplaceable (no muster path for foreign elites) |
| Venetian Marines | Byzantine | 1 | 2 | 1 | **2** | Crews/soldiers off Minotto's ships — semi-professional mid-tier; their greater numbers show up as a slightly larger pool, not more steps (mirrors the Ottoman Azap tier) |
| Cretan Sailors | Byzantine | 1 | 2 | **2** | **1** | Single tenacious token — historically fought on for days after the city itself had fallen; the 2-step is a legend/tenacity reward, not a numbers claim |
| Isidore's Legation | Byzantine | 1 | 2 | 1 (removed on hit) | **1** | Cardinal Isidore of Kiev's ~200-man papal legation — a small, symbolic Western-Church contingent; single token, no step reduction (too small a company for a meaningful "reduced" state). Def lowered 3→2 this session — a couple hundred hired archers shouldn't defend on par with Giustiniani's condottieri |
| Orhan's Loyalists | Byzantine (allied) | 2 | 2 | **2** | **1** | ~600 exiled followers of the Ottoman pretender Orhan Çelebi, fighting to the death (Orhan was executed after the fall); held part of the Golden Horn sea wall. Genoese-sized (~600 vs ~700) so a resilient 2-step is justified, but one notch below in Defense — loyal ex-prisoners, not professional condottieri |

Multi-step units (New Levy Janissary, Janissary, Solak, Genoese Company,
Cretan Sailors, Orhan's Loyalists) take a hit, flip to a reduced/spent
face, and are only removed on a second hit — the mechanic is identical on
both sides (per your steer: symmetric rule, asymmetric quantity is where
the real imbalance should live). The actual difficulty gap between the two
armies comes from how many tokens of each type exist in the pools.

**Reduced-face principle (set this session):** a flipped **Byzantine**
multi-step unit **keeps its full Defense but loses Attack** — a bloodied
company still mans the wall as well, it just can't sally as hard. So
Giustiniani's Company flips **2/3 → 1/3** (Def 3 held; historically the
Genoese held defensively until Giustiniani himself was wounded, so the
sector's collapse should come from losing the *leader*, not from the unit
degrading) and Orhan's Loyalists **2/2 → 1/2**. The **Cretan Sailors are
the deliberate exception — 1/2 → 1/2, no degradation at all**: their 2-step
is pure staying power, embodying the historical Cretans who fought on
undiminished from their towers even after the city had fallen. (Ottoman
units carry no Defense stat, so their reduced faces simply drop Attack:
Janissary 3→2, Solak 4→3, New Levy 2→1.)

**Byzantine pool sizes are now set (this session)** — see the Pool column
above. The good troops are painfully few: Imperial Guard ×2, Genoese
Company ×2, Venetian Marines ×2, Clergy Levy ×2, and only a **single**
Cretan, Isidore, and Orhan token each, with Roman militia supplied via the
**20–30 Reserve Pool** (§4.1). The named/fixed contingents total ≈ **15
Garrison steps** (the Initial Garrison), which with the Reserve Pool lands
the whole defence at ≈ **40 total capacity** — inside the 32–45 target
(§6.5). Foreign elites have **no muster path**, so a lost Genoese or Cretan
token is gone for good — the historical knife's edge that makes
Giustiniani's wounding catastrophic. **Ottoman pool sizes remain TBD (§7)**
beyond the capped Solak pool of 2 and the "large" bulk pools of
Bashi-bazouk / Azap / Janissary.

The Ottoman roster now mirrors the Byzantine one's shape: a free/expendable
base tier (Bashi-bazouk ~ Roman militia), a paid-professional middle tier
(Azap ~ Venetian Marines), and elite tiers where overcommitting carries
real political or logistical risk (Janissary/Solak ~ Genoese Company),
which is the same tension on both sides of the table by design.

**A "step" doesn't represent the same number of soldiers on both sides
(added this session)** — this is the in-fiction justification for why
the CRT (§6.5) deals such asymmetric raw numbers, an Attacker step
costing the Ottomans comparatively little while a Defender step costs
the Byzantines comparatively more. A Byzantine unit token is a genuinely
small, specific formation — Roman militia companies, Giustiniani's
~400-700 Genoese, a couple hundred Venetian marines — so one step lost
there plausibly represents on the order of **~200 men**. An Ottoman unit
token, by contrast, abstracts a much larger corps or muster (the
besieging army numbered in the tens of thousands against a defending
garrison of a few thousand at most), so one Ottoman step lost plausibly
represents something closer to **~2,000 men** — an order of magnitude
more bodies for the "same" one step on the CRT. This means the CRT's
raw Attacker-loss/Defender-loss numbers were never meant to read as
equal-weight casualties; the game already encodes the historical reality
that the Ottomans could absorb losses the Byzantines simply couldn't, on
top of (not instead of) the deliberate CRT-tuning reasons in §6.5 for
why Defender steps lost run higher than Attacker steps lost per roll.

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
- **Giustiniani**: **+3 Defense** (raised from +2 this session — the single
  best field commander in the city, the defensive anchor whose wounding
  triggered the historical collapse; his loss should be the biggest single
  swing on the board). Commands the Genoese Company only.
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
- **Theophilos Palaiologos**: **+1 Defense.** A real kinsman of the Emperor,
  a scholar-soldier who vowed he would rather die than outlive the city, and
  did. A *native* commander — commands militia without the foreign-contingent
  restriction (§6.2.1), sector-flexible. Secondary to the supreme trio, hence
  +1 rather than +2; his one-round heroic surge is the Event card **Theophilos
  Palaiologos' Vow** (+2 Defense + no-retreat, EVENT_DECK.md #21), for which
  the token is the standing presence.
- **Demetrios Kantakouzenos**: **+1 Defense.** Another imperial kinsman,
  historically posted to the **southern** stretch of the land wall near the
  Golden Gate. Native commander, same terms as Theophilos; his surge is the
  Event card **Demetrios Kantakouzenos' Stand** (+2 Defense at the Golden
  Gate / Gate of the Spring, EVENT_DECK.md #22).
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
- **Mahmud Pasha (Angelović)**: **+2 Attack** (added this session) — the
  campaign's most gifted field commander and later one of the great Ottoman
  Grand Viziers, of Byzantine/Serbian convert origin (a neat mirror to Orhan
  crossing the other way). **Flexible Command:** unlike the zone-locked
  Karaca and Ishak, Mahmud has *no* sector restriction — his +2 applies
  wherever he is committed, the roving reserve commander. He is the
  offensive counterpart to Giustiniani's +3 on the Byzantine side, and does
  not overshadow the Sultan: Mehmed still reaches an effective +3 via
  Combined Arms at a cannon-sited sector, whereas Mehmed's own *base* combat
  stays a deliberately modest +1 (his brilliance is strategic, not
  close-in).
- Between the four zone commanders (Mahmud is the mobile fifth), every zone
  of the wall now has its own
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

- **Attacker cap: 5 units per Assault** (any mix of Ottoman troops) —
  **reduced to 4 units at the Golden Horn seawall sectors (§3.2)**, where a
  shipborne escalade has far less usable frontage to land and press troops
  across than an open land breach does. **The War Council (EVENT_DECK.md
  card 25, R7+, Forced) permanently raises this cap by +1 — to 6 (5 at the
  Golden Horn) — for the rest of the game once played**, as the Sultan
  commits to the final all-out push.
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

- **Elite Casualty pool (revised this session, replaces the old
  per-Assault "doubled Morale hit" surcharge):** whenever a committed
  **New Levy Janissary, Janissary, or Solak** unit is fully destroyed (second step lost, not
  just flipped — and per §6.3.1, the Byzantine player chooses which
  committed Ottoman unit takes each lost step, so elites can't just be
  shielded by cheap troops), add its Attack value to a running, whole-game
  **Elite Casualty pool** — New Levy Janissary +2, Janissary +3, Solak +4. Bashi-bazouks
  and Azaps are exempt (§6.1) and never contribute.
  **Ottoman Morale -1 every time the pool crosses another multiple of 5**
  (lowered from 10 this session, once §6.3.1 made the pool actually fill
  up under realistic play — full mechanic and rationale in §4.0.4). This
  replaces the old "doubles the Morale hit from this Assault" wording,
  which depended on an automatic per-roll Attacker-steps-lost trigger
  that no longer exists — Janissaries and Solaks were expensive, prized,
  and politically sensitive to lose in numbers, and taking real
  casualties among veteran troops should hurt the Ottoman player far more
  than losing irregulars or green recruits, mirroring the real political
  risk Mehmed carried every time he fed his best troops into a failed
  assault; the pool now makes that cost cumulative and trackable rather
  than a per-roll multiplier.
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

### 6.3.1 Step Loss Assignment (revised this session — Byzantine chooses both)

Deliberately **asymmetric in the Byzantine player's favor**, and the
asymmetry is the point:

- **Attacker (Ottoman) steps lost are assigned by the Byzantine player.**
  This closes a real shielding exploit: with self-assignment, a
  disciplined Ottoman could always park 1-2 free Bashi-bazouks at the
  front of any committed stack and absorb every plausible loss there (the
  rescaled CRT, §6.5, never deals more than 2 Attacker steps lost in any
  column a rational player would actually fight at), meaning Janissaries
  and Solaks would effectively never die and the Elite Casualty pool
  (§6.3, §4.0.4) would sit near zero all game regardless of its
  threshold. Letting the Byzantine player choose instead means any
  Janissary or Solak present in a losing Assault is a live target the
  moment a step is lost — the defenders naturally focus fire on the
  visually-distinct elite corps — which is what actually makes committing
  them a real, felt risk every time, not just in a rare all-in stack.
- **Defender (Byzantine) steps lost are also assigned by the Byzantine
  player (changed this session — was Attacker's choice).** Letting the
  Ottoman player pick instead would create the mirror-image problem to
  the one just closed above: a rational Ottoman would simply always
  target whichever committed Byzantine unit is most valuable — Giustiniani's
  Genoese Company, Cretan Sailors — and with those pools already tiny
  (2 Genoese, 1 Cretan token, §6.1), a defender could lose an
  irreplaceable elite unit almost on demand, which isn't a real defensive
  choice so much as a forced loss. Self-assignment here is standard,
  defensible on its own terms (a commander director's their own troops'
  positioning better than an attacker outside the walls could target
  specific formations in the chaos of an escalade), and — unlike the
  Ottoman side — there's no shielding exploit to worry about, since
  Byzantine has no cumulative casualty-triggered track analogous to the
  Elite Casualty pool that self-protection could quietly neutralize.
- **Net effect:** the Byzantine player now controls both allocations —
  aiming Ottoman losses at Janissaries/Solaks to feed the Elite Casualty
  pool, while protecting their own scarce elites (Genoese Company,
  Cretan Sailors) behind militia. This is an intentional asymmetry, not
  an oversight: Byzantine is the side fighting from a fixed, dug-in
  position with much less material depth to lose from, so giving them
  the sharper tactical control on both sides of the ledger is consistent
  with the "razor-thin garrison, no reserves" framing in §1's
  High-Concept.
- **Mandatory Kill Priority (added this session, clarified — applies to
  only the first point of damage):** whichever player is assigning steps
  lost (Byzantine, per both bullets above) must spend the **first point**
  of any roll's damage completing a **confirmed kill**, if one is
  available — a 1-step unit outright, or a multi-step unit already
  flipped and one hit from destruction. Every point *after* that first
  one is freely assignable, however the assigning player likes —
  including a second confirmed kill if they want one, or "chip" damage
  that only flips a healthy multi-step unit without killing anything.
  This is a **single mandatory kill, not a chain**: the rule only
  guarantees that *if a kill is possible, at least one unit comes off the
  board this roll* — it doesn't force every available kill to be taken
  before any free assignment happens. So: **Atk-1**, with a confirmed
  kill available, must take that kill. **Atk-2**: 1 point mandatory kill,
  1 point free (enough to flip a healthy Janissary, or take a second kill
  if the player prefers). **Atk-3**: 1 point mandatory kill, **2** points
  free (e.g. flip *and* finish a Janissary in the same roll, or spread
  across other units) — the mandatory portion doesn't grow with the
  damage total, only the free portion does. This reintroduces a real,
  thematically sound way for the Ottoman player to protect elites — keep
  a cheap unit alive in the stack and it absorbs the guaranteed-kill
  portion of every roll — without fully reopening the shielding exploit
  §6.3.1 closed above, since any damage beyond the first point still
  reaches past the sacrificial unit.

### 6.4 Combat Calculation

- **Attacker Strength** = sum of committed attacking units' Attack values
  (max 5 units, or 4 at a Golden Horn seawall, §6.3) + any Ottoman leader
  bonus + event modifiers.
- **Defender Strength** = sum of committed garrison units' Defense values
  (max 4 units, §6.3) + Wall Defense (§3.1 band) or Naval Defense (§3.2,
  Golden Horn only) + Giustiniani bonus if present + event modifiers.
- Compute **Attacker : Defender**, rounded down to the nearest standard
  column: 1:2 (or worse), 3:4 (0.75), 1:1 (1.0), **4:3** (1.33), 3:2
  (1.5), 2:1 (2.0), 3:1 (3.0), 4:1+ (4.0). (Added the 3:4 column
  2026-07-11 — the jump straight from 1:2 to 1:1 was the single biggest
  gap in the ladder, and it's exactly the range a partially-softened
  wall spends a lot of time in. **Added 4:3 this session** for the same
  reason on the other side of 1:1 — the 1.0-to-1.5 gap between 1:1 and
  3:2 turned out to be exactly where a maxed-out Ottoman elite push
  lands, and rounding that whole range down to a flat 1:1 was throwing
  away a real distinction between "a decent push" and "an all-in 5-unit
  gambit." See §6.5 for the worked example that surfaced this.)
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

The fix (superseded below by this session's Def-4 cap): every cell was
**half the 2026-07-11 table**, rounded, with Attacker loss floored at 1
(a won assault roll should always cost the attacker something) and
Defender loss allowed down to 0 at bad ratios.

**Defender loss capped at 4, new session (2026-07-10) — matches the
Force Commitment Cap.** A Def-5 result never made sense once you look at
it against §6.3: the Defender cap is **4 committed units**, so a single
roll dealing 5 Garrison steps could out-damage the entire committed
defense in one blow even before accounting for the new Commander
Casualty rule below. Every cell that read Def-5 is now Def-4, and the
columns leading up to it were smoothed to match rather than just
clipping the top (avoids several rows piling up on the same top value).
**Attacker loss nudged marginally higher** in exchange, mainly at the
worst-for-attacker column (1:2 or worse) — a roll-1 there is now Atk-3
instead of Atk-2 — so the bad-ratio column still reads as genuinely
costly to a reckless Ottoman even though the defender's own ceiling came
down.

**Attacker loss nudged up again, small pass this session** — direct
consequence of the new Mandatory Kill Priority rule (§6.3.1): as long as
the Ottoman keeps one cheap unit alive in a stack, every single-point
roll (the large majority of rolls, per the survivability analysis
earlier this session) now kills that sacrificial unit *instead of*
touching a Janissary, which meaningfully lowers how often the Elite
Casualty pool actually gets fed compared to the version of the rule
without a kill-priority requirement. To compensate without changing the
table's overall shape, a few more low-roll cells in the columns combat
actually tends to land in (1:1, 3:2, 2:1, plus one more row each in 3:4
and 1:2-or-worse) now deal **Atk-2 instead of Atk-1** — enough that a
2-damage roll (1 point to the confirmed kill, 1 point free to chip a
Janissary) happens noticeably more often, keeping elite exposure real
without re-tuning the whole table. The 3:1/4:1+ columns are untouched —
they're already the reliable finishing-blow columns and don't need help.

| Roll | 1:2 or worse | 3:4 | 1:1 | 4:3 | 3:2 | 2:1 | 3:1 | 4:1+ |
|---|---|---|---|---|---|---|---|---|
| 1 | Atk-3/Def-0 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 |
| 2 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 |
| 3 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-2 |
| 4 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 |
| 5 | Atk-2/Def-0 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 |
| 6 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 |
| 7 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-3 |
| 8 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-4 |
| 9 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-4 | Atk-1/Def-4 |
| 10 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-4 | Atk-1/Def-4 | Atk-1/Def-4 |

Whenever Attacker steps lost ≥ 1 (every roll): Ottoman Draw Track steps
down (§4.0, wasted materiel = fewer cards next round), small Morale hit
(doubled per the Elite Casualty Morale Surcharge, §6.3). Whenever
Defender steps lost ≥ 1: Garrison Strength drops accordingly, and check
for Sector Falls per the rule above, **and check the Commander Casualty
rule (§6.5.1, new) if this loss fully wipes the committed defense.**

**Defender damage marginally reduced, this session** — a capacity check
rather than a gut call: the 12-15 Initial Garrison + 20-30 Reserve Pool
(§4.1) is a *whole-game aggregate across 6 sectors*, not a per-sector
war chest — keeping any single sector adequately held (call it ~15
units actually on the walls at once, spread across the line) already
ties up a meaningful share of that total, so the *effective* cushion
available to absorb combat losses is smaller than the raw 32-45 number
suggests. Every column's Defender average is down roughly 15-20% from
the previous pass (Attacker values untouched — this is specifically
about Byzantine losses, not the Ottoman's own risk from §6.5's worked
example above).

Average steps lost per roll, this table:

| Column | Avg Atk | Avg Def |
|---|---|---|
| 1:2 or worse | 1.8 | 0.5 |
| 3:4 | 1.4 | 1.0 |
| 1:1 | 1.2 | 1.3 |
| 4:3 | 1.1 | 1.7 |
| 3:2 | 1.1 | 1.9 |
| 2:1 | 1.1 | 2.3 |
| 3:1 | 1.0 | 2.7 |
| 4:1+ | 1.0 | 3.0 |

Same shape as before — bad ratio still punishes the attacker hardest,
good ratio still punishes the defender hardest, and it should still take
several rounds of Bombard grinding a sector from Intact (Wall Defense 6)
to Battered (3) to Breached (1) before Assault odds are actually worth
taking. The top end (4:1+, best roll) now caps at **Def-4**, matching
the Defender's own 4-unit commitment cap (§6.3) — enough to meaningfully
hurt an under-garrisoned sector, but no longer able to mathematically
out-damage the maximum possible committed defense in a single roll. This
also makes the new Commander Casualty rule (§6.5.1) mean something: a
total wipe now specifically requires the committed defense's *remaining*
steps to already be at or below what a single roll can deal, rather than
being trivially achievable by any lucky high-ratio roll regardless of
committed strength. Against a 12-15 initial + 20-30 reinforced Garrison
pool (§4.1) and an expected 20-25 Assaults across the game, a defender
who keeps Wall Defense maintained (via Repair, keeping ratios out of the
3:1/4:1+ columns as long as possible) should clear the "hold off at
least 20 Assaults" bar comfortably; a defender who lets a sector go
untended into repeated high-ratio Assaults will still lose it, which is
the intended risk/reward. All values are a first-draft placeholder
pending playtesting, and this interacts directly
with whatever Initial Garrison and Reserve Pool numbers end up being
(§4.1) — those need tuning together, not independently.

**Worked example, this session — the Ottoman's theoretical maximum
push.** Attacker: a full 5-unit elite stack at the Force Commitment Cap
(§6.3) — 4 Janissary (3 Attack each = 12) + 1 Solak (4) = 16, + Mehmed's
own +1, + Combined Arms +2 (§4.0.2), + one battle-event card (+1) = **17-20
Attack**. Defender: also at cap — 3 Roman militia (1 each = 3) +
Giustiniani's Genoese Company (Defense 3) = 6, + a leader bonus (+2 to
+3 depending on who's present) + full Wall Defense (Intact, +2 in this
example rather than the full 6, reflecting some prior softening) = **11-12
Defense**. Ratio range: 17:12 = 1.42 (now the new **4:3** column,
previously would've rounded all the way down to 1:1 and lost the
distinction) up to 20:11 = 1.82 (**3:2**). Two findings:

1. **Even the Ottoman's absolute maximum investment — every elite unit,
   every leader bonus, a spent event card, three extra discarded cards
   for the Mustering Cost surcharge (§6.3) — tops out around 3:2, not
   2:1 or higher.** This confirms what the earlier 1:1-column analysis
   this session suggested: troop/leader stacking alone has a ceiling
   close to parity by design (§6.1's "symmetric mechanic, asymmetric
   quantity"), and reaching the genuinely high-damage columns (2:1, 3:1,
   4:1+) requires Wall Defense to have already been ground down by
   Bombard, not just a bigger stack. That's the intended lever, and it
   holds even at the extreme.
2. **This all-in stack has zero cheap units to sacrifice under the
   Mandatory Kill Priority rule (§6.3.1)** — every single Attacker step
   lost from this Assault lands directly on a Janissary or Solak, no
   exceptions. At 3:2's average Atk-1.1, that's a near-certain elite hit
   *every time this play is used*, feeding the Elite Casualty pool fast
   and making the all-in gambit meaningfully riskier than a mixed stack
   — appropriate for what's supposed to be a rare, high-stakes push, not
   a routine opener. On the defender's side, this composition carries 5
   total steps (3 militia + Giustiniani's 2-step Company) — above the
   Def-4 cap even at a best-case roll, so **Commander Casualty (§6.5.1)
   cannot trigger from a single roll here**, even against the Ottoman's
   biggest possible push, unless the defense was already worn down
   beforehand. Both findings together read as the table doing its job:
   the ceiling on a single all-in roll is real but bounded on both sides.

### 6.5.1 Commander Casualty on Total Defeat (new this session)

If a single Assault's resolution reduces a sector's **committed garrison
to zero remaining steps** (i.e. every unit committed to that Defense,
§6.3, is fully destroyed by this roll's Defender steps lost — not just
gradually worn down across separate Assaults, but wiped out in this one
resolution) **and a Byzantine leader was present and committed at that
sector**, roll 1d10:

- **6+**: the commander manages to flee the collapse — removed from that
  sector (returns to the reserve/off-map pool, available to be
  re-committed elsewhere next round) but stays in the game.
- **5 or less**: the commander is killed, removed from play for the rest
  of the game — same permanent-removal consequence as a failed roll on
  Strike the Commander or The Emperor Falls (EVENT_DECK.md, Ottoman
  pile), just triggered by battlefield collapse rather than a named
  targeted-assault card.

This is a **general rule, not a card** — it applies automatically
whenever the trigger condition is met, layering on top of (not
replacing) the existing named cards that let the Ottoman player
specifically target a leader. With Defender loss now capped at 4
(§6.5, this session) matching the 4-unit commitment cap, a total wipe in
a single roll requires the committed defense to already be reduced to 4
or fewer remaining steps going into that Assault — so this fires when a
sector's defense has been ground down and then makes one last, doomed
stand, not as a random one-roll swing against a fresh garrison. Fits the
historical shape of both Giustiniani's wounding and Constantine's death:
both happened as their respective defensive lines were already
collapsing, not out of nowhere.

### 6.5.2 Alternative CRT — Difference / Margin variant (revised for the +2-to-+8 play band, 2026-07-12)

**This does not replace §6.5.** It is a parallel table to playtest against
the ratio table, and the design intent is explicitly a **war of
attrition** — there is no decisive one-roll breakthrough here; committing
more simply grinds the garrison down faster and more reliably. A
**difference** column index — `Attacker Strength − Defender Strength`, same
strength definitions as §6.4 — gives every point of committed Attack a
constant value and lets Wall Defense act as a clean flat **−6 / −3 / −1**
to the margin instead of distorting a ratio.

**Why a difference index (vs the §6.5 ratio):** realistic assaults land at
**12–15 Attack vs 7–10 Defence** at the two decisive sectors (Blachernae,
St. Romanus) once a wall is Breached — i.e. a **margin of about +2 to +8**.
That whole range collapses into a *single* wide ratio column (3:2 covers
odds 1.5–1.99), so under the ratio table committing an extra Janissary
there often buys nothing. The difference index breaks that band up, so
concentration is visibly rewarded exactly where the game is actually
played. **The bands below are therefore deliberately fine through +1 to +8
and coarse in the tails**, which competent play rarely touches (no wise
Ottoman assaults at a negative margin).

This is a **mutual-damage** table — every cell is **Atk-x / Def-y**: the
Attacker loses *x* committed steps and the Defender loses *y* Garrison
steps. The **Approach / Defenders' Fire** stage (§6.5.3) is a *separate,
additional* step that resolves **first** and only ever hurts the attacker
(extra casualties + force reduction); this table is the main clash where
both sides bleed.

**Procedure:** resolve Defenders' Fire (§6.5.3) first and remove its
casualties; then compute **Margin = surviving Attacker Strength − Defender
Strength**, find its band, roll **1d10** (same flat single die as
§6.4/§6.5), and read **Atk-x / Def-y**. Attacker steps lost → Draw Track
step-down + Elite Casualty pool; Defender steps lost → Garrison damage,
Sector-Falls check, Commander Casualty (§6.5.1).

| Roll | ≤ 0 | +1 to +2 | +3 to +4 | +5 to +6 | +7 to +8 | +9 to +11 | +12 or more |
|---|---|---|---|---|---|---|---|
| 1 | Atk-3/Def-0 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-2/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 |
| 2 | Atk-3/Def-0 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-2/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 |
| 3 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 |
| 4 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 |
| 5 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 |
| 6 | Atk-2/Def-0 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 |
| 7 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 |
| 8 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-4 |
| 9 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-4 |
| 10 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-4 | Atk-1/Def-4 |

Average steps lost per roll (Atk +0.2 / Def −0.2 tweak applied to the +3-4
through +7-8 combat bands this session — Ottoman bleeds slightly more, the
Byzantine slightly less, where play concentrates):

| Band | Avg Atk | Avg Def | Net (2·Def − Atk) |
|---|---|---|---|
| ≤ 0 | 2.0 | 0.4 | −1.2 |
| +1 to +2 | 1.5 | 1.0 | +0.5 |
| +3 to +4 | 1.4 | 1.3 | +1.2 |
| +5 to +6 | 1.3 | 1.8 | +2.3 |
| +7 to +8 | 1.2 | 2.3 | +3.4 |
| +9 to +11 | 1.0 | 2.9 | +4.8 |
| +12 or more | 1.0 | 3.3 | +5.6 |

**How this reads, by design:**

- **Monotone in value — a better result is never worse.** Score each cell
  as **2·Def − Atk** (Byzantine step = 2, Ottoman step = 1). Down every
  column (rising roll) *and* across every row (rising margin) that score is
  non-decreasing — the net ladder climbs **−1.2 → +0.5 → +1.2 → +2.3 →
  +3.4 → +4.8 → +5.6** — so a higher roll or a bigger margin can only ever
  improve the Ottoman's weighted outcome. Conventional shape: attacker loss
  highest at the worst results, tapering to 1; defender loss rising to a
  capped 3.3.
- **Reward rises with the push.** Def climbs across the realistic +2 → +8
  band, so concentrating more attack always grinds more (vs the ratio
  table's single wide 3:2 column).
- **Still attrition, no breakthrough.** Def capped at 4; reward flattens
  past the realistic band. A Breached sector bleeds steadily; it is never
  stormed to nothing in one roll.
- **This-session tweak — the combat bands lean defender.** In +3-4 through
  +7-8 (where play concentrates) Atk is ~0.2 higher and Def ~0.2 lower than
  the untweaked baseline: the Ottoman pays a little more and grinds a little
  less exactly where it matters, so the outnumbered Byzantine holds longer.

**Plus the Approach stage.** On top of this mutual clash, **Defenders' Fire
(§6.5.3)** resolves first and only ever hurts the attacker — extra
casualties + a force reduction that also drops the survivors onto a lower
margin band here. So total attacker loss = Defenders' Fire *plus* this
table's Atk; the two stages together are why the Ottoman must spend the
fodder to reach a wall (historically: elites spared, irregulars bled).

**Tuning caveat.** A typical +5 assault now averages Def 1.8, so ~22
concentrated assaults ≈ the Byzantine's ~40 capacity (§4.1/§6.5) — the
intended knife's edge, slightly kinder to the defender than before. Adjust
the **+5-6 / +7-8** values if playtest holds too few / too many.

### 6.5.3 Approach — Defenders' Fire (decided this session, 2026-07-12)

**An Assault resolves in two steps:**

1. **Approach (this stage, Byzantine rolls):** as the attackers cross the
   ditch under fire, the defenders shoot them up — **extra attacker
   casualties**, removed *before* the clash (which also drops the survivors
   onto a lower §6.5.2 margin). This stage **only ever hurts the attacker** —
   a defender-favouring bonus layer, not the main combat.
2. **Assault (§6.5.2, mutual):** the main clash on the Atk/Def margin CRT,
   where **both** sides take steps.

**Procedure:** the Byzantine rolls **one d8 per garrison unit committed to
the defence** (x dice, x = 1–4, the §6.3 defender cap). Each die showing its
**top two faces (7–8)** inflicts **one attacker step loss**, assigned per
§6.3.1 (mandatory kill priority, focus-fire). Wall/Naval Defense are *not*
dice — they stay flat modifiers to the §6.5.2 margin.

Expected attacker casualties = x × 2⁄8 = **x ÷ 4**:

| Garrison committed (x) | Avg attacker steps lost |
|---|---|
| 1 | 0.25 |
| 2 | 0.50 |
| 3 | 0.75 |
| 4 | 1.00 |

**Why this shape:**

- **The defender's roll, keyed to the defender's strength** — fixes the old
  complaint that attacker casualties keyed off the Ottoman's own commitment
  while the Byzantine sat idle. Their garrison investment drives it, they
  roll it.
- **Light on its own, per the history.** A fully-manned wall inflicts ~1
  attacker casualty per assault here; with a bashi absorber soaking the
  first (§6.3.1), an **elite dies only on a 2+ hit roll** — occasional, not
  routine, matching the real doctrine (elites spared; the fodder and the
  killing-ground took the losses). **Note:** this now *stacks on top of* the
  §6.5.2 table's Atk column, so combined attacker loss is ~2–2.5/assault and
  the Elite Casualty pool fills faster (→ ~4–5 ticks/game at −1 per 5). The
  morale rate therefore likely wants revisiting to **−1 per 10** — flagged,
  **not changed this session** per direction.
- **Thematic:** the deadliest phase of a real assault was crossing the ditch
  under massed arrow / crossbow / gun / Greek-fire; more defenders on the
  parapet = more volleys.

**Resolved this session:**
- **Force reduction — yes.** Approach casualties are removed from the
  attacking force *before* the §6.5.2 margin is computed, so a good
  defensive volley both kills attackers **and** drops the survivors onto a
  lower margin band ("the reduced column"). A deliberate double effect —
  heavy fire is doubly punishing (fewer attackers now, and a weaker assault).
- **Wall firing positions (enrichment adopted):** **Wall Intact → +1 die,
  Battered → no change, Breached → −1 die** (minimum 0). The parapet's firing
  positions degrade as the wall is battered, so an intact wall shreds the
  approach while a breached one barely fires — which also means the sectors
  the Ottoman actually assaults (Battered/Breached) inflict *lighter* fire,
  keeping elite loss rare.

**Remaining knob:**
- **Die size = the magnitude dial** (always top-two-faces): **d8** = 0.25
  per die (chosen — lightest), d7 = 0.29, d6 = 0.33 (heaviest, commonest die).

This **replaces** the earlier flat "commitment casualty table" idea entirely.

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
   closes the open question from §2.2. ~~Note: §2.2 specifies 3-4
   designated draws/round, not a flat 3~~ — **resolved this session**:
   designated-pile draw is now a flat 3/round for both sides (§4.0), as
   part of the broader draw-count rebase (Ottoman 10-11/round, Byzantine
   9/round, plus a new Card Carryover rule letting up to 3 unused cards
   bank into next round, §2.2). ~~Still need a reshuffle-fallback rule~~
   — **resolved this session, mechanically**: the Reshuffle Rule (§2.2)
   applies to all three piles — Event cards are removed from the game
   permanently once their Event is played, everything else (Ops-spent
   cards, unplayed named cards, generic cards) discards and reshuffles
   back in once the draw pile empties. **Worth flagging, not fully
   resolved:** since the designated piles are ~100% named cards (no
   generic filler mixed in, unlike Neutral), and most named cards will
   eventually get played as their Event rather than banked for Ops, each
   designated pile's *playable pool* genuinely shrinks over the game as
   Events get triggered and permanently removed — a flat 3/round draw
   against a ~27-28 card pile could plausibly thin out by round 8-9,
   leaving a late-game hand skewed toward whatever wasn't played as an
   Event yet plus Ops-only discards. Thematically fine (fewer big beats
   left as the siege drags on) but worth a playtest check that it doesn't
   leave either designated pile too threadbare late. A new [Forced] tag
   (11 cards so far)
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
4. **Sue for Aid redesigned 2026-07-13 — now fully specified in §4.0.5**
   (Powers Stirring track: 2 Ops, roll 1d10, 6+ advances a 0→4 marker,
   filling it = permanent Draw Track −1 + Pressure to Attack requirement
   +1). This replaced the old proposal (2 Ops, 8+ → Reserve Pool +1),
   which was strictly dominated by Reinforce and paid in scarce Guile
   cards — see §4.0.5 for the reasoning. **Still pending confirmation
   (separate from the redesign):** Reserve Pool hard-capped at its
   starting value (now **20-30**, §4.1, up from the old flat 20 — overflow
   wasted) to fix the "too generous" cumulative-bonus-card problem
   identified 2026-07-10; 1 Reserve Pool token = 1 militia-equivalent unit
   fielded via Reinforce (1-for-1). Track numbers (fill threshold 4,
   6+ advance, payoff size) are placeholders pending playtesting.
6. Tune placeholder numbers via playtesting: bombard slot count (3 vs 4)
   and doubling cost, Reserve Pool size (20-30) and per-action token
   cost, HP-band thresholds, force commitment caps (5/4, §6.3), the
   mutual-damage CRT (§6.5), and the **Ottoman** unit token pool sizes
   (§6.1 — the large Bashi-bazouk/Azap/Janissary bulk pools; the Byzantine
   pools and the capped Solak pool of 2 are now set this session).
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
17. **Mustering Cost retuned, new session (2026-07-10), then tightened
    further in a second pass — §4.0.1.** First pass: Bashi-bazouk no
    longer free (3 per card), Azap 4-per-card → 1-per-card, fresh
    Janissary 1 card → 2 cards to make the New Levy upgrade path (1 card)
    the efficient route. Second pass: New Levy Janissary itself tightened
    2-per-card → 1-per-card, and **fresh-mustered Janissary removed
    entirely** — the only way to field a Janissary now is muster New Levy
    then upgrade, no queue-skip option left. **Solak's mustering ability
    was removed too** rather than re-pricing it (resolves the earlier
    price-compression flag by eliminating the comparison). **Open
    decision this creates:** how do Solak's 2 tokens enter play at all,
    if not mustered? Leading options — (a) both pre-deployed at game
    start (fits "the Sultan's own personal bodyguard," §6.1 — they'd
    already be with Mehmed, not raised mid-siege), or (b) gated behind a
    specific named Event card. Needs a decision before this is playable
    as written.
