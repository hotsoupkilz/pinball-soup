# Ozztesting Implementation Plan

## Quick Reference
- **Virtualenv**: `pyenv activate ozzfest_3118`
- **Test without hardware**: `mpf -vtX`
- **Test with hardware** (APC on /dev/ttyACM0): `mpf both -vt`
- **MPF docs MCP**: https://context7.com/missionpinball/mpf-docs
- **Local repos**: ~/repos/mpf, ~/repos/mpf-gmc, ~/repos/mpf-docs, ~/repos/APC

---

## Current Status

### ✅ Working
- Ball save mode
- Basic attract mode
- Segment display player
- Hardware connection (LISY/APC)
- Ball devices (trough, plunger, kickout holes)

### ⚠️ In Progress - Carousel Band Selection
- Slide displays but highlight switching not working

### ❌ Not Started
- Band modes (meatloaf, dio, zombie, rivers, ozzy)
- Wizard mode (Black Sabbath)
- Game progression tracking
- Achievement system

---

## Phase 1: Fix Carousel Mode (Priority: HIGH)

### Issue 1: Combo Switch Event Not Firing
**File**: [config/config.yaml](config/config.yaml#L50)
**Problem**: `events_when_both` is commented out
**Fix**: Uncomment line 50

```yaml
combo_switches:
  combo_magnasave:
    tag_1: magnasave_left
    tag_2: magnasave_right
    events_when_both: combo_magnasave_both  # UNCOMMENT THIS LINE
```

### Issue 2: MPFCarousel Node Type Declaration
**File**: [modes/carousel_band/slides/carousel_band_base.tscn](modes/carousel_band/slides/carousel_band_base.tscn)
**Problem**: The MPFCarousel node may not be recognized properly. The node is declared as `type="MPFCarousel"` but needs `type="Control"` with the script attached.
**Current**: `[node name="HighlightCarousel" type="MPFCarousel" parent="."]`
**Fix**: Should be `type="Control"` with script, but the current setup looks correct. Verify GMC plugin is properly activated in Godot project settings.

### Issue 3: Verify carousel_name Property
**File**: [modes/carousel_band/slides/carousel_band_base.tscn](modes/carousel_band/slides/carousel_band_base.tscn#L50)
**Current**: `carousel_name = "carousel_band"`
**Verification**: This matches the mode name in mode_settings, so this is correct.

### Debugging Steps
1. Run with verbose logging: `mpf both -vV`
2. Check for `carousel_item_highlighted` events in log
3. Verify GMC console shows carousel connection
4. Verify child node names match selectable_items exactly: `meatloaf`, `dio`, `ozzy`, `rivers`, `zombie`

### Test Checklist
- [ ] Uncomment events_when_both in config.yaml
- [ ] Start game and verify carousel mode starts on ball_starting
- [ ] Press left magnasave - should highlight previous item
- [ ] Press right magnasave - should highlight next item  
- [ ] Press both magnasaves - should select and start band mode
- [ ] Verify audio plays on highlight
- [ ] Verify slide shows highlighted band name

---

## Phase 2: Create Band Mode Templates

Each band mode needs:
1. Mode config YAML
2. Slides (Godot scenes)
3. Shot definitions
4. Audio hooks

### Mode Structure Template
```
modes/
  {band_name}/
    config/
      {band_name}.yaml
    slides/
      {band_name}.tscn
    shows/
      (optional)
```

### Band Modes to Create

#### 2.1 Meatloaf Mode
**Folder**: `modes/meatloaf/`
**Theme**: "Bat Out of Hell" - dark red, bat imagery
**Shots to complete**: 3 targets
**Duration**: Timed (60s) or complete all shots
**Song**: `meatloaf_bat_out_of_hell.snd`

#### 2.2 Dio Mode  
**Folder**: `modes/dio/`
**Theme**: "Holy Diver" - deep blue, underwater/dragon imagery
**Shots to complete**: 3 targets
**Duration**: Timed (60s) or complete all shots
**Song**: `dio_holy_diver.snd`

#### 2.3 Rob Zombie Mode
**Folder**: `modes/zombie/`
**Theme**: "Living Dead Girl" - green/orange, horror imagery
**Shots to complete**: 3 targets
**Duration**: Timed (60s) or complete all shots
**Song**: `zombie_living_dead_girl.snd`

#### 2.4 Rivers of Nihil Mode
**Folder**: `modes/rivers/`
**Theme**: "The Silent Life" - dark teal/black, cosmic imagery  
**Shots to complete**: 3 targets
**Duration**: Timed (60s) or complete all shots
**Song**: `rivers_dustman.snd`

#### 2.5 Ozzy Mode
**Folder**: `modes/ozzy/`
**Theme**: "Crazy Train" - purple/black, bat imagery
**Shots to complete**: 3 targets (or unlocks wizard if selected first)
**Special**: If selected as first band, marks all other bands as "completed"
**Song**: `MUSIC.SND`

---

## Phase 3: Game Progression System

### Player Variables to Track
```yaml
player_vars:
  bands_completed:
    value_type: int
    initial_value: 0
  meatloaf_completed:
    value_type: int
    initial_value: 0
  dio_completed:
    value_type: int  
    initial_value: 0
  zombie_completed:
    value_type: int
    initial_value: 0
  rivers_completed:
    value_type: int
    initial_value: 0
  ozzy_completed:
    value_type: int
    initial_value: 0
  selected_ozzy_first:
    value_type: int
    initial_value: 0
  wizard_qualified:
    value_type: int
    initial_value: 0
```

### Band Completion Logic
When a band mode is completed:
1. Set `{band_name}_completed: 1`
2. Increment `bands_completed`
3. Check if `bands_completed >= 5` OR `selected_ozzy_first == 1 AND ozzy_completed == 1`
4. If qualified, set `wizard_qualified: 1`

### Ozzy-First Special Logic
When player selects Ozzy as first band:
1. Set `selected_ozzy_first: 1`
2. Set all other band variables to completed: `meatloaf_completed: 1`, etc.
3. Set `bands_completed: 4`
4. Start Ozzy mode

---

## Phase 4: Wizard Mode (Black Sabbath)

### Trigger Conditions
- `wizard_qualified == 1`
- Ball lands in upper OR lower kickout hole

### Wizard Mode Features
**File**: `modes/black_sabbath/config/black_sabbath.yaml`
**Theme**: Ultimate heavy metal - fire, dark imagery
**Music**: Black Sabbath song
**Priority**: 200 (high to override other modes)

### Implementation
```yaml
mode:
  start_events: start_mode_black_sabbath
  stop_events: ball_will_end
  priority: 200

# Wizard mode should have special shots, multiball potential, etc.
```

---

## Phase 5: Carousel Re-Entry Logic

### When Carousel Should Start
1. `ball_starting` - Initial band selection
2. `s_kickout_hole_upper_active` WHEN no band mode is running AND `wizard_qualified == 0`

### Updated Event Player
**File**: [config/config.yaml](config/config.yaml#L53)
```yaml
event_player:
  # Start carousel when ball is captured in upper kickout (if no band mode active)
  s_kickout_hole_upper_active{device.state_machine.current_band_mode=="none"}:
    - start_mode_carousel_band
  
  # Start wizard mode when qualified and ball captured
  s_kickout_hole_upper_active{current_player.wizard_qualified==1}:
    - start_mode_black_sabbath
  s_kickout_hole_lower_active{current_player.wizard_qualified==1}:
    - start_mode_black_sabbath
```

---

## Phase 6: Audio Integration

### Hardware Sound Files Required
All files must be on APC SD card:
- `meatloaf_bat_out_of_hell.snd`
- `dio_holy_diver.snd`
- `zombie_living_dead_girl.snd`
- `rivers_dustman.snd`
- `MUSIC.SND` (Ozzy)
- `black_sabbath_*.snd` (Wizard mode)

### Hardware Sound Player Pattern
```yaml
hardware_sound_player:
  mode_{band_name}_started:
    "{song_file}":
      track: 1
      action: play_file
      platform_options:
        loop: true
  mode_{band_name}_stopped:
    stop_track:
      track: 1
      action: stop
```

---

## Implementation Order

### Week 1: Fix & Test Carousel
1. [ ] Uncomment combo_magnasave_both in config.yaml
2. [ ] Test carousel mode with `mpf -vtX`
3. [ ] Verify all 5 bands highlight correctly
4. [ ] Verify audio plays on each highlight
5. [ ] Verify selection fires correct events

### Week 2: Create Band Mode Stubs
1. [ ] Create meatloaf mode folder structure
2. [ ] Create dio mode folder structure
3. [ ] Create zombie mode folder structure
4. [ ] Create rivers mode folder structure
5. [ ] Create ozzy mode folder structure
6. [ ] Add all modes to config.yaml modes list

### Week 3: Implement Band Mode Logic
1. [ ] Define shots for each mode
2. [ ] Create slides for each mode
3. [ ] Wire up completion events
4. [ ] Test each mode individually

### Week 4: Game Progression
1. [ ] Add player_vars to config.yaml
2. [ ] Wire up completion tracking
3. [ ] Implement Ozzy-first special logic
4. [ ] Test progression flow

### Week 5: Wizard Mode
1. [ ] Create black_sabbath mode
2. [ ] Implement wizard trigger logic
3. [ ] Create wizard slides/shows
4. [ ] Final integration testing

---

## File Reference

### Key Configuration Files
- [config/config.yaml](config/config.yaml) - Main machine config
- [modes/carousel_band/config/carousel_band.yaml](modes/carousel_band/config/carousel_band.yaml) - Carousel mode
- [modes/base/config/base.yaml](modes/base/config/base.yaml) - Base game mode
- [modes/ball_save/config/ball_save.yaml](modes/ball_save/config/ball_save.yaml) - Ball save mode

### GMC/Godot Files
- [gmc.cfg](gmc.cfg) - GMC configuration
- [project.godot](project.godot) - Godot project settings
- [addons/mpf-gmc/](addons/mpf-gmc/) - GMC addon (do not modify)

### Reference Projects
- [~/repos/pinball-soup/ozzy/modes/carousel_artist/](../ozzy/modes/carousel_artist/) - Working carousel example
- [~/repos/mpf-docs/docs/cookbook/carousel.md](~/repos/mpf-docs/docs/cookbook/carousel.md) - MPF carousel docs

---

## Troubleshooting

### Carousel Not Switching Items
1. Check `events_when_both` is uncommented
2. Verify MPFCarousel node has correct `carousel_name` property
3. Check child node names match `selectable_items` exactly (case-sensitive)
4. Look for `carousel_item_highlighted` in verbose logs

### Audio Not Playing
1. Verify .snd files exist on APC SD card
2. Check file names match exactly (case-sensitive)
3. Verify track number is valid (0-2)

### Mode Not Starting
1. Check mode is listed in config.yaml `modes:` section
2. Verify start_events are being posted
3. Check for config validation errors in logs

### GMC Not Connecting
1. Verify virtualenv is active
2. Check Godot project has GMC addon enabled
3. Verify BCP connection in gmc.cfg
4. Run `mpf both` not just `mpf`
