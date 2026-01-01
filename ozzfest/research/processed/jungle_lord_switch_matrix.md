# Jungle Lord Switch Matrix (verified transcription)

Primary references:
- Williams Jungle Lord schematic (Playfield Switch Wiring Diagram)
- Pinrepair Williams System 3–7 switch matrix summary (wire colors and pinouts)

OCR (ImageMagick crop + Tesseract) provided the initial capture; the tables below reflect manual corrections against the references above.

## Switch matrix buses

### Columns (green harness, driver board 2J2)

| Column | Driver pin | Wire color | Notes |
| --- | --- | --- | --- |
| 1 | 2J2-9 | GRN-BRN | Standard Williams column 1; 2J2-4 is the key position between columns 4 and 5. |
| 2 | 2J2-8 | GRN-RED | |
| 3 | 2J2-7 | GRN-ORN | |
| 4 | 2J2-6 | GRN-YEL | |
| 5 | 2J2-5 | GRN-BLK | |
| 6 | 2J2-3 | GRN-BLU | 2J2-4 unused (key). |
| 7 | 2J2-2 | GRN-VIO | |
| 8 | 2J2-1 | GRN-GRY | |

### Rows (white harness, driver board 2J3)

| Row | Driver pin | Wire color | Notes |
| --- | --- | --- | --- |
| 1 | 2J3-9 | WHT-BRN | |
| 2 | 2J3-8 | WHT-RED | |
| 3 | 2J3-7 | WHT-ORN | |
| 4 | 2J3-6 | WHT-YEL | |
| 5 | 2J3-5 | WHT-GRN | |
| 6 | 2J3-4 | WHT-BLU | 2J3-2 unused (key). |
| 7 | 2J3-3 | WHT-VIO | |
| 8 | 2J3-1 | WHT-GRY | |

Harness routing (2P2/8P1 for columns, 2P3/8P2 for rows) matches the pin numbering above; only the driver-board pins are listed here to keep the APC mapping focused. Upper playfield switches bypass 8P4/8J4 per schematic annotation.

### Connector path (per schematic callouts)

| Matrix leg | Driver board plug | Interconnect board plug | Playfield harness | Notes |
| --- | --- | --- | --- | --- |
| Columns | 2J2 | 2P2 | 8P1 → 8U1 | OCR block (“2J2 2P2 8P1 8U1”) confirms the standard Williams path from driver to playfield for the green column bundle. |
| Rows | 2J3 | 2P3 | 8P2 → 8U2 | OCR block (“2J3 2P3 8P2 8U2”) shows the equivalent white row bundle path. |

When documenting the APC harness, mirror this sequence (driver → interconnect → cabinet plug → playfield plug). Once the official schematic PDF is in the repository, verify the `8U1/8U2` designators and update if the manual uses `8J1/8J2` instead.

## Switch matrix assignments

| Switch | Row | Column | Description | Score notes |
| --- | --- | --- | --- | --- |
| 09 | 1 (WHT-BRN) | 2 (GRN-RED) | Right Ball Ramp | |
| 10 | 2 (WHT-RED) | 2 (GRN-RED) | Left Ball Ramp | |
| 11 | 3 (WHT-ORN) | 2 (GRN-RED) | Not used | |
| 12 | 4 (WHT-YEL) | 2 (GRN-RED) | Left Kicker | 10 |
| 13 | 5 (WHT-GRN) | 2 (GRN-RED) | "L" Rollover | 5000 |
| 14 | 6 (WHT-BLU) | 2 (GRN-RED) | "O" Rollover | 5000 |
| 15 | 7 (WHT-VIO) | 2 (GRN-RED) | "R" Rollover | 5000 |
| 16 | 8 (WHT-GRY) | 2 (GRN-RED) | "D" Rollover | 5000 |
| 17 | 1 (WHT-BRN) | 3 (GRN-ORN) | 1 Target | 1000 |
| 18 | 2 (WHT-RED) | 3 (GRN-ORN) | 2 Target | 1000 |
| 19 | 3 (WHT-ORN) | 3 (GRN-ORN) | 3 Target | 1000 |
| 20 | 4 (WHT-YEL) | 3 (GRN-ORN) | 4 Rollover | 1000 |
| 21 | 5 (WHT-GRN) | 3 (GRN-ORN) | 5 Rollover | 1000 |
| 22 | 6 (WHT-BLU) | 3 (GRN-ORN) | Left Drain Lane | 5000 |
| 23 | 7 (WHT-VIO) | 3 (GRN-ORN) | Right Drain Lane | 5000 |
| 24 | 8 (WHT-GRY) | 3 (GRN-ORN) | Turnaround Lower Rollover | 1000 / 16000* |
| 25 | 1 (WHT-BRN) | 4 (GRN-YEL) | Right 3-Bank, Lower Drop Target | 1000 |
| 26 | 2 (WHT-RED) | 4 (GRN-YEL) | Right 3-Bank, Center Drop Target | 1000 |
| 27 | 3 (WHT-ORN) | 4 (GRN-YEL) | Right 3-Bank, Upper Drop Target | 1000 |
| 28 | 4 (WHT-YEL) | 4 (GRN-YEL) | Right Kicker | 10 |
| 29 | 5 (WHT-GRN) | 4 (GRN-YEL) | Left 3-Bank, Lower Drop Target | 1000 |
| 30 | 6 (WHT-BLU) | 4 (GRN-YEL) | Left 3-Bank, Center Drop Target | 1000 |
| 31 | 7 (WHT-VIO) | 4 (GRN-YEL) | Left 3-Bank, Upper Drop Target | 1000 |
| 32 | 8 (WHT-GRY) | 4 (GRN-YEL) | Turnaround, Upper Rollover | 1000* |
| 33 | 1 (WHT-BRN) | 5 (GRN-BLK) | 5-Bank, #1 Drop Target (Left) | 10000** |
| 34 | 2 (WHT-RED) | 5 (GRN-BLK) | 5-Bank, #2 Drop Target | 10000** |
| 35 | 3 (WHT-ORN) | 5 (GRN-BLK) | 5-Bank, #3 Drop Target | 10000** |
| 36 | 4 (WHT-YEL) | 5 (GRN-BLK) | 5-Bank, #4 Drop Target | 10000** |
| 37 | 5 (WHT-GRN) | 5 (GRN-BLK) | 5-Bank, #5 Drop Target (Right) | 10000** |
| 38 | 6 (WHT-BLU) | 5 (GRN-BLK) | Upper Eject Hole | 1000 |
| 39 | 7 (WHT-VIO) | 5 (GRN-BLK) | Lower Eject Hole | 1000 |
| 40 | 8 (WHT-GRY) | 5 (GRN-BLK) | Upper Kicker | 10 |
| 41 | 1 (WHT-BRN) | 6 (GRN-BLU) | Playfield Tilt | |
| 42 | 2 (WHT-RED) | 6 (GRN-BLU) | Outhole | |
| 43 | 3 (WHT-ORN) | 6 (GRN-BLU) | Ballshooter Trough | |
| 44 | 4 (WHT-YEL) | 6 (GRN-BLU) | Playfield Entry | |
| 45 | 5 (WHT-GRN) | 6 (GRN-BLU) | Upper Left Standup | 10 |
| 46 | 6 (WHT-BLU) | 6 (GRN-BLU) | Left Standup | 10 |
| 47 | 7 (WHT-VIO) | 6 (GRN-BLU) | Right Standup | 10 |
| 49 | 1 (WHT-BRN) | 7 (GRN-VIO) | Spine Target Button | |
| 50 | 2 (WHT-RED) | 7 (GRN-VIO) | Left Magnet Button | |

* Switch 24 scores 1000 when triggered before switch 32, 1000 after switch 32 if Advance Bonus X or Lite Drain Shield are lit, and 16,000 after switch 32 with neither lamp lit.

** Jungle Lord doubles 5-bank awards to 100,000 during Double-Throw.

## Upper playfield harness note

The schematic callout tagged to the matrix diagram states: “Switches mounted on upper playfield bypass 8P4/8J4.” In practice, the white/green and green/xx pairs for the mini-playfield components (5-bank drop targets 33–37, upper eject 38, upper kicker 40, turnaround rollover 32, and the upper standup cluster 45–47) run directly from the main playfield harness back to interconnect plugs 2P2/2P3 without first breaking at the cabinet inline connector set. When mapping the APC, treat those switches as continuous runs: there is no intermediate disconnect between the upper-playfield assembly and the driver board.

## Outstanding items

1. After the official schematic PDF is staged, annotate each switch row/column entry with its specific 8P#/8U# pin and update the connector table accordingly.
