# Ozzfest Gameplay Rules Proposal (Draft)
- this game is a fan project that will be used on a single machine at home. It is considered a "homebrew" and as such does not require obtaining licensing/copywrights or similar. Songs, images, fonts, graphics, videos etc. can be used without restriction
- pinball-soup contains folders of independent pinball machines using various hardware types for each (machines can use Arduino Pinball Controller, FAST, etc.)
- this file is focused on building the Ozzfest machine

## Game Overview:
- Pinball player(s) are trying to progress through bands at Ozzfest to get to Black Sabbath Wizard Mode.
- If player does not select Ozzy Osborne at beginning of game, player must complete all other band modes before being able to play Ozzy Osborne band mode.
- If player selects Ozzy as band when game starts, all other band modes should show as "completed". This allows player to skip progression through other bands.
- If all band modes are completed, "Black Sabbath Wizard Mode" begins when player lands a ball in either opper or lower kickout hole.

- Carousel selection: implemented and verified (highlights, switching, selection, audio/slide integration)

## context for understanding software & hardware used for this game
- python virtualenv ozzy_3118 with python 3.11.8 has been built for running the software layer of the game. all mpf commands should be run in this virtualenv.

- godot editor 4.4.1 has been downloaded and gmc plugin has been activated using steps defined in ~/repos/mpf-docs/docs/gmc/installation.md. The mpf-gmc repo was cloned to ~/repos/mpf-gmc and the contents of ~/repos/mpf-gmc/addons/mpf-gmc have been copied into ~/repos/pinball-soup/Ozzfest

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


# Ozzfest Gameplay Rules Overview (Draft)
Bands
- Meatloaf
- Dio
- Rob Zombie
- Rivers of Nihil
- Ozzy Osbourne
- Black Sabbath


Band Carousel Selection (Status: Implemented)
- Implementation notes: carousel highlights, left/right switching, and "both" selection have been verified. Audio and slide/video highlight integration are functioning during carousel rotation.
- At game start, player selects a band from the carousel using the cabinet magnasave buttons: left/right to move the highlight, pressing both selects the highlighted band and starts that band's mode. MPF's combo switch event is used for the "both" selection when magnasave switches are configured in `config/config.yaml`.
- Selecting a band immediately begins that band's mode.
- Each band remains a separate mode with its own shot tasks and completion tracking.
- Black Sabbath remains Wizard Mode and is not selectable from the carousel.
- Re-entry behavior: when no band mode is running and a ball is captured in the upper kickout, the machine starts/opens the carousel and holds the ball until the player selects a new band via the carousel.
