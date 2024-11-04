# pinball_soup

The below steps will get a) a python virtualenv to work in, b) the godot engine needed by mpf, c) mpf and d) the gmc addons mpf needs into a given machine folder

MissionPinball Docs: https://missionpinball.org/latest/start/quickstart/

- install godot: https://godotengine.org/download/linux/
- $ mv ~/Downloads/Godot_v4.3-stable_linux.x86_64 godot
- $ sudo mv godot /usr/local/bin
- install pyenv & activate virtualenv plugin
- install python versions
- $ env PYTHON_CONFIGURE_OPTS='--enable-optimizations --with-lto' PYTHON_CFLAGS='-march=native -mtune=native' pyenv install --verbose 3.11.8
- $ env PYTHON_CONFIGURE_OPTS='--enable-optimizations --with-lto' PYTHON_CFLAGS='-march=native -mtune=native' pyenv install --verbose 3.9.12
- $ pyenv virtualenv 3.9.12 mpf3912
- $ pyenv virtualenv 3.11.8 mpfgmc3118_timewarp
- $ pyenv activate mpfgmc3118_timewarp
- Download latest mpf-gmc from https://github.com/missionpinball/mpf-gmc
- $ cp -rv ~/repos/mpf-gmc/addons ~/repos/pinball_soup/time_warped/
- follow MPF instructions on godot editor for setting main scene, window size, audio buses, attract mode slide



