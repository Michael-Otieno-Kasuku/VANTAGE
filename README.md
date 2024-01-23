# Vantage: An Arcade Car Racing Game

Written using Python 3.9.2 and Pygame 2.5.2 as a third year Computer Science Project.

### Playing

Ensure that you have [Python 3.x](https://www.python.org/) and [Pygame](http://www.pygame.org/download.shtml) installed, and then:

```
  $ ./vantage
```

Accelleration and steering is performed via the arrow keys. [ENTER] to start, [ESC] to kill the game in fullscreen mode.

Many in-game settings can be changed in `GameSetting Class`


### TODO
  
  * !Design 2nd and 3rd level properly
  * !Congratulations sequence when game is finished
  * !Package better for distribution (ship with Pygame?)
  * Rethink player checkpoint logic to fix "time left" bug in pause and make countdown easy to disable/enable.
    * Use current actual FPS to determine time left.
    * Move all time/checkpoint stuff into game (or maybe level?) and out of player.
  * Local highscore file outside of git
  * Engine sounds based on speed
  * Screech sound and sprite when hitting tunnel wall
  * Walls
  * Multiple roads with forks
  * Get Mel to create art for: Bonuses, Tunnel roof, Other players, Other levels
  * Random boxes that penalise time-left when hit
  * Random boxes that give player temporary speed boost
  * General refactor and Pythonify of sloppy code
