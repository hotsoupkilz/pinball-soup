# Ozztesting Session Context

## Quick Reference
- **Virtualenv**: `pyenv activate ozzfest_3118` (Python 3.11.8, MPF 0.80.0.dev11)
- **Test without hardware**: `mpf -vtX`  
- **Test with hardware** (APC on /dev/ttyACM0): `mpf both -vt`
- **Godot editor**: 4.4.1 with GMC 0.1.6 plugin

## MCP Context Server
- MPF docs: https://context7.com/missionpinball/mpf-docs

## Local Repositories
- **mpf source**: ~/repos/mpf (use 0.80.x branch, NOT main/dev)
- **mpf-gmc source**: ~/repos/mpf-gmc
- **mpf-docs**: ~/repos/mpf-docs
- **APC (Arduino Pinball Controller)**: ~/repos/APC

## This Machine
- pinball-soup repo contains directories that each contain code to run a physical pinball machine using the mission pinball framework. Each can use different hardware configurations (FAST, arduino pinball controller, etc.)
- this session is focused on the ozztesting machine directory. changes in other directories are not desired unless specifically noted
- Physical machine: Jungle Lord (Williams System 3-11c) via APC board
- 2 pinballs installed, plus mini bagatelle playfield with separate small ball

## Key Implementation Notes
- mpf version 0.8X uses mpf-gmc (Godot media controller), NOT mpf-mc
- Do NOT reference mpf-mc - that's the legacy media controller for mpf 0.5X
- Carousel mode uses `mpf.modes.carousel.code.carousel.Carousel`
- MPF carousel posts `carousel_item_highlighted` event with `carousel` and `item` kwargs
- GMC's MPFCarousel node listens for this and shows/hides children by name match
- Hardware sounds use APC SD card with .snd files

## Current Work: Carousel Band Selection
- **Implementation plan**: See [implementation.md](implementation.md)
- Carousel mode config: [modes/carousel_band/config/carousel_band.yaml](modes/carousel_band/config/carousel_band.yaml)
- Carousel slide: [modes/carousel_band/slides/carousel_band_base.tscn](modes/carousel_band/slides/carousel_band_base.tscn)
- Reference working carousel: [ozzy/modes/carousel_artist/](../ozzy/modes/carousel_artist/)

### Recent Fix Applied
**Issue**: Carousel slide showed wrong item (Rob Zombie) instead of first item (Meatloaf), and navigation didn't work.

**Root Cause**: The MPFCarousel component approach (single slide with show/hide children) wasn't working reliably due to timing race conditions between MPF events and Godot slide creation.

**Solution Applied**: Changed to slide_player approach (like MPF cookbook example):
- Each carousel item gets its own slide file (carousel_band_meatloaf.tscn, etc.)
- slide_player plays the appropriate slide on each `carousel_item_highlighted` event
- This is simpler and more reliable than the MPFCarousel component

**Configuration Changes** (carousel_band.yaml):
- Removed: carousel_band_base slide with MPFCarousel component
- Added: Individual slide_player entries for each carousel_item_highlighted event
- Each band has its own slide: carousel_band_meatloaf, carousel_band_dio, etc.

**GMC Version Notes**:
- ozzy project uses GMC 0.1.5 (expects `item_highlighted` event)
- ozztesting uses GMC 0.1.6 (expects `carousel_item_highlighted` event)
- MPF 0.80.0.dev11 posts `carousel_item_highlighted` - matches ozztesting GMC

## Game Rules
- See [game_rules.md](game_rules.md) for full gameplay rules
- Bands: Meatloaf, Dio, Rob Zombie, Rivers of Nihil, Ozzy Osbourne
- Black Sabbath is wizard mode (not selectable in carousel)
- Player progresses through bands to unlock wizard mode



