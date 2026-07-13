# Constantinople 1453 — Event Deck (Draft v0.1)

Companion to [DESIGN.md](DESIGN.md) — see §2.2 there for how the Card Phase
works (each round, both players are dealt a hand of 8-9 cards: ~5-6 from
the shared Neutral pile, ~3-4 from their own designated pile; each card is
playable for its Event text *or* its Ops value, never both), §2.3 for the
generic 1-Ops Attack/Supplies/Move action cards (actual card content
below, in their own section — these make up most of the Neutral-pile
draw), and §2.4 for the revised 1-5 Ops value scale used below. §6.5 also
has a significant revision: Assault resolution is now a mutual-damage
system (both sides take losses on most rolls) rather than a single
categorical result — "Repulsed" is gone from the rules entirely, replaced
by "Attacker/Defender steps lost."

## Deck Structure

- **Ottoman pile** and **Byzantine pile**: cards whose Event **benefits
  the owning player**, full stop — not "represents that player's own
  agency." Those aren't the same thing, and conflating them was a bug in
  earlier drafts: a card lives in a pile because playing its Event helps
  that side, regardless of whose historical action triggered it. A
  designated-pile card whose Event actively hurts its own owner is dead
  weight — a rational player will simply never choose Event over Ops for
  it, wasting the card's design. (Fixed 2026-07-09 — see the corrected
  Ottoman/Byzantine tables below; The Union's Discontent and The Fallen
  Icon moved from Byzantine to Ottoman, Trial by the Chain reworked into
  a Byzantine card as The Chain Holds.) No fixed card-count target for
  now — add as many as make sense; trim to a clean per-round draw number
  later if desired.
- **Neutral pile**: shared, double-edged, or complication-style cards
  (weather, disease, court politics) that don't clearly belong to one
  side's agency. Target ~30-40 unique cards, with the discard pile
  reshuffled back in once exhausted rather than writing ~100 one-offs.
- **Ops values** (revised 2026-07-10 — see DESIGN.md §2.4 for the full
  scale): named Event Deck cards now range **2-5 Ops** (2 minor, 3
  moderate/default, 4 major, 5 reserved for a small handful of pivotal,
  story-defining beats), widened from the original 1-3 scale specifically
  so a genuinely pivotal card feels heavier than two generic filler
  cards stapled together. Plain 1-Ops generic action cards (Attack /
  Supplies / Move, DESIGN.md §2.3) are a separate, non-narrative layer
  underneath this deck — most of the "5-6 from the Neutral pile" draw
  each round is those, not the named cards below. Only a representative
  set of the most obviously pivotal cards has been rescaled into the new
  2-5 range so far (the Forced tier below, mostly) — the rest of the
  deck still needs a full pass against the new scale.
- **Gating tags** used below:
  - **[Round N+]** — not shuffled into its pile until round N.
  - **[Requires: X]** — only playable as an Event once game-state X is true
    (still usable for Ops value beforehand).
  - **[Dual-Use]** — lives in the Neutral pile, but has *two separate Event
    texts* depending on which side plays it. These are for genuinely
    contested history — Galata's neutrality, Janissary pay grievances —
    where both sides have a plausible angle on the same underlying
    tension, so ownership by one pile would be arbitrary.
  - **[Forced]** (added 2026-07-10) — must be played as its Event
    immediately, the moment it's drawn: no banking it for Ops value, no
    holding it to time later. Reserved for fixed historical beats that
    happened on their own regardless of what either player "wanted" —
    the Golden Horn Manoeuvre, a lunar eclipse, a real ship's return —
    as opposed to cards representing a strategic choice a player weighs
    (which stay optional Event-or-Ops, even when the underlying history
    is real, e.g. Terms of Surrender is a real offer but playing it is
    still a choice). Not currently combined with [Requires: X] — if a
    Forced card's prerequisite isn't met when it would otherwise resolve,
    that interaction isn't defined yet (see Open Questions).

## Generic Action Cards

The actual card content behind DESIGN.md §2.3 — these make up the bulk of
every round's Neutral-pile draw, sitting underneath the named cards
below rather than replacing them. Each is worth a flat **1 Ops**, no
Event text, and is typed to a specific action (full value on-type, 2-for-1
discard penalty off-type — full rule in DESIGN.md §2.3):

| Type | Ops | Ottoman action it fuels | Byzantine action it fuels |
|---|---|---|---|
| **Attack** | 1 | Assault | Sortie, Fire-ship raid |
| **Supplies** | 1 | Diplomacy | Repair |
| **Move** | 1 | Muster Reinforcements | Reinforce — puts one troop on the board at a sector, spending a Reserve Pool token (§4.1); this is the actual mechanical content behind Reinforce regardless of which card pays for it |
| **Guile** | 1 | Sap/Mine | Sue for Aid |

Proposed pool size: **8 copies each of Attack/Supplies/Move (24 cards),
6 copies of Guile** — 30 generic cards total, mixed into the physical
Neutral pile alongside the 23 named cards below, bringing the full
Neutral pile to ~53 physical cards before any reshuffling. Guile is
deliberately fewer copies than the other three — Sap/Mine and Sue for
Aid should still feel less routine than the "big three" actions, just no
longer permanently locked out of an efficient funding path the way they
were with only 3 types. All counts are placeholders pending playtesting.

## Ottoman Pile (no fixed target for now — trim to a clean draw number later)

Grouped 2026-07-11: cards with no round restriction first, then round-
gated cards in ascending round order.

| # | Card | Ops | Event |
|---|---|---|---|
| 1 | **Zaganos' Sappers** | 2 | Zaganos Pasha's miners drive a gallery beneath the ramparts, prising at the foundations. Automatically succeeds against one chosen sector's garrison (small Garrison step loss), if Zaganos Pasha is present. |
| 2 | **Demand Tribute** | 3 | Byzantine Reserve Pool -1 token, or Ottoman draws 2 extra cards (defender's choice) — economic pressure on the besieged city. |
| 3 | **Karaca Pasha's Push** [Requires: Karaca Pasha present] | 2 | Karaca Pasha, commander of the Rumelian corps, throws his weight against the northern land walls. +1 Attack to the first Assaults this round on Blachernae and Charisius. |
| 4 | **Ishak Pasha's Push** [Requires: Ishak Pasha present] | 2 | Ishak Pasha drives his Anatolian troops hard against the southern stretch of the walls. +1 Attack to the first Assaults this round on Gate of the Spring or Golden Gate. |
| 5 | **Promise of Plunder** | 4 | +1 Attack to all Assaults this round, but if the Attacker takes any steps lost this exchange (DESIGN.md §6.5), apply the Elite Casualty Morale Surcharge (§6.3) even if no Janissary/Solak was committed — rallying troops with the promise of the city's wealth raises the stakes of failure along with the odds of success. |
| 6 | **Baltaoğlu's Punishment** [Requires: The Four Ships already played, unique] | 2 | Mehmed publicly disgraces and replaces his admiral after the humiliation of April 20. Ottoman draws 2 extra cards — the reorganized command restores logistics efficiency. **No longer a Morale card (revised this session)** — a public scapegoating doesn't actually put fight back in the army, so it shouldn't read as raising Morale; Ottoman Morale gain is now reserved for a single card, The Hadith of Conquest (see the Morale-scarcity policy, Open Questions). |
| 7 | **The Union's Discontent** | 2 | Ottoman agents quietly encourage the real religious/political backlash against the Church Union with Rome, deepening the city's internal rift. Byzantine Reserve Pool -1. (Moved here from the Byzantine pile — a card whose Event only ever hurts Byzantines belongs where a player would actually choose to play it.) |
| 8 | **The Serbian Vassals** | 2 | A striking historical irony: Christian troops from the vassal Serbian Despotate served in Mehmed's besieging army under their feudal obligations, even as Constantinople — a fellow Orthodox city — was stormed. Free muster of 2 Azap and 2 Bashi-bazouk units this round (no card cost). |
| 9 | **Orban's Great Cannon** [Special Card obtained by Ottoman player before game start, must be played in Round 1, unique, Forced] | 3 | Permanently adds +1 to the Bombard slot count (DESIGN.md §2.1) for the rest of the game — the great bombard's arrival and emplacement, until the great cannon is destroyed by overuse. Forced — the cannon simply arrives; no player chose to delay it. |
| 10 | **The Hadith of Conquest** [Round 1-2 only, unique] | 5 | The ulema invoke the real hadith attributed to Muhammad — "Constantinople will be conquered by a good commander with a good army" — to root the campaign in religious destiny at its outset. Ottoman Morale +1 (lowered from +2 in an earlier revision — see the Morale-scarcity policy, Open Questions). Now the *only* Ottoman Morale-gain card in the entire deck (The War Council's +1 was removed this session when it was repurposed to a permanent Force Commitment Cap boost, §6.3), deliberately — it's the strongest religious-legitimacy card available, gated to the campaign's opening and usable once. (Replaces Zeal of the Ghazis, which was too generic for the designated pile — moved to Neutral.) |
| 11 | **The Siege Trench** [Round 2+] | 1 | The Ottomans dug an entrenchment and threw up a palisade facing the walls to shield their lines and guns from Byzantine sorties. Until your next Assault resolves, Byzantine Sortie actions have their effect halved (round down). |
| 12 | **Golden Horn Manoeuvre (旱地行舟)** [Round 4+, Forced] | 5 | Unlocks the Golden Horn sector (DESIGN.md §3.2). Doesn't resolve combat itself. Forced — this is the pivotal story beat, not a strategic option; it happens the moment it's drawn. |
| 13 | **Strike the Commander** [Round 4+, Requires: Giustiniani present at target sector] | 4 | Focus this Assault on Giustiniani specifically: roll 1d10, on a 7+ he is removed from play for the rest of the game. Mirrors his historical wounding at Mesoteichion, which triggered a real defensive collapse — see First Strike, DESIGN.md §6.2, for what the Byzantines lose. |
| 14 | **The Emperor Falls** [Round 4+, Requires: Constantine present at target sector] | 5 | Focus this Assault on Constantine XI specifically: roll 1d10, on an 8+ he is removed from play for the rest of the game. If he falls, Byzantine Wall Defense is permanently -1 at every sector for the rest of the game — resolves the open "what does losing Constantine actually cost" question from DESIGN.md §7, matching the real, near-total collapse of organized resistance after his death. Higher Ops value than Strike the Commander, reflecting how much harder and more consequential this is. |
| 15 | **Under Siege of Sound** [Round 4+] | 1 | Continuous drums and trumpets through the night, a documented tactic to deny the defenders rest. Byzantine Repair this round restores 1 less Integrity than normal. |
| 16 | **Third Tunnel** [Round 5+] | 2 | A larger, more desperate mining effort than Zaganos' Sappers — costs 2 discarded cards instead of a discount, but inflicts a full Garrison step loss at one chosen sector on success (roll 1d10, 6+). |
| 17 | **Fresh Reserves from Anatolia** [Round 5+, unique] | 4 | Provincial reinforcements and volunteer ghazis arrive mid-siege. Immediately deploys 4 Azap and 4 Bashi-bazouk tokens on the board for free. |
| 18 | **Rumeli Fort, the Throat-Cutter** [Before Round 5, unique] | 3 | The great fortress Mehmed built on the Bosphorus in 1452, before the siege proper, its guns sinking any ship that refused to stop — it strangled the city's northern supply line before a single wall was touched. For the rest of the game, every Byzantine Sue for Aid advance roll is at **-1** (§4.0.5) — the strangled supply line makes relief that much harder to summon. Flavor-rich and genuinely iconic. |
| 19 | **The Kerkoporta Left Open** [Round 6+, Requires: target sector Breached] | 2 | +1 column shift on the next Assault this round against a Breached sector — exploiting an unlocked postern gate. Historically debated whether this was carelessness or betrayal; play it either way. |
| 20 | **The Eclipse Omen** [Round 6+, unique, Forced] | 4 | The real lunar eclipse of May 22 — a prophecy held the city could never fall under a waning moon, and the omen badly shook the defenders. Byzantine Reserve Pool -1, and -1 Wall Defense at one sector (Ottoman player's choice) for this round only. Attacker steps lost this round do not reduce Ottoman Morale (the omen offsets the sting of a failed assault). Forced — an eclipse isn't optional. |
| 21 | **Weight of Numbers** [Round 6+] | 2 | The Ottomans' sheer numerical advantage finally tells as the siege grinds on and the host regroups for another push: **3 free Replenishment actions** — restore up to 3 flipped Janissary or Solak units to full strength at no card cost (§4.0.1). |
| 22 | **Double Pay Proclaimed** [Round 6+, unique] | 3 | With the siege dragging and the army restless, Mehmed proclaims doubled pay and first rights to the plunder to reignite zeal. Ottoman Draw Track +1 (§4.0) — a real injection of renewed capability, distinct from the Attack-boost of Promise of Plunder. |
| 23 | **The War Council** [Round 7+, unique, Forced] | 5 | Mehmed's real historical council: Halil Pasha argues one last time for lifting the siege, and is overruled. Permanently raises the attacker Force Commitment Cap (DESIGN.md §6.3) by +1 — 6 units per Assault instead of 5 — for the rest of the game, as the Sultan commits to throwing his full weight into the final push without restraint. The clearest "point of no return" card in the deck — Forced, since this council happened regardless of either player's preference. |
| 24 | **Final Preparations** [Round 7+, unique] | 3 | The methodical staging in the days before May 29. This round's Bombard phase gets +1 extra sector slot (temporary, this round only). |
| 25 | **Zaganos' Final Push** [Round 7+, Requires: Zaganos Pasha present] | 2 | A late escalation on the Golden Horn. Removes the Naval Defense malus (§3.2) entirely for one Assault there this round. |
| 26 | **The Fallen Icon** [Round 7+, Forced] | 3 | The real dropped icon of the Theotokos during a procession, followed by a sudden violent storm and unnatural fog — Ottoman agents make sure word of the omen spreads to unsettle the defenders further. Byzantine Reserve Pool -1. (Moved here from the Byzantine pile for the same reason as The Union's Discontent — round gate preserved from the original.) Forced — a dropped icon and a sudden storm aren't something either player chooses to trigger. |

## Byzantine Pile (no fixed target for now — trim to a clean draw number later)

Grouped 2026-07-11: cards with no round restriction first, then round-
gated cards in ascending round order.

| # | Card | Ops | Event |
|---|---|---|---|
| 1 | **Halil Pasha's Doubt** | 5 | The Grand Vizier's real historical opposition to the siege becomes public: an immediate **Ottoman Morale -1**, and starting **next round**, the Pressure to Attack rule (§2.2) permanently requires **2 Assault attempts** per round instead of 1 to avoid the Morale penalty, for the rest of the game. One of the strongest Byzantine cards in the deck — a direct Morale hit *and* a permanent structural squeeze that forces the Ottoman to commit real troops to more Assaults than a single cheap probe would (feeding the Elite Casualty pool, §4.0.4, faster too). Best played early, since the extra pressure compounds over every remaining round. (Revised this session — was a Morale -1 / discard-4 choice; retuned to combine a direct Morale hit with the commitment-forcing structural change, rather than offering it as an either/or.) |
| 2 | **John Grant's Countermine** [Requires: Ottoman Sap/Mine active] | 4 | Cancels all active Ottoman Sap/Mine efforts — the Scottish/German engineer's real countermining successes. |
| 3 | **Hungarian Envoy** | 1 | +1 to this round's Sue for Aid advance roll toward the Powers Stirring track (§4.0.5) — a Hungarian envoy slips through with word that relief may yet be coming. |
| 4 | **Emperor's Rally** [Requires: Constantine present] | 2 | Reinforce a sector this round for free (no Reserve Pool cost) — Constantine personally riding the walls to rally defenders. |
| 5 | **The Venetian Council Holds** [Requires: Golden Horn unlocked] | 2 | The historical Venetian debate over whether to slip away or stay and fight resolves in favor of staying — one Venetian Marine unit becomes free to field this round (no Reserve Pool cost) at any sector Minotto is present. |
| 6 | **Relics Borne Along the Walls** | 3 | The city's holiest icons and relics carried in procession atop the ramparts to steady the defenders' spirits. Negates the Reserve Pool loss from one Ottoman-played omen card (The Eclipse Omen or The Fallen Icon) this game, or if none is pending, Reserve Pool +1. (A deliberate counter to the Ottoman omen cards — faith cuts both ways.) |
| 7 | **The Chain Holds** [Before Golden Horn opened, Forced] | 4 | The historical repulse of Mehmed's direct naval attempt to force the Golden Horn chain by brute strength, before he settles on the overland portage instead. Reserve Pool +1 and Ottoman discards 1 card (a wasted naval effort costs materiel, not just morale) — a real, if minor, early setback for the attacker. (Replaces Trial by the Chain, which lived in the Ottoman pile as a pure own-goal with no benefit to its owner — the same historical event, correctly reframed as the Byzantine success it actually was.) Forced — this repulse happened whether or not either player "chose" it. |
| 8 | **Blockade Runners** [Round 2+] | 3 | A small resupply convoy breaks the naval blockade: Reserve Pool +2 tokens. Historically a real, one-time event early in the siege. |
| 9 | **The Four Ships** [Round 2+, unique, Forced] | 5 | A genuine, celebrated historical moment: on April 20, four Christian relief ships (three Genoese, one Byzantine grain carrier) fought clean through the entire Ottoman fleet in full view of the city *and* the Sultan, breaking into the Golden Horn despite Baltaoğlu's much larger force trying to stop them. Ottoman Morale -2 (a public humiliation for Mehmed), Ottoman discards 2 cards (the blockade effort itself was wasted), and Reserve Pool +1 (the grain ship's cargo). The single strongest Morale-hit card in the deck for its Ops cost — deliberately rare and round-limited so it can't be relied on as a repeatable lever. Forced — a real, dated naval engagement, not a strategic option. |
| 10 | **The Grand Duke's Fleet** [Round 2+, Requires: Notaras present] | 2 | Notaras' naval command bears fruit. +1 Defense at the Golden Horn sector this round, if he's stationed there. |
| 11 | **A Merchant's Gold** [Round 2+] | 3 | Wealthy citizens are pressured into funding the defense. Reserve Pool +2. |
| 12 | **The Podestà's Dilemma** [Round 2+] | 2 | Galata's technically-neutral Podestà quietly leaks word of Ottoman cannon positions to old contacts inside the city. +2 Sortie attack power this round when targeting artillery. |
| 13 | **Bells of Defiance** [Round 3+] | 2 | Church bells rung continuously to rally the population and signal alarm. Free Reinforce action this round (no Reserve Pool cost) at any single sector. |
| 14 | **The Walls Endure** [Round 3+] | 3 | The sheer resilience of thousand-year-old fortifications. This round's Repair action may bypass the "rubble cap" (§3.1) once. |
| 15 | **Coco's Raid** [Round 4+, Requires: Golden Horn unlocked] | 4 | Attempt to neutralize the Golden Horn threat: on success the Ottoman Draw Track steps down 1 (§4.0) (ships burned/damaged — this is literally an attempt to torch the fleet, and a durable loss of materiel should cut the Ottoman war-effort tempo, not just cost a card or two; consistent with §2.2's "Byzantine naval/raid successes step the Draw Track down") — but on a bad roll, lose a committed unit and the sector stays active. Real risk, matching Coco's historical death. |
| 16 | **Night Repairs** [Round 4+] | 2 | The defenders' desperate nightly repair work, civilians included. This round's Repair Ops action restores +1 extra Integrity. |
| 17 | **Sortie by Torchlight** [Round 4+] | 2 | A night raid slips past the siege lines to strike the works directly. +2 Sortie attack power this round when targeting siege engines (mines, mantlets, saps) — the direct-action counterpart to The Podestà's Dilemma's intelligence-driven bonus against artillery specifically. |
| 18 | **The Great Ditch** [Round 4+] | 3 | The deep fosse before the Theodosian Walls — a real, formidable obstacle that had to be filled with rubble before any assault could press home. Choose one sector: the first Assault against it this round commits one fewer attacker unit (minimum 1), as the attackers spend the exchange clawing across the ditch. |
| 19 | **Bell Chimes of Hagia Sophia** [Round 4+, unique] | 3 | Bells and the wooden semantron rung across the city to muster every able body to the walls — a general call to arms, not the specific final-assault beat (see The Last Liturgy for that). Free Reinforce action (no Reserve Pool cost) at up to two sectors this round, and Reserve Pool +1. **Redesigned 2026-07-11** — was a Round 8+ Forced card duplicating The Last Liturgy's "Reserve Pool +2 plus a bonus" shape; now an earlier, optional, troop-*mobilization*-focused card (free Reinforce is the actual mechanical content) rather than a second morale/unity card. |
| 20 | **The Stockade at the Breach** [Round 5+, Requires: target sector Breached, unique per sector] | 3 | Giustiniani's real improvised wooden palisade behind the crumbling outer wall at Mesoteichion. A Breached sector permanently gains +1 Wall Defense once built. |
| 21 | **Theophilos Palaiologos' Vow** [Round 5+, unique] | 2 | A real kinsman of the Emperor, a scholar-soldier who reportedly swore he would rather die than outlive the city, and did — fighting to the end at the walls. Choose one sector: +2 Defense there this round, and its committed garrison cannot be forced to retreat by any event this round. |
| 22 | **Demetrios Kantakouzenos' Stand** [Round 5+, unique] | 2 | Another real kinsman of the Emperor, historically posted to the southern stretch of the land wall near the Golden Gate. +2 Defense at the Golden Gate or Gate of the Spring this round. The southern counterpart to Theophilos Palaiologos' Vow (which stays sector-flexible, matching how his own historical post is less precisely fixed) — together the two named-general cards give the Byzantine pile the same paired north/south commander shape as Karaca Pasha's Push and Ishak Pasha's Push do for the Ottomans, just adding Defense where theirs add Attack. |
| 23 | **Empire's Last Muster** [Round 6+, unique] | 4 | Reserve Pool +3 tokens, one time only — the desperate final call-up of monks, clergy, and every able body left in the city. |
| 24 | **Desperate Muster of Youths** [Round 6+, unique] | 3 | As casualties mount, boys and elderly men are pressed into wall duty. Reserve Pool +2, one time only. |
| 25 | **The Emperor's Vigil** [Round 6+, Requires: Constantine present] | 2 | Constantine's real habit of patrolling the walls personally, night after night, without rest. +1 Defense at his current sector and one adjacent sector this round. |
| 26 | **The Scout Ship's Return** [Round 7+, unique, Forced] | 5 | The real May 23 event: a brigantine Constantine sent in secret to search for the promised Venetian relief fleet returns with grim news — no fleet is coming. Its crew nonetheless volunteers to stay and share the city's fate rather than flee. Freezes the Powers Stirring marker permanently where it stands — no further Sue for Aid advances for the rest of the game (hope of relief is gone) — but Reserve Pool +1 — the crew's loyalty steadies the garrison even as hope dies. The most bittersweet card in the deck — Forced, per your own example. |
| 27 | **The Last Liturgy** [Round 7+, unique, Forced] | 4 | The real May 28 unifying service in Hagia Sophia, where Orthodox and Catholic set aside their bitter dispute over Church Union to face the common threat together. Reserve Pool +2, and +1 Defense at every sector engaged in an Assault this round (unified resolve stiffens the whole line at once, however briefly) — if "The Union's Discontent" was already played this game, this card also cancels its lingering effect, a deliberate thematic full circle. **Redesigned 2026-07-11** — added the city-wide Defense bonus to differentiate this from Bell Chimes of Alarm: this card is about morale/combat resolve, that one is about troop mobilization. Forced — a fixed, dated religious event. |

## Neutral Pile (starter batch — 27 of ~30-40, including 17 dual-use)

| # | Card | Ops | Event |
|---|---|---|---|
| 1 | **Storm Over the Bosphorus** | 3 | Cancel this round's Bombard phase entirely — bad weather halts the guns. |
| 2 | **Disease Within the Walls** | 2 | Byzantine Reserve Pool -1 — the defenders were just as exposed to camp disease inside a crowded, besieged city. |
| 3 | **Rumors of a Relief Fleet** | 2 | Advance the Byzantine Powers Stirring marker 1 step (§4.0.5) — even false rumors of a Hungarian/Venetian relief fleet stir the outside powers and force the Ottoman to keep hedging. (Re-pointed 2026-07-13 from a flat Reserve Pool +1 onto the relief track, giving the track a booster to balance against its suppressors; earlier it was changed off Ottoman Morale per the Morale-scarcity fix.) |
| 4 | **Plague in the Camp** | 2 | Ottoman discards 2 cards — disease was a constant siege-camp threat on the attacking side. (Trimmed to card-loss-only; Morale should move only on weighty, named beats, not routine attrition.) |
| 5 | **Powder Shipment Arrives** | 2 | Ottoman draws 2 extra cards — restocking after a costly bombardment cycle. |
| 6 | **A Gate Left Unbarred** | 1 | Either player's choice, once per game: minor free Ops action of their choice, representing the general fog of war/logistics friction on both sides. |
| 7 | **Council of War** | 1 | Both players may look at the top 2 cards of their own designated pile before the next draw — a rare piece of shared information/tension-breaking utility card. |
| 8 | **The Long Wall Wearies** | 1 | Both sides' committed leader in the current sector (if any) loses their bonus for one Assault this round — exhaustion affects everyone equally. |
| 9 | **Zeal of the Ghazis** [Round 2+] | 1 | Religious volunteer warriors (ghazis) reinforce the irregular ranks. +1 Attack to Bashi-bazouks specifically for one Assault this round. (Demoted from the Ottoman pile — generic flavor, no unique/named hook, better suited to the shared pool than a designated slot.) |
| 10 | **The Last Grain Stores** [Round 5+] | 2 | Careful rationing of the city's dwindling food stores. Reserve Pool +1. (Demoted from the Byzantine pile for the same reason — see Zeal of the Ghazis.) |

### Dual-Use Cards (alt-historical branch points)

These reflect a real historical tension that never actually broke one way
or the other — Galata's studied neutrality, the Janissaries' unspoken
pay-via-plunder arrangement — so the card lets *whichever player draws
it* decide how that tension resolves in this timeline.

**Branch labels (added 2026-07-11):** each side of every card below is
tagged **[Historical]** (this is what actually happened), **[Unhistorical]**
(the counterfactual "what if" branch — didn't happen), or **[Generic]**
(neither branch is a specific attested event; both are plausible
extrapolations of a real underlying tension, so calling either one "the
historical outcome" would overclaim).

Grouped 2026-07-11: cards with no round restriction first, then round-
gated cards in ascending round order.

| # | Card | Ops | If Ottoman plays | If Byzantine plays |
|---|---|---|---|---|
| 1 | **Galata's Choice** | 4 | **[Unhistorical]** Break Galata's neutrality and besiege it directly: immediately unlock the Golden Horn sector (skipping the need for the Golden Horn Manoeuvre card) at a cost of discarding 2 cards — but outraged Genoese refugees and mercenaries flee into the city and join its defense: Byzantine Reserve Pool +3. | **[Unhistorical]** A diplomatic overture persuades Galata to quietly abandon its neutrality: Reserve Pool +3, no card cost. Neither branch is what actually happened — Galata's neutrality held throughout the real siege, which means the real "historical" outcome is this event simply never triggering at all. |
| 2 | **Janissary Bribes** | 3 | **[Generic]** Preemptively address the corps' pay grievances before they become a problem: Ottoman Morale +1. Not a specific attested event, just ordinary military management. | **[Unhistorical]** Attempt to bribe the Janissary corps into partial desertion: roll 1d10, 6+ permanently removes one Janissary-tier unit (New Levy, Janissary, or Solak — attacker's choice which tier) from the Ottoman pool for the rest of the game; on a miss, nothing happens but the card is spent. Grounded in a real tension — the traditional three-day sack of a captured city was effectively the Janissaries' implicit wage — but no successful bribe campaign is attested. |
| 3 | **Whispers of Betrayal** | 3 | **[Unhistorical]** Spread rumors that a prominent Byzantine noble (implicitly Notaras, given his real historical reputation for divided loyalties) favors surrender: Byzantine Reserve Pool -1. | **[Unhistorical]** Spread rumors of internal Ottoman succession disputes and court discontent: Ottoman discards 1 card. A propaganda war fought symmetrically by both sides, each exploiting a real seed of internal distrust on the other side, though neither specific rumor campaign is attested. (Changed off Ottoman Morale — this card lives in the reshuffling Neutral pool, so it could recur multiple times in one game, making a Morale effect here worse than in a designated pile.) |
| 4 | **The Winds Shift** | 1 | **[Generic]** Favorable winds aid the fleet: if the Golden Horn is unlocked, +1 Attack on an Assault there this round. | **[Generic]** Favorable winds aid a hoped-for relief ship: +1 to this round's Sue for Aid advance roll (§4.0.5) (the weather-driven counterpart to the Hungarian Envoy's diplomacy-driven version of the same bonus). |
| 5 | **Orban's Offer** [Round 1 only, unique] | 2 | **[Historical]** Confirms the Hungarian engineer's full commitment to the Ottoman cause after Byzantium couldn't match Mehmed's price. Ottoman draws 1 extra card. | **[Unhistorical]** A real historical fork: Orban genuinely approached Constantine XI *first* with his cannon-casting services, and was turned away for lack of funds and raw material — this is the "what if Byzantium had paid him instead" branch. This round's Repair action restores +1 extra Integrity. (Not treated as mutually exclusive with "Orban's Great Cannon" in the Ottoman pile — a deliberate simplification rather than airtight causality between the two cards.) |
| 6 | **The Defector** [Round 2+] | 3 | **[Generic]** A Byzantine deserter reveals a weak point in the defense: +1 column shift on the next Assault this round. Desertion happened on both sides throughout the siege generally, but no specific attested instance matches this. | **[Generic]** An Ottoman deserter reveals troop dispositions: reveals the Ottoman player's Bombard targets for next round in advance. (Distinct from The Podestà's Dilemma, which is specifically about Galata's political position rather than battlefield desertion — both can coexist without redundancy.) |
| 7 | **The Despots of the Morea** [Round 2+] | 3 | **[Historical]** Turahan Bey's real historical deployment to the Peloponnese successfully pins Constantine's own brothers, Thomas and Demetrios Palaiologos (the Despots of the Morea), in place — exactly as it did historically, preventing any relief force from that direction. Byzantine Reserve Pool -1. | **[Unhistorical]** The counterfactual branch: word reaches Thomas and Demetrios of the city's plight, and despite Turahan Bey's screening force, a token relief contingent slips through from the south. Reserve Pool +2. |
| 8 | **Prince Orhan's Claim** [Round 2+] | 4 | **[Historical]** Mehmed refuses the Byzantine attempt to leverage the Ottoman pretender Orhan (a real pensioner-hostage in the city), and the failed blackmail only hardens his resolve to take Constantinople outright. Byzantine Reserve Pool -1. | **[Unhistorical]** The counterfactual: the Byzantines actively promote Orhan's rival claim to the Ottoman throne, sowing doubt in the ranks. Ottoman Draw Track -1, and Mehmed's Combined Arms (§6.2) cannot be used next round (his attention is on the succession threat). (Kept off Ottoman Morale despite the flavor fit — this is a reshuffling Neutral-pool card, and per the Morale-scarcity policy those shouldn't move Morale.) |
| 9 | **Rivalry of the Republics** [Round 3+] | 2 | **[Generic]** Exploits the real, documented mutual distrust between Genoese and Venetian contingents: the Command Coordination exception (DESIGN.md §6.2.1) is suspended this round — even Constantine cannot combine two different foreign contingents in one Defense. The underlying rivalry is real; this specific mechanical exploitation of it isn't a discrete attested event. | **[Generic]** Skillful mediation between the rival factions grants a one-time exception: any single non-Constantine foreign leader may combine their own contingent with militia *and* one other foreign contingent this round, without Constantine present. |
| 10 | **Galata's Timber** [Round 3+] | 2 | **[Historical, probable]** Galata quietly supplies timber and logistics for the ship-portage effort: if the Golden Horn is not yet unlocked, reduces the Ops cost of the next Golden Horn Manoeuvre played this game by 1. The portage route physically crossed Genoese territory behind Galata — some degree of complicity is widely inferred by historians, though not universally confirmed, hence "probable" rather than fully [Historical]. | **[Unhistorical]** Galata quietly smuggles food into the city instead: Reserve Pool +2. (A different angle on Galata's ambiguous position than Galata's Choice — this one is about material support, not neutrality/troops.) |
| 11 | **Hunyadi's Truce** [Round 3+] | 2 | **[Historical]** The Hungarian regent John Hunyadi's real truce with the Ottomans holds — no relief ever comes from that quarter, exactly as history records. Knocks the Byzantine Powers Stirring marker back 1 step (§4.0.5) — the truce holds and the nearest hope of relief turns away. | **[Unhistorical]** The counterfactual branch: word of the city's desperate plight briefly reignites old crusading fervor and threatens to override the truce. The credible risk of Hunyadi breaking it forces Mehmed to keep forces watching the frontier instead of committing them fully to the siege: Ottoman discards 1 card. (Moved here from the Ottoman pile, where it lived as a single-effect card — the real tension is that Hunyadi's restraint was a choice with a live alternative, which is exactly what dual-use is for.) |
| 12 | **The Venetian Senate's Delay** [Round 3+] | 3 | **[Historical]** The real, documented slow deliberation in the Venetian Senate over committing a relief fleet becomes known in the city, deepening despair as yet another council session ends without a decision. Byzantine Reserve Pool -1. | **[Unhistorical]** The counterfactual branch: Venetian merchants and ship captains already present in the city press their case through back channels, accelerating the Senate's decision. Reserve Pool +2. (Deliberately does *not* touch the Powers Stirring track / Sue for Aid — that lever already has two suppressors, Hunyadi's Truce and Intercepted Dispatch, both now marker knock-backs since the 2026-07-13 track redesign; a third would risk over-saturating it.) |
| 13 | **The Karamanid Rising** [Round 3+] | 3 | **[Historical]** Mehmed's pre-siege subjugation of the Karamanid emirate (his 1451 campaign) holds — the Anatolian rear stays quiet and his southern troops are free to press the siege. Ottoman Draw Track +1. | **[Unhistorical]** The counterfactual: the Karamanid emir seizes the moment and raids Ottoman Anatolia. Ishak Pasha (the Anatolian commander, §6.2) is recalled — remove him and his Southern Command bonus from play for **2 rounds**, and Ottoman Draw Track -1. The single most literal "second front in the south" card, mapped onto the Ottoman command that historically came from Anatolia. |
| 14 | **Skanderbeg's Revolt** [Round 3+] | 3 | **[Historical]** Skanderbeg's very real Albanian revolt is contained by Ottoman frontier forces without ever drawing on the siege army — which is exactly what happened. Ottoman Draw Track +1. | **[Unhistorical]** The counterfactual escalation: the Albanian revolt flares badly enough to demand reinforcement. Karaca Pasha (the Rumelian/Balkan commander, §6.2) is recalled — remove him and his Northern Command bonus for **2 rounds**, and Ottoman Draw Track -1. The northern mirror of The Karamanid Rising, mapped onto the Ottoman command that historically came from the Balkans. |
| 15 | **Intercepted Dispatch** [Round 4+] | 2 | **[Generic]** Intercepts a Byzantine plea for outside help: knocks the Byzantine Powers Stirring marker back 1 step (§4.0.5). (Stacking with Hunyadi's Truce is now fine — two knock-backs cost the Byzantine tempo on the relief track rather than bricking the action outright, which was the whole point of the 2026-07-13 track redesign.) | **[Generic]** Intercepts Ottoman correspondence: disables one enemy leader's flat combat bonus for the next Assault this round. |
| 16 | **The Papal Galleys** [Round 4+] | 4 | **[Historical]** The relief fleet the Pope and Venice were slowly assembling dawdles and never arrives in time — some ships got only as far as the Aegean before turning back. The dashed hope stings: Byzantine Reserve Pool -1. | **[Unhistorical]** The counterfactual: the papal galleys arrive in the nick of time. Reserve Pool +3, and if the Golden Horn is unlocked, it is re-locked (dormant again) as the relief fleet breaks the naval position. The single biggest Byzantine swing in the dual-use set — deliberately high Ops (4) and late-gated to match. (Does *not* touch Sue for Aid, keeping that lever from over-saturating.) |
| 17 | **Terms of Surrender** [Round 8+, unique] | 3 | **[Unhistorical]** A real historical event: Mehmed genuinely offered Constantine safe passage and lordship elsewhere in exchange for peacefully surrendering the city. The psychological weight of a real, tempting offer: Byzantine Reserve Pool -1. | **[Historical]** Constantine's own defiant public refusal of those terms — historically attested — rallies the city instead: Reserve Pool +2. The historical outcome (he refused) is the Byzantine branch; the Ottoman branch is the counterfactual "what if the offer had actually landed." |

## Open Questions

1. **No fixed card-count target for now (per user direction, 2026-07-10).**
   Current counts: **Ottoman 26, Byzantine 27, Neutral 27 (17 dual-use).**
   (Ottoman trimmed from 28 to 26 on 2026-07-13, alongside the Sue for
   Aid redesign: **The Sultan's Resolve** cut as a bland duplicate of
   Double Pay Proclaimed's Draw Track +1, and **The Long Encampment** cut
   as the weakest, self-penalizing member of the temporary-Attack-bonus
   cluster; Ottoman pile renumbered consecutively 1-26. The Byzantine
   pile's stated count had earlier drifted out of sync with its actual
   row count — renumbered consecutively, and Demetrios Kantakouzenos'
   Stand added as the southern-sector counterpart to Theophilos
   Palaiologos' Vow, mirroring Karaca/Ishak Pasha's Push on the Ottoman
   side; see the Byzantine table.) User intends to skim these *down* to a
   clean per-round draw number, so the piles are still deliberately
   over-provisioned — the read-through pass should prune for
   redundancy/overlap (e.g. Karaca/Ishak Pasha's Push vs Weight of
   Numbers still both touch "temporary Attack bonus"; several
   late-round-gated cards cluster around rounds 5-8 — check the curve
   isn't lumpy) rather than add more. New this pass: Ottoman flavor
   (Rumeli Hisarı, Serbian Vassals, Siege Trench, Double Pay); Byzantine
   flavor (Theophilos Palaiologos' Vow, Demetrios Kantakouzenos' Stand,
   Relics Borne Along the Walls, The Great Ditch); alt-history dual-use
   (The Karamanid Rising, Skanderbeg's Revolt, Prince Orhan's Claim, The
   Papal Galleys).
2. ~~DESIGN.md §2.2 specifies "3-4" designated draws/round, not a flat
   3~~ — **resolved, two sessions back-to-back:** designated draw is now
   a flat 3/round for both sides (Ottoman 10-11 total/round, Byzantine 9
   total/round — DESIGN.md §4.0), and both designated piles now have the
   same reshuffle-discard fallback as Neutral (DESIGN.md §2.2's new
   Reshuffle Rule: Event cards removed from the game permanently once
   played, everything else discards and reshuffles). Since designated
   piles are ~100% named cards, their playable pool still genuinely
   shrinks over the game as Events get triggered — flagged as worth a
   playtest check in DESIGN.md §7, not fully resolved.
3. Neutral pile is now at 23 of its ~30-40 target, including 13 dual-use
   cards (exceeds the earlier 10-card soft cap on dual-use, per user
   direction 2026-07-10 — Hunyadi's Truce moved here from the Ottoman
   pile, plus two new additions: The Despots of the Morea and The
   Venetian Senate's Delay). ~~Note: Intercepted Dispatch's Ottoman branch
   stacks with Hunyadi's Truce's Ottoman branch (both negate a Byzantine
   "Sue for Aid" attempt) — worth a playtesting look at whether that
   over-cripples the Ops action.~~ **Resolved by the 2026-07-13 track
   redesign:** both are now Powers Stirring marker knock-backs (§4.0.5),
   so stacking merely costs the Byzantine tempo on the relief track
   instead of bricking the action — no longer a concern. The Venetian
   Senate's Delay is still deliberately kept off that lever to avoid a
   third suppressor.
4. ~~Exact reshuffle trigger for the Neutral pile discard~~ — **resolved
   this session**: empty-deck reshuffle, per DESIGN.md §2.2's Reshuffle
   Rule — and it clarifies *what* gets reshuffled, not just *when*: Event
   cards (any pile) are removed from the game permanently once their
   Event is played and never return; everything else (Ops-spent cards,
   unplayed named cards, and all generic Attack/Supplies/Move/Guile
   cards) goes to that pile's discard stack and reshuffles back in once
   the draw pile empties. The Neutral pile's ~30 generic cards in
   particular always cycle this way, since they have no Event text to
   ever remove.
5. ~~A few cards reference mechanics not yet fully specified in DESIGN.md
   (e.g. "Sue for Aid" doesn't yet have a defined success mechanic beyond
   being listed as an Ops action, §2.2).~~ **Sue for Aid fully specified
   2026-07-13 — DESIGN.md §4.0.5** (the Powers Stirring track). All six
   cards that touch the lever (Hungarian Envoy, The Winds Shift/Byz,
   Rumors of a Relief Fleet, Rumeli Fort, Hunyadi's Truce/Ott, Intercepted
   Dispatch/Ott) plus The Scout Ship's Return re-pointed to it this pass.
   Still worth scanning for any *other* card citing a mechanic that isn't
   yet nailed down in DESIGN.md.
6. Several cards (Weight of Numbers, Fresh Reserves from Anatolia,
   Promise of Plunder) push Ottoman Attack output up further on top of
   Mehmed's Combined Arms and Giustiniani's First Strike, both already
   flagged for CRT-interaction playtesting in
   DESIGN.md §7 — worth re-checking that stack once the full deck exists.
   (The Long Encampment, previously listed here, was cut 2026-07-13.)
7. **Morale-scarcity policy (added 2026-07-09, tightened this session):**
   Ottoman Morale should move only on weighty, mostly named/unique/gated
   beats, not routine weekly upkeep — Resources/Draw Track absorbs the
   routine economic push-and-pull instead. **Morale gain now comes from a
   single card in the entire deck: The Hadith of Conquest (+1, round 1-2
   only, unique)** — max +1 across a full game. (The War Council's +1 was
   removed this session when the card was repurposed to a permanent Force
   Commitment Cap boost, §6.3 — it had been the second gain card, so the
   well is now down to one.) Baltaoğlu's Punishment was
   pulled off the gain list this session (now a pure card-draw effect,
   Ottoman draws 2) since a public scapegoating doesn't actually read as
   restoring army will. Morale-loss cards, still deliberately short: The
   Four Ships (-2, unique, round-limited), Halil Pasha's Doubt (-1,
   immediate, plus a permanent structural squeeze — see below), plus The
   Eclipse Omen (which *protects* Morale for its round rather than
   draining it). **Halil Pasha's Doubt revised this session** to combine
   an immediate Morale -1 with a structural change: it permanently raises
   the Pressure to Attack rule's Assault requirement from 1 to 2 per
   round (§2.2), forcing the Ottoman toward real Assault commitments
   (and the Morale exposure that comes with them via the Elite Casualty
   pool below) on top of the direct hit — deliberately one of the
   strongest cards in the Byzantine pile. Apply this same bar to
   any future card before adding a Morale effect — especially a gain,
   now that the well is down to a single named card — and especially in
   the Neutral pile, where cards can recur after a reshuffle and so are a
   worse offender than a one-shot designated-pile card. **Open design
   thread, resolved this session:** Morale's primary drain is now the
   **Elite Casualty pool** (DESIGN.md §4.0.4) — Janissary/Solak losses
   only (matching the existing exemption list in §6.3), counted by
   Attack value (Janissary +3, Solak +4) on full removal only, cumulative
   across the whole game, Morale -1 every time the running total crosses
   another multiple of **5** (lowered from an initial draft of 10 once
   DESIGN.md §6.3.1's defender-assigns-losses fix made the pool actually
   fill up under realistic play — estimated 14-21 total points, i.e. 2-4
   Morale ticks, over a full game). The earlier flat time-decay idea (-1
   every 2 rounds) was dropped in favor of this — the round-limit auto-win
   at round 9/10 (§5) already supplies the "hurry up" clock, so a second,
   unconditional Morale timer would have been redundant; the casualty
   pool instead ties Morale specifically to how hard the Ottoman commits
   real troops, which Halil Pasha's Doubt above now directly pressures
   them to do. **§6.3.1 (added this session)** also closes a shielding
   exploit: Attacker step losses are now assigned by the *Byzantine*
   player, not the Ottoman, specifically so Janissaries/Solaks can't be
   routinely hidden behind cheap Bashi-bazouk/Azap losses.
8. **[Forced] tag added 2026-07-10** — 11 cards now tagged, reserved for
   fixed historical beats rather than strategic options: Golden Horn
   Manoeuvre, Orban's Great Cannon, The War Council of May 26, The
   Eclipse Omen, The Fallen Icon (Ottoman); The Chain Holds, The Four
   Ships, The Scout Ship's Return, The Last Liturgy, Cardinal Isidore's
   Men, The Bell Chimes of Hagia Sophia (Byzantine). Two mechanical
   questions still need resolving before this is fully playable:
   - **Timing**: does a Forced card resolve immediately upon draw
     (interrupting the normal alternating mini-turn sequence, §2.2), or
     must it simply be the first card that player plays on their next
     mini-turn? The current wording in Deck Structure implies the
     former but doesn't nail down the mechanical interaction with
     Phase B's turn order.
   - **Forced + Requires interaction**: none of the 11 tagged cards
     currently combine [Forced] with [Requires: X], deliberately, to
     dodge the question of what happens if a Forced card's prerequisite
     isn't met when drawn (discarded? held until true? played anyway
     with no effect?). If a future card needs both tags, this has to be
     answered first.
9. **Mutual-damage combat revision (2026-07-10)** — DESIGN.md §6.5 no
   longer produces a single categorical result; every roll now pairs
   Attacker steps lost with Defender steps lost. "Repulsed" is gone from
   the rules — Promise of Plunder and The Eclipse Omen were updated to
   reference "Attacker steps lost ≥ 1" instead. Worth a scan for any
   *future* card that says "Repulsed" or "No Effect," since those result
   categories no longer exist.
10. **Ops value rescale (2026-07-10)** — the scale widened from 1-3 to
    1-5 (DESIGN.md §2.4). Only the clearest pivotal-tier cards were
    rescaled so far: Golden Horn Manoeuvre, The War Council of May 26,
    The Emperor Falls, Terms of Surrender, The Four Ships, The Scout
    Ship's Return (all now 5), The Eclipse Omen and The Last Liturgy
    (now 4). The other ~65 cards in the deck are still sitting at their
    original 1-3 values and need a full pass against the new scale —
    this was deliberately scoped down to a representative sample rather
    than done all at once.
11. **Generic action card economy (2026-07-10/11, DESIGN.md §2.3)** —
    actual cards now added, own section above: **4 types** (Attack,
    Supplies, Move, Guile — Guile added 2026-07-11 to cover Sap/Mine and
    Sue for Aid, which previously had no efficient funding path at all).
    30 copies total (8 each Attack/Supplies/Move, 6 Guile), physically
    mixed into the Neutral pile alongside the 23 named cards (~53 total
    before reshuffling). **Still unresolved: how the draw guarantees
    "mostly generic" per round.** A single shuffled ~53-card pool with
    roughly even generic/named composition doesn't reliably produce the
    intended ~4-5 generic + ~1 named split per round on its own — needs
    either (a) two separate physical sub-decks within the Neutral pile, or
    (b) a much higher generic:named ratio. Needs a decision before this
    is actually playable as described.
12. **Ottoman Resources sync pass (2026-07-11)** — Byzantine naval/raid
    actions should generally cost Ottoman Resources on success, not just
    move Byzantine-side tracks. Added: Coco's Raid (-2 on success), The
    Chain Holds (-1, alongside its existing Reserve Pool +1), The Four
    Ships (-1, alongside its existing Morale -2). Fire-ship raid's base
    Ops action (DESIGN.md §2.2) now explicitly costs Ottoman Resources on
    success too, matching Sortie's existing logic. Worth a similar check
    on any *future* Byzantine naval-flavored card.
13. **Dual-Use branch labels added (2026-07-11)** — every dual-use card's
    two branches are now tagged [Historical], [Unhistorical], or
    [Generic]. Three cards have both branches [Generic] (Rivalry of the
    Republics, The Defector, The Winds Shift, Intercepted Dispatch) since
    neither side is a specifically attested event, only a real underlying
    tension. Galata's Choice is unusual — both branches are
    [Unhistorical], since the real historical outcome (neutrality held,
    nothing happened) isn't representable by either branch of a card that
    exists specifically to break that neutrality one way or the other.
14. ~~Ottoman Resources restructured to a card economy — CARD-TEXT
    CONVERSION PENDING~~ — **done 2026-07-11.** Every card that said
    "Ottoman Resources ±N" has been converted to an immediate,
    one-shot **draw/discard effect** rather than a persistent Draw Track
    shift: "Ottoman draws N extra cards" (was +N) or "Ottoman discards N
    cards" (was -N). This is deliberately a *different* mechanic from
    the Draw Track (§4.0, DESIGN.md) — the Draw Track is for genuinely
    persistent, multi-round effects (e.g. the Karamanid Rising/
    Skanderbeg's Revolt leader-recall cards, which correctly still use
    "Draw Track ±1"), while ordinary one-off Resource-flavored cards are
    now simple immediate hand-size effects. DESIGN.md §4.0 should get a
    short note distinguishing the two, since right now it only describes
    the Draw Track and doesn't mention this simpler immediate-effect
    layer that most individual cards actually use.
