# Williams Jungle Lord Lamp Matrix

Sources: [ozzfest/research/raw/Williams Jungle Lord - Williams_Jungle_Lord_Tech_Chart.pdf](ozzfest/research/raw/Williams%20Jungle%20Lord%20-%20Williams_Jungle_Lord_Tech_Chart.pdf), [ozzfest/research/raw/handbook_page9_large_psm6.tsv](ozzfest/research/raw/handbook_page9_large_psm6.tsv), and the implemented device list in [ozzfest/config/config.yaml](ozzfest/config/config.yaml#L420-L518).

System 7 numbers count columns left-to-right and rows top-to-bottom. Column 1/Row 1 corresponds to lamp 01; Column 8/Row 8 corresponds to lamp 64. General illumination strings are powered through the main GI bus and are globally controlled by the GI relay coil (see c_gi_relay in [ozzfest/config/config.yaml](ozzfest/config/config.yaml#L294-L300)).

| No. | Row | Column | MPF ID | Description |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | l_shoot_again_backbox | Shoot Again (Backbox) |
| 2 | 1 | 2 | l_ball_in_play | Ball In Play |
| 3 | 1 | 3 | l_tilt | Tilt |
| 4 | 1 | 4 | l_game_over | Game Over |
| 5 | 1 | 5 | l_match | Match |
| 6 | 1 | 6 | l_high_score | High Score |
| 7 | 1 | 7 | l_multiball_timer | Multi-Ball Timer |
| 8 | 1 | 8 | l_right_magnet_1_bottom | Right Magnet Lamp #1 (Bottom) |
| 9 | 2 | 1 | l_right_magnet_2 | Right Magnet Lamp #2 |
| 10 | 2 | 2 | l_right_magnet_3 | Right Magnet Lamp #3 |
| 11 | 2 | 3 | l_right_magnet_4 | Right Magnet Lamp #4 |
| 12 | 2 | 4 | l_right_magnet_5_top | Right Magnet Lamp #5 (Top) |
| 13 | 2 | 5 | l_letter_l | Letter L |
| 14 | 2 | 6 | l_letter_o | Letter O |
| 15 | 2 | 7 | l_letter_r | Letter R |
| 16 | 2 | 8 | l_letter_d | Letter D |
| 17 | 3 | 1 | l_target_1 | Target 1 |
| 18 | 3 | 2 | l_target_2 | Target 2 |
| 19 | 3 | 3 | l_target_3 | Target 3 |
| 20 | 3 | 4 | l_rollover_4 | Rollover 4 |
| 21 | 3 | 5 | l_rollover_5 | Rollover 5 |
| 22 | 3 | 6 | l_left_drain_shield | Left Drain Shield |
| 23 | 3 | 7 | l_right_drain_shield | Right Drain Shield |
| 24 | 3 | 8 | l_minifield_illumination_24 | Mini-field Illumination (2 lamps) |
| 25 | 4 | 1 | l_right_threebank | Right 3-Bank |
| 26 | 4 | 2 | l_scoring_2x | 2X Scoring |
| 27 | 4 | 3 | l_keep_shooting_playfield | Keep Shooting (Playfield) |
| 28 | 4 | 4 | l_minifield_special | Mini-field Special |
| 29 | 4 | 5 | l_left_threebank | Left 3-Bank |
| 30 | 4 | 6 | l_loop_spots_letter | Loop Spots Letter |
| 31 | 4 | 7 | l_loop_spots_x_value | Loop Spots X-Value |
| 32 | 4 | 8 | l_minifield_illumination_32 | Mini-field Illumination |
| 33 | 5 | 1 | l_fivebank_arrow_1_left | 5-Bank #1 Arrow (Left) |
| 34 | 5 | 2 | l_fivebank_arrow_2 | 5-Bank #2 Arrow |
| 35 | 5 | 3 | l_fivebank_arrow_3 | 5-Bank #3 Arrow |
| 36 | 5 | 4 | l_fivebank_arrow_4 | 5-Bank #4 Arrow |
| 37 | 5 | 5 | l_fivebank_arrow_5_right | 5-Bank #5 Arrow (Right) |
| 38 | 5 | 6 | l_minifield_illumination_38 | Mini-field Illumination |
| 39 | 5 | 7 | l_left_magnet_1_bottom | Left Magnet Lamp #1 (Bottom) |
| 40 | 5 | 8 | l_left_magnet_2 | Left Magnet Lamp #2 |
| 41 | 6 | 1 | l_left_magnet_3 | Left Magnet Lamp #3 |
| 42 | 6 | 2 | l_left_magnet_4 | Left Magnet Lamp #4 |
| 43 | 6 | 3 | l_left_magnet_5_top | Left Magnet Lamp #5 (Top) |
| 44 | 6 | 4 | l_extra_kick_when_lit | Extra Kick When Lit |
| 45 | 6 | 5 | l_lock_lamps_pair | Lock Lamps (2 lamps) |
| 46 | 6 | 6 | l_double_trouble | Double-Trouble |
| 47 | 6 | 7 | l_minifield_illumination_47 | Mini-field Illumination |
| 48 | 6 | 8 | l_minifield_illumination_48 | Mini-field Illumination |
| 49 | 7 | 1 | l_bonus_1 | 1 Bonus |
| 50 | 7 | 2 | l_bonus_2 | 2 Bonus |
| 51 | 7 | 3 | l_bonus_3 | 3 Bonus |
| 52 | 7 | 4 | l_bonus_4 | 4 Bonus |
| 53 | 7 | 5 | l_bonus_5 | 5 Bonus |
| 54 | 7 | 6 | l_bonus_6 | 6 Bonus |
| 55 | 7 | 7 | l_bonus_7 | 7 Bonus |
| 56 | 7 | 8 | l_bonus_8 | 8 Bonus |
| 57 | 8 | 1 | l_bonus_9 | 9 Bonus |
| 58 | 8 | 2 | l_bonus_10 | 10 Bonus |
| 59 | 8 | 3 | l_bonus_20 | 20 Bonus |
| 60 | 8 | 4 | l_bonus_30 | 30 Bonus |
| 61 | 8 | 5 | l_bonus_multiplier_2x | Bonus Multiplier 2X |
| 62 | 8 | 6 | l_bonus_multiplier_3x | Bonus Multiplier 3X |
| 63 | 8 | 7 | l_bonus_multiplier_5x | Bonus Multiplier 5X |
| 64 | 8 | 8 | l_bonus_multiplier_10x | Bonus Multiplier 10X |
