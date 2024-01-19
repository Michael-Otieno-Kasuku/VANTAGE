Background Class
================

.. py:class:: Background

   A class for handling background images with parallax scrolling in a game.

   .. attribute:: image

      The pygame Surface object representing the background image.

   .. attribute:: parallax_speed

      The parallax speed of the background.

   .. attribute:: y

      The y-coordinate position of the background.

   .. attribute:: width

      The width of the background image.

   .. attribute:: height

      The height of the background image.

   .. attribute:: curvature

      The curvature of the background, calculated based on the game dimensions.

   .. attribute:: scale_height

      A boolean indicating whether to scale the height of the background.

   .. attribute:: visible_height

      The visible height of the background when scaling is enabled.

   .. method:: __init__(name, parallax_speed, scale_height=False, convert=False)

      Initializes a Background object.

      :param name: The name of the background image.
      :param parallax_speed: The parallax speed of the background.
      :param scale_height: Whether to scale the height of the background.
      :param convert: Whether to convert the image.

   .. method:: step(curve, speed_percent)

      Updates the background position based on the curve and speed percentage.

      :param curve: The curve affecting the background.
      :param speed_percent: The percentage of speed to apply.

   .. method:: render(window)

      Renders the background on the given window.

      :param window: The game window to render the background on.

   Example usage:

   .. code-block:: python

      # Import the Background class
      from your_module import Background

      # Example usage
      background = Background("background_image", 2, scale_height=True)
      background.step(1.5, 0.8)
      background.render(game_window)

