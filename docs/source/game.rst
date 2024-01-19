Game Class
===========

.. py:class:: Game

   A class representing the main game engine.

   .. attribute:: window

      The Pygame window.

   .. attribute:: clock

      The Pygame clock.

   .. attribute:: paused

      A boolean indicating whether the game is paused.

   .. attribute:: waiting

      A boolean indicating whether the game is waiting.

   .. attribute:: selected_player

      The index of the selected player.

   .. attribute:: player

      The player object.

   .. attribute:: level

      The current game level.

   .. attribute:: high_scores

      The high scores for the game.

   .. method:: __init__(window, clock)

      Initializes a Game.

      :param window: The Pygame window surface.
      :param clock: The Pygame clock.

   .. method:: play()

      Runs the main game loop.

   .. method:: wait()

      Displays the high scores and waits for player input.

   .. method:: __game_cycle()

      Executes a cycle of the game loop.

   .. method:: __pause_cycle()

      Executes a cycle when the game is paused.

   .. method:: __progress(screen, fps)

      Updates and renders the progress of a screen.

   .. method:: __title_screen()

      Displays the title screen.

   .. method:: __countdown(level_number)

      Displays the countdown screen for the start of a level.

   .. method:: __player_select()

      Displays the player select screen.

   .. method:: __credits_screen()

      Displays the credits screen.
