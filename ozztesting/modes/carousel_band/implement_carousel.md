# Carousel Band Selection Mode — Implementation Plan

Context
- Machine: ozztesting (Jungle Lord hardware via APC/Lisy), MPF 0.8, GMC in Godot 4.4.1.
- Inputs: s_magnasave_button_left, s_magnasave_button_right for navigation and combo-select; s_kickout_hole_upper is the hold-and-select entry during gameplay; s_plunger for manual launch; 2-ball trough.
- Bands (selectable): Meatloaf, Dio, Rob Zombie, Rivers of Nihil, Ozzy Osbourne. Black Sabbath is wizard and should not be selectable.
- Reference: ozzy/modes/carousel_artist (uses MPF carousel code) and mpf-docs cookbook carousel.

Goals
- Let player choose a band at game start before first plunge.
- Let player re-enter carousel after finishing a band: when no band mode is running and the upper kickout holds a ball until selection is made.
- Navigate with magnasave buttons (left = previous, right = next). Selecting requires pressing both simultaneously via an MPF switch combo.
- Play band song preview and show a band video slide while rotating through options.
- Start the chosen band mode and resume play (release held ball) on selection; do not allow Black Sabbath in the carousel list.

High-level flow
1) Start trigger: On ball_starting (or a custom event from base) if no active band mode, start carousel_band mode.
2) In-mode navigation: left/right magnasave events drive previous/next; combo event triggers select.
3) Highlight handling: carousel code posts highlighted events per item; use them to play the matching song loop and show the matching video slide.
4) Selection: when select fires, post an event (e.g., band_selected_<name>), start that band mode, set machine/player vars, stop carousel, and release any held ball.
5) Re-entry mid-game: If no band mode running and s_kickout_hole_upper made active, divert ball to hold, start carousel, resume after selection.
6) Exit: stop carousel mode when a band is selected or when ball will end.

MPF configuration steps
- Modes list: add carousel_band to ozztesting/config/config.yaml.
- Mode folder: ozztesting/modes/carousel_band/{config,shows,slides}.
- Mode config (carousel_band.yaml):
  - mode.start_events: ball_starting or a dedicated event from base when band_needed.
  - mode.stop_events: carousel_band_item_selected, ball_will_end.
  - mode.code: mpf.modes.carousel.code.carousel.Carousel (MPF built-in).
  - mode_settings.selectable_items: [meatloaf, dio, zombie, rivers, ozzy].
  - next_item_events: s_magnasave_button_right_active
  - previous_item_events: s_magnasave_button_left_active.
  - select_item_events: combo_magnasave_both (see switch_combos below).
  - Map highlight events (carousel_band_<item>_highlighted) to set a player var highlighted_band and fire song/slide triggers.
- switch_combos (in config/config.yaml or a mode-scoped config): define a combo for pressing both magnasave buttons within ~400ms that posts combo_magnasave_both.
- Device control for upper kickout hold: in base or this mode, add an event_player rule so when s_kickout_hole_upper_active and no band mode running, eject is suppressed, ball is tagged held_for_carousel, and start_carousel_band event is posted.
- Event plumbing:
  - band_mode_started: set player var current_band and maybe add to completed list (except wizard) when finished.
  - band_mode_completed: post band_cleared and allow carousel relaunch on next upper kickout.
  - carousel_band_item_selected: carries selected item; stop carousel; release held ball (trigger bd_kickout_hole_upper_eject) and post start_mode_<band>.

Audio/GMC assets
- Font already available: ozztesting/assets/fonts/gothic/IMFeENrm28P.ttf (gothic, readable).
- Songs: add placeholder .snd files for each band in sounds/. Use hardware_sound_player or sound_player in the mode to play looped preview on highlight (stop previous before starting new). Map highlights to these tracks in assets/music:
  - Meatloaf: assets/music/bat_out_of_hell
  - Dio: assets/music/dio_holy_diver
  - Rob Zombie: assets/music/living_dead_girl
  - Rivers of Nihil: assets/music/dustman
  - Ozzy: placeholder or silence until track chosen; still stop any preview on Ozzy highlight
- Video slides: create one GMC slide per band under modes/carousel_band/slides/<band>.tscn (or reuse mpf-gmc widgets if preferred). Use placeholder textures or videos; wire a slide_player mapping from highlight events to show the corresponding slide, with `loops: -1` until selection.

Display/slide wiring
- slide_player (in carousel_band.yaml):
  - mode_carousel_band_started: show a base carousel slide (title, instructions, current band).
  - carousel_band_<item>_highlighted: show band-specific slide (video/cover art) and maybe a small text overlay.
  - carousel_band_item_selected: clear carousel slides.
- Optional: a text marquee for controls ("Left/Right = browse, Both = select").

Variables and logic
- Player vars: current_band (active), completed_bands (set), highlighted_band (preview).
- Machine vars (optional): last_selected_band for analytics.
- Prevent Black Sabbath from list; only unlocked via rule (all bands completed) outside carousel.
- Ensure carousel does nothing if a band mode is already running (guard start event with condition or enable_if not running band mode).

Ball handling integration
- On start carousel: disable flippers if desired; keep ball at plunger if pre-plunge; or hold in upper kickout during mid-game invocation.
- On selection: re-enable flippers, release held ball from bd_kickout_hole_upper, or allow manual plunge if at start.

Testing checklist
- Start-of-game: carousel appears before plunge; magnasave buttons move selection; combo selects; selected band mode starts; ball can be plunged.
- Mid-game: complete a band, shoot upper kickout; ball holds; carousel appears; selection starts next band and releases ball.
- Audio: highlight changes stop previous preview and start new preview.
- Display: slides change on highlight; no Black Sabbath option visible.
- Fail-safes: carousel aborts on ball_will_end; no stale holds on tilt or drain.

File/layout plan to implement
- ozztesting/config/config.yaml: add mode, add switch_combo for magnasave, optional event_player to gate carousel start on kickout when no band running.
- ozztesting/modes/carousel_band/config/carousel_band.yaml: main mode config (mode, mode_settings, slide_player, sound_player/hardware_sound_player, event_player for release on select).
- ozztesting/modes/carousel_band/shows/: optional attract-style instruction show or transitions.
- ozztesting/modes/carousel_band/slides/: base carousel slide plus per-band slides (placeholder images/videos).
- ozztesting/modes/base/config/base.yaml (or a helper logic_block file): add logic to mark band completion and trigger carousel re-entry when no band is running and upper kickout is hit.

Execution order
- [x] Add switch_combo for magnasave-both select; verify events fire in MPF monitor.
- [x] Add carousel_band mode config with selectable items, events, and highlight mappings; wire slide_player and sound_player.
- [x] Build GMC slides (base + per-band placeholders) and ensure paths are correct.
- [x] Add band start/complete events (or stubs) in each band mode to coordinate with carousel; ensure Black Sabbath start is gated elsewhere.
- [x] Add upper kickout hold-and-start logic; test physical behavior.
- [ ] Playtest full loop in MPF: start-of-game selection, mid-game reselection, audio/visual correctness, recovery on tilt/end.
