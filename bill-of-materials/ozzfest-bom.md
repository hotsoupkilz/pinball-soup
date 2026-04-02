# Ozzfest — Bill of Materials (FAST Pinball Modern Platform)

> **Machine**: Ozzfest (Ozzfest-themed homebrew)
> **Cabinet Base**: Williams Jungle Lord (System 7)
> **Hardware Platform**: FAST Pinball Modern Platform
> **Controller**: FAST Neuron (FP-CPU-2000)
> **Software**: Mission Pinball Framework (MPF) 0.57+ with Godot Media Controller (GMC)
> **Source Spreadsheet**: https://docs.google.com/spreadsheets/d/1JEHx_08Zi1kPXPQiNM-eau-H2xfTsLFBgkRzyfTPdEI/edit?gid=1386834576#gid=1386834576 (requires auth — see [google-sheets-import.md](google-sheets-import.md))

---

## Table of Contents
1. [FAST Pinball Control System](#1-fast-pinball-control-system)
2. [Power System](#2-power-system)
3. [I/O Boards (Switches & Drivers)](#3-io-boards-switches--drivers)
4. [Expansion Boards (LEDs, Servos, etc.)](#4-expansion-boards-leds-servos-etc)
5. [Lighting](#5-lighting)
6. [Display](#6-display)
7. [Audio](#7-audio)
8. [Playfield Mechanical Parts](#8-playfield-mechanical-parts)
9. [Cabinet & Backbox](#9-cabinet--backbox)
10. [Wiring & Connectors](#10-wiring--connectors)
11. [Host Computer](#11-host-computer)
12. [Playfield Components — Switches](#12-playfield-components--switches)
13. [Playfield Components — Coils & Solenoids](#13-playfield-components--coils--solenoids)
14. [Playfield Components — Assemblies & Mechanisms](#14-playfield-components--assemblies--mechanisms)
15. [Balls](#15-balls)
16. [Software & Firmware](#16-software--firmware)
17. [Reference Links](#17-reference-links)

---

## 1. FAST Pinball Control System

> **Purchasing note — FAST Neuron Starter Bundle**: The Neuron Controller, Power Filter Board, one Expansion Board, one Playfield I/O 3208, and the Playfield Interchange Board are all available as a single **FAST Neuron Starter Bundle** for **$569** at https://shop.fastpinball.com/product/fast-neuron-starter-bundle/53?cs=true&cst=custom. Optional add-ons within the bundle: power supplies (+$150) and connectors+pins (+$29). Items included in the bundle are marked *(included in Starter Bundle)* below.

### FAST Neuron Controller (FP-CPU-2000)
- **Qty**: 1
- **Price**: Included in Starter Bundle ($569 bundle total)
- **Vendor**: https://shop.fastpinball.com/product/fast-neuron-starter-bundle/53?cs=true&cst=custom
- **Docs**: https://fastpinball.com/products/controllers/neuron/
- *(included in Starter Bundle)*
- Central hub connecting host PC to all FAST I/O boards, expansion boards, and display bus
- Mounts in backbox; connects to host PC via USB, provides NET (I/O Loop), EXP (Expansion Bus), and DSP (Display Bus) connections
- Built-in expansion board provides 4 LED ports (128 RGB LEDs for backbox lighting) and 3 breakout headers for servos/steppers
- Supports up to 120 switches and 120 drivers through connected I/O boards
- Has Raspberry Pi header for direct mounting of Pi as host PC with integrated power and fan management

---

## 2. Power System

### FAST Smart Power Filter Board (Neuron version)
- **Qty**: 1
- **Price**: *(included in Starter Bundle)*
- **Vendor**: https://shop.fastpinball.com/product/fast-neuron-starter-bundle/53?cs=true&cst=custom
- **Docs**: https://fastpinball.com/products/power/smart-power-filter-board/
- *(included in Starter Bundle)*
- Connects between power supplies and Neuron; filters and distributes 48V and 12V power throughout the machine
- Contains three large capacitors that store reserve power for high-current coil bursts (flipper power strokes)
- Provides machine-wide voltage and current monitoring; reports status to Neuron via EXP bus
- Required for any FAST Modern Platform machine — do not skip this board

### 48V Power Supply — Mean Well RSP-500-48
- **Qty**: 1
- **Price**: Part of optional power supply add-on ($150 for both PSUs when added to Starter Bundle)
- **Vendor**: FAST (via Starter Bundle add-on) or Mouser, Digi-Key, Amazon
- **Spec Sheet**: https://www.meanwellusa.com/webapp/product/search.aspx?prod=RSP-500
- Can optionally be added to the FAST Neuron Starter Bundle — includes all PSUs required for machine
- Powers all high-voltage coils, solenoids, and magnets at 48VDC (10.5A rated)
- Constant current limiting overload protection — critical for pinball coil spikes that briefly exceed rated current
- Wide AC input range (85-264VAC) supports both North American 120V and European 240V power
- Has internal fan; ensure proper airflow in backbox mounting location

### 12V Power Supply — Mean Well LRS-150-12
- **Qty**: 1
- **Price**: Part of optional power supply add-on ($150 for both PSUs when added to Starter Bundle)
- **Vendor**: FAST (via Starter Bundle add-on) or Mouser, Digi-Key, Amazon
- **Spec Sheet**: https://www.meanwellusa.com/webapp/product/search.aspx?prod=LRS-150
- Can optionally be added to the FAST Neuron Starter Bundle — includes all PSUs required for machine
- Powers all low-voltage systems: FAST boards, LEDs (via 5V generated on-board), host PC, audio, displays, optos, servos
- 12.5A rated; sufficient for typical machine with ~100 LEDs, host PC, and audio amplifiers
- Alternative: Mean Well LRS-100-12 (8.5A) if machine has fewer LEDs and lower 12V requirements

### FAST Smart Fuse Block
- **Qty**: 1
- **Vendor**: https://shop.fastpinball.com/
- **Docs**: https://fastpinball.com/products/power/smart-fuse-block/
- Distributes fused power from power filter board to multiple circuits throughout the machine
- Each fuse is individually monitorable for blown fuse detection
- Simplifies wiring by centralizing fuse management in one location in the backbox

### FAST Playfield Interchange Board
- **Qty**: 1
- **Price**: *(included in Starter Bundle)*
- **Vendor**: https://shop.fastpinball.com/product/fast-neuron-starter-bundle/53?cs=true&cst=custom
- **Docs**: https://fastpinball.com/products/power/playfield-interchange-board/
- *(included in Starter Bundle)* — on playfield, connects playfield to backbox
- Mounts at rear of playfield; provides single disconnect point between cabinet and playfield
- All I/O loop Cat-5 cables, expansion bus cables, and power cables pass through this board
- Allows complete playfield removal by unplugging a few connectors — essential for maintenance and assembly

### Solid State Relay (SSR) — for soft power control (optional)
- **Qty**: 1
- **Vendor**: Mouser, Digi-Key, Amazon
- **Docs**: https://fastpinball.com/wiring/neuron/solid-state-relay/
- Enables soft power on/off via a low-voltage pushbutton instead of a hard AC toggle switch
- Must be rated for combined inrush current of both power supplies (check PSU datasheets)
- Wires between AC mains input and power supplies, controlled by Neuron's SSR output

### IEC Line Input Receptacle + EMI Filter
- **Qty**: 1
- **Vendor**: Mouser, Amazon, pinball parts suppliers
- **Docs**: https://fastpinball.com/wiring/neuron/ac-line-input/#ac-line-fuse
- IEC inlet panel mount with integrated EMI filter
- Do not use EMI filter if trying to make fully compliant, but FAST says it is fine for home use
- Mounts on rear of cabinet for AC mains power input

### Fuse Holder (5×20mm)
- **Qty**: 1
- **Vendor**: [Mouser — 5×20mm fuse holders](https://www.mouser.com/c/?for%20use%20with=Fuse%20Holders%2C%20No.%20821%205%20x%2020%20mm)
- **Docs**: https://fastpinball.com/wiring/neuron/ac-line-input/#ac-line-fuse
- Holds the AC line fuse; mounts near the IEC inlet

### 8A Fuse (AC Line)
- **Qty**: 1
- **Docs**: https://fastpinball.com/wiring/neuron/ac-line-input/#ac-line-fuse
- AC line fuse — 8A rating for combined inrush of both power supplies

### SPDT Switch (AC Power)
- **Qty**: 1
- **Docs**: https://fastpinball.com/wiring/neuron/ac-line-input/#ac-power-switch
- Main AC power on/off switch for the machine

### Power Cord
- **Qty**: 1
- Standard IEC C13/C14 power cord for AC mains input

---

## 3. I/O Boards (Switches & Drivers)

The Ozzfest machine is based on Jungle Lord which has approximately 33 switches and 20 drivers/coils. The FAST I/O board selection below accommodates this layout with room for additional custom switches and drivers.

### FAST I/O 3208 Board (32 switches, 8 drivers)
- **Qty**: 1
- **FAST Part #**: FP-IO-3208
- **Price**: *(included in Starter Bundle)*
- **Vendor**: https://shop.fastpinball.com/product/fast-neuron-starter-bundle/53?cs=true&cst=custom
- **Docs**: https://fastpinball.com/products/ioboards/3208/
- Primary I/O board for the majority of playfield switches (rollover, target, slingshot, pop bumper switches)
- 32 switch inputs cover most of the Jungle Lord playfield switches including trough, outlanes, inlanes, standup targets, and drop targets
- 8 driver outputs for lower-current coils such as kickout holes, drop target reset, and slingshots
- Located under the playfield near the center for shortest wire runs to most switches

### FAST I/O 1616 Board (16 switches, 16 drivers)
- **Qty**: 1
- **FAST Part #**: FP-IO-1616
- **Vendor**: https://shop.fastpinball.com/
- **Docs**: https://fastpinball.com/products/ioboards/1616/
- Secondary I/O board for remaining switches and the high-current drivers (flippers, pop bumpers)
- 16 driver outputs cover flippers (2 main + optional upper), pop bumpers (3), ball launch, trough eject, and remaining solenoids
- 16 additional switch inputs for cabinet buttons, coin door, tilt, slam tilt, and any additional playfield switches
- Located under the playfield near the flippers/cabinet area

### FAST Cabinet I/O Board
- **Qty**: 1
- **FAST Part #**: FP-IO-0024
- **Price**: $159
- **Vendor**: https://shop.fastpinball.com/product/fp-io-0024/56?cs=true&cst=custom
- **Docs**: https://fastpinball.com/products/ioboards/cabinet/
- Used for cabinet switches (start, flippers, others): start button, coin door switches, service buttons, tilt bob, slam tilt
- 24 switch inputs, 1 high-current driver, 7 low-current/digital drivers
- Includes coin door interface for credit/coin switches, and digital outputs for coin counter/lockout
- Mounts in cabinet near the coin door area for short wire runs

### RJ45 / Cat-5 Ethernet Cables (for I/O Loop)
- **Qty**: 4-6 (varies by routing)
- **Vendor**: Any — Amazon, Monoprice, etc.
- Used for connecting FAST boards to each other via the FAST I/O Loop ring topology
- Each cable goes from the "OUT" port of one board to the "IN" port of the next, plus the return cable back to the Neuron
- Keep cables as short as practical; measure your specific routing before ordering lengths
- Route through the Playfield Interchange Board for any cables crossing the playfield-to-cabinet boundary

---

## 4. Expansion Boards (LEDs, Servos, etc.)

### FAST Expansion Board FP-EXP-0071 (128 LEDs, 4 Servos)
- **Qty**: 1 (under playfield)
- **Price**: *(included in Starter Bundle)* — choose one: 256 LEDs, or 128 LEDs + 4 servos
- **Vendor**: https://shop.fastpinball.com/product/fast-neuron-starter-bundle/53?cs=true&cst=custom
- **Docs**: https://fastpinball.com/products/expansion/71/
- Primary playfield expansion board: drives all under-playfield RGB insert LEDs and up to 4 servos for playfield toys
- 128 LED outputs at 4 ports (32 per port) — sufficient for all Jungle Lord playfield insert positions plus additional custom inserts
- 4 servo outputs for interactive playfield toys (e.g., animated figures, diverters, rotating mechanisms)
- Connects to Neuron via Expansion Bus (Cat-5 cable through Playfield Interchange Board)

### FAST Expansion Board FP-EXP-0081 (256 LEDs) — Optional
- **Qty**: 0-1 (if more LEDs needed)
- **Vendor**: https://shop.fastpinball.com/
- **Docs**: https://fastpinball.com/products/expansion/81/
- Additional LED-only expansion board if the 128 LEDs from the 0071 plus the Neuron's built-in 128 are insufficient
- 256 LED outputs across 8 ports — for machines with extensive RGB lighting effects
- Useful if adding under-cabinet lighting, side rail lighting, or extensive topper lighting
- Can be daisy-chained from the 0071's expansion port

### RJ45 / Cat-5 Ethernet Cables (for Expansion Bus)
- **Qty**: 2-4
- **Vendor**: Any
- Expansion Bus uses Cat-5 cables in a tree topology (NOT a loop — differs from I/O Loop)
- One cable from Neuron to under-playfield expansion board (through Playfield Interchange Board)
- Additional cables if daisy-chaining expansion boards or adding a cabinet/backbox expansion board

---

## 5. Lighting

### FAST RGB Playfield Insert LEDs
- **Qty**: 30-50 (depends on number of playfield inserts)
- **Vendor**: https://shop.fastpinball.com/
- **Docs**: https://fastpinball.com/products/lighting/rgb-led-insert/
- Direct replacement for incandescent bulbs in standard pinball playfield inserts
- Full RGB color control per LED — any color/animation can be set per insert via MPF light_player or show_player
- Wired to expansion board LED ports with 3-wire connections (data, 5V, ground)
- Jungle Lord has approximately 35 controlled lamp positions (L-O-R-D indicators, drop target indicators, specials, bonuses, etc.)
- The existing config uses lights like `l_letter_l`, `l_letter_o`, `l_letter_r`, `l_letter_d` for band indicators

### FAST RGB GI (General Illumination) LEDs
- **Qty**: 10-20
- **Vendor**: https://shop.fastpinball.com/
- **Docs**: https://fastpinball.com/products/lighting/rgb-gi-led/
- Replace original GI incandescent bulbs with individually-addressable RGB LEDs
- Provides ambient playfield illumination that can change color dynamically based on game mode (e.g., red for Meatloaf, blue for Dio)
- Distributed across the playfield for even illumination coverage
- Wired to expansion board LED ports same as insert LEDs

---

## 6. Display

### FAST RGB DMD (Dot Matrix Display) — Optional if using LCD
- **Qty**: 0-1
- **Vendor**: https://shop.fastpinball.com/
- **Docs**: https://fastpinball.com/products/display/rgb-dmd/
- Full color RGB LED-based dot matrix display; connects to Neuron via FAST Display Bus
- Mounts in backbox in the traditional DMD location
- Alternative to an LCD screen; provides a classic pinball DMD look with modern full-color capability
- If using an LCD monitor for display with Godot/GMC instead, this is not needed

### LCD Monitor (if not using FAST DMD)
- **Qty**: 0-1
- **Vendor**: Amazon, etc.
- If using Godot Media Controller for display output, a small LCD monitor (15-19") mounts in the backbox
- Connects to host PC via HDMI; displays Godot-rendered slides, videos, and animations
- Consider a monitor with VESA mount for clean backbox installation
- Ozzfest currently uses segment displays (from Jungle Lord) plus optional LCD for GMC content

### Segment Displays (existing from Jungle Lord)
- **Qty**: 5 (reuse from Jungle Lord — 4 player displays + 1 info display)
- **Source**: Original Jungle Lord machine
- The current config defines 5 segment displays: `info_display` (4 digit), `player1_display` through `player4_display` (7 digit each)
- These may continue working via FAST Neuron Display Bus with appropriate adapter, or can be replaced with FAST RGB segment displays
- If keeping originals, ensure proper wiring to Neuron's Display Bus connectors per FAST docs

---

## 7. Audio

### FAST Audio Interface Board (FP-AUD-0100)
- **Qty**: 1
- **FAST Part #**: FP-AUD-0100
- **Price**: $99
- **Vendor**: https://shop.fastpinball.com/product/fp-aud-0100/57?cs=true&cst=custom
- **Docs**: https://fastpinball.com/products/audio/audio-interface/
- Dedicated audio board for the FAST platform; connects to Neuron via Expansion Bus
- Provides amplified stereo output for main speakers, subwoofer output, and headphone jack
- Supports volume control commands from MPF game code
- Mounts in backbox near speakers

### Speakers (Main)
- **Qty**: 2
- **Vendor**: Pinball parts suppliers, Amazon
- Standard 4" or 5.25" full-range speakers for the backbox speaker panel
- Handle music, sound effects, and voice callouts during gameplay
- Match impedance and power handling to FAST Audio Interface output specifications
- Mount in backbox speaker panel openings (reuse Jungle Lord's existing speaker panel if compatible)

### Subwoofer (optional)
- **Qty**: 0-1
- **Vendor**: Amazon, car audio suppliers
- Small powered or passive subwoofer (6.5" or 8") for bass reinforcement
- Mounts inside the cabinet body for low-frequency impact during gameplay
- Connects to FAST Audio Interface subwoofer output
- Adds physical "thump" to bass-heavy Ozzfest music (Meatloaf, Black Sabbath, etc.)

---

## 8. Playfield Mechanical Parts

These are the physical mechanisms on the playfield that interact with the ball. Many of these can be salvaged from the donor Jungle Lord machine.

### Flipper Assemblies
- **Qty**: 2 (left and right main flippers; optionally a 3rd upper flipper)
- **Vendor**: Pinball Life, Marco Specialties, Planetary Pinball
- Complete flipper assembly includes: flipper bat, shaft, coil sleeve, link, plunger, return spring, EOS switch, coil stop, bushing
- Flippers use high-current coils with pulse+hold driver mode (initial strong pulse to flip, then reduced hold power)
- The FAST I/O board handles flipper logic locally with hardware rules for instant response
- Jungle Lord uses standard Williams 3" flipper bats

### Pop Bumper Assemblies
- **Qty**: 3 (standard Jungle Lord layout)
- **Vendor**: Pinball Life, Marco Specialties
- Complete pop bumper includes: body, cap, skirt, ring, spoon, coil, switch (normally-closed leaf switch under skirt)
- Each pop bumper has its own coil fired as an autofire rule on the I/O board (switch triggers coil with no host PC delay)
- Jungle Lord has 3 pop bumpers in the upper playfield area
- Replace worn caps, skirts, and rings as needed during rebuild

### Slingshot Assemblies
- **Qty**: 2 (left and right slingshots above flippers)
- **Vendor**: Pinball Life, Marco Specialties
- Each slingshot has: 2 leaf switches, 1 coil, rubber rings, slingshot plastic, metal bracket
- Operates as autofire — switch closure instantly fires coil to kick ball
- Replace worn rubber rings, check leaf switch alignment during assembly

### Drop Targets
- **Qty**: 1 bank (Jungle Lord has a set of drop targets)
- **Vendor**: Pinball Life, Marco Specialties
- Individual drop target faces, return springs, and the bank reset coil
- Each dropped target has a switch that registers the hit; bank reset coil pops all targets back up
- Check target faces for chips/cracks and replace as needed

### Kickout Holes / Saucers
- **Qty**: 2 (upper and lower kickout holes per current Ozzfest config)
- **Vendor**: Pinball Life
- Each has a coil that fires to eject the captured ball and a switch to detect ball presence
- Upper kickout hole triggers carousel band selection or wizard mode based on game state
- Lower kickout hole triggers wizard mode when qualified
- The current config references `s_kickout_hole_upper` and `s_kickout_hole_lower` switches

### Ball Trough Assembly
- **Qty**: 1
- **Vendor**: Pinball Life, Marco Specialties, or FAST Pinball (for IR trough boards)
- Houses balls when not in play; detects ball count via switches
- The current config defines `s_ball_trough_left` and `s_ball_trough_right` switches
- Trough eject coil launches ball to the plunger lane
- Consider upgrading to FAST Trough IR Boards for optical ball detection (more reliable than mechanical switches)

### FAST Trough IR Boards (optional upgrade)
- **Qty**: 1 set
- **Vendor**: https://shop.fastpinball.com/
- **Docs**: https://fastpinball.com/products/aux/trough-ir-boards/
- Infrared optical sensors replace mechanical trough switches for reliable ball detection
- No mechanical parts to wear out; more consistent detection than leaf switches
- Connect to I/O board switch inputs; require 12V power for IR emitters

### Ball Shooter / Plunger Assembly
- **Qty**: 1
- **Vendor**: Pinball Life, Marco Specialties
- Manual spring plunger (standard Jungle Lord) or auto-launch coil
- Plunger lane switch detects ball ready for launch
- If converting to auto-launch: replace manual plunger with a launch coil wired to an I/O board driver output

### Playfield (Surface)
- **Qty**: 1 (reuse/refurbish Jungle Lord playfield)
- **Source**: Original Jungle Lord machine
- Strip, clean, and optionally clear-coat the playfield before populating with new hardware
- Fill any unnecessary holes (from original Jungle Lord features not used in Ozzfest design)
- Drill new holes for any additional Ozzfest-specific switches, posts, or inserts
- Consider a custom playfield overlay or vinyl wrap for Ozzfest artwork theme

---

## 9. Cabinet & Backbox

### Cabinet Body
- **Qty**: 1 (reuse Jungle Lord cabinet or build custom)
- **Source**: Original Jungle Lord machine or custom-built
- Standard pinball cabinet dimensions (~22" wide × 52" long × variable height)
- Sand, fill, and repaint/wrap for Ozzfest theme
- Ensure all screw holes and mounting points are solid; repair any wood damage

### Backbox
- **Qty**: 1 (reuse Jungle Lord backbox or build custom)
- **Source**: Original Jungle Lord machine
- Houses: Neuron controller, power supplies, power filter board, fuse block, audio interface, speakers, display
- Ensure hinge and latch mechanism works properly
- Repaint/wrap/decal for Ozzfest artwork

### Backglass / Translite
- **Qty**: 1
- **Vendor**: Custom print (local print shop or online translite printing service)
- Custom Ozzfest-themed translite artwork printed on appropriate material
- Backlit by RGB LEDs driven from Neuron's built-in expansion board for dynamic color effects
- Standard Williams System 7 translite dimensions

### Cabinet Side Art
- **Qty**: 1 set (left + right)
- **Vendor**: Custom print / vinyl wrap providers
- Ozzfest-themed side art — vinyl decals or full cabinet wraps
- Applied after cabinet body is prepped and painted

### Legs (4) with Levelers
- **Qty**: 4
- **Vendor**: Pinball Life, Marco Specialties
- Standard pinball cabinet legs with threaded leveler feet
- Reuse Jungle Lord legs if in good condition, or replace with new chrome/black legs

### Coin Door Assembly
- **Qty**: 1
- **Vendor**: Pinball Life, Marco Specialties
- Includes coin door frame, coin mechanisms (or free play bypass), service buttons, and slam tilt switch
- Connects to FAST Cabinet I/O Board for switch inputs
- Reuse Jungle Lord coin door if in acceptable condition

### Lockdown Bar & Receiver
- **Qty**: 1
- **Vendor**: Pinball Life, Marco Specialties
- Secures the playfield glass in place
- Reuse from Jungle Lord or replace if chrome is degraded

### Playfield Glass
- **Qty**: 1
- **Vendor**: Pinball Life, Marco Specialties, or local glass shop
- Tempered glass cut to Jungle Lord playfield opening dimensions
- Replace if scratched, chipped, or cracked

---

## 10. Wiring & Connectors

### Wire — 18 AWG Stranded (multiple colors)
- **Qty**: ~200-500ft total across colors
- **Vendor**: Mouser, Digi-Key, Amazon
- **Docs**: https://fastpinball.com/wiring/standards/
- Primary wire gauge for switch wiring and lower-current connections
- FAST recommends using color coding per their wiring standards documentation
- Use stranded (not solid) wire for pinball — handles vibration and flexing better

### Wire — 16 AWG Stranded (for power and high-current drivers)
- **Qty**: ~100-200ft
- **Vendor**: Mouser, Digi-Key, Amazon
- **Docs**: https://fastpinball.com/wiring/neuron/ac-line-input/#your-machines-power-box
- Used for 48V power distribution, high-current coil connections (flippers, pop bumpers)
- Also used for ground bus wiring
- For AC line wiring to power boxes, use three colors: **white** (neutral), **black** (hot), **green** (ground)

### Fork Crimp Connector Terminals (16 AWG)
- **Qty**: 16
- **Unit Price**: ~$1.05
- **Vendor**: [Mouser — Fork Terminals, 16 AWG](https://www.mouser.com/c/connectors/terminals/?product=Fork%20Terminal&wire%20gauge%20max=16%20AWG)
- **Docs**: https://fastpinball.com/wiring/neuron/ac-line-input/#your-machines-power-box
- Distribution: 3 on AC input, 2 on line fuse, 2 on switch, 3–6 on 48V PSU, 3 on 12V PSU

### Molex 0.156" Connector Housings & Pins
- **Qty**: Assorted — 2-pin, 3-pin per FAST board requirements
- **Price**: $29 for connector+pin kit when added to Starter Bundle
- **Vendor**: FAST (via Starter Bundle add-on) or Mouser, Digi-Key
- **Docs**: https://fastpinball.com/products/controllers/neuron/#connectors-housings-needed
- 0.156" pitch connectors for power connections to FAST boards (12V in/out on Neuron, power filter board, I/O boards)
- Neuron needs: 1× 3-pin (12V in), 1× 2-pin (12V out)
- Each I/O board and expansion board has its own connector requirements — check product docs

### Molex 0.100" Connector Housings & Pins
- **Qty**: Assorted — 3-pin, 4-pin, 5-pin per FAST board requirements
- **Vendor**: Mouser, Digi-Key
- 0.100" pitch connectors for LED wiring (4-pin), host PC control headers (5-pin), SSR/power switch (3-pin), breakout headers (5-pin)
- Neuron needs: 4× 5-pin (host PC control, breakouts), 4× 4-pin (LEDs), 2× 3-pin (SSR, power switch)

### Crimp Pins (for above connectors)
- **Qty**: 200+ (buy extras — crimping takes practice)
- **Vendor**: Mouser, Digi-Key
- Matching crimp pins for both 0.156" and 0.100" connector housings
- Practice crimping technique before wiring the machine — see FAST skill guide: https://fastpinball.com/learning/skills/crimping/

### Crimp Tool
- **Qty**: 1
- **Vendor**: Amazon, Mouser
- **Docs**: https://fastpinball.com/learning/skills/crimping/
- Engineer PA-09 or equivalent precision crimp tool for 0.100" and 0.156" pins
- Good crimps are essential — bad crimps cause intermittent connection issues that are extremely difficult to debug
- This is the single most important tool for wiring a FAST pinball machine

### Quick-Connect / Spade Connectors (for switches and coils)
- **Qty**: 100+
- **Vendor**: Mouser, Digi-Key, Amazon
- 0.187" (3/16") and 0.250" (1/4") female quick-connect terminals for switch and coil lugs
- Standard pinball switches use 0.187" spades; some coils and large terminals use 0.250"

### Heat Shrink Tubing (assorted sizes)
- **Qty**: 1 assortment kit
- **Vendor**: Amazon
- Insulates solder joints and provides strain relief on connections
- Get an assortment of sizes from 1.5mm to 10mm diameter

### Cable Ties & Mounting Hardware
- **Qty**: 100+ cable ties, assorted sizes
- **Vendor**: Amazon
- Wire loom management: cable ties, adhesive cable tie mounts, wire loom/braiding for organized routing
- See FAST wire routing guide: https://fastpinball.com/wiring/neuron/routing/

### Ring Terminals & Ground Bus Bar
- **Qty**: 20+ ring terminals, 1 ground bus bar
- **Vendor**: Mouser, Digi-Key, hardware store
- **Docs**: https://fastpinball.com/wiring/grounding/
- Ground bus bar provides central grounding point; ring terminals connect individual ground wires to the bus
- Proper grounding is critical for noise-free switch reading and driver operation

### Fuses (assorted values)
- **Qty**: Assorted per FAST fuse sizing guide
- **Vendor**: Mouser, Digi-Key, Amazon
- **Docs**: https://fastpinball.com/wiring/neuron/fuses/
- Values depend on your specific power distribution design — follow the FAST fuse sizing and current calculation guide
- Typical values: 3A, 5A, 7A for various 48V and 12V distribution circuits
- Always match fuse rating to the wire gauge and expected circuit load

---

## 11. Host Computer

### Raspberry Pi 4 (or 5) — or SBC / Mini PC
- **Qty**: 1
- **Vendor**: Amazon, Adafruit, Raspberry Pi distributors
- **Docs**: https://fastpinball.com/wiring/neuron/raspberry-pi/
- Runs MPF game code and Godot/GMC for display rendering
- Raspberry Pi can mount directly on the Neuron Controller's Pi header for integrated power and connection
- Alternative: Intel NUC or similar mini PC / SBC if more processing power is needed for Godot rendering
- Raspberry Pi is suitable for machines without graphics; an SBC or mini PC is recommended when running Godot/GMC
- Pi 4 with 4GB RAM minimum recommended; 8GB preferred for Godot

### MicroSD Card (for Raspberry Pi)
- **Qty**: 1
- **Vendor**: Amazon
- 32GB or 64GB high-quality microSD (Samsung EVO Select, SanDisk Extreme)
- Holds Raspberry Pi OS, MPF installation, and Ozzfest game code
- Use a reliable brand — SD card corruption will take down the whole machine

### USB Cable (host PC to Neuron)
- **Qty**: 1
- **Vendor**: Any
- USB-A to USB-B (or USB-C depending on Neuron revision) cable connecting host PC to Neuron Controller
- This is the only cable connecting the computer to the FAST control system — all I/O, expansion, and display bus traffic flows through this
- If using Pi mounted on Neuron header, this cable is not needed (connection is direct through header)

---

## 12. Playfield Components — Switches

All switches connect to FAST I/O board switch inputs. The exact quantity depends on the final Ozzfest playfield design. Below is based on the current Ozzfest config and Jungle Lord layout.

### Leaf Switches (normally-open)
- **Qty**: 20-30
- **Vendor**: Pinball Life, Marco Specialties
- Standard pinball leaf switches for: standup targets, rollovers, lane switches, slingshot activation
- Each switch wires to one I/O board switch input with two wires (switch input + ground)
- Replace all original Jungle Lord leaf switches during rebuild — used switches are unreliable

### Microswitch (cherry/roller type)
- **Qty**: 5-10
- **Vendor**: Pinball Life, Marco Specialties
- Used for: ball trough detection, plunger lane, kickout hole detection, coin door switches
- More durable than leaf switches; used where reliability is critical (ball counting, coin input)
- Ensure switch type (NO/NC) matches your MPF config for each position

### Opto Switches (optional upgrade for some positions)
- **Qty**: 0-10
- **Vendor**: Pinball Life, FAST Pinball
- **Docs**: https://fastpinball.com/wiring/neuron/optos/
- Infrared optical switches for positions where mechanical switches are unreliable or undesirable
- No moving parts to wear out; useful for high-traffic positions like spinner or orbit shots
- Require power (12V/5V for IR emitter) plus signal wire — different wiring than mechanical switches

### FAST 4-Channel Opto Emitter (if using optos)
- **Qty**: 0-2
- **Vendor**: https://shop.fastpinball.com/
- **Docs**: https://fastpinball.com/products/aux/4-channel-opto-emitter/
- Drives up to 4 opto emitters from a single board; simplifies opto wiring
- Mount near opto switch locations under the playfield

### Tilt Bob Assembly
- **Qty**: 1
- **Vendor**: Pinball Life, Marco Specialties
- Pendulum tilt sensor mounted inside the cabinet
- Connects to Cabinet I/O Board switch input
- Sensitivity adjusted by raising/lowering the ring on the pendulum

### Slam Tilt Switch
- **Qty**: 1
- **Vendor**: Pinball Life, Marco Specialties
- Leaf switch mounted inside the coin door; detects hard impacts that could damage the machine
- Connects to Cabinet I/O Board; triggers MPF slam_tilt event which ends the game and disables coils

---

## 13. Playfield Components — Coils & Solenoids

All coils connect to FAST I/O board driver outputs. The FAST platform uses 48V coils.

### Flipper Coils
- **Qty**: 2-3 (left, right, optional upper)
- **Vendor**: Pinball Life, Marco Specialties
- Dual-winding coils: high-power winding for initial flip, low-power winding for hold
- Must be 48V rated for FAST platform (NOT the original 25V or 50V System 7 coils)
- FAST I/O boards handle flipper hardware rules locally — sub-millisecond response with no host PC latency
- See FAST flipper wiring guide: https://fastpinball.com/wiring/neuron/flippers/

### Pop Bumper Coils
- **Qty**: 3
- **Vendor**: Pinball Life, Marco Specialties
- Single-winding pulse coils; fire briefly when pop bumper switch is hit
- Must be 48V rated; configured as autofire rules on the I/O board
- See FAST pop bumper docs: https://fastpinball.com/programming/devices/pop_bumpers/

### Slingshot Coils
- **Qty**: 2
- **Vendor**: Pinball Life, Marco Specialties
- Single-winding pulse coils for left and right slingshots
- Configured as autofire rules; switch hit instantly fires coil
- 48V rated; standard pinball slingshot coil size

### Kickout / Eject Coils
- **Qty**: 2-3 (upper kickout, lower kickout, trough eject)
- **Vendor**: Pinball Life, Marco Specialties
- Pulse coils that fire to eject captured balls from saucers/trough
- Pulse duration configured in MPF coil settings; typically 25-50ms
- 48V rated

### Drop Target Reset Coil
- **Qty**: 1 (per drop target bank)
- **Vendor**: Pinball Life, Marco Specialties
- Fires to reset all drop targets in a bank back to the upright position
- Strong pulse coil; uses more current than typical coils for the mechanical reset action
- 48V rated

### Coil Sleeves, Coil Stops, Coil Wrappers
- **Qty**: 1 per coil position (matching sizes)
- **Vendor**: Pinball Life, Marco Specialties
- Coil sleeves protect the coil bore from plunger wear; coil stops prevent over-travel and absorb impact
- Replace all sleeves and stops during rebuild — worn parts cause sluggish coil action and increased wear
- Match sleeve and stop dimensions to each specific coil and mechanism

---

## 14. Playfield Components — Assemblies & Mechanisms

### Rubber Rings (assortment kit)
- **Qty**: 1 full rubber ring kit for Jungle Lord
- **Vendor**: Pinball Life, Marco Specialties, Titan Pinball
- Silicone or standard rubber rings for: slingshots, pop bumpers, posts, flippers, star posts
- Replace all rings during rebuild — old rubber is dead and affects ball behavior
- Titan Pinball makes premium silicone ring kits by machine model

### Post / Bumper Caps / Sleeves
- **Qty**: Assorted per playfield layout
- **Vendor**: Pinball Life, Marco Specialties
- Guide posts, jet bumper caps, lane guide posts, etc.
- Replace cracked or discolored posts; choose translucent if using RGB underglow for illumination effects

### Playfield Plastics / Ramps
- **Qty**: 1 set (custom or reproduced)
- **Vendor**: Custom fabrication or Pinball Life for original Jungle Lord plastics
- If keeping Jungle Lord layout: refurbish or reproduce original plastics
- If customizing for Ozzfest theme: design and CNC-cut or 3D-print custom plastics
- Plastics protect the playfield and provide ball guides, ramp entries, etc.

### Rollover Guides / Wire Forms
- **Qty**: Per playfield design
- **Vendor**: Pinball Life, Marco Specialties, custom fabrication
- Wire forms and metal guides that direct ball flow on the playfield
- Reuse Jungle Lord wire forms if layout is preserved; fabricate new ones for custom shot paths
- Chrome or stainless steel preferred for durability

### Spinner (if present in design)
- **Qty**: 0-1
- **Vendor**: Pinball Life, Marco Specialties
- Spinning target that registers multiple switch hits as ball passes through
- Each revolution triggers the spinner switch
- Include in design if a spinner shot fits the Ozzfest playfield layout

---

## 15. Balls

### Pinball Machine Balls (1-1/16" diameter, chrome steel)
- **Qty**: 3-5 (2 in play per Jungle Lord design + spares)
- **Vendor**: Pinball Life, Marco Specialties, Amazon
- Standard 1-1/16" (27mm) chrome steel pinball balls
- Jungle Lord uses 2 balls in play simultaneously on the main and upper mini playfield
- Always start with fresh, scratch-free balls — worn balls damage the playfield and affect gameplay
- Keep spares for replacement as balls develop surface wear

---

## 16. Software & Firmware

These are not physical purchases but required software components. Listed for completeness.

### Mission Pinball Framework (MPF)
- **Source**: `pip install mpf --pre`
- **Docs**: https://missionpinball.org/
- Python virtualenv `ozzfest_3118` (Python 3.11.8) is already configured per [game_rules.md](../../ozzfest/game_rules.md)
- FAST platform support is built into MPF — configure `hardware: platform: fast` in machine config

### MPF-GMC (Godot Media Controller)
- **Source**: https://github.com/missionpinball/mpf-gmc
- Godot 4.4+ editor with GMC addon provides display rendering (slides, videos, animations)
- Already cloned to ~/repos/mpf-gmc; addons copied to ozzfest machine folder

### FAST Pinball Firmware
- **Source**: https://fastpinball.com/firmware/
- Neuron Controller and all I/O/expansion boards have updateable firmware
- Always update to latest firmware before first use — see NET and EXP firmware update guides
- Firmware updates are performed via USB connection from host PC

---

## 17. Reference Links

| Resource | URL |
|---|---|
| FAST Pinball Documentation Home | https://fastpinball.com/docs/ |
| FAST Product Catalog | https://fastpinball.com/products/ |
| FAST Pinball Shop | https://shop.fastpinball.com/ |
| FAST Modern Platform Overview | https://fastpinball.com/modern/ |
| FAST Wiring Guides (Neuron) | https://fastpinball.com/wiring/neuron/ |
| FAST Power Supply Guide | https://fastpinball.com/wiring/choosing-power-supplies/ |
| FAST + MPF Configuration | https://fastpinball.com/mpf/ |
| FAST MPF Starter Configs | https://fastpinball.com/mpf/fast-mpf-starter-configs/ |
| FAST Crimping Skills Guide | https://fastpinball.com/learning/skills/crimping/ |
| FAST Cabinet Layout | https://fastpinball.com/modern/cabinet-layout/ |
| MPF Documentation | https://missionpinball.org/ |
| Ozzfest Implementation Plan | [../../ozzfest/implementation.md](../../ozzfest/implementation.md) |
| Ozzfest Game Rules | [../../ozzfest/game_rules.md](../../ozzfest/game_rules.md) |
| Master BOM Spreadsheet (auth required) | https://docs.google.com/spreadsheets/d/1JEHx_08Zi1kPXPQiNM-eau-H2xfTsLFBgkRzyfTPdEI/edit?gid=1386834576#gid=1386834576 |
| Google Sheets Import Guide | [google-sheets-import.md](google-sheets-import.md) |
