# Jungle Lord Reference Assets

The Jungle Lord schematics and manuals hosted on IPDB are behind a Cloudflare JavaScript challenge. Automated tools (curl, wget, pdftotext) inside the workspace return HTML 404/503 placeholders and cannot complete the download.

## Required documents

| Asset | IPDB listing | Notes |
| --- | --- | --- |
| Schematic Diagrams | https://www.ipdb.org/files/1338/Williams_1981_Jungle_Lord_Schematic_Diagrams.pdf | Downloaded 2025-12-29 → [ozzfest/research/raw/Williams_1981_Jungle_Lord_Schematic_Diagrams_paginated_some_with_red_lining.pdf](ozzfest/research/raw/Williams_1981_Jungle_Lord_Schematic_Diagrams_paginated_some_with_red_lining.pdf). |
| Playfield Solenoid Wiring Diagram | https://www.ipdb.org/files/1338/Williams_1981_Jungle_Lord_Playfield_Solenoid_Wiring_Diagram.pdf | Covered by the paginated schematic bundle above. |
| Parts Supplement (March 1981) | https://www.ipdb.org/files/1338/Williams_1981_Jungle_Lord_Parts_Supplement.pdf | Optional but useful for coil part numbers and specs. |
| Instruction Booklet | https://www.ipdb.org/files/1338/Williams_1981_Jungle_Lord_Instruction_Booklet.pdf | Downloaded 2025-12-29 → [ozzfest/research/raw/Williams_1981_Jungle_Lord_Operators_Handbook.pdf](ozzfest/research/raw/Williams_1981_Jungle_Lord_Operators_Handbook.pdf). |

## Manual download workflow

1. Open the desired URL in a normal web browser (Chrome/Firefox). Cloudflare will present a "Just a moment" spinner and set a cookie after a few seconds.
2. Once the PDF loads, download it locally.
3. Copy the file into the repository under `ozzfest/research/raw/` using the same filenames listed above (or append `_manual` if you want to keep the original failed placeholders).
4. Run `file <filename>` inside the repo to confirm it reports `PDF document` instead of `HTML document`.

### Download status (Dec 29, 2025)

- Schematic bundle and operator handbook copied from IPDB via browser session; see filenames noted above.
- Legacy `Jungle_Lord_Schematic*.pdf` placeholders were removed after verification (all now confirm as `%PDF` headers).

After the real PDFs are present, re-run the solenoid verification tasks:

- Update [ozzfest/research/processed/jungle_lord_solenoid_map.md](processed/jungle_lord_solenoid_map.md) with driver transistor numbers, connector IDs, and confirmed coil functions.
- Extract any missing switch or lamp tables as needed.

With authentic PDFs staged, use the new images for any follow-up OCR instead of the older placeholder captures.
