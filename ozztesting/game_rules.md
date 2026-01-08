# Ozztesting Gameplay Rules Proposal (Draft)
- this game is a fan project that will be used on a single machine at home. It is considered a "homebrew" and as such does not require obtaining licensing/copywrights or similar. Songs, images, fonts, graphics, videos etc. can be used without restriction
- pinball-soup contains folders of independent pinball machines using various hardware types for each (machines can use Arduino Pinball Controller, FAST, etc.)
- this file is focused on building the ozztesting machine

## Game Overview:
- Pinball player(s) are trying to progress through bands at Ozzfest to get to Black Sabbath Wizard Mode.
- If player does not select Ozzy Osborne at beginning of game, player must complete all other band modes before being able to play Ozzy Osborne band mode.
- If player selects Ozzy as band when game starts, all other band modes should show as "completed". This allows player to skip progression through other bands.
- If all band modes are completed, "Black Sabbath Wizard Mode" begins when player lands a ball in either opper or lower kickout hole.

## context for understanding software & hardware used for this game
- python virtualenv ozzy_3118 with python 3.11.8 has been built for running the software layer of the game. all mpf commands should be run in this virtualenv.

- godot editor 4.4.1 has been downloaded and gmc plugin has been activated using steps defined in ~/repos/mpf-docs/docs/gmc/installation.md. The mpf-gmc repo was cloned to ~/repos/mpf-gmc and the contents of ~/repos/mpf-gmc/addons/mpf-gmc have been copied into ~/repos/pinball-soup/ozztesting

- mpf (mission pinball framework): software
    - mpf source code has been cloned to /home/hotsoup/repos/mpf
    - mpf-gmc source code has been cloned to /home/hotsoup/repos/mpf-gmc
    - mpf source documentation & code examples has been cloned to /home/hotsoup/repos/mpf-docs

- APC (Arduino Pinball Controller): board that uses lisy protocol to run pinmame on Williams 3-11c pinball machines. Also supports mpf for writing new game software for these machines
    - APC source code has been cloned to /home/hotsoup/repos/APC


- This game is currently running on Jungle Lord physical pinball machine via mpf software and APC board.

- Jungle Lord has 2 pinballs installed, and a separated "mini bagatelle playfield" on the upper playfield. This mini playfield has a kicker to launch a small ball that will roll over one of the LORD switches with each kick.

## MPF/GMC testing context
- ensure virtualenv ozzfest_3118 is active in terminal
- before completing steps in any implementation plan, run command `mpf -vtX` in machine folder to verify successful startup when not connected to the physical pinball machine. when connected, the command should be mpf both -vt. connection to physical machine exists if port is connected to /dev/ttyACM0. once verified. machine can be stopped with command CTRL+C
- if connected to physical machine (/dev/ttyACM0 exists), run command `mpf -vt` and verify successful startup before completing step. once verified. machine can be stopped with command CTRL+C.

## MPF/GMC startup test log
- 2026-01-06: Ran `mpf both -vtX` in pyenv env `ozzfest_3118` (virtual/no hardware). Result: startup aborted due to config error "slide_player:p" invalid in mode_carousel_band_started slides; Attract not active. Fix slide_player config before next run.
- 2026-01-06: Ran `mpf both -vtX` in `ozzfest_3118` after slide_player fix; startup reached attract, GMC connected; exited via SIGINT. Warnings: segment_display update_method deprecation; virtual switch audit chatter expected.


# Ozztesting Gameplay Rules Overview (Draft)
Bands
- Meatloaf
- Dio
- Rob Zombie
- Rivers of Nihil
- Ozzy Osbourne
- Black Sabbath


Band Carousel Selection
- use ~/repos/mpf-doc/docs/cookbook/carousel.md and ~/repos/pinball-soup/ozzy/modes/carousel_artist for context on creating carousel mode
- at the beginning of the game, player selects a band from the carousel menu using right/left magnasave buttons on cabinet to move carousel option right and left. pressing both buttons at same time selects the highlighted option. mpf has a "combo switch" event to handle this if the magnasave buttons are configured correctly in config/config.yaml.
- selecting a band begins that band's mode
- each band is a mode that has specific shot tasks to complete
- the band's song should play while player is rotating through carousel
- a video of the band should play while player is rotating through carousel. Each video will be a show/slide in godot. Use placeholder videos for now, these will be added at a later stage
- Black Sabbath is Wizard Mode and cannot be selected in band carousel

- additionally to selecting a band via carousel mode at the beginning of the game, if no band's mode is currently running in mpf (meaning a player has completed at least one band mode after game start) and player shoots ball into upper kickout hole, the ball is held in that kickout hole until a player selects a new band mode via the carousel mode
