# pinball_soup

#### The below steps will get a) arduino IDE, b) raspi set up with lisy, c) sd cards for APC to run Time Warped

- Arduino Pinball Controller Docs: https://github.com/AmokSolderer/APC
- Arduino IDE: https://docs.arduino.cc/software/ide-v2/tutorials/getting-started-ide-v2/
- lisy: https://lisy.dev/software.html

### APC software
- install arduino IDE (IDE 2) appimage from arduino site
- make downloaded file executable & open
- install Arduino IDE SPI (if needed) and sdfat libraries as detailed on APC github
- clone/download V1.02 version of APC repo
- upload APC.ino sketch in Arduino IDE (the other .ino files from repo should open as separate register cards)
- connect DUE to comp via "programming port" (closest to DC power)
- in IDE, select Tools > Board > Boards Manager, then search for DUE and download sam boards core.
- in IDE, select Tools > Board > Arduino SAM boards > Arduino DUE (programming port)
- in IDE, select Tools > Serial Port > select arduino IDE serial port
- upload APC.ino sketch to DUE via "Upload" button.
- if permission error, likely need to add user to group that controls port access. check which group owns ports (how TBD), if "dialout" group exists, it is likely this one
- `$ less /etc/group` (this lists all groups)
- add user to appropriate group & reboot afterwards: `$ sudo usermod -a -G dialout $USER`. retry upload after reboot & it should work.
- format an SD card from SDcard assoc (in windows machine only) for use on APC board. There will be a second SD card for use with raspi outlined below.

#### The below steps will get a) a python virtualenv to work in, b) the godot engine needed by mpf, c) mpf and d) the gmc addons mpf needs into a given machine folder

MissionPinball Docs: https://missionpinball.org/latest/start/quickstart/

WIP
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



