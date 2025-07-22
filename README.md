# pinball_soup

#### The below steps will enable running mpf on Williams System 3-11c & Data East 1-3
#### a) arduino IDE, b) raspi set up with lisy, c) sd cards for APC to run Time Warped

- Arduino Pinball Controller Docs: https://github.com/AmokSolderer/APC
- Arduino IDE: https://docs.arduino.cc/software/ide-v2/tutorials/getting-started-ide-v2/
- lisy: https://lisy.dev/software.html

## APC: PCB ordering
- follow instructions on APC github docs for assembly files, parts to order, etc
- APC thread notes: https://pinside.com/pinball/forum/topic/arduino-pinball-controller/page/20#post-8326182
    - note: sw versions (APC from 1.02 to 1.03 and mpf from .5x to .8x w/godot) changed from initial post to completion
- PCB maker did not have all parts available/in stock. Order list details for parts to solder for board completion:
  - https://docs.google.com/spreadsheets/d/1Lxnt1CGEWpybvpkPa3vRJebU48Qeu8h9te3dvZjng0g/edit?gid=0#gid=0

## APC: Arduino Due & onboard SD card
- install arduino IDE (IDE 2) appimage from arduino site
- make downloaded file executable & open
- install Arduino IDE SPI (if needed) and sdfat libraries as detailed on APC github
- clone/download V1.02 version of APC repo
- upload APC.ino sketch in Arduino IDE (the other .ino files from repo should open as separate register cards)
- connect Due to comp via "programming port" (closest to DC power)
- in IDE, select Tools > Board > Boards Manager, then search for Due and download sam boards core.
- in IDE, select Tools > Board > Arduino SAM boards > Arduino Due (programming port)
- in IDE, select Tools > Serial Port > select arduino IDE serial port
- upload APC.ino sketch to Due via "Upload" button.
- if permission error, likely need to add user to group that controls port access. check which group owns ports (how TBD), if "dialout" group exists, it is likely this one
- `$ less /etc/group` (this lists all groups)
- add user to appropriate group & reboot afterwards: `$ sudo usermod -a -G dialout $USER`. retry upload after reboot & it should work.
- format an SD card using formatter from SDcard assoc (in windows machine only) for use on APC board. There will be a second SD card for use with raspi outlined in later steps.
  - wyze 32gb card: card with RED sharpie has Time Warp settings (APC & usb) & sounds from amoksolderer (via dropbox) pre-loaded
  - wyze 32gb card: card with BLACK X/LINES sharpie has no pre-loaded settings (will need to configure APC correctly upon first use, which will save settings to card)
- Install Due on APC, put sd card into APC's onboard slot
- Install APC in pinball machine (no raspi yet):
  - take one cord from old board, clearly label it based on name printed on old board (e.g. 2J4 on connector housing)
  - take that same cord and plug into corresponging port on APC using this diagram: https://github.com/AmokSolderer/APC/blob/master/DOC/InitialTests.md
  - run each test in order as described in APC initial test docs (linked in line above)

## Lisy: Lisy image & raspberry pi
- download latest lisy embedded image via https://lisy.dev/swrep/LISY_Image/embedded/latest/
  - align image type with raspi type: ensure pi0w image since that's the raspi we're using here
- optional: download latest full image via https://lisy.dev/swrep/LISY_Image/stable/
- upload image to sdcard using a good image writer tool (can be linux or windows ex: raspi imager, dd)
- put sdcard into raspi (pi0w v 1.1) slot, install raspi (pi0w) on APC

## Pinball Machine: lisy config & running original rom
- APC creator sent Time Warp sound files, APC config, and usb/lisy/raspi config pre-set to pull up Time Warp.
- unzip if needed from download, and upload files to (correctly formatted) sdcard as indicated in previous steps. Install card on APC board
- Turn machine on. It should come up as original Time Warp
  - the "first" time this is done (or sdcard wiped/reuploaded), machine will enter Williams settings vs gameplay. Flip coin door dipswitch to "Down", short press "Advance" to navigate back to final "exit" setting, then press start button. Settings will save to sdcard and game should start as normal going forward.
  - rom is coin-based. will need to add credits to machine to start game.


#### The below linux-based steps will get a) a python virtualenv to work in, b) the godot engine needed by mpf, c) mpf and d) the gmc addons mpf needs into a given machine folder

### mpf: godot engine/IDE, local development env, table project setup
MissionPinball Docs: https://missionpinball.org/latest/start/quickstart/
GMC installation instructions (although godot not needed for machines with segment displays only)

- install godot: https://godotengine.org/download/linux/
- `$ mv ~/Downloads/Godot_v4.3-stable_linux.x86_64 godot`
- `$ sudo mv godot /usr/local/bin`

- install pyenv & activate virtualenv plugin
- install python versions
- `$ env PYTHON_CONFIGURE_OPTS='--enable-optimizations --with-lto' PYTHON_CFLAGS='-march=native -mtune=native' pyenv install --verbose 3.11.8`
- `$ env PYTHON_CONFIGURE_OPTS='--enable-optimizations --with-lto' PYTHON_CFLAGS='-march=native -mtune=native' pyenv install --verbose 3.9.12`
- `$ pyenv virtualenv 3.9.12 mpf3912`
- `$ pyenv virtualenv 3.11.8 mpfgmc3118_timewarp`
- `$ pyenv activate mpfgmc3118_timewarp`

- ` (mpfgmc3118_timewarp)$ pip install mpf --pre`
- ` (mpfgmc3118_timewarp)$ mpf --version`
- download latest mpf-gmc from https://github.com/missionpinball/mpf-gmc
- `$ cp -rv ~/repos/mpf-gmc/addons ~/repos/pinball_soup/time_warped/`
- follow MPF instructions/docs on godot editor for setting main scene, window size, audio buses, attract mode slide

## mpf: making the game
- new Time Warped in progress, but code that runs a simple game can be found in time_warped folder in this repo
- as noted above, if only working with segment displays the godot media controller basically wont be used
unless a screen is added to machine or virtual testing
- follow the mpf tutorial on setting up modes
- follow the docs (lisy.dev mpf example, APC docs, mpf docs) on setting up segment displays in mpf
- older Williams systems have some quirks with driver/lamp/switch/coil configs
    - pay attention to "special solenoids". Flippers, jet bumpers or others may need special configs
    - For time warp, do not add mpf "flippers" section and only add coils. Time Warp doesnt have numbers
    in manual for these, so lisy/apc use numbers 23 & 24 for flippers
    - Time Warp jet bumpers use special solenoids as well. Replace switch numbers 17-22 with 65-70 in
    machine config as needed
    - This also means that some things aren't possible like rotating lane shots by flipper fire (as far as I can tell so far)
- sounds/music:
    - mpf's `hardware_sound_systems` should use APC
    - with this, music/sound files can be converted and saved to the sdcard installed on the APC
    - TODO: determine whether APC/lisy sound systems can be combined, for example to use lisy's text-to-speech feature
    - use audacity to convert files into 44.1khz .wav files
        - Download audacity, open source song/sound as audacity project.
        - To convert, File > Export Audio. Then change name; Channels: Mono; Sample Rate: 44100 Hz; Encoding: Signed 16-bit PCM
     - ensure you have a perl interpreter (strawberryperl on windows works fine)
     - use amoksolderer's Audio Data Converter (https://github.com/AmokSolderer/APC/blob/master/DOC/UsefulSWtools.md#audio-data-converter) to generate sound files APC can interpret.
        - save perl script in same directory as files you're touching.
        - if using the single file method, rename converted sound file to Data.wav & execute perl script in powershell/similar
        - if using the whole folder method, execute script in powershell/similar
    - upload the file(s) generated by Audio Data Converter to sdcard
    - in mpf, set track/sound names & configs using example in APC docs (or time_warped folder in this repo)

## mpf/APC: running the game without a laptop
- Upload raspi OS lite 32-bit, debian bullseye (not the one after as pip install w/o venv removed), to sdcard via official raspi imager tool.
    - raspi: regular pi V1.2
    - enable settings:
        - change default hostname to timewarpedapc
        - add user/pw (otherwise default will be used)
        - add home wifi connection
        - enable ssh
    - storage: sdcard in reader/usb should pop up
- place sdcard into raspi and connect raspi to (approved) power source.
- raspi should boot once connected. wait a minute or so.
- find ip address of connected raspi (assuming wifi creds were added correctly
  via imager tool) using details from router (usually entering some ip into
  browser based on router details and visually locating)
- ssh into raspi
    - `$ ssh hotsoup@ip`
        - enter pw

- Set root pw, update system (again ensure bullseye vs newer)
```
hotsoup@timewarpedapc:~ $ sudo passwd root (set a good password & confirm)
hotsoup@timewarpedapc:~ $ sudo apt update
hotsoup@timewarpedapc:~ $ sudo apt full-upgrade
hotsoup@timewarpedapc:~ $ systemctl reboot
<ssh terminal connection will break>
```

- This will install mpf system-wide for user, and newer debian version either
  requires venv or apt to support pip package - the reason bullseye is used.
```
$ ssh hotsoup@ip
(enter pw)
hotsoup@timewarpedapc:~ $ sudo apt install python3-pip
verify install with...
hotsoup@timewarpedapc:~ $ pip --version
assuming this returns a pip version (ie pip 20.3.4)...
hotsoup@timewarpedapc:~ $ pip install mpf --pre
hotsoup@timewarpedapc:~ $ systemctl reboot
<ssh terminal connection will break>
```

- verify mpf install, download time_warped repo to use as machine folder
- it appears that raspi needs powersource when connecting to programming port of arduino

```
$ ssh hotsoup@ip
hotsoup@timewarpedapc:~ $ sudo apt install git
follow instructions for generating/adding ssh keys to github account online
hotsoup@timewarpedapc:~ $ git clone git@github.com:hotsoupkilz/pinball_soup.git

```

- test run mpf `$ cd pinball_soup/time_warped && mpf -b -t`

- since we dont want to manually start mpf every time machine is turned on,
  add details to `/etc/rc.local` that executes mpf comman at system start

```

hotsoup@timewarpedapc:~/pinball_soup/time_warped $ sudo vi /etc/rc.local
... add the following and save/close: su hotsoup -c 'cd /home/hotsoup/pinball_soup/time_warped && mpf -b -t'...
hotsoup@timewarpedapc:~/pinball_soup/time_warped $ sudo chmod +x /etc/rc.local
hotsoup@timewarpedapc:~/pinball_soup/time_warped $ sudo vi /etc/systemd/system/rc-local.service
..add the following to rc-local.service...
[Unit]
Description=/etc/rc.local
ConditionPathExists=/etc/rc.local
After=network.target

[Service]
Type=forking
ExecStart=/etc/rc.local start
TimeoutSec=0
StandardOutput=tty
RemainAfterExit=yes
SysVStartPriority=99

[Install]
WantedBy=multi-user.target

hotsoup@timewarpedapc:~/pinball_soup/time_warped $ sudo systemctl enable rc-local
Created symlink /etc/systemd/system/multi-user.target.wants/rc-local.service → /etc/systemd/system/rc-local.service.
hotsoup@timewarpedapc:~/pinball_soup/time_warped $ sudo systemctl start rc-local
hotsoup@timewarpedapc:~/pinball_soup/time_warped $ systemctl reboot
