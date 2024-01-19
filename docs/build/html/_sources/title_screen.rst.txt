TitleScreen Class
=================

.. py:class:: TitleScreen

   A class representing the title screen of the game.

   .. attribute:: finished

      A boolean indicating whether the title screen is finished.

   .. attribute:: ready

      A boolean indicating whether the game is ready to start.

   .. attribute:: background

      The background image for the title screen.

   .. attribute:: logo_a

      The first part of the game logo.

   .. attribute:: logo_b

      The second part of the game logo.

   .. attribute:: bg_offset

      The offset of the background animation.

   .. attribute:: font

      The font for rendering text.

   .. attribute:: state

      The current state of the title screen (0, 1, or 2).

   .. attribute:: frame

      The frame counter for animation.

   .. attribute:: logo_a_off

      The x-offset of the first part of the logo.

   .. attribute:: logo_b_off

      The x-offset of the second part of the logo.

   .. method:: __init__()

      Initializes the TitleScreen class.

   .. method:: progress(window)

      Updates and renders the title screen.

      :param window: The Pygame window surface.

   .. method:: state_0_step(window)

      Performs the animation step for state 0.

      :param window: The Pygame window surface.

   .. method:: state_1_step(window)

      Performs the animation step for state 1.

      :param window: The Pygame window surface.

   .. method:: state_2_step(window)

      Performs the animation step for state 2.

      :param window: The Pygame window surface.

   .. method:: render_title(window)

      Renders the title text on the window.

   .. method:: render_press_start(window)

      Renders the "Press Start" text on the window.

