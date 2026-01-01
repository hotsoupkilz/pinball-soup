# Jungle Lord Solenoid Map (initial transcription)

Primary reference: [ozzfest/research/raw/Williams_1981_Jungle_Lord_Schematic_Diagrams_paginated_some_with_red_lining.pdf](ozzfest/research/raw/Williams_1981_Jungle_Lord_Schematic_Diagrams_paginated_some_with_red_lining.pdf) — Playfield Solenoid Wiring Diagram (page 27)
Derived assets: [ozzfest/research/raw/jl_page27-27.png](ozzfest/research/raw/jl_page27-27.png), [ozzfest/research/raw/driver_crop_full_psm11.txt](ozzfest/research/raw/driver_crop_full_psm11.txt), [ozzfest/research/raw/driver_special_psm11.txt](ozzfest/research/raw/driver_special_psm11.txt)
OCR method: pdf → `pdftoppm -r 400` PNG → Tesseract (psm 11 for driver matrix, psm 6 for special solenoids)

## Driver outputs and coil leads

Williams' operator handbook cross-check (Table 4, page 11) confirms the full solenoid list, wire colors, and harness pins. Blending that table with the schematic OCR yields the consolidated map below.

| Solenoid | Function | Wire color | Driver transistor | Harness pins | Coil part |
| --- | --- | --- | --- | --- | --- |
| 01 | Ball release | GRY-BRN | Q15 | 2P11-4 / 8P3-1 / 8P6-17 | SA-23-850-DC |
| 02 | Ball ramp thrower | GRY-RED | Q17 | 2P11-5 / 8P3-2 / 8P6-18 | SG-23-850-DC |
| 03 | Special relay (A/C) | GRY-ORN | Q19 | 2P11-7 / 3P7-1 | 5580-09555-00 |
| 04 | Left 3-bank reset | GRY-YEL | Q21 | 2P11-8 / 8P3-4 / 8P6-20 | SA3-23-850-DC |
| 05 | Right 3-bank reset | GRY-GRN | Q23 | 2P11-9 / 8P3-5 / 8P6-21 | SA3-23-850-DC |
| 06 | Buzzer | GRY-BLU | Q25 | 2P11-3 / 8P3-6 / 8P6-22 | A-8597 |
| 07 | Lower eject hole | GRY-VIO | Q27 | 2P11-2 / 8P3-7 | SG-23-850-DC |
| 08 | Upper eject hole | GRY-BLK | Q29 | 2P11-1 / 8P3-8 | SG-23-850-DC |
| 09 | 5-bank #1 (left) reset | BRN-BLK | Q31 | 2P9-9 / 8P3-9 | SA5-24-750-DC |
| 10 | 5-bank #2 reset | BRN-RED | Q33 | 2P9-7 / 8P3-10 | SA5-24-750-DC |
| 11 | 5-bank #3 reset | BRN-ORN | Q35 | 2P9-1 / 8P3-11 | SA5-24-750-DC |
| 12 | 5-bank #4 reset | BRN-YEL | Q37 | 2P9-2 / 8P3-12 | SA5-24-750-DC |
| 13 | 5-bank #5 (right) reset | BRN-GRN | Q39 | 2P9-3 / 8P3-13 | SA5-24-750-DC |
| 14 | 5-bank release | BRN-BLU | Q41 | 2P9-4 / 8P3-14 | SA6-24-750-DC |
| 15 | Bell | BRN-VIO | Q43 | 2P9-5 / 7P1-17 | SM-29-1000-DC |
| 16 | Coin lockout | BRN-GRY | Q45 | 2P9-6 / 7P1-18 / 7P2-4 | SM-35-4000-DC |
| 17 | Left kicker (spec. sw. 5) | BLU-BRN | Q47 | 2P12-7 / 8P3-17 / 8P6-11 | SG-23-850-DC |
| 18 | Right kicker (spec. sw. 3) | BLU-RED | Q49 | 2P12-4 / 8P3-18 / 8P6-12 | SG-23-850-DC |
| 19 | Upper kicker (spec. sw. 2) | BLU-ORN | Q51 | 2P12-3 / 8P3-19 | SG-23-850-DC |
| 20 | Mini-ball kicker | BLU-YEL | Q53 | 2P12-6 / 8P3-20 | SG-23-850-DC |
| 21 | Left Magna-Save relay | BLU-GRN | Q55 | 2P12-8 / 8P3-21 / 8P6-15 | A-8592 |
| 22 | Right Magna-Save relay | BLU-BLK | Q57 | 2P12-9 / 8P3-22 / 8P6-16 | A-8592 |

Special switch and flipper wiring (from the same table):

- Solenoids 17–19 share cabinet switch feeds via 2P13 (ORN-BRN / ORN-RED / ORN-BLK).
- Flipper buttons run through ORN-VIO (right) and ORN-GRY (left) at 2P12, with coil harnesses:
	- Lower right flipper — BLU-VIO — 7P1-8 / 8P3-34 / 8P6-3 — SFL-19-400/30-750-DC
	- Upper right flipper — BLK-YEL — 7P1-31 / 8P3-33 — SFL-19-400/30-750-DC
	- Lower left flipper — BLU-GRY — 7P1-10 / 8P3-32 / 8P6-4 — SFL-19-400/30-750-DC
	- Upper left flipper — BLK-BLU — 7P1-30 / 8P3-31 — SFL-19-400/30-750-DC

These handbook values align with the wire colors and connector tags recovered from the schematic OCR, giving us a definitive reference for MPF naming.

## Playfield device list (legible strings)

| Device text | Context from OCR |
| --- | --- |
| 5-BANK #2 DROP TARGET RESET | Column 2 block |
| 5-BANK #3 DROP TARGET RESET | Column 2 block |
| LOWER EJECT HOLE | Column 2 block |
| UPPER EJECT HOLE | Column 2 block |
| BALL RELEASE | Column 2 block |
| 5-BANK #5 DROP TARGET RESET (BOT.) | Column 2 block |
| UPPER MINI-BALL KICKER | Column 2 block |
| BALL KICKER | Column 2 block |
| TARGET RELEASE | Column 2 block |
| RIGHT RAMP THROWER | Column 3 block |
| RIGHT 3-BANK RESET | Column 3 block |
| LEFT KICKER / RIGHT KICKER | Column 3 block, near `8L21/8L22` |
| MAGNET | Column 3 block (two entries, likely left/right Magna-Save) |
| RIGHT RELAY | Column 3 block |
| 100 KICKER | Column 3 block |
| BOTTOM RIGHT FLIPPER | Column 3 block |
| FLIPPER | Column 3 block |

## Interconnect harness callouts (OCR transcription)

| Connector | OCR label | Notes |
| --- | --- | --- |
| 8L10 | 5-BANK #2 DROP TARGET RESET | Confirmed on schematic p27 (row header above 8L10). |
| 8L11 | 5-BANK #3 DROP TARGET RESET | Confirmed on schematic p27. |
| 8L7 | LOWER EJECT HOLE | Verified label on schematic p27. |
| 8L8 | UPPER EJECT HOLE | Verified label on schematic p27. |
| 8L18 | BALL RELEASE | Tag legible on schematic p27; feed for ball release coil. |
| 8L13 | 5-BANK #5 (BOT.) DROP TARGET RESET | Confirmed via manual text (bottom reset coil). |
| 8L15 | 5-BANK #4 DROP TARGET RESET | Digit clarified on new scan; sequential order 5-bank #4. |
| 8L19 | UPPER MINI-BALL KICKER | Verified via manual label. |
| 8L20 | BALL KICKER / TARGET RELEASE | Manual shows combined note; coil handles lower ball kick + gate release. |
| 8C21 | RIGHT RAMP THROWER | Confirmed label on schematic p27. |
| 8L21 | LEFT KICKER | Verified label; cabinet side kicker. |
| 8L22 | RIGHT KICKER | Verified label; matches manual. |
| 8R2 | RIGHT RELAY | Confirmed (A/C relay) on schematic p27. |
| 8R6 | 100 KICKER (LEFT) | Manual identifies left 100-point kicker at this plug. |
| 8R7 | 100 KICKER (CENTER) | Label clarified by manual; central jet/slingshot. |
| 8R8 | 100 KICKER (RIGHT) | Label clarified by manual; right-side jet/slingshot. |
| 8L25 | LEFT MAGNET | Magna-Save left coil, confirmed. |
| 8L28 | RIGHT MAGNET | Magna-Save right coil, confirmed. |
| 8D156 | BOTTOM RIGHT FLIPPER | Lower-right flipper coil harness. |
| 8D157 | FLIPPER | Adjacent connector; probably upper flipper assembly. |

## Proposed MPF coil identifiers (WIP)

| Solenoid | Candidate MPF name | Device (from OCR) | Confidence |
| --- | --- | --- | --- |
| 07 | c_jl_right_ramp_thrower | Right ramp thrower (8C21) | High — schematic p27 labels 8C21 as ramp thrower. |
| 08 | c_jl_right_threebank_reset | Right 3-bank reset (8D133) | Medium — need driver column confirmation from manual. |
| 09 | c_jl_fivebank_reset_upper | 5-bank #2 drop target reset (8L10) | High — schematic p27. |
| 10 | c_jl_fivebank_reset_mid | 5-bank #3 drop target reset (8L11) | High — schematic p27. |
| 11 | c_jl_fivebank_reset_lower | 5-bank #5 (bot.) drop target reset (8L13) | High — schematic p27. |
| 12 | c_jl_fivebank_reset_tail | 5-bank #4 drop target reset (8L15) | High — digit clarified on new scan. |
| 14 | c_jl_threebank_reset_left | Left 3-bank reset (label near 8D132) | Medium — need to lock exact connector. |
| 15 | c_jl_threebank_reset_right | Right 3-bank reset (label near 8D133) | Medium — confirm once coil chart transcribed. |
| 17 | c_jl_100_kicker_left | 100-point kicker (8R6) | Medium — confirm which sling/jet via switch table. |
| 18 | c_jl_special_sw3 | Special solenoid (schematic `SPEC. SW 3`) | High — manual indicates switch 3. |
| 19 | c_jl_special_sw2 | Special solenoid (schematic `SPEC. SW 2`) | High — manual indicates switch 2. |
| 20 | c_jl_special_sw4 | Special solenoid (schematic `SPEC. SW 4`) | High — manual shows switch 4. |
| 21 | c_jl_left_magna_save | Magna-Save left (8L25) | High — schematic p27. |
| 22 | c_jl_right_magna_save | Magna-Save right (8L28) | High — schematic p27. |

## Special solenoid triggers (OCR)

| Solenoid | OCR text | Probable special switch | Notes |
| --- | --- | --- | --- |
| 17 | `SPEC. SW S` | 5 | Characters align with "S" = 5; likely right slingshot. |
| 18 | `SPEC. SW 3` | 3 | Text is clear; probably left slingshot or jet. |
| 19 | `SPEC. SW 2` | 2 | Matches lower pop bumper in other System 7 layouts. |
| 20 | `SPEC. SW 4` | 4 | Confirmed via driver_special_psm11.txt (manual page 27). |
| 21 | `SPEC. SW 8` | 8 | Manual shows switch 8; confirm actual device (likely Magna-Save enable relay). |
| 22 | `SPEC. SW 9` | 9 | Confirmed. |

## Outstanding items

1. Map each special solenoid to its exact playfield device (slingshots vs. jet bumpers vs. Magna-Save relay) using the operator handbook switch chart.
2. Confirm driver transistors for SOL.23–SOL.26 once a higher fidelity scan is available; current entries rely on harness observations.
3. Capture coil resistance / part numbers from the parts supplement once switch/coil tables are complete.
