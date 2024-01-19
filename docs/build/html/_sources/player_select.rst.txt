PlayerSelect Class
==================

.. py:class:: PlayerSelect

   A class representing the player selection screen in the game.

   .. attribute:: selected

      The index of the currently selected player.

   .. attribute:: finished

      A boolean indicating whether the player selection process is finished.

   .. attribute:: player_chosen

      A boolean indicating whether a player has been chosen.

   .. attribute:: selection_colour

      An integer representing the color of the player selection highlight.

   .. attribute:: background

      The background image for the player selection screen.

   .. attribute:: fonts

      A dictionary containing font objects for different text elements.

   .. method:: __init__()

      Initializes the PlayerSelect class.

   .. method:: progress(window)

      Updates and renders the player selection screen.

      :param window: The Pygame window surface.

   .. method:: finalise_selection(player)

      Finalizes the player selection by playing sound effects and setting the finished flag.

      :param player: The selected player.

   .. method:: normalise(v, low, high)

      Normalizes a value between a given range.

      :param v: The value to be normalized.
      :param low: The lower bound of the range.
      :param high: The upper bound of the range.

   Note: The PlayerSelect class relies on external constants and assets defined in the `GameSetting` class.

