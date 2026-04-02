# Time Warped — Bill of Materials (APC / Arduino Pinball Controller)

> **Machine**: Time Warped (custom game on Time Warp cabinet)
> **Cabinet Base**: Williams Time Warp (System 7)
> **Hardware Platform**: APC (Arduino Pinball Controller) with LISY protocol
> **Controller**: Arduino Due on APC board + Raspberry Pi Zero W
> **Software**: Mission Pinball Framework (MPF) with Godot Media Controller (GMC)
> **Status**: Partially assembled — APC board built, basic game running. BOM below is for reference and remaining parts.

---

> **NOTE**: This BOM is a placeholder. Time Warped uses a fundamentally different hardware platform (APC) than Ozzfest (FAST). The main README at ~/repos/pinball-soup/README.md contains detailed setup steps for the APC platform. This file should be expanded with specific part details as the build progresses.

---

## Table of Contents
1. [APC Control System](#1-apc-control-system)
2. [Power (Original System 7)](#2-power-original-system-7)
3. [Compute](#3-compute)
4. [Playfield & Cabinet](#4-playfield--cabinet)
5. [Reference Links](#5-reference-links)

---

## 1. APC Control System

### APC Board (Arduino Pinball Controller PCB)
- **Qty**: 1 (already assembled)
- **Source**: PCB ordered per APC GitHub docs; components soldered per BOM at https://docs.google.com/spreadsheets/d/1Lxnt1CGEWpybvpkPa3vRJebU48Qeu8h9te3dvZjng0g/edit?gid=0#gid=0
- Drop-in replacement for original Williams System 7 MPU board
- Interfaces with all original System 7 connectors (existing wiring harness is reused)
- Supports LISY protocol for MPF communication via Raspberry Pi
- All original switches, coils, and lamps remain connected through existing cable harness

### Arduino Due
- **Qty**: 1 (already installed on APC)
- **Vendor**: Arduino official, Amazon, Adafruit
- Microcontroller that runs APC firmware; connects to APC board via programming port
- APC firmware (V1.02+) uploaded via Arduino IDE
- Requires SAM boards core installed in Arduino IDE

### SD Card (for APC board)
- **Qty**: 1 (32GB, already formatted and loaded)
- **Vendor**: Amazon
- Stores APC configuration, game settings, and sound files
- Must be formatted with SDCard Association formatter (Windows)
- Sound files converted to APC format using Audio Data Converter perl script

---

## 2. Power (Original System 7)

### Original Williams System 7 Power Supply
- **Qty**: 1 (reuse from Time Warp machine)
- The APC board is designed to work with the original System 7 power supply and transformer
- Provides all voltages needed: 5V logic, solenoid drive voltage, lamp voltage
- No changes required from original power setup

---

## 3. Compute

### Raspberry Pi Zero W (v1.1)
- **Qty**: 1 (already installed on APC)
- **Vendor**: Adafruit, Amazon, Raspberry Pi distributors
- Runs LISY embedded image; communicates with APC board to bridge MPF commands to hardware
- Pi Zero W provides WiFi for remote debugging and config updates
- LISY image downloaded from https://lisy.dev/swrep/LISY_Image/embedded/latest/

### SD Card (for Raspberry Pi)
- **Qty**: 1 (32GB, already loaded with LISY image)
- **Vendor**: Amazon
- Holds LISY embedded OS image
- Uploaded using Raspberry Pi Imager or dd

### Development PC (for running MPF)
- **Qty**: 1 (existing Linux workstation)
- Runs MPF game code that connects to LISY/APC over serial (/dev/ttyACM0)
- Python virtualenv `mpfgmc3118_timewarp` with Python 3.11.8 and MPF installed
- Connected to APC via USB cable from PC to Arduino Due programming port

---

## 4. Playfield & Cabinet

> All playfield and cabinet parts are reused from the original Williams Time Warp machine. The APC platform is a drop-in board replacement that uses all existing wiring, switches, coils, and lamps. No new mechanical parts are required for the base conversion.

### Replacement Parts (as needed for refurbishment)
- Rubber ring kit for Williams Time Warp
- New pinballs (1-1/16" chrome steel)
- Replacement coil sleeves and stops for any worn positions
- Replacement lamps if converting to LED (bayonet base LED bulbs for System 7 sockets)

---

## 5. Reference Links

| Resource | URL |
|---|---|
| APC GitHub & Documentation | https://github.com/AmokSolderer/APC |
| APC PCB Parts BOM (Google Sheet) | https://docs.google.com/spreadsheets/d/1Lxnt1CGEWpybvpkPa3vRJebU48Qeu8h9te3dvZjng0g/edit?gid=0#gid=0 |
| APC Initial Tests | https://github.com/AmokSolderer/APC/blob/master/DOC/InitialTests.md |
| APC Useful SW Tools | https://github.com/AmokSolderer/APC/blob/master/DOC/UsefulSWtools.md |
| LISY Software | https://lisy.dev/software.html |
| MPF Documentation | https://missionpinball.org/ |
| Main README Setup Steps | [../README.md](../README.md) |
