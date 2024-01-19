Util Class
==========

.. py:class:: Util

   A utility class providing various static methods for common tasks.

   .. method:: try_quit(e)

      Handles quitting the game when the quit event or ESC key is triggered.

      :param e: The pygame event.

   .. method:: limit(v, low, high)

      Limits the value v within the specified range [low, high].

      :param v: The value to be limited.
      :param low: The lower bound of the range.
      :param high: The upper bound of the range.

      :return: The limited value.

   .. method:: render_text(text, window, font, color, position)

      Renders text on the window using the provided font, color, and position.

      :param text: The text to be rendered.
      :param window: The game window.
      :param font: The font for rendering the text.
      :param color: The color of the text.
      :param position: The position to render the text.

      :return: The rendered text surface.

   .. method:: middle(surface, x_offset=0, y_offset=0, x=-1, y=-1)

      Calculates the middle position for placing a surface on the screen.

      :param surface: The surface to be placed.
      :param x_offset: The x-offset from the middle.
      :param y_offset: The y-offset from the middle.
      :param x: The x-coordinate for a specific position.
      :param y: The y-coordinate for a specific position.

      :return: A tuple representing the calculated position.

