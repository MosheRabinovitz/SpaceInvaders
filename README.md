# python_course

# Space invaders

In short:
This program contains an extended implementation of the "Space Invaders" game - including several levels of increasing difficulty and a changing background sound that accompanies the game.

In length :
The program contains the well known game "Space Invaders"; The player controls a spaceship that can move left or right by pressing the arrow keys, and must shoot and destroy the aliens invading from space before they reach the bottom.
As they move, the aliens randomly fire timed shots towards the spaceship, with the player having a limited number of 'lives' to lose (accumulated throughout the levels) until the player is finally eliminated and the game ends.
Bonus: once every ten seconds the alien-mothership passes by at the top of the screen. Destroying it earns the player an additional high score.

Throughout the game, the following data is displayed in the upper left part of the screen: 
1. the current level.
2. The time passed since the player started the current level. 
3. The score the player has earned. 
4. The number of 'lives' he has left.
 
Levels:
The game includes 4 levels of increasing difficulty, with each levele the following is being updated and changed.
1. The speed of movement of the invading aliens. 
2. their rate of descent.
3. the background image. 
4. background music. 
At the end of each level, a praise message will appear for the player (which can be skipped by pressing the 'Enter' key), and then an announcement of the next level (which can be skipped by pressing the 'Space' key).

Score:
The score for each destroyed alien is given according to its height 10, 20, 25, 40. For the destruction of the alien-mothership, the player will earn a random number ranging from 50 to 200 points. The score is accumulated from level to level.

Remarks:
Pressing the P key will pause the game. The game can be resumed by pressing 'Enter'.
Also, there is a 'back door' in the game to move between levels with the press on the 'Left shift' key together with 'Left control' key.

Note: The game is built using the Pygame module of Python. If the library is not installed on your computer, it must be installed before running the program. 
