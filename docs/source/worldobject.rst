WorldObject Class
=================

.. py:class:: WorldObject

   A base class for game objects in the world.

   .. attribute:: rendered_area

      A list representing the rendered area of the object.

   .. attribute:: quantifier

      The quantifier for scaling dimensions.

   .. method:: __init__(quant=3)

      Initializes a WorldObject.

      :param quant: The quantifier for scaling dimensions.

   .. method:: non_renderable()

      Checks if the object is non-renderable.

      :return: True if the sprite path is None, False otherwise.

   .. method:: screen_dim(dimension, screen_pos)

      Calculates the screen dimension based on the world dimension and screen position.

      :param dimension: The dimension to be calculated ("width" or "height").
      :param screen_pos: The screen position.

      :return: The calculated screen dimension.

   .. method:: render(window, segment)

      Renders the object on the given window within the specified segment.

      :param window: The game window.
      :param segment: The segment to render the object on.
