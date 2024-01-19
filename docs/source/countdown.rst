CountDown Class
===============

.. py:class:: CountDown

   A class for managing countdowns in the game.

   .. attribute:: level_number

      The number of the current level.

   .. attribute:: level_name

      The name of the current level.

   .. attribute:: remaining

      The remaining time in the countdown.

   .. attribute:: finished

      A flag indicating if the countdown has finished.

   .. attribute:: text_font

      The font for rendering text.

   .. attribute:: cd_font

      The font for rendering the countdown text.

   .. method:: __init__(level_number, level_name)

      Initializes a CountDown.

      :param level_number: The number of the current level.
      :param level_name: The name of the current level.

   .. method:: progress(window)

      Progresses the countdown and renders the countdown text on the window.

      :param window: The game window.
