# Ozzfest Gameplay Rules Proposal (Draft)

This draft translates the initial requirements into actionable rules, scoring, and progression. Values are suggested starting points and should be tuned during playtesting.

## Core Scoring
- Sling hits: 250
- Standups/targets (non-mode): 500
- Rollover lanes: 750
- Turnaround lanes (upper/lower): 2,000
- Outlane inlane returns: 250 (no bonus if shielded)
- Pop bumpers (if added later): 300
- Upper/lower popper entries: 1,500 (also tags the source for bagatelle/band advance)

## Band Mode Shot Values (consistent across bands)
- Lit LORD letters during any band mode: +2,500 on top of base (total ~5,000); Rivers focuses on rollovers so its LORD hits pay +4,000 instead (total ~6,500).
- Dio focus: turnaround loops +3,000 on top of base (total ~5,000).
- Meatloaf focus: any threebank target +3,000 and threebank completion +2,000 (stacked on base values).
- Ozzy focus: magnet activations +3,000 on top of the base magnet award (net ~8,000).
- Rob Zombie focus: fivebank targets +1,000 each (base 500) and fivebank completion +5,000 (base 10,000).
- Black Sabbath remains to be defined separately; use above values as the baseline feel.

## Bonus Table (per ball end)
- Target completions: 1,000 each
- Loop/turnaround shots: 2,000 each
- Threebank completions (any side): 5,000 each
- Fivebank single drop: 500 each; full fivebank sweep: +10,000
- LORD letters lit: 2,500 each
- Bagatelle completion (mini-ball lands on unlit letter): +5,000 and lights that letter
- Multiplier: 2x/3x/5x/10x from bonus multiplier lamps (61–64). Cap total bonus at 250,000 for early tuning.

## Band Selection and Progression
- Bands: Dio, Meatloaf, Ozzy, Rob Zombie, Rivers of Nihil; Black Sabbath is wizard mode.
- Base mode auto-requests a band on start (`band_progression_request`) and when no band is running the upper popper triggers the same request; the next band starts based on `band_progress_index` with no player choice needed.
- Mode complete condition: all LORD letters lit (either via rollover switches or completing any threebank within 10s). Completing both threebanks within the 10s windows lights all LORD letters immediately.
- Completing a band: award 50,000 base + 10,000 per previously completed band; increment `bands_completed` and `band_progress_index`; clear `band_current`, then auto-request the next band. Upper popper falls back to bagatelle when a band is already running.
- Black Sabbath (wizard): starts when `bands_completed >= 5` and `band_progression_request` fires; baseline award 150,000 plus progressive jackpots (see jackpots).
- Band completion hurry-up: when a band is finished, light a 25,000 hurry-up at the upper popper for 10s; collecting it pauses band selection until taken or expired.

## High Score Target
- Seed the initial high score at 2,000,000; tune difficulty upward after playtesting. A full five-band run with solid focus-shot play should approach but not trivialize this number.

## LORD Lighting Logic
- Each letter is a rollover switch; alternatively, completing a threebank within 10s lights all letters on that bank’s side.
- Timer: start 10s on first target drop of a threebank; if timer expires, bank resets; if bank completes before expiry, light all LORD letters and award 5,000.
- Bagatelle (mini-ball kicker) can also light letters: lower eject hole enables bagatelle after 3s delay; upper eject hole enables band select if mode complete, otherwise also bagatelle.

## Magnasave Tokens
- Dropping a single target in a threebank grants 1 magnasave token for that side (max 5 tokens side). Stored in `magnet_save_left_tokens` / `_right_tokens`.
- Activation: holding left/right magnet button consumes 1 token and holds magnet for up to 3s; releasing early refunds remaining time? (TBD; start with consume-on-press behavior).
- Shots during active magnet do not grant extra tokens.

## Drain Shield Logic
- Sequence: roll over switch 24 then 25 within 1s -> activate drain shield for current side, stored in `drain_shield_left_active` / `_right_active` (value 1 when lit).
- Side flips when a slingshot fires; lamps 22/23 indicate side. Active shield saves the next outlane hit on that side by auto-launching from trough.
- Second activation in same ball lights both shields (both lamps) for one save each.

## Bagatelle Mini-Game
- Entry: lower popper always starts bagatelle; upper popper starts bagatelle only when a band is already running (otherwise it advances to the next band).
- On start, `bagatelle_active` and `bagatelle_ball_locked` set to 1 and the source popper is recorded (upper/lower). A 3s timer runs for a 10,000 award; a 12s window auto-ejects from the source popper if nothing else ends it.
- LORD rollover hits while bagatelle is active and the ball is “locked” score 750 and clear the lock flag; lit LORD letters score 2,500, add to bonus/LORD counts, and immediately eject from the source popper.
- If all LORD letters are already complete during bagatelle, the next letter hit triggers a random reward of 15,000 plus 1 magnasave token to a side (respecting the 5-token cap) and ejects the ball.
- Starting any band mode or closing the bagatelle window also ejects from the source popper to resume play.

## Jackpots and Multiball
- Multiball skeleton: `jungle_multiball` (3-ball) starts on `multiball_jungle_start`.
- Standard jackpot: 50,000 lit at start; super jackpot 150,000 lights after two jackpots; reset on multiball end.
- Add-a-ball: completing fivebank during multiball awards +1 ball (once per multiball) and lights super jackpot.
- Jackpot shots to assign later (recommend upper eject, turnaround lanes, and fivebank center shot).

## Band Mode Scoring Suggestions
- Base shot value while mode running: 5,000.
- LORD letter lights during band mode: 7,500 each.
- Completing LORD (finishing band): see completion award above and light an add-on hurry-up: 25,000 counting down over 10s at upper eject.
- Per-mode flavor (to be detailed later):
  - Dio: favors loop/turnaround shots; turnaround value +1,000 during mode.
  - Meatloaf: favors threebank hits; each threebank drop +1,000 stacking.
  - Ozzy: favors magnets; consuming a magnasave during mode awards 5,000.
  - Rob Zombie: favors fivebank; completing fivebank adds +10,000 bonus and +1x to fivebank completion value for remainder of mode.
  - Rivers: favors rollovers; rollover lanes +2,000 and extend LORD timer to 12s.
  - Black Sabbath: wizard; every major shot 15,000, jackpots doubled, LORD timer 8s with instant relight on threebank complete.

## Bonus Multipliers
- Lamps 61–64 represent 2x/3x/5x/10x bonus. Advance multiplier via fivebank completions (one step per completion). Cap at 10x.

## Ball Save and Kickbacks
- Ball save active 20s at ball start (already configured); drain during save returns ball with no bonus loss.
- Drain Shield behaves like a one-time kickback per side as defined above.

## Base Mode Interactions
- Attract -> band select -> base mode runs concurrently with band mode.
- Base mode owns generic scoring and relays completed bands to Black Sabbath gate.

## Logging and Audits (future)
- Track: bands started/completed, magnasave tokens earned/spent, drain shields lit/used, LORD letters lit per ball, fivebank completes, multiball starts/jackpots.
