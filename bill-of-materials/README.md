# Bill of Materials (BOM) — pinball-soup

This directory contains bills of materials for each physical pinball machine in the pinball-soup project. Each machine has its own BOM file listing every purchasable part required to build it, along with usage details.

## Structure

```
bill-of-materials/
├── README.md                        # this file
├── google-sheets-import.md          # steps to access & import the master Google Sheets BOM
├── common-tools-and-supplies.md     # shared tools, consumables, and supplies across all machines
├── ozzfest-bom.md                   # Ozzfest machine — FAST Pinball + Jungle Lord cabinet
└── time-warped-bom.md               # Time Warped machine — APC + Williams System 7 cabinet
```

## Machine Overview

| Machine | Cabinet Base | Hardware Platform | Controller | Status |
|---|---|---|---|---|
| Ozzfest | Williams Jungle Lord (System 7) | FAST Modern Platform | FAST Neuron | In Progress — software mostly complete, hardware BOM being defined |
| Time Warped | Williams Time Warp (System 7) | APC (Arduino Pinball Controller) | Arduino Due + LISY/Pi | In Progress — software functional, APC assembled |

## How to Use

1. Start with the machine-specific BOM (e.g. `ozzfest-bom.md`) for the full parts list
2. Cross-reference `common-tools-and-supplies.md` for tools and consumables you'll need regardless of machine
3. If importing from the master Google Sheet, follow `google-sheets-import.md`

## Key Reference Links

- **FAST Pinball Docs**: https://fastpinball.com/docs/
- **FAST Pinball Shop**: https://shop.fastpinball.com/
- **FAST Modern Platform Overview**: https://fastpinball.com/modern/
- **FAST Wiring Guides**: https://fastpinball.com/wiring/
- **FAST + MPF Configuration**: https://fastpinball.com/mpf/
- **MPF Documentation**: https://missionpinball.org/
- **APC Documentation**: https://github.com/AmokSolderer/APC
