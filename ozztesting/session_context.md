- pinball-soup repo contains directories that each contain code to run a physical pinball machine using the mission pinball framework. Each can use different hardware configurations (FAST, arduino pinball controller, etc.)
- this session is focused on the ozztesting machine directory. changes in other directories are not desired unless specifically noted
- this machine will run with mpf. the core mpf repo is https://github.com/missionpinball/mpf/tree/0.80.x (not main or dev) and the media controller repo is https://github.com/missionpinball/mpf-gmc.
- mpf docs provide excellent code examples and are available at https://github.com/missionpinball/mpf-docs. However do not reference mpf-mc, the legacy media controller with mpf version .5X and below. mpf version .8X uses the much-improved mpf-gmc framework
- only reference other directories in pinball-soup repo as requested. Otherwise mpf code examples can be found from official repos and/or docs
- a virtualenv with mpf installed is required to run this machine 
this virtualenv has the mission pinball framework installed on it, enabling mpf commands. it was installed with pip install mpf --pre
- python commands should typically only be run while in virtualenv ozzfest_3118
- this machine uses mpf version .8 and above only.
- the godot editor has been installed

- the code for the ozztesting machine is currently set up to run on Jungle Lord using the Arduino Pinball Controller and lisy. The game rules are dictacted by the physical hardware defined in config/config.yaml
- this is a 4 player game
- Jungle Lord is a "two ball game", meaning multiball modes are possible.
- jungle lord has a confined mini bagatelle-style playfield that consists of the LORD switches and corresponding playfield lights, a small ball and a kicker to send the small ball over one of the 4 LORD switches.

