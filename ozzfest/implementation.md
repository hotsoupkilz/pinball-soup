# Ozzfest Implementation Plan

Derived from the shared requirements (mission pinball framework 0.80.x/dev, Godot-driven display, APC hardware) and awaiting Ozzfest-specific gameplay specs that will be captured in ozzfest/reqs.md. Each step below will be checked off upon completion.

[x] Step 1 — Establish machine workspace scaffold  
Reviewed the Mission Pinball tutorial structure and mirrored the layout (with Ozzy as reference) to create config, data, modes, shows, and assets directories for Ozzfest; placeholder files added to preserve structure.

[x] Step 2 — Configure MPF core settings  
Created config/config.yaml with Ozzfest machine metadata, APC (lisy) hardware linkage, and placeholder switches/coils/lights/displays aligned to MPF 0.80.x/dev expectations.

[x] Step 3a — Document switch matrix inventory  
Enumerated every cabinet and playfield switch, verified row/column wiring against the Williams System 7 schematic, and captured the cleaned mapping in [ozzfest/research/processed/jungle_lord_switch_matrix.md](ozzfest/research/processed/jungle_lord_switch_matrix.md). The validated matrix (switches 09–50) is mirrored within [ozzfest/config/config.yaml](ozzfest/config/config.yaml), with OCR lineage tracked in [ozzfest/research/raw/jungle_lord_switch_wiring_ocr.txt](ozzfest/research/raw/jungle_lord_switch_wiring_ocr.txt).

[x] Step 3b — Finalize coil driver and special solenoid mapping  
Captured every solenoid’s APC/lisy address, reconciled System 7 Q-numbers, and aligned driver transistor sequencing using [ozzfest/research/raw/jungle_lord_solenoid_wiring_ocr.txt](ozzfest/research/raw/jungle_lord_solenoid_wiring_ocr.txt), [ozzfest/research/processed/jungle_lord_solenoid_map.md](ozzfest/research/processed/jungle_lord_solenoid_map.md), and the tech chart archive in [ozzfest/research/raw/Williams Jungle Lord - Williams_Jungle_Lord_Tech_Chart.pdf](ozzfest/research/raw/Williams%20Jungle%20Lord%20-%20Williams_Jungle_Lord_Tech_Chart.pdf). Coil names and numbers now match the function list inside [ozzfest/config/config.yaml](ozzfest/config/config.yaml#L286-L385), including Magna-Save targets for future hold tuning.

[x] Step 3c — Build lamp, GI, and feature light channels  
Derived the 8×8 lamp matrix and GI summary from handbook OCR exports ([ozzfest/research/raw/handbook_page9_large_psm6.tsv](ozzfest/research/raw/handbook_page9_large_psm6.tsv)) and the tech chart PDF ([ozzfest/research/raw/Williams Jungle Lord - Williams_Jungle_Lord_Tech_Chart.pdf](ozzfest/research/raw/Williams%20Jungle%20Lord%20-%20Williams_Jungle_Lord_Tech_Chart.pdf)). Normalized lamp names inside [ozzfest/config/config.yaml](ozzfest/config/config.yaml#L420-L518), documented the cleaned matrix in [ozzfest/research/processed/jungle_lord_lamp_matrix.md](ozzfest/research/processed/jungle_lord_lamp_matrix.md), and noted GI relay control for future Godot integration.

[x] Step 4 — Stand up base game modes  
Boilerplate mode folders now cover attract, base, tilt, ball save, bonus, and a multiball skeleton with configs in [ozzfest/modes](ozzfest/modes). Core mode registration lives in [ozzfest/config/config.yaml](ozzfest/config/config.yaml#L526-L531), providing starter logic that will be expanded as rules solidify.

[x] Step 5 — Implement gameplay rules and scoring hooks  
Rules updated in [ozzfest/game_rules.md](ozzfest/game_rules.md); base mode tracks bonus loops/targets and fivebank drops, lights LORD letters with 10s threebank timers, routes bagatelle via popper-specific logic, and auto-advances band modes/Jungle Multiball jackpots. Bonus mode pays out LORD letter counts. Band modes now carry consistent LORD shot bumps plus focus-specific scoring (turnarounds, threebanks, magnets, fivebank, rollovers) to support the 2,000,000 initial high score target. Added band start slides and a post-band 25k hurry-up at the upper popper with a 10s timer to gate band progression.

[x] Step 6 — Build Godot/GMC presentation layer  
Enabled MPF BCP for GMC on port 5050, added an Ozzfest slide HUD with black/white/red/purple palette and gothic IM Fell English font, and set base mode to play it. Added a reusable theme asset stub for Godot; mpf-gmc will render slides via BCP.

[ ] Step 7 — Integrate and validate MPF↔Godot communication  
Wire MPF events into the Godot mpf-gmc plugin, exercise websocket/event channels between MPF and Godot, and verify end-to-end flows for attract loops, mode start/stop, and score updates (no legacy MPF-MC components).

[ ] Step 8 — Execute iterative testing and calibration  
Run MPF in simulation, then with the APC hardware; adjust timing, debounce, and power settings; log issues and iterate until gameplay is stable and hardware-safe.

[ ] Step 9 — Document operations and deployment  
Document setup instructions, maintenance notes, and operator adjustments in README/operations docs; capture any calibration tables and final configuration values for long-term support.
