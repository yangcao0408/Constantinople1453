# Constantinople 1453 — Design Document (Draft v0.1)

A 2-player, card-driven wargame (GMT COIN/CDG-adjacent) simulating the siege of
Constantinople, April–May 1453. One player is the Ottoman besieger, the other
the Byzantine defender.

## 1. High-Concept

- **Length:** 9 rounds, each round = one week of the historical 53-day siege.
- **Ottoman goal:** Breach the walls and take the city before Morale runs
  out (§4.0.4, the sole hard-loss track) — while their card economy
  (§4.0) steadily throttles what they can afford to do each round.
- **Byzantine goal:** Prevent any wall sector from being breached until the
  Ottoman player is forced to withdraw (a track hits zero) or the round track
  is exhausted (game ends turn 9 — Byzantine automatic win, since the
  historical relief-fleet clock is what the Ottomans are racing).
- **Core tension:** Ottomans have overwhelming force but a shrinking clock
  (political capital + army will to fight); Byzantines have almost no
  reserves and must allocate a razor-thin garrison across a long wall.

## 2. Turn Structure — Card-Driven

Each round (= one week, one "day" of action in game terms — the two are the
same beat, "day" is just the flavor name for the round's action sequence)
runs in two phases.

**Start of each round 2–9 — flip a Siege Event (added 2026-07-15).** Before
Phase A, flip the next card of the shuffled **Siege Events** deck
(EVENT_DECK.md) — a Forced ambient event (weather, disease, supply, zeal…)
that resolves immediately and colours the round for one or both sides. One
per round, 8 events across rounds 2–9; rounds 1 and 10 have none. These are
separate from the drawable card piles and cost no Ops.

### 2.1 Phase A — Bombardment

- The Ottoman player bombards **3–4 sectors**, gated by cannon placement
  (i.e. which sectors currently have artillery sited against them — this is
  the spatial/logistics lever, not a free choice of any 3–4 sectors every
  round).
- **Each Bombard action removes 1 Wall HP** from its target sector
  (§3.1) — the baseline damage rate behind the "several rounds of
  grinding" tempo the whole game is built around.
- **Second Barrage** (added 2026-07-10, **redefined 2026-07-14 / 2026-07-16**):
  the general term for an **Attack-type card funding an extra Bombard
  action against a wall sector** in the Card Phase — a fresh supporting
  barrage to grind masonry (§2.3, Attack type). It is **purely
  structural**: wall strength only, **no combat effect**. Resolved on a
  **1d10 — 1–3 nothing, 4–10 = 1 Wall HP, capped at 1 HP** (no 9–10
  breaching bonus, no burst — those are unique to Orban's gun, §2.1). Not
  to be confused with **Combined Arms**, Mehmed's +2-Attack *combat* buff
  (§4.0.2). Full details in §4.0.3.
- **The Great Cannon — Cannon Determination (added 2026-07-13, replaces
  Orban's old "+1 Bombard slot" effect):** once Orban's Great Cannon is in
  play (EVENT_DECK.md, Ottoman card 10, played Round 1), it fires each
  round at one chosen sector as **one extra Bombard shot** — but that shot
  is *variable and fragile* rather than a flat 1 HP. Roll **1d10** on the
  **Cannon Determination** table:
  - **1–3:** **no damage** — misfire, a fresh crack in the barrel, or the
    great bombard's notoriously slow reload eats the round.
  - **4–8:** **1 Wall HP** — a normal hit.
  - **9–10:** **2 Wall HP** — a great breaching shot. This +1 over a
    normal cannon *is* the "damage to wall +1" the piece is now worth.
  - **On a 1–4 the great cannon *also* bursts** — it cracks and falls
    silent, ceasing to fire. A single d10 does double duty: **1–3 → no
    damage *and* it bursts; 4 → its one hit lands *and* it bursts on the
    same shot; 5–8 → 1 HP, gun keeps firing; 9–10 → 2 HP, gun keeps
    firing.** So the gun stays in service only on 5+ (60%/shot) and cracks
    on average after ~2–3 shots — matching the historically temperamental
    great bombard.
  - **A burst is permanent (revised 2026-07-15):** when Orban's Great
    Cannon bursts on its own Determination roll (the 1–4 above), it is
    **removed from the game for good — the card goes with it** and is never
    redrawn. There is no re-cast for a self-burst: the barrel that failed
    under its own firing is gone. (Historically Orban's bombard did crack
    repeatedly, but for the game a self-burst is the clean end of the piece
    — the fragility *is* the counterweight to its firepower.)
  - **Re-casting a cannon destroyed by a Sortie (revised 2026-07-15):** the
    5-Ops re-cast applies **only** to a great cannon that a Byzantine
    **Sortie** silences (§4.0.6), *not* to a self-burst. In that case the
    gun is knocked out by enemy action rather than shattered from within,
    so the Ottoman may repair/re-cast it by spending **5 Ops** (discarding
    5 Ops' worth of cards, §4.0), returning it to service from the
    following round. Five cards is a large slice of a round's economy, so a
    successful raid genuinely drains the Ottoman even though the gun comes
    back — the tempo cost is the real pressure.
  - The great-cannon shot **does not count toward the Concentration
    Bonus**. (*Design flag:* I've kept it as an *extra* shot on top of the
    normal 3–4 slots, preserving Orban's "more firepower" identity; if it
    over-performs, demote it to consuming one of the normal slots instead.
    Also flag if you wanted damage and burst on two *separate* d10 rolls
    rather than the single-roll reading above — your "1–3 / 4–8 / 9–10"
    and "1–4" figures overlap, so I read them as one die.)

### 2.2 Phase B — Card Phase

- A single shared **Event Deck** (target ~35–45 cards for a 9-round
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
- **Reshuffle Rule (refined 2026-07-13 — now keyed to card *ownership*,
  not just Event-vs-Ops):** applies to all three piles (Ottoman,
  Byzantine, Neutral), standard CDG convention:
  - **A card played for its Event text, if it is from the playing side's
    own designated pile, is removed from the game permanently** — your
    side's historical beats fire once and are then gone (the Ottoman's
    Orban's Great Cannon, the Byzantine's Blockade Runners, etc.). It
    never returns to its pile, reshuffled or otherwise.
  - **Everything else washes back** — into its pile's discard stack, which
    reshuffles into the draw pile once that pile is exhausted. This
    explicitly covers three cases: **(a)** *any* card spent for its **Ops
    value** rather than its Event — the beat never happened, so the card
    can recur (this includes a card from your own pile spent for Ops);
    **(b)** a **Neutral-pile card, played by either side, even for its
    Event** — Neutral cards model *recurring* conditions (weather, camp
    disease, rumor, ration crises), so a Neutral Event is deliberately
    never a once-and-gone historical beat and cycles back to be drawable
    again; and **(c)** all generic Attack/Supplies/Move/Guile cards
    (§2.3), which have no Event text at all — a fixed pool of ~30 that
    recirculates all game (EVENT_DECK.md's Generic Action Cards section).
  - **Exception — `unique`-tagged cards:** a card explicitly tagged
    *unique* is removed permanently the moment its **Event** resolves,
    regardless of which pile it came from — a one-time, dated historical
    event (an eclipse, the April 20 relief run) cannot recur even from the
    recirculating Neutral pool. `unique` overrides the Neutral wash-back in
    (b); it does **not** make an *Ops*-play of a unique card remove it (the
    event still never happened, so it recirculates like any Ops-play).
  - Net effect: **only your own pile's Events, plus any `unique` card's
    Event, ever leave the game permanently.** Ops-plays, non-unique
    Neutral Events, and all generic cards recirculate. Each designated
    pile's *named* count still shrinks over the game as its owner triggers
    and burns its beats, while the Neutral pool stays a stable, renewable
    resource — so a late-game hand skews toward whatever named cards a
    side hasn't yet spent, on top of a steady Neutral floor.
- Ops actions (spendable by either side, gated by role):
  - **Ottoman:** Assault a wall sector (also usable here outside the
    concentration-bonus trigger in Phase A), Move (re-site the guns to new
    sectors, §2.1, **or** shift up to 3 units anywhere on the map), Deploy
    (bring uncommitted units onto the map from the Ottoman pool, §4.0.1 —
    replaces the old Muster/recruitment action), Sap/mine, and Blockade (knock the Byzantine Powers
    Stirring marker back 1 step — "diplomatic support −1", §4.0.5; the old
    standalone "Diplomacy" action, now the Guile-type lever, §2.3).
    Bombard is a Phase A slot action *and* — resolved 2026-07-14, revised
    2026-07-15 — can also be funded by an Attack-type card in the Card
    Phase, which grants **another full Bombard action** targeting wall
    strength only. It is **not** flat damage: resolve it on a **1d10 —
    1–3 no damage, 4–10 = 1 Wall HP, capped at 1 HP**. Like the great
    cannon (§2.1) but with **neither the 9–10 breaching bonus (never 2 Wall
    HP) nor the burst check** — both are unique to Orban's gun — so an
    Attack-card Bombard (**Second Barrage**, §4.0.3) can only ever wear a
    wall down 1 HP at a time. §2.3/§3.1.
  - **Byzantine:** Repair a wall sector, Reinforce a sector (spend Reserve
    Pool tokens, §4.1), Move soldiers (shift up to 3 garrison units
    between sectors), Sortie (raid to burn/wreck the Ottoman siege works —
    resolved on a success roll + d8 return fire, §4.0.6), Sue for
    Aid (advance the
    Powers Stirring track — the West's stirring forces the Ottoman to
    hedge; filling it permanently steps the Draw Track down and forces
    the Sultan toward a rushed assault, §4.0.5), Fire-ship raid (Coco's Raid —
    contest an unlocked Golden Horn, and on success also steps the
    Ottoman Draw Track down for ships lost/damaged, same logic as Sortie
    — Byzantine naval/raid actions should generally cut into the Ottoman
    card economy when they succeed, not just move Byzantine-side tracks).
- End-of-round bookkeeping: track adjustments, reserve/resource upkeep.
- **Each Ops action costs 2 Ops points** to perform (Assault, Repair,
  Reinforce, Sortie, Sap/Mine, Sue for Aid, Blockade, Deploy — every entry
  in the lists above) for its base (**1×**) effect. **Exception —
  Concentration (§2.3):** stacking multiple generic cards of the same type
  on one action multiplies its effect per the card count; see §2.3 for how
  ×N scales each action and the cost-model flag there.
- **Post-Assault Recovery (§6.3.2):** units and leaders that fight in an
  Assault are *Recovering* the next round — they may not Move or join
  another Assault (a defender still defends its own sector if re-assaulted).
  Sustaining pressure round after round means rotating in **fresh** troops
  (Deploy, §4.0.1), not re-throwing the same stack.
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
| **Attack** | Assault, **or** a Card-Phase Bombard (another full Bombard action, wall strength only, resolved on the damage roll — §2.1/§3.1) | Sortie, Fire-ship raid |
| **Move** | Re-site the guns (change which sectors are cannon-sited, §2.1) **or** shift up to 3 units anywhere on the map | Move up to 3 garrison units between sectors |
| **Supplies** | Deploy from the Ottoman pool (≥2 units **or** units summing to ≤5 combined Attack — §4.0.1) | Reinforce a sector **or** Repair a wall |
| **Guile** | Sap/Mine **or** Blockade (knock the Byzantine Powers Stirring marker back 1 step — "diplomatic support −1", §4.0.5) | Sue for Aid |

Remapped 2026-07-14 so each type is a *category of action both sides share*,
replacing the old semantically-mismatched pairings (Supplies used to be
Ottoman Diplomacy vs Byzantine Repair — two unrelated things). Now: **Attack**
= apply violence, **Move** = reposition forces already on the board,
**Supplies** = field new force or shore up a sector, **Guile** = the
asymmetric special lever. Fire-ship raid stays under Attack (an aggressive
strike, same category as a Sortie). Three notes on the design:

- **Byzantine Supplies carries both Reinforce *and* Repair** — the defender's
  two sustain levers now compete for one card type, so a Supplies-starved
  round pinches both at once (the 2-for-1 off-type conversion is the relief
  valve). A deliberate concentration of defender pressure vs the old split;
  watch its variance in playtest.
- **Byzantine Move** set to "up to 3 units" to mirror the Ottoman figure —
  the defender's interior lines make repositioning at least as free as the
  attacker's.
- **Bombard under Attack — the Second Barrage — resolved 2026-07-14,
  revised 2026-07-16: yes, and it targets wall strength only.** An
  Attack-type card funds **another full Bombard action** in the Card Phase;
  this Attack-card bombard is exactly what **"Second Barrage"** names in
  play (§4.0.3). Resolve it on a **1d10: 1–3 nothing, 4–10 = 1 Wall HP,
  capped at 1 HP** — like the great cannon (§2.1) but with **no 9–10
  breaching bonus (never 2 HP) and no burst check**, both unique to Orban's
  gun. It does nothing else. **Each wall sector may take at most one Second
  Barrage per round** (§4.0.3). Distinct from **Combined Arms** (Mehmed's +2
  Attack combat buff, §4.0.2): **Second Barrage = structural wall damage,
  Combined Arms = combat.**
- **Ottoman Guile — resolved 2026-07-14:** its two uses are **Sap/Mine**
  and **Blockade**, where Blockade = "diplomatic support −1 for the
  Byzantines" = knock the Powers Stirring marker back 1 step (§4.0.5), the
  repeatable Guile-funded version of the suppressor cards (Rumeli Fort,
  Hunyadi's Truce, Intercepted Dispatch). The old standalone Diplomacy
  action is now exactly this.

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

- **Concentration — stacking same-type cards (added 2026-07-15):** two or
  more generic cards **of the same type**, played together in one turn on a
  **single action of that matching type**, resolve that action at a
  **multiplied effect equal to the number of cards committed — 2 cards →
  2×, 3 cards → 3×**, and so on. A glut of one type is no longer something
  you can only spend on repeating the base action once per pair; you may
  fold it into one oversized action instead. The committed cards *are* the
  cost. The multiplier scales the action's **quantitative magnitude**:

  | Type → action | What ×N multiplies |
  |---|---|
  | **Attack → Card-Phase Bombard** | **N** separate damage rolls (§2.1), each capped at 1 HP and each at a **different sector** (max one Second Barrage per sector/round, §4.0.3) |
  | **Move** | shift up to **3 × N** units (or re-site the guns to N sectors) |
  | **Supplies → Deploy** | **N×** the allowance: **≥2N units, or units summing to ≤5N combined Attack** (§4.0.1) |
  | **Supplies → Repair** | roll Repair **N times** (§4.0.8), sum the HP (still capped at the current band ceiling, §3.1) |
  | **Supplies → Reinforce** | field **N** units (spending N Reserve tokens, §4.1) |
  | **Guile → Blockade** | knock the Powers Stirring marker back **N steps** (§4.0.5) |

  **Actions with no natural magnitude don't take a ×N** — a single
  **Assault** or **Sortie** clash, **Sue for Aid** / **Fire-ship** (each a
  single d10 resolution), and **Sap/Mine** (hard-capped at one *new*
  gallery per round, §4.0.7). Committing extra same-type cards to these
  instead buys **N separate actions** (e.g. two Attack pairs → two distinct
  Assaults; two Guile-funded Sue for Aid rolls), still subject to every
  per-round cap. Concentration never bypasses a cap — it can't open two new
  galleries or exceed the §6.3 Force Commitment cap in one Assault.

  *(Design flag: as written, N matching cards → N× makes a concentrated
  action more card-efficient than the flat "2 Ops = one base action" cost
  (§2.2) — effectively 1 matching card = one ×1 unit of effect. That's the
  natural reading of "2 cards → 2×," and it reads intuitively (2 Move cards
  = 6 units, 2 Attack cards = 2 Bombard rolls). If you instead want the
  flat 2-Ops base preserved, the alternative is **2N cards → N×** (a base
  ×1 action still costs its 2 cards). Flag which you intend; I've
  implemented the literal per-card version.)*

This creates the intended tension directly: draw the right generic card
for what you want to do, and it's efficient — and drawing several of one
type now lets you concentrate them for a proportionally bigger swing;
draw the wrong mix, and you either wait, spend a named card's Ops value
instead, or burn cards 2-for-1 to force it through.

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

**Odd Ops values — discard-to-round-up (added 2026-07-15).** Because every
Ops action costs **2 Ops** (§2.2), a named card spent for its **Ops value**
with an **odd** total (3 or 5) strands 1 Ops after funding whole actions.
To avoid wasting it, the player may **discard one additional generic action
card (1 Ops) to top the odd card up by +1**, rounding it to an even total
that funds one more complete 2-Ops action. So a **3-Ops card + 1 discard →
4 Ops = two actions**; a **5-Ops card + 1 discard → 6 Ops = three actions**.
Only the leftover odd 1 Ops may be topped up this way — it is a rounding
lever, not a general card-to-Ops converter (that is the flat 2-for-1
off-type rule, §2.3). The discarded card may be any generic card (type
doesn't matter, since it's only supplying the missing 1 Ops).

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
- **Wall Integrity (HP)**, reduced by Bombard, restored by Repair (now a
  die roll — §4.0.8) — but
  **Repair can only raise a sector's HP up to the top of its *current*
  status band** (the green Intact / yellow Battered / red Breached bands
  in the table below), never across a band boundary into a healthier one
  (refined 2026-07-13 — this is the concrete form of the old "rubble
  cap"). Once Bombard knocks a sector down into Battered or Breached, that
  lower band becomes a **permanent ceiling**: Repair keeps the wall topped
  up *within* its band but can never lift it back into a greener band.
  **Consequence to note:** a Breached (red) sector sitting at the top of
  its band gets *nothing* from a normal Repair — masonry work cannot
  un-breach a wall. The only way to add defense at such a band-topped sector
  is a **Stockade**: either the card *The Stockade at the Breach* (**+2 Wall
  Defense**, Breach-only, EVENT_DECK.md), or — added 2026-07-16 — a
  band-topped **Repair to erect a lighter +1 Stockade directly** (§4.0.8).
  The two are the same kind of modifier and **do not stack** — use the
  higher. This makes Bombard progress into a lower band genuinely sticky
  while giving the defender a standing-defense use for an otherwise wasted
  Repair. (*Design flag:* this is the literal
  reading of "repair only up to the top of the status band." The one
  escape hatch is *The Walls Endure*, which lets a single Repair bypass
  the band ceiling once. Flag if you instead wanted Repair able to slowly
  climb bands over repeated actions.)
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

**Band cushion — a band-crossing Bombard is softened by 1 HP (added
2026-07-17).** When a *single* Bombard hit would carry a wall sector
*across* a band threshold — Intact→Battered (down to ≤ ½ max) or
Battered→Breached (down to ≤ ⅓ max) — **reduce that hit by 1 HP.** The
rubble and improvised stockading thrown up at the transition (the same
fiction as the ≤⅓ "token defense" row above) soaks the blow: a 2-HP
great-cannon shot that would knock a sector a full band down instead
deals **1**, and if that single point no longer crosses the line the
sector **holds in its current band**. *Worked example:* a Battered wall
sitting two points above the Breached threshold, hit for 2, loses only 1
and stays Battered. This applies to **every** wall sector regardless of
any standing Stockade structure (§4.0.8) or which leaders are present.
*Open knob:* as written it fires on every band-crossing hit, so a wall
can stall one point above a threshold under repeated 1-HP bombards (only
a 2-HP great-cannon shot then pushes it across) — cap it at **once per
sector per round** if that proves too sticky.

**Wall Defense is a combat modifier, not a second health pool** (made
explicit 2026-07-11, §6.5) — it never runs out on its own the way
Garrison Strength does. Its only job is shaping the Assault ratio, which
in turn shapes how much Garrison damage a hit deals. A sector falls only
when its Garrison Strength hits 0, regardless of remaining Wall HP — an
intact but empty wall offers no one to actually stop the Ottomans.

**Sap resistance — per-sector mining penalty (added 2026-07-15).** Beyond
Wall Defense, each land sector has a fixed **sap penalty** subtracted from a
gallery's Mining Strength when its dig roll is computed (§4.0.7): the
harder-to-undermine the ground, the more it eats into the sappers' odds.

| Sector | Sap penalty | Effective Mining Strength `M_eff` |
|---|---|---|
| **Blachernae** | **0** | `M` — the single wall on soft, flanked terrain gives miners a free hand (the historically weakest construction) |
| **Mesoteichion / St. Romanus** | **−1** | `M − 1` — the low-ground breach point, next-easiest to dig under |
| **Charisius, Gate of the Spring, Golden Gate** | **−2** | `M − 2` — the full Theodosian triple wall on high ground resists mining hardest |

`M_eff` is floored at 0 and feeds directly into the §4.0.7 roll. Worked
examples at a full 3-unit gallery (`M = 3`): Blachernae `M_eff = 3` (blows
on 8+), St. Romanus `M_eff = 2` (blows on 9–10, digger dies on 1–3), and
the three triple-wall sectors `M_eff = 1` (**blows on a 10 only**). This is
separate from **John Grant's Countermine** (EVENT_DECK Byz #2), which
doesn't apply a penalty at all — it *permanently seals* two chosen sectors
so no gallery may ever be opened there again.

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
- **No Approach / Defenders' Fire phase (decided 2026-07-14).** Unlike a
  land assault, a Golden Horn Assault skips the §6.5.3 approach stage
  entirely — no d8 return-fire roll. The flat Naval Defense 3 above is the
  sea's substitute for it. (A future Byzantine card, *Ready the Sea
  Walls*, will grant a reduced ⌈n∕2⌉-d8 approach roll here — see §6.5.3.)
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
    next round's baseline. Baltaoğlu's Punishment, Demand Tribute,
    deployment costs, Second Barrage, Combined Arms — all
    of these are immediate hand-size effects, not Draw Track edits. This
    is the far more common case; treat Draw Track shifts as the
    exception reserved for effects that are explicitly about a
    sustained, multi-round change in capability.
  - **Effect timing — everything is immediate (codified 2026-07-15):**
    unless a card explicitly says "next round" or "for the rest of the
    game," **every effect resolves the moment it's played**, in
    particular: **card draws and discards happen immediately, and cards
    drawn mid-round may be played that same round** (there is no
    "drawn cards sit out until next round" rule — explicitly ruled out);
    **Reserve Pool gains/losses apply immediately.** **Two structural
    levers are the deliberate exception and take effect only from the
    *next* round (revised 2026-07-15 — this reverses the earlier "cap is
    immediate" note):** the **Ottoman forced-assault requirement**
    (Pressure to Attack, §2.2 — e.g. Halil Pasha's Doubt's +1) and the
    **max-unit-commitment / Force Commitment Cap** (§6.3 — e.g. The War
    Council's +1). A card that changes either does *not* touch the current
    round's Assaults; the new value applies from the following round.
    Other deferred effects are those whose text says so (commander recalls
    lasting "2 rounds," etc.).
- Either way, a card-starved Ottoman hand (whether from a lowered Draw
  Track or a run of discard-heavy cards) has both fewer actions *and*
  fewer cards to burn on Second Barrages or elite deployments — the intended
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
**Powers Stirring track** (0 → 5 steps) rather than granting an immediate
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
- **Filling the track (marker reaches 5) — "The Powers Stir":** a
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
  - *Repeatable Ottoman action — Blockade (added 2026-07-14):* the
    Ottoman's Guile-type Ops action (§2.3), "diplomatic support −1,"
    **knocks the marker back 1 step** — the generic, re-drawable version of
    the suppressor cards above. This is what gives the Ottoman a standing
    way to contest the track every round they draw Guile, rather than only
    when a named suppressor comes up; it's the direct counterplay to the
    Byzantine's own Sue for Aid advances, so the marker becomes a genuine
    tug-of-war rather than a one-sided climb.
  - *Finality:* The Scout Ship's Return (Byzantine, Round 7+, Forced)
    **freezes the marker permanently** where it stands — no further
    advances, hope of relief is dead — alongside its Reserve Pool +1.

#### 4.0.6 Sortie Resolution — success roll + return fire (revised 2026-07-14, phase framing 2026-07-15)

The Byzantine **Sortie** Ops action — a sally out of the gates to burn or
wreck the Ottoman artillery (the besiegers' guns, including the great cannon) —
resolves in **two phases, exactly like an Assault (§6.5.3):** a **Volley
phase** (the return fire the raiders take crossing the open ground) and a
**Combat phase** (the raid's actual effect on the works). The
damage-allocation rule differs by phase, and this is the single place the
distinction bites (§6.3.1): **the mandatory-kill rule — "if a kill is
possible, one unit must be destroyed" — applies *only* in the Volley phase;
in the Combat phase the side taking damage distributes it however it
likes.** A stronger raiding party succeeds more often *and* takes more fire
on the way back — the historical gamble, legible in the dice.

- **The action:** Sortie costs **2 Ops** (§2.2). Commit any number of
  garrison units (and, optionally, one or more leaders) from the sallying
  sector to form the raiding force. **The only sortie target is *artillery*
  (revised 2026-07-15)** — the besiegers' guns, *including Orban's great
  cannon* if it is in play (the great cannon is artillery). Siege
  engines / saps are **no longer** a sortie target; countermining galleries
  is now solely John Grant's job (§4.0.7).
- **Success roll (Combat phase) — 1d10, succeed on `(11 − x)` or higher**,
  where **`x` = the raid's total attacking power** = the sum of committed
  units' **Attack** values (Clergy Levy's 0 adds nothing — no sortie
  capability, §6.1) **+1 per committed leader** and **+ card modifiers**.
  **A committed Byzantine general contributes only a flat +1 to `x`,
  regardless of his own combat stat (confirmed 2026-07-15)** — a captain
  leads and coordinates the raid but his personal leadership bonus does
  *not* apply as sortie attack power the way it would on a defended wall;
  the raiders' own Attack values do the work. A stronger raid needs a lower
  roll: `x = 3` → **8+**; `x = 5` → **6+**; `x = 8` → **3+**; `x ≥ 10` →
  auto-success; `x = 1` → only a natural 10.
  - On **success**, the works are wrecked — **Ottoman discards 1 card** (a
    one-shot Draw Track hit, §4.0); or, if the declared target was **the
    great cannon**, it is **silenced** — knocked out of action (it stops
    firing) rather than shattered. This is the one cannon-loss the Ottoman
    *can* re-cast, for 5 Ops (§2.1) — a sortie kill is enemy action, not
    the permanent self-burst. This is the Byzantine route to shutting down
    Orban's gun.
  - **Critical success (added 2026-07-15) — this is Combat-phase damage:**
    if the successful **success roll was a natural 9 or 10**, the raid also
    draws blood among the covering troops — inflict **1 step loss (on a 9)
    or 2 step losses (on a 10)** on Ottoman units at the target sector.
    Because this is the **Combat phase**, the **Ottoman (the side taking the
    damage) distributes these step losses freely** — no mandatory-kill
    restriction (that applies only to the Volley phase below). (*Design
    flag:* this is my reading of "on a 9/10, deal 1/2 damage to the
    defender" — the natural die showing 9→1, 10→2 step losses on the target
    force, on top of the normal success effect. Flag if you meant a
    different magnitude or a different target.)
  - On a **miss**, the raid achieves nothing — but the return fire below
    still applies, so a failed sortie can cost troops for nothing.
  - *Card modifiers to `x`:* **The Podestà's Dilemma** and **Sortie by
    Torchlight** each add **+2** to attacking power (their old target
    qualifiers dropped 2026-07-15 now that artillery is the only target —
    Torchlight is consequently under review as a likely duplicate of the
    Podestà); **The Siege Trench** halves `x` (round down) for the success
    roll. These cards' "+N Sortie attacking power" wording maps directly
    onto `x`.
- **Return-fire roll (Volley phase) — `y` d8, where `y` = the number of
  defence (garrison) units present in the sallying sector, capped at `max
  4d8`** (revised 2026-07-15 — was one die per committed unit, uncapped; now
  keyed to the sector's garrison presence and hard-capped to match the §6.3
  defender cap of 1–4). This is exactly the Approach/Volley mechanic
  (§6.5.3): **each die showing 7–8 inflicts one step loss** on the raiding
  force (a 1-step unit destroyed, a multi-step unit flipped). Because this
  is the **Volley phase, the Ottoman allocates these losses**, under the
  **mandatory-kill rule (§6.3.1): if a hit can complete a kill, it must**
  (revised 2026-07-15 — was Byzantine's choice). So the Ottoman focus-fires
  the raid's most valuable committed unit and is forced to finish it when
  able — the mirror of the Byzantine focus-firing Ottoman elites during an
  Assault's Volley. Leaders add no dice and are never hit — only garrison
  units are exposed. Expected losses = `y ÷ 4` (so at most 1 step on average
  at the 4d8 cap).
- The two rolls are **independent**: a raid can wreck the works and still
  bleed on the way back, or achieve nothing yet bring everyone home.
- **The trade-off:** committing more raises `x` (better odds), while the
  return fire is now bounded by the sector's garrison (max 4d8) — so a
  bigger sortie lands more reliably without runaway bleed, but a
  heavily-garrisoned sector always sallies into more fire.

*Placeholder numbers* (the 2-Ops cost, the `11 − x` threshold, the 7–8 hit
band, the 4d8 return-fire cap, the 9/10 critical-success magnitude) pending
playtesting. Shape chosen 2026-07-14 to reuse the Approach stage's d8
return-fire mechanic so the two combat systems rhyme; the return fire is
now capped at 4d8 (2026-07-15) to match the §6.3 defender cap. *Open knob:*
whether the raiding *force* (not just return fire) is also size-capped —
left uncapped for now; flag if it wants one.

**Balance note on Ottoman-allocated return fire (the "is this balanced?"
question, 2026-07-15).** Handing the Ottoman the raider-loss allocation
*with* a forced kill is the exact situation §6.3.1 deliberately avoided on
*defence* — it warned that letting the Ottoman pick would let them delete an
irreplaceable Byzantine elite (Genoese Company, Cretan Sailors — pools of
2 and 1) "almost on demand." On a Sortie that danger is real: commit a
Genoese unit to a raid, roll a single 7–8 on return fire, and the Ottoman
*must* kill it. My read: this is **balanced only as a deterrent** — it
correctly makes sending your scarce captains and elite companies on raids a
bad idea, pushing the Byzantine to sortie with expendable militia/Azap-tier
units (which, combined with the general contributing only +1, keeps raid
`x` modest). That's thematically right (raids are a gamble with expendable
troops), **but** if you find it makes Sorties a dead action — militia-only
raids rarely clear the `11 − x` bar — the fix is one of: (a) restrict the
mandatory kill to the **first hit only**, as in §6.3.1's first-point rule,
rather than every 7–8; (b) let the **Byzantine** protect one designated
unit per raid; or (c) exempt named elite units from the forced kill. Flag
which, if any, after playtest. As written, the rule is implemented exactly
as directed: Ottoman allocates, mandatory kill, Volley phase only.

#### 4.0.7 Sap/Mine Resolution — commit-and-fire mining (added 2026-07-13, reworked 2026-07-15)

The Ottoman **Sap/Mine** Ops action (the Guile action, funded by Guile
generic cards, §2.3) drives a gallery beneath a wall sector to collapse it
from below — the one way to breach masonry *fast*, bypassing the slow
round-by-round Bombard-vs-Repair race. How well it works is driven by how
many troops the Ottoman is willing to bury in the dig.

- **Open a gallery (2 Ops):** choose one land sector and **commit 1–3
  Ottoman units** to it, placed at the sector as *sapping*. **Mining
  Strength `M` = the *number* of units committed (max 3)** — reworked
  2026-07-15, was the units' combined Attack; unit *quality* no longer
  matters underground, only bodies in the dig, so cheap Bashi-bazouks are
  now the natural sappers. Committed units are **tied up**: while sapping
  they cannot Assault, support Bombard, or move (they are underground).
  **Only one *new* gallery may be opened per round.** Galleries at more
  than one sector may stand simultaneously (opened across successive
  rounds); a later Sap action may still **add units to an existing
  gallery** (raising its M, never above 3).
- **Effective Mining Strength `M_eff` = M − the target sector's sap penalty**
  (§3.1: Blachernae 0, St. Romanus −1, all others −2), floored at 0. Every
  threshold below is keyed to `M_eff`, so *where* you dig matters as much as
  *how many* you commit.
- **The dig roll — 1d10, rolled for each standing gallery once per round**
  (a new gallery rolls immediately on opening; an already-standing gallery
  keeps digging and rolls again each round without further Ops cost — so
  with several galleries standing, more than one sap roll can happen in a
  single round even though only one *new* sap may be attempted):
  - **≥ (11 − M_eff) → the charge blows.** The target sector loses **3 Wall
    HP at once**, and this loss **may cross a band boundary** (Intact →
    Battered → Breached, §3.1) — a mine breaches in a single blow, unlike
    gradual Bombard. The gallery is spent; its units survive and are freed.
    The roll is deliberately *reversed* from the old ≤ M form so high rolls
    are always good for the roller, consistent with every other d10.
  - **≤ (5 − M_eff) → a digger dies.** The tunnel partially collapses:
    **one committed unit is destroyed** (Ottoman's choice which). The
    gallery itself **persists** and keeps digging (its M drops by the lost
    unit). So a bigger, better-placed dig is *both* likelier to blow *and*
    less likely to bleed — expertise and mass push the death band down as
    they push the success band down. (*Design flag:* I've read "a unit
    dies" as the gallery surviving at reduced M rather than caving in
    entirely — flag if you wanted the whole gallery lost.)
  - **Everything in between → nothing yet.** The dig hits rock or water —
    no damage. The gallery and its M **persist** into the next round (keep
    digging, roll again) — the window the Byzantine counterplay exploits.
  - **Worked bands (M = 3 committed):** at **Blachernae** (`M_eff = 3`) →
    blows on **8+**, digger dies on **1–2**; at **St. Romanus**
    (`M_eff = 2`) → blows on **9–10**, dies on **1–3**; at the three
    triple-wall sectors (`M_eff = 1`) → blows on a **10 only**, dies on
    **1–4**. With **Zaganos Pasha** present the gallery digs at **M + 1**
    *before* the sap penalty (so a 3-unit gallery under Zaganos at St.
    Romanus is `M_eff = 3` → blows on 8+).
- **Exposed underground (the Byzantine counterplay):** a standing gallery
  is vulnerable. **John Grant's Countermine** (EVENT_DECK Byz #2, reworked
  2026-07-15) may be played *immediately, at any moment* — even during the
  Ottoman's turn — to **permanently seal two land sectors against sapping**:
  any active galleries at the two chosen sectors are destroyed (their
  committed units killed underground), and **the Ottoman may never open a
  gallery at either sector again for the rest of the game.** (The old
  "Sortie targeting siege engines" counter was removed 2026-07-15 — Sorties
  now target artillery only, §4.0.6 — so **John Grant's Countermine is the
  sole way to destroy a standing gallery**, on top of the dig's own
  digger-death rolls.) This is the price of a multi-round dig: every round a
  gallery stands unfired is a round the countermine can catch it.
- **Zaganos' Sappers** (EVENT_DECK Ott #1, reworked 2026-07-15): while
  Zaganos Pasha is present at the gallery's sector, that gallery adds **+1
  to M *before* the sector's sap penalty** (so `M_eff = M + 1 − penalty`).
  A full 3-unit gallery under Zaganos blows on **7+** at Blachernae, **8+**
  at St. Romanus, **9–10** at a triple-wall sector — one band better than
  the same dig without him, and its higher `M_eff` also shrinks the death
  band. Expertise buys both reach and safety.

*Placeholder numbers* (the (11 − M_eff) thresholds, 3 Wall HP per blow, the
(5 − M_eff) death band, the per-sector penalties) pending playtesting,
consistent with the rest of §4. **Design shape (2026-07-15):** M = unit
*count* capped at 3 keeps the knob coarse and legible and stops
attack-value stacking; the per-sector penalty (§3.1) makes success span a
clean 10%→40% range (a 10-only dig at the triple walls up to 40% under
Zaganos at Blachernae) so *where* you tunnel is a real choice; success and
survival move together (higher `M_eff` raises the blow chance and lowers
the death chance at once); the per-round free re-roll makes a standing
gallery a ticking clock the Byzantine must answer rather than a one-shot
gamble; and the (5 − M_eff) death band bleeds a long or badly-placed dig so
parking galleries forever isn't free. **Flag:** (a) *interpretation* — the free
per-round re-roll for standing galleries is my reading of "existing saps
may still roll"; if you instead want each re-roll to cost a fresh Sap
action, say so and the counterplay window widens a lot. (b) Third Tunnel
(old Ott #17) has been **removed from the deck** and its slot refilled by
**Mahmud Pasha's Push** (2026-07-15); Zaganos' Sappers is re-pointed as
above, closing the old "mine cards hit Garrison" inconsistency.

#### 4.0.8 Repair Resolution — die roll (added 2026-07-15)

The Byzantine **Repair** Ops action (a Supplies-type action, §2.3) is no
longer a guaranteed flat restore; like the Great-Cannon shot (§2.1), the
Sortie (§4.0.6) and the Sap (§4.0.7), it now resolves on a die, so the
round-to-round Bombard-vs-Repair race carries real variance instead of a
fixed outcome. (Decision 2026-07-15, per user steer to move Repair off a
"free"/automatic restore.)

- **Repair (2 Ops):** choose one land sector below the top of its current
  status band (§3.1) and roll **1d10**:
  - **1 → the work is undone** — 0 Wall HP restored (masons scattered, a
    fresh section slumps back).
  - **2–7 → 1 Wall HP restored.**
  - **8–10 → 2 Wall HP restored** — a good night's work.
  - Restoration is **capped at the top of the sector's current band**
    (§3.1); overflow is wasted, and a Breached sector already at band-top
    gains nothing (only *The Stockade at the Breach* adds defense there).
- **Expected ≈ 1.2 HP per Repair** — deliberately just above a single
  Bombard shot's flat 1 HP, so a committed defender can *occasionally*
  out-repair one shot (the 8–10 double) at the cost of a 10% whiff, rather
  than losing the race by a fixed margin every round. It still can't keep
  pace with a full 3–4-shot barrage plus the great cannon — the wall is
  still meant to grind down.
- **Modifiers:** cards reading "+N extra Integrity on Repair" (Night
  Repairs, Orban's Offer / Byzantine branch) add **+N to the HP restored**
  after the roll (still band-capped unless stated); **The Walls Endure**
  lets one Repair's result bypass the band ceiling once; **Under Siege of
  Sound** (Ott 16) **blocks Repair entirely** that round (no roll at all).
- **Concentration (§2.3):** N Supplies cards spent on Repair roll it **N
  times** (sum the HP, still band-capped) — the die-roll form of the "N×
  Integrity" entry in the §2.3 table.
- **Stockade — converting a band-topped Repair into standing defense (added
  2026-07-16):** when the chosen sector is already at the **top of its
  current status band** (HP maxed for its current state, so a normal Repair
  would restore nothing, §3.1), the Repair action may instead **erect a
  Stockade** there — a **+1 Wall Defense** modifier (§3.1/§6.4), the
  improvised timber-and-rubble breastwork of the kind Giustiniani threw up
  at the Mesoteichion breach. This is the defender's relief valve for a
  band-topped wall Repair can no longer help:
  - **One Stockade per sector** at a time — a second may not be stacked
    while one stands. It does **not** stack with the card *The Stockade at
    the Breach* (EVENT_DECK.md), which grants a stronger **+2** modifier
    directly; when both would apply, use the higher (+2), not the sum.
  - **Removal — normal:** a Stockade is removed the moment the sector
    **drops into the next lower band** (Intact→Battered or
    Battered→Breached) — the degrading wall overruns the breastwork. So a
    Stockade erected while Intact or Battered is fragile; it is worth the
    most at the breach.
  - **Removal — Breached exception:** a Stockade on a **Breached** sector
    (no lower band beneath it) instead stands until the sector's **HP is
    ground to 0.**
- **Repairs per round scale with the Reserve Pool (added 2026-07-16).** Wall
  repair needs hands, and those hands are the same militia well the Reserve
  Pool (§4.1) tracks — so the number of **Repair actions the Byzantine may
  take per round is capped by the Reserve Pool level**, each still resolved
  on its own 1d10 (above):
  - **Reserve Pool above half → up to 3 Repairs per round.**
  - **Reserve Pool at or below half → up to 2 Repairs per round.**
  This cap sits **on top of** the normal 2-Ops Supplies cost per Repair
  (§2.2) — low reserves throttle repair *capacity*, not just reinforcement.
  The threshold is marked on the Byzantine player board by the
  'Free repair −1' box at the last slot of the full-strength 1/1 militia
  block (the 15th reserve slot). (*Design flag:* the
  original note gave overlapping "≤ half → 3" and "< half → 2" thresholds;
  I've read that as a single half-threshold two-tier cap — **3 above, 2
  at/below**. Say if you wanted a third, lower band, e.g. dropping to 1
  Repair/round when the pool nears empty.)

*Placeholder numbers* (the 1 / 2–7 / 8–10 bands) pending playtest, tuned to
sit just above Bombard's flat 1 HP.

#### 4.0.1 Deployment from the Ottoman pool (replaces Mustering, §6.1)

**Overhauled 2026-07-15 — the Ottoman no longer *musters* (creates) units
from the card economy. Instead the army's manpower already exists as a
pool of *uncommitted* units off-board; the Ottoman player *deploys* them
onto the map.** This models the historically huge besieging host that was
already gathered — the constraint is getting the right troops into the
right sector at the right time, not raising them.

- **The pool — elites only (clarified 2026-07-15):** the finite pool of
  uncommitted units covers **Janissaries and Solaks only**. (Exact pool
  composition is a setup number, pending the §6.1 order-of-battle pass;
  Solak's 2 tokens live here from the start, resolving the old "Solak has
  no muster path" flag below.) Elite units removed in combat are gone; the
  pool only ever shrinks. **Bashi-bazouk, Azap, and New Levy are *not*
  pool-limited** — they come from open supply (effectively unlimited
  counters), modelling the host's bottomless irregular manpower; what
  gates them is the Deploy allowance below, not a finite stock. (This is
  why e.g. Fresh Reserves from Anatolia freely fielding 4 Azap + 4
  Bashi-bazouk doesn't contradict the shrinking-pool rule — those types
  were never pool-counted.)
- **Deploy action (a Supplies-type card / Ops action, §2.3):** one
  Deployment brings units from the pool onto the map at a legal staging
  sector. Per Deployment card, you may field **either**:
  - a **minimum of 2 units** (any units, regardless of their Attack), **or**
  - any number of units whose **combined Attack ≤ 5**,
  whichever lets you deploy more. So a single card always lets you land at
  least 2 units — even 2 elite Solaks — *or* flood a batch of cheap
  irregulars (e.g. up to 5 Bashi-bazouk at Attack 1) when you want mass
  over quality. This replaces the old per-unit tiered card cost entirely.

**Deploy also handles upgrades and elite recovery (resolved 2026-07-17):**
- **Upgrades (New Levy → Janissary)** are folded into the Deploy action:
  in place of fielding fresh units, a Deploy may **upgrade fielded New
  Levies where they stand**, each upgrade counting as a **3-Attack** deploy
  against the allowance above — so one Deploy upgrades **up to 2** New
  Levies (via the ≥2-units branch). No separate upgrade action.
- **Elite recovery** is likewise a **Deploy** action now (replacing the old
  *Replenish* standing action and the earlier Weight-of-Numbers-only
  routing): a Deploy may instead **return up to 2 destroyed
  Janissary/Solak units** to the board, same ≤2-per-card cap. A
  Deploy-recovery does **not** touch the Elite Casualty pool counter — the
  units simply reappear, and the next kill resumes the ratchet as normal.
  Drawing the counter *down* (buffering Morale) stays unique to **Weight of
  Numbers** (§4.0.4), which is what that card's 3-Ops cost now buys
  (resolved 2026-07-17).
- **Replenish as a standing action has been dropped (2026-07-15).**
- **Solak** is pre-seeded in the pool (see above), so it needs no special
  muster path.

**Design history (superseded by the pool model above, 2026-07-15):** the
prior model was a tiered *mustering* economy — pay N discarded cards to
raise units, with per-tier ratios (Bashi-bazouk 3/card, Azap and New Levy
1/card), Janissaries fielded *only* by upgrading a New Levy (no fresh
muster), Solak unmusterable, and a **Replenish** action (1 card to restore
a flipped Janissary/Solak to full step count). The pool-and-deploy model
folds all of that away: units aren't *raised* anymore, they're *deployed*
from a pre-existing pool under the ≥2-units-or-≤5-combined-Attack allowance.
Upgrades are now folded into the Deploy action (resolved 2026-07-17, above);
**Replenish as an action is dropped**, its elite-recovery role likewise
folded into Deploy (return up to 2 destroyed elites per card). The New-Levy-first training bottleneck and
Solak-from-start intent both carry over — Solak now simply starts in the
pool.

#### 4.0.2 Mehmed's Combined Arms

Combined Arms (§6.2, +2 Attack when leading an Assault at a cannon-sited
sector) now **costs 1 discarded card to activate** — a real spend of your
hand each time, not a free passive.

#### 4.0.3 Second Barrage

**Redefined 2026-07-16 — Second Barrage *is* the Attack-card Bombard, not a
combat buff.** In play, "Second Barrage" is simply the general name for an
**Attack-type card funding an extra Bombard action against a wall sector**
in the Card Phase (§2.3) — the besiegers laying a fresh supporting barrage
to grind masonry. It is **purely structural**:
- Targets **wall strength only** — no combat effect, no Attack bonus to any
  Assault, no effect on wall *status* beyond the HP it removes.
- Resolved on a **1d10: 1–3 nothing, 4–10 = 1 Wall HP — capped at 1 HP.**
  Unlike Orban's great cannon (§2.1) it gets **no 9–10 breaching bonus
  (never 2 HP) and no burst check**: a generic supporting barrage can wear
  a wall down but **cannot land the single 2-HP breaching shot that only
  the great bombard is capable of.** (1-HP cap added 2026-07-16 — the 2-HP
  result is now exclusive to Orban's Great Cannon.)
- Under Concentration (§2.3), N Attack cards fire **N separate 1d10 rolls**,
  each still capped at 1 HP — but subject to the per-sector cap next.
- **One Second Barrage per sector per round (added 2026-07-16).** Second
  Barrage may be played **any number of times a round** (each its own Attack
  card), but **each wall sector may be targeted by at most one Second
  Barrage per round.** A sector already takes its Phase-A bombard(s) and, if
  applicable, the great-cannon shot; the Card Phase may add **one** further
  supporting barrage to it, no more. Multiple Second Barrages in a round
  must therefore be **spread across different sectors** — and a Concentrated
  stack of N Attack cards fires its N rolls at **N different sectors**, not
  N times at one wall.

**Not to be confused with Combined Arms (§4.0.2)** — that is Mehmed's
*combat* ability: when Mehmed leads an Assault at a cannon-sited sector, the
Ottoman may discard 1 card for **+2 Attack to that Assault**. Combined Arms
= combat; Second Barrage = wall damage. Two unrelated levers that each
happen to cost a card.

#### 4.0.4 Morale (revised this session — track size and gain/loss sources)

- **Morale** (janissary/army will to fight + Sultan's political capital to
  keep the siege going against court opposition) — **track runs 0-8,
  starting at 7 (full strength), hard-capped at 8.** The one point of
  headroom above the 7 start means the single Morale-gain card (Hadith of
  Conquest, below) is **never wasted** — it always lands as a real 7→8
  step rather than overflowing a full track, which is the point of the
  cap sitting at 8 rather than at the starting value.
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
    - **The Morale drops ratchet; the counter itself can move down (added
      2026-07-15 for Weight of Numbers).** Track two things: the **running
      counter `P`** (elite Attack value lost) and the **Morale-lost level
      `L`** already inflicted. `L` only ever *rises* — Morale lost to this
      pool is never refunded. Normally `L` climbs to `floor(P / 5)` as `P`
      grows. The **one** effect that reduces `P` is **Weight of Numbers**
      (EVENT_DECK Ott #22, now 3 Ops): returning destroyed elites to the
      board subtracts their Attack value from `P` **but leaves `L`
      unchanged**. (A *plain* Deploy-recovery, §4.0.1, also returns up to 2
      destroyed elites, but does **not** touch `P` — the units come back
      while the counter keeps climbing on the next kill. Buying `P` down is
      what separates Weight of Numbers from routine recovery and justifies
      its higher cost.)
      After such a reduction the next Morale drop fires only when `P` climbs
      back up to `5 × (L + 1)` — the recovered points are a *buffer before
      the next drop*, not a Morale refund. *Worked example:* `P = 16` →
      `L = 3` (Morale −3, since 16 has crossed 15). Weight of Numbers takes
      8 points back → `P = 8`, but `L` **stays 3** (Morale still −3, not
      −1). The **−4** drop now waits until `P` reaches 20 again — another
      **12** points of destroyed elites — so the Byzantine must re-kill
      roughly those two formations before Morale resumes falling.
- **Morale hitting 0 → the Ottoman army lifts the siege → immediate
  Byzantine win.** This is the sole hard-loss track for the Ottoman side.
  Note this isn't the *only* way Byzantine wins — reaching round 9
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
unconditional). Reasoning: the round-limit auto-win at round 9 above
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

**Track size confirmed this session: 0-8, starting at 7.** Against the
+1 max from a named card (Hadith of Conquest — now genuine headroom to
8, never a wasted overflow) and the
drains above (Four Ships -2, Halil Pasha's Doubt -1 plus its structural
squeeze, the Elite Casualty pool's -1-per-5 ticks, and occasional
Pressure to Attack penalties), a full 7-point swing down to a Byzantine
win is crossable but not trivial over 9 rounds — still first-draft
pending playtesting, but no longer an open question.

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
- The pool has **one graduated depletion penalty** (added 2026-07-16):
  when it falls **to half or below, Byzantine Repair capacity drops from 3
  to 2 actions per round** (§4.0.8) — fewer hands in the city means fewer
  wall sections worked each week. That single step aside, there are no other
  debuff bands: running low otherwise just means fewer tokens on hand to
  spend, and the only hard threshold is empty (below). (The Ottoman Morale
  track, by contrast, keeps a fuller set of graduated bands, §4.0.4 — that
  track is a hard loss condition, so texturing its decline earns its keep.)
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
  the siege runs (9).

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
- **Byzantine wins:** Survive to the end of round 9 without losing an
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
  flavor for a future defensive counter-sapper card). He is the natural
  leader for Assaults on the Golden Horn sector, reflecting his actual
  area of command. *(The old "Engineering" ability — Sap/Mine costs 1 less
  Ops when he is present — was removed 2026-07-17.)*
- **Karaca Pasha**: **+1 Attack.** Beylerbey of Rumelia, commanded the
  European/Balkan troops, historically positioned toward the **northern**
  end of the line. **Northern Command:** +1 further Attack when leading
  an Assault on Blachernae or Charisius. He **survived** the 1453 siege
  and was killed three years later at the **Siege of Belgrade (1456)** —
  *corrected 2026-07-17, fact-checked against Wikipedia.* The earlier
  note here (“killed by fire from the walls,” proposed as a mid-game
  “Karaca Pasha Killed” Morale event) was based on a mistaken death date
  and has been dropped. No major statted Ottoman commander actually died
  during the siege of Constantinople, so there is no clean historical
  mirror to Giustiniani’s wounding on the Ottoman side — the nearest
  honest alternative is the Baltaoğlu naval-disgrace beat noted below.
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
  (whichever single foreign leader is present) — no coordination gate, but
  this mix now incurs **Faction Discontent** (below) unless a coordinator
  (Constantine anywhere, or Notaras at the Golden Horn) is present to
  unify it.
- **Combining two or more different foreign contingents in the same
  Defense requires Constantine XI present in that sector.** Only the
  Emperor has the standing to coordinate rival factions together — no
  other leader can.
- **Exception: Notaras at the Golden Horn.** As Megas Doux he may command
  any mix of units present at that specific sector without needing
  Constantine — the one deliberate crack in an otherwise strict rule,
  reflecting his real naval authority there (§6.2).
- **Faction Discontent — mixed defenses fight at odds (added 2026-07-17).**
  Whenever a single Defense contains units *or* leaders of **more than one
  faction** — e.g. Roman militia standing under a Venetian leader, or
  Genoese and Venetian troops side by side — the rival contingents bicker
  over precedence. The defender must **pick one faction to favour:** that
  faction's units (and its matching leader's Defense bonus) fight at
  **full** Defense, while **every other faction's Defense contribution is
  halved, rounded up.** A **coordinator cancels it entirely:** with
  **Constantine XI** present (any sector) or **Notaras at the Golden
  Horn**, there is *no* discontent and the whole mixed stack fights at full
  strength. This is what makes those two special — not merely *permission*
  to combine contingents, but the only way to combine them *without* the
  half-strength tax. *Worked example:* a Venetian leader (+1 Def) with 2
  Roman militia — side with the Romans and the militia defend in full while
  the leader's bonus halves (⌈1/2⌉ = 1, so no change at +1); side with the
  Venetian and his +1 stands while the militia's Defense halves, rounded
  up. *(Rounding and whether a favoured leader's bonus is itself subject to
  the tax are tunable — flagged for playtest.)*
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
  Golden Horn) — for the rest of the game, taking effect from the round
  *after* it is played (§4.0 effect-timing) rather than the current round**,
  as the Sultan commits to the final all-out push.
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
- **Two phases — where Mandatory Kill applies (framing clarified
  2026-07-15):** an Assault (and a Sortie, §4.0.6) resolves in a **Volley
  phase** (Approach / Defenders' Fire, §6.5.3 — the pre-contact ranged
  fire) followed by the **Combat phase** (the main mutual clash, §6.5.2).
  **The Mandatory Kill Priority below applies *only* in the Volley phase.**
  In the **Combat phase there is no forced kill at all** — the assigning
  player distributes every step of that phase's damage however they like
  (the defender freely distributes their own garrison losses; the Byzantine
  still assigns the Ottoman's Combat losses per the first bullet above, but
  now with no mandatory-kill constraint on any of it). Who *allocates* is
  unchanged; only the forced-kill constraint is now phase-scoped.
- **Mandatory Kill Priority (Volley phase only — applies to
  only the first point of damage):** whichever player is assigning the
  Volley's steps lost (in an Assault: the Byzantine, firing on the
  approaching Ottoman; in a Sortie: the **Ottoman**, returning fire on the
  raiders — §4.0.6) must spend the **first point** of any roll's damage
  completing a **confirmed kill**, if one is
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

### 6.3.2 Post-Assault Recovery (added 2026-07-15)

**Any unit or leader that takes part in an Assault is *Recovering* for the
following round.** When an Assault resolves, mark every piece that fought it
— **both** the attacking units/leaders **and** the defending garrison
units/leaders committed to that sector. During the **next round**, a
Recovering piece:

- **may not be committed to an Assault**, and
- **may not be Moved** (the Move action, §2.3) — it is regrouping, tending
  wounded, redistributing shot and ladders.

The marker clears at the end of that next round, so the piece is free again
the round after. **A Recovering defender that is itself assaulted again
still defends its own sector normally** (it cannot refuse a defense, and its
Wall/Naval Defense and garrison count as usual) — Recovery only bars
*initiating* movement, a Sortie, or joining a *new* Assault elsewhere; it
never pulls a unit off the wall it is standing on.

**Why:** this stops either side from hurling the exact same stack at the
wall every single round. It turns the Ottoman's numerical mass into a real
rotation problem — you need fresh troops (Deploy, §4.0.1) to keep pressure
up round after round, the historical pattern of committing wave after wave
of *different* formations — and it gives the Byzantine a reason to husband
and rotate a thin garrison rather than fight the same companies to
exhaustion. It also pairs with the deferred Force Commitment Cap / forced-
assault changes (§4.0): tempo is now something you plan a round ahead.

*(Design flags: (a) applied to **both** sides' committed forces — say if
you meant only the attacker. (b) A Recovering defender keeps full Defense if
re-assaulted; only its own movement/sortie/other-sector commitment is
suspended. (c) Leaders recover too, per "armies + generals." (d) Placeholder
duration of exactly one round — flag if a heavy Assault should recover
longer.)*

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

> **Ratio-indexed CRT removed (2026-07-13).** The odds-ratio table that
> used to sit here has been retired in favour of the **difference / margin
> CRT (§6.5.2)**, which is now the single adopted Assault table. The margin
> index breaks up the wide 3:2 ratio column that was swallowing the real
> +2-to-+8 play band, so concentrating attack is visibly rewarded where the
> game is actually played (full reasoning in §6.5.2). The prose below is
> retained as the shared combat-design rationale — Sector Falls, Wall
> Defense as a pure modifier, the capacity targets, and the tuning history
> — all of which still feeds the surviving table. A printable player aid for
> the two adopted tables lives at [artifacts/combat_crt.html](artifacts/combat_crt.html).

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

Average steps lost per roll (of the retired ratio table, kept for the
tuning-history record): bad ratio punished the attacker hardest (avg
Atk ~1.8 / Def ~0.5 at 1:2-or-worse), good ratio the defender hardest
(avg Atk ~1.0 / Def ~3.0 at 4:1+). The adopted margin table (§6.5.2)
carries the same shape onto a difference index.

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

### 6.5.2 Assault CRT — Difference / Margin table (adopted 2026-07-13; revised for the +2-to-+8 play band, 2026-07-12)

**This is now the adopted Assault CRT** (the ratio table at §6.5 was
retired 2026-07-13). The design intent is explicitly a **war of
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
Ottoman assaults at a negative margin). **The far-left `< -3` column (added
2026-07-15) splits the old "≤ 0" band in two** — a genuinely hopeless
assault (attacker outmatched by 4+) now bleeds even harder (avg Atk 2.5,
Def ~0.1) than a merely bad one, deterring desperate throws at a fully
intact, well-garrisoned wall while keeping the "a better result is never
worse" monotonicity intact.

This is a **mutual-damage** table — every cell is **Atk-x / Def-y**: the
Attacker loses *x* committed steps and the Defender loses *y* Garrison
steps. The **Approach / Defenders' Fire** stage (§6.5.3) is a *separate,
additional* step that resolves **first** and only ever hurts the attacker
(extra casualties + force reduction); this table is the main clash where
both sides bleed.

**Procedure:** resolve Defenders' Fire (§6.5.3 — the Volley phase) first and
remove its casualties; then compute **Margin = surviving Attacker Strength −
Defender Strength**, find its band, roll **1d10** (same flat single die as
§6.4/§6.5), and read **Atk-x / Def-y**. Attacker steps lost → Draw Track
step-down + Elite Casualty pool; Defender steps lost → Garrison damage,
Sector-Falls check, Commander Casualty (§6.5.1). **This is the Combat
phase, so both sides' step losses are distributed freely by their owners —
no Mandatory Kill Priority here** (that binds only in the Volley phase,
§6.3.1); the Byzantine still assigns the Ottoman's Combat losses per §6.3.1,
now without the forced-kill constraint.

| Roll | < -3 | -3 to 0 | +1 to +2 | +3 to +4 | +5 to +6 | +7 to +8 | +9 to +11 | +12 or more |
|---|---|---|---|---|---|---|---|---|
| 1 | Atk-3/Def-0 | Atk-3/Def-0 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-2/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 |
| 2 | Atk-3/Def-0 | Atk-3/Def-0 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-2/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 |
| 3 | Atk-3/Def-0 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 |
| 4 | Atk-3/Def-0 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-2/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 |
| 5 | Atk-3/Def-0 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 |
| 6 | Atk-2/Def-0 | Atk-2/Def-0 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 |
| 7 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 |
| 8 | Atk-2/Def-0 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-4 |
| 9 | Atk-2/Def-0 | Atk-1/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-4 |
| 10 | Atk-2/Def-1 | Atk-1/Def-1 | Atk-1/Def-2 | Atk-1/Def-2 | Atk-1/Def-3 | Atk-1/Def-3 | Atk-1/Def-4 | Atk-1/Def-4 |

Average steps lost per roll (Atk +0.2 / Def −0.2 tweak applied to the +3-4
through +7-8 combat bands this session — Ottoman bleeds slightly more, the
Byzantine slightly less, where play concentrates):

| Band | Avg Atk | Avg Def | Net (2·Def − Atk) |
|---|---|---|---|
| < -3 | 2.5 | 0.1 | −2.3 |
| -3 to 0 | 2.0 | 0.4 | −1.2 |
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
  non-decreasing — the net ladder climbs **−2.3 → −1.2 → +0.5 → +1.2 →
  +2.3 → +3.4 → +4.8 → +5.6** — so a higher roll or a bigger margin can only
  ever improve the Ottoman's weighted outcome. Conventional shape: attacker
  loss highest at the worst results, tapering to 1; defender loss rising to a
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

**An Assault resolves in two phases** (the same two-phase structure a
Sortie uses, §4.0.6):

1. **Approach — the Volley phase (this stage, Byzantine rolls):** as the
   attackers cross the ditch under fire, the defenders shoot them up —
   **extra attacker casualties**, removed *before* the clash (which also
   drops the survivors onto a lower §6.5.2 margin). This stage **only ever
   hurts the attacker** — a defender-favouring bonus layer, not the main
   combat. **This is the one phase where the Mandatory Kill Priority
   (§6.3.1) applies.**
2. **Assault — the Combat phase (§6.5.2, mutual):** the main clash on the
   Atk/Def margin CRT, where **both** sides take steps. **No mandatory kill
   here** — each side's losses are distributed freely (§6.3.1).

**Procedure:** the Byzantine rolls **one d8 per garrison unit committed to
the defence** (x dice, x = 1–4, the §6.3 defender cap). Each die showing its
**top two faces (7–8)** inflicts **one attacker step loss**, assigned per
§6.3.1 (mandatory kill priority, focus-fire). Wall/Naval Defense are *not*
dice — they stay flat modifiers to the §6.5.2 margin.

**Sea sectors have no Approach phase (decided 2026-07-14).** The Golden
Horn (§3.2) skips this stage entirely — a shipborne escalade crosses no
fosse into a prepared killing ground, and the sea wall has no HP band to
key the die count off anyway. Its flat Naval Defense 3 *is* the sea's
whole "hard to storm" tax, folded into the §6.5.2 margin; there is no
separate defenders'-fire roll at the Golden Horn. (Planned hook: a future
Byzantine card — working title *Ready the Sea Walls* — will grant the
Golden Horn a *reduced* Approach roll of **⌈n∕2⌉ d8** for that assault,
where n = garrison units committed there, i.e. half the land rate rounded
up. Not yet written; the user will design it.)

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
   (Powers Stirring track: 2 Ops, roll 1d10, 6+ advances a 0→5 marker,
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
