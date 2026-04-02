#!/usr/bin/env python3
"""Rebuild the Ozzfest BOM xlsx with all items from ozzfest-bom.md.

Preserves the original spreadsheet column layout:
  A: (empty)
  B: Ordered (checkbox — False for all new rows)
  C: group
  D: subgroup
  E: product combo (bundle grouping)
  F: part/product
  G: qty needed
  H: qty incl. (qty included in a bundle/combo)
  I: unit price
  J: total price
  K: order company
  L: product url
  M: product notes
  N: usage docs
"""
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from copy import copy
import os

XLSX_PATH = os.path.expanduser('~/Downloads/Bill of Materials_ Ozzfest.xlsx')
OUTPUT_PATH = XLSX_PATH  # overwrite in place

# ---------- BOM DATA ----------
# Each tuple: (group, subgroup, product_combo, part_product, qty_needed, qty_incl,
#               unit_price, total_price, order_company, product_url, product_notes, usage_docs)

rows = [
    # === 1. FAST Pinball Control System ===
    ("boards & wiring", "PC", "SBC", "SBC", 1, None, None, None,
     None, None, "raspi for things without graphics. otherwise SBC", None),

    ("boards & wiring", "boards", "FAST Neuron Starter Bundle", "Neuron Controller", 1, 1, None, 569,
     "FAST", "https://shop.fastpinball.com/product/fast-neuron-starter-bundle/53?cs=true&cst=custom",
     "central hub; USB to host PC; NET, EXP, DSP buses; built-in 128 LED + 3 servo breakout; Pi header",
     "https://fastpinball.com/products/controllers/neuron/"),

    # === 2. Power System ===
    ("boards & wiring", "boards", "FAST Neuron Starter Bundle", "Power Filter Board", 1, 1, None, None,
     "FAST", "https://shop.fastpinball.com/product/fast-neuron-starter-bundle/53?cs=true&cst=custom",
     "filters & distributes 48V/12V; reserve capacitors for coil bursts; voltage/current monitoring",
     "https://fastpinball.com/products/power/smart-power-filter-board/"),

    ("boards & wiring", "boards", "FAST Neuron Starter Bundle", "Expansion Board", None, 1, None, None,
     "FAST", "https://shop.fastpinball.com/product/fast-neuron-starter-bundle/53?cs=true&cst=custom",
     "choose one for 256 LEDs, or 128 LEDs + 4 servos)",
     "https://fastpinball.com/products/expansion/71/"),

    ("boards & wiring", "boards", "FAST Neuron Starter Bundle", "Playfield I/O 3208", None, 1, None, None,
     "FAST", "https://shop.fastpinball.com/product/fast-neuron-starter-bundle/53?cs=true&cst=custom",
     "32 switch inputs + 8 driver outputs; primary playfield I/O board",
     "https://fastpinball.com/products/ioboards/3208/"),

    ("boards & wiring", "boards", "FAST Neuron Starter Bundle", "Playfield Interchange Board", 1, 1, None, None,
     "FAST", "https://shop.fastpinball.com/product/fast-neuron-starter-bundle/53?cs=true&cst=custom",
     "on playfield, connects playfield to backbox; single disconnect point",
     "https://fastpinball.com/products/power/playfield-interchange-board/"),

    ("boards & wiring", "power supply", "FAST Neuron Starter Bundle",
     "optional:  add Power Supplies   Mean Well RSP-500-48 (48V, 10.5A) & Mean Well LRS-150-12 (12V, 12.5A)",
     2, 2, None, 150,
     "FAST", "https://shop.fastpinball.com/product/fast-neuron-starter-bundle/53?cs=true&cst=custom",
     "can optionally be added to FAST neuron startle bundle. includes all PSUs required for machine",
     "https://www.meanwellusa.com/webapp/product/search.aspx?prod=RSP-500"),

    ("boards & wiring", "connectors", "FAST Neuron Starter Bundle", "optional:  add connectors+pins",
     None, None, None, 29,
     "FAST", "https://shop.fastpinball.com/product/fast-neuron-starter-bundle/53?cs=true&cst=custom",
     "can optionally be added to FAST neuron startle bundle",
     "https://fastpinball.com/products/controllers/neuron/#connectors-housings-needed"),

    ("boards & wiring", "boards", None, "FAST Smart Fuse Block", 1, None, None, None,
     "FAST", "https://shop.fastpinball.com/",
     "distributes fused power; individually monitorable fuses; centralizes fuse management in backbox",
     "https://fastpinball.com/products/power/smart-fuse-block/"),

    ("boards & wiring", "cabinet power", None, "Solid State Relay (SSR) — optional", 1, None, None, None,
     None, None,
     "soft power on/off via pushbutton; rated for combined PSU inrush; wires between AC mains and PSUs",
     "https://fastpinball.com/wiring/neuron/solid-state-relay/"),

    ("boards & wiring", "cabinet power", None, "IEC line input receptacle + EMI filter", 1, None, None, None,
     None, None,
     "dont use emi filter if trying to make compliant. but FAST says okay for home use",
     "https://fastpinball.com/wiring/neuron/ac-line-input/#ac-line-fuse"),

    ("boards & wiring", "cabinet power", None, "Fuse holder (5x20mm)", 1, None, None, None,
     None, "https://www.mouser.com/c/?for%20use%20with=Fuse%20Holders%2C%20No.%20821%205%20x%2020%20mm",
     None,
     "https://fastpinball.com/wiring/neuron/ac-line-input/#ac-line-fuse"),

    ("boards & wiring", "cabinet power", None, "8A Fuse", 1, None, None, None,
     None, None, "AC line fuse",
     "https://fastpinball.com/wiring/neuron/ac-line-input/#ac-line-fuse"),

    ("boards & wiring", "cabinet power", None, "SPDT switch (AC Power)", 1, None, None, None,
     None, None, "main AC power on/off switch",
     "https://fastpinball.com/wiring/neuron/ac-line-input/#ac-power-switch"),

    ("boards & wiring", "cabinet power", None, "Power cord", 1, None, None, None,
     None, None, "standard IEC C13/C14 power cord", None),

    # === 3. I/O Boards ===
    ("boards & wiring", "boards", None, "FAST I/O 1616 Board (FP-IO-1616)", 1, None, None, None,
     "FAST", "https://shop.fastpinball.com/",
     "16 switches + 16 drivers; flippers, pop bumpers, ball launch, trough eject",
     "https://fastpinball.com/products/ioboards/1616/"),

    ("boards & wiring", "boards", None, "FAST Audio Interface Board (FP-AUD-0100)", 1, 1, None, 99,
     "FAST", "https://shop.fastpinball.com/product/fp-aud-0100/57?cs=true&cst=custom",
     None,
     "https://fastpinball.com/products/audio/audio-interface/"),

    ("boards & wiring", "boards", None, "FAST Cabinet I/O Board (FP-IO-0024)", 1, 1, None, 159,
     "FAST", "https://shop.fastpinball.com/product/fp-io-0024/56?cs=true&cst=custom",
     "used for cabinet switches (start, flippers, others)",
     "https://fastpinball.com/products/ioboards/cabinet/"),

    ("boards & wiring", "boards", None, "FAST Expansion Board FP-EXP-0081 (256 LEDs) — optional", None, None, None, None,
     "FAST", "https://shop.fastpinball.com/",
     "additional LED-only expansion board if 128+128 insufficient; 256 LEDs across 8 ports",
     "https://fastpinball.com/products/expansion/81/"),

    # === Wiring / cables ===
    ("boards & wiring", "wiring", None, "rj45 network cable", None, None, None, None,
     None, None, "used for connecting FAST boards to each other (I/O loop + expansion bus)", None),

    ("boards & wiring", "cabinet wiring", None, "16ga stranded wire (white)", None, None, None, None,
     None, None, "for wiring from AC line to power boxes",
     "https://fastpinball.com/wiring/neuron/ac-line-input/#your-machines-power-box"),

    ("boards & wiring", "cabinet wiring", None, "16ga stranded wire (black)", None, None, None, None,
     None, None, "for wiring from AC line to power boxes",
     "https://fastpinball.com/wiring/neuron/ac-line-input/#your-machines-power-box"),

    ("boards & wiring", "cabinet wiring", None, "16ga stranded wire (green)", None, None, None, None,
     None, None, "for wiring from AC line to power boxes",
     "https://fastpinball.com/wiring/neuron/ac-line-input/#your-machines-power-box"),

    ("boards & wiring", "cabinet wiring", None, "18ga stranded wire (multiple colors)", None, None, None, None,
     None, None, "200-500ft total; primary switch wiring and lower-current; use stranded not solid",
     "https://fastpinball.com/wiring/standards/"),

    ("boards & wiring", "connectors", None, "fork crimp connector terminals (16ga)", 16, None, 1.05, None,
     None, "https://www.mouser.com/c/connectors/terminals/?product=Fork%20Terminal&wire%20gauge%20max=16%20AWG",
     "3 on ac in, 2 on line fuse, 2 on switch, 3 or 6 on 48V PSU, 3 on 12v psu",
     "https://fastpinball.com/wiring/neuron/ac-line-input/#your-machines-power-box"),

    ("boards & wiring", "connectors", None, "Molex 0.156\" connector housings & pins", None, None, None, None,
     None, None, "0.156\" pitch for power connections to FAST boards; Neuron: 1x 3-pin (12V in), 1x 2-pin (12V out)",
     "https://fastpinball.com/products/controllers/neuron/#connectors-housings-needed"),

    ("boards & wiring", "connectors", None, "Molex 0.100\" connector housings & pins", None, None, None, None,
     None, None, "0.100\" pitch for LED wiring (4-pin), host PC control (5-pin), SSR/power (3-pin), breakout (5-pin)", None),

    ("boards & wiring", "connectors", None, "Crimp pins (0.156\" and 0.100\")", None, None, None, None,
     None, None, "200+ buy extras; practice crimping technique first",
     "https://fastpinball.com/learning/skills/crimping/"),

    ("boards & wiring", "connectors", None, "Quick-connect / spade connectors", None, None, None, None,
     None, None, "100+; 0.187\" and 0.250\" female for switch and coil lugs", None),

    ("boards & wiring", "connectors", None, "Heat shrink tubing (assorted)", None, None, None, None,
     None, None, "assortment kit 1.5mm-10mm; insulates joints and strain relief", None),

    ("boards & wiring", "connectors", None, "Cable ties & mounting hardware", None, None, None, None,
     None, None, "100+ cable ties, adhesive mounts, wire loom",
     "https://fastpinball.com/wiring/neuron/routing/"),

    ("boards & wiring", "connectors", None, "Ring terminals & ground bus bar", None, None, None, None,
     None, None, "20+ ring terminals, 1 ground bus bar; central grounding point",
     "https://fastpinball.com/wiring/grounding/"),

    ("boards & wiring", "connectors", None, "Fuses (assorted 3A, 5A, 7A)", None, None, None, None,
     None, None, "match fuse rating to wire gauge and circuit load",
     "https://fastpinball.com/wiring/neuron/fuses/"),

    # === Tools ===
    ("tools", "crimping", None, "Crimp tool (Engineer PA-09 or equiv)", 1, None, None, None,
     None, None, "precision crimp tool for 0.100\" and 0.156\" pins; most important wiring tool",
     "https://fastpinball.com/learning/skills/crimping/"),

    # === 5. Lighting ===
    ("lighting", "playfield LEDs", None, "FAST RGB Playfield Insert LEDs", None, None, None, None,
     "FAST", "https://shop.fastpinball.com/",
     "30-50 qty; direct replacement for incandescent; full RGB per insert; ~35 lamp positions on JL",
     "https://fastpinball.com/products/lighting/rgb-led-insert/"),

    ("lighting", "GI LEDs", None, "FAST RGB GI (General Illumination) LEDs", None, None, None, None,
     "FAST", "https://shop.fastpinball.com/",
     "10-20 qty; individually addressable RGB GI; dynamic color per game mode",
     "https://fastpinball.com/products/lighting/rgb-gi-led/"),

    # === 6. Display ===
    ("display", "DMD", None, "FAST RGB DMD — optional if using LCD", None, None, None, None,
     "FAST", "https://shop.fastpinball.com/",
     "full color RGB LED DMD; connects via Display Bus; not needed if using LCD",
     "https://fastpinball.com/products/display/rgb-dmd/"),

    ("display", "LCD", None, "LCD Monitor (15-19\") — if not using DMD", None, None, None, None,
     None, None, "for Godot/GMC display; HDMI to host PC; VESA mount recommended", None),

    ("display", "segment", None, "Segment Displays (existing from Jungle Lord)", 5, None, None, None,
     None, None, "reuse from JL; 4 player (7-digit) + 1 info (4-digit); may need adapter for Neuron Display Bus", None),

    # === 7. Audio ===
    ("audio", "speakers", None, "Speakers (main, 4\" or 5.25\")", 2, None, None, None,
     None, None, "full-range backbox speakers; match impedance to FAST Audio Interface", None),

    ("audio", "speakers", None, "Subwoofer (6.5\" or 8\") — optional", None, None, None, None,
     None, None, "bass reinforcement; mounts in cabinet; connects to Audio Interface sub output", None),

    # === 8. Playfield Mechanical Parts ===
    ("playfield mechanical", "flippers", None, "Flipper assemblies (complete)", 2, None, None, None,
     None, None, "left + right (optional 3rd upper); bat, shaft, sleeve, link, plunger, spring, EOS switch, coil stop",
     "https://fastpinball.com/wiring/neuron/flippers/"),

    ("playfield mechanical", "pop bumpers", None, "Pop bumper assemblies (complete)", 3, None, None, None,
     None, None, "body, cap, skirt, ring, spoon, coil, switch; autofire rule on I/O board", None),

    ("playfield mechanical", "slingshots", None, "Slingshot assemblies (complete)", 2, None, None, None,
     None, None, "2 leaf switches, 1 coil, rubber rings, plastic, bracket per slingshot; autofire", None),

    ("playfield mechanical", "drop targets", None, "Drop target bank (faces, springs, reset coil)", 1, None, None, None,
     None, None, "individual target faces + return springs + bank reset coil", None),

    ("playfield mechanical", "kickout holes", None, "Kickout holes / saucers", 2, None, None, None,
     None, None, "upper + lower; each has eject coil + ball-detect switch", None),

    ("playfield mechanical", "ball trough", None, "Ball trough assembly", 1, None, None, None,
     None, None, "trough switches (s_ball_trough_left, s_ball_trough_right) + eject coil", None),

    ("playfield mechanical", "ball trough", None, "FAST Trough IR Boards — optional upgrade", None, None, None, None,
     "FAST", "https://shop.fastpinball.com/",
     "IR optical sensors replace mechanical trough switches; more reliable",
     "https://fastpinball.com/products/aux/trough-ir-boards/"),

    ("playfield mechanical", "plunger", None, "Ball shooter / plunger assembly", 1, None, None, None,
     None, None, "manual spring plunger (JL standard) or auto-launch coil conversion", None),

    ("playfield mechanical", "playfield", None, "Playfield surface (reuse/refurbish JL)", 1, None, None, None,
     None, None, "strip, clean, clear-coat; fill unused holes; drill new Ozzfest-specific holes", None),

    # === 9. Cabinet & Backbox ===
    ("cabinet", "body", None, "Cabinet body", 1, None, None, None,
     None, None, "reuse JL or build custom; ~22\"x52\"; sand, fill, repaint/wrap for Ozzfest theme", None),

    ("cabinet", "backbox", None, "Backbox", 1, None, None, None,
     None, None, "reuse JL; houses Neuron, PSUs, fuse block, audio, speakers, display", None),

    ("cabinet", "art", None, "Backglass / translite (custom Ozzfest)", 1, None, None, None,
     None, None, "custom print on translite material; backlit by Neuron RGB LEDs", None),

    ("cabinet", "art", None, "Cabinet side art (vinyl wraps)", 1, None, None, None,
     None, None, "left + right; vinyl decals or full cabinet wraps", None),

    ("cabinet", "hardware", None, "Legs (4) with levelers", 4, None, None, None,
     None, None, "standard pinball legs with threaded leveler feet; reuse JL if in good condition", None),

    ("cabinet", "hardware", None, "Coin door assembly", 1, None, None, None,
     None, None, "frame, coin mechanisms or free play bypass, service buttons, slam tilt; connects to Cabinet I/O", None),

    ("cabinet", "hardware", None, "Lockdown bar & receiver", 1, None, None, None,
     None, None, "secures playfield glass; reuse JL or replace if chrome degraded", None),

    ("cabinet", "hardware", None, "Playfield glass (tempered)", 1, None, None, None,
     None, None, "cut to JL playfield opening dimensions; replace if scratched/chipped", None),

    # === 11. Host Computer ===
    ("host computer", "SBC", None, "Raspberry Pi 4/5 or SBC / Mini PC", 1, None, None, None,
     None, None, "runs MPF + Godot/GMC; Pi mounts on Neuron header; 4GB min, 8GB preferred for Godot",
     "https://fastpinball.com/wiring/neuron/raspberry-pi/"),

    ("host computer", "storage", None, "MicroSD card (32-64GB)", 1, None, None, None,
     None, None, "Samsung EVO Select or SanDisk Extreme; holds OS + MPF + Ozzfest game code", None),

    ("host computer", "cable", None, "USB cable (host PC to Neuron)", 1, None, None, None,
     None, None, "USB-A to USB-B/C; not needed if Pi mounted on Neuron header", None),

    # === 12. Switches ===
    ("playfield switches", "leaf", None, "Leaf switches (normally-open)", None, None, None, None,
     None, None, "20-30 qty; standup targets, rollovers, lane switches, slingshot activation", None),

    ("playfield switches", "microswitch", None, "Microswitches (cherry/roller type)", None, None, None, None,
     None, None, "5-10 qty; trough, plunger lane, kickout hole, coin door; more durable than leaf", None),

    ("playfield switches", "opto", None, "Opto switches — optional upgrade", None, None, None, None,
     None, None, "0-10 qty; IR optical; no moving parts; good for spinner/orbit",
     "https://fastpinball.com/wiring/neuron/optos/"),

    ("playfield switches", "opto", None, "FAST 4-Channel Opto Emitter", None, None, None, None,
     "FAST", "https://shop.fastpinball.com/",
     "0-2 qty; drives 4 opto emitters per board",
     "https://fastpinball.com/products/aux/4-channel-opto-emitter/"),

    ("playfield switches", "tilt", None, "Tilt bob assembly", 1, None, None, None,
     None, None, "pendulum tilt sensor; connects to Cabinet I/O; adjustable sensitivity", None),

    ("playfield switches", "tilt", None, "Slam tilt switch", 1, None, None, None,
     None, None, "leaf switch in coin door; triggers slam_tilt event in MPF", None),

    # === 13. Coils & Solenoids ===
    ("playfield coils", "flippers", None, "Flipper coils (48V dual-winding)", None, None, None, None,
     None, None, "2-3 qty; high-power + hold winding; must be 48V rated for FAST",
     "https://fastpinball.com/wiring/neuron/flippers/"),

    ("playfield coils", "pop bumpers", None, "Pop bumper coils (48V)", 3, None, None, None,
     None, None, "single-winding pulse; autofire rules on I/O board",
     "https://fastpinball.com/programming/devices/pop_bumpers/"),

    ("playfield coils", "slingshots", None, "Slingshot coils (48V)", 2, None, None, None,
     None, None, "single-winding pulse; autofire rules", None),

    ("playfield coils", "eject", None, "Kickout / eject coils (48V)", None, None, None, None,
     None, None, "2-3 qty; upper kickout, lower kickout, trough eject; 25-50ms pulse", None),

    ("playfield coils", "drop target", None, "Drop target reset coil (48V)", 1, None, None, None,
     None, None, "strong pulse coil for mechanical reset", None),

    ("playfield coils", "consumables", None, "Coil sleeves, coil stops, coil wrappers", None, None, None, None,
     None, None, "1 per coil position; replace all during rebuild", None),

    # === 14. Assemblies & Mechanisms ===
    ("playfield mechanical", "rubber", None, "Rubber rings (full kit for Jungle Lord)", 1, None, None, None,
     None, None, "silicone or standard; slingshots, pop bumpers, posts, flippers; Titan Pinball makes kits by model", None),

    ("playfield mechanical", "posts", None, "Post / bumper caps / sleeves (assorted)", None, None, None, None,
     None, None, "guide posts, jet bumper caps, lane guides; translucent if using RGB underglow", None),

    ("playfield mechanical", "plastics", None, "Playfield plastics / ramps", 1, None, None, None,
     None, None, "refurbish JL originals or design custom CNC/3D-print for Ozzfest theme", None),

    ("playfield mechanical", "wire forms", None, "Rollover guides / wire forms", None, None, None, None,
     None, None, "reuse JL or fabricate new; chrome or stainless steel", None),

    ("playfield mechanical", "spinner", None, "Spinner — if present in design", None, None, None, None,
     None, None, "0-1 qty; spinning target registering multiple switch hits per pass", None),

    # === 15. Balls ===
    ("balls", None, None, "Pinball machine balls (1-1/16\" chrome steel)", None, None, None, None,
     None, None, "3-5 qty; JL uses 2 in play; keep spares", None),

    # === 16. Software & Firmware ===
    ("software", None, None, "Mission Pinball Framework (MPF)", None, None, None, None,
     None, None, "pip install mpf --pre; Python 3.11.8 venv ozzfest_3118",
     "https://missionpinball.org/"),

    ("software", None, None, "MPF-GMC (Godot Media Controller)", None, None, None, None,
     None, None, "Godot 4.4+ with GMC addon; cloned to ~/repos/mpf-gmc",
     "https://github.com/missionpinball/mpf-gmc"),

    ("software", None, None, "FAST Pinball Firmware", None, None, None, None,
     None, None, "update all boards to latest firmware before first use",
     "https://fastpinball.com/firmware/"),
]


def build_xlsx():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "bom"

    # --- Row 1: blank spacer ---
    # --- Row 2: title row ---
    ws.merge_cells('B2:H2')
    title_cell = ws['B2']
    title_cell.value = 'Bill of Materials'
    title_cell.font = Font(bold=True, size=14)

    # --- Row 3: summary formula + blank ---
    ws['B3'] = '=CONCATENATE(COUNTIF($B$5:$B$200,TRUE), "/", COUNTA($F$5:$F$200), " orders completed  ")'

    # --- Row 4: header row ---
    headers = [
        '',  # A
        'Ordered',       # B
        'group',         # C
        'subgroup',      # D
        'product combo', # E
        'part/product',  # F
        'qty needed',    # G
        'qty incl.',     # H
        'unit price',    # I
        'total price',   # J
        'order company', # K
        'product url',   # L
        'product notes', # M
        'usage docs',    # N
    ]
    header_font = Font(bold=True)
    header_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    thin_border = Border(
        bottom=Side(style='thin')
    )
    for col_idx, h in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col_idx, value=h)
        cell.font = header_font
        cell.fill = header_fill
        cell.border = thin_border

    # --- Data rows starting at row 5 ---
    for row_idx, row_data in enumerate(rows, 5):
        (group, subgroup, product_combo, part_product,
         qty_needed, qty_incl, unit_price, total_price,
         order_company, product_url, product_notes, usage_docs) = row_data

        ws.cell(row=row_idx, column=2, value=False)   # Ordered
        ws.cell(row=row_idx, column=3, value=group)
        ws.cell(row=row_idx, column=4, value=subgroup)
        ws.cell(row=row_idx, column=5, value=product_combo)
        ws.cell(row=row_idx, column=6, value=part_product)
        ws.cell(row=row_idx, column=7, value=qty_needed)
        ws.cell(row=row_idx, column=8, value=qty_incl)
        ws.cell(row=row_idx, column=9, value=unit_price)
        ws.cell(row=row_idx, column=10, value=total_price)
        ws.cell(row=row_idx, column=11, value=order_company)
        ws.cell(row=row_idx, column=12, value=product_url)
        ws.cell(row=row_idx, column=13, value=product_notes)
        ws.cell(row=row_idx, column=14, value=usage_docs)

    # --- Column widths for readability ---
    ws.column_dimensions['A'].width = 3
    ws.column_dimensions['B'].width = 10
    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['D'].width = 18
    ws.column_dimensions['E'].width = 30
    ws.column_dimensions['F'].width = 50
    ws.column_dimensions['G'].width = 12
    ws.column_dimensions['H'].width = 10
    ws.column_dimensions['I'].width = 12
    ws.column_dimensions['J'].width = 12
    ws.column_dimensions['K'].width = 16
    ws.column_dimensions['L'].width = 60
    ws.column_dimensions['M'].width = 60
    ws.column_dimensions['N'].width = 60

    wb.save(OUTPUT_PATH)
    return len(rows)


if __name__ == '__main__':
    count = build_xlsx()
    with open('/home/hotsoup/repos/pinball-soup/bill-of-materials/_update_log.txt', 'w') as f:
        f.write(f'SUCCESS: Wrote {count} BOM rows to {OUTPUT_PATH}\n')
