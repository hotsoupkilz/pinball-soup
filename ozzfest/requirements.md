machine setup (hardware and software)
- this pinball machine is a fan-inspired homebrew machine to be used at my house with no monetary prospects
- each folder within pinball-soup contains the code to run a physical pinball machine using the mission pinball (mpf) software framework. Each folder (ozzy, ozzfest, time_warped) are all distinct machines that run independently on different hardware as of 
- only 0.80.x or newer and dev branches from mpf repo should be considered as godot is needed for all machines in pinball-soup
- the Arduino Pinball Controller (APC) is the Hardware Platform used for the ozzy and time_warped machines
- the Mission Pinball tutorial (https://missionpinball.org/latest/tutorial/) and its repos are the preferred reference for new machine scaffolds; clone only if helpful, otherwise mirror their structure with ozzy as the fallback baseline
- virtualenv required to run mpf commands, and virtualenv must have mpf installed in it initially via `pip install mpf --pre`



General gameplay rules
- theme is "concertgoer journey at ozzfest"
- at the beginning of game, player will select a band to start with via carousel. each band is a mode. 
- bands are dio, meatloaf, ozzy osborne, black sabbath, rob zombie an rivers of nihil
- getting through all band modes brings player into wizard mode. black sabbath is wizard mode band
- each band mode is completed when the all "LORD" lights have been lit in bagatelle portion of playfield. LORD lights are lit by either ball running over corresponding switch or dropping all targets in either of the 3bank drop target banks within 10 seconds. if all three targets in a threebank have not been completed within 10 seconds, the bank resets
- ball landing in lower eject hole enables bagatelle minigame. in this mode, after 3 seonds the miniball kicker shoots a mini ball over one of the LORD rollover switches.
- if band mode has been completed ball langing in upper eject hole enables player to select next band mode. if current band mode has not been completed, bagatelle minigame is enabled like lower eject hole
- dropping a single target in 3bank activates ability to use magna-save for that side once. up to 5 magnasaves can be "stored" per side, and are used when player presses corresponding Magnet Button on cabinet.
- left magnasave is activated via Left Magnet Button (switch 49) right magnasave is activated via Right Magnet Button (switch 50). magnet is magnetized while holding button down and releases if button is not being pressed
- ball rolling over switch 24 first then switch 25 within 1 second enables "Drain Shield" for the remainder of the ball. Drain Shield switches from left to right side if a slingshot is hit. left drain shield (light 22) will put ball back in play one time if left outlane switch (switch 22) is hit. Right Drain Shield (light 23) will put ball back in play one time if right outlane switch (switch 23) is hit. If player hits Drain Shield switch comination a second time, on same ball both Drain Shields are activated


Base Scoring:
- slingshots: 10
- threebank single target: 20
- threebank completion: 500
- LORD switches: 50
- 1-5 Targets: 100
- outlanes: 1000
- Upper eject hole: 500
- Lower eject hole: 250


Band mode rules
- TODO


Wizard modes
- TODO