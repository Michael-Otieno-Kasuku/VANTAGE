Sprite Class
============

.. py:class:: Sprite(WorldObject)

   A class representing a sprite in the game world.

   .. attribute:: offset

      The x-offset of the sprite.

   .. attribute:: offset_y

      The y-offset of the sprite.

   .. attribute:: sprite

      The sprite information for the object.

   .. attribute:: hit

      A boolean indicating whether the sprite has been hit.

   .. method:: __init__(name, x, y)

      Initializes a Sprite.

      :param name: The name of the sprite.
      :param x: The x-offset of the sprite.
      :param y: The y-offset of the sprite.

   .. method:: is_hooker()

      Checks if the sprite represents a "hooker".

      :return: True if the sprite is a "hooker," False otherwise.

   .. method:: is_speed_boost()

      Checks if the sprite represents a "speed boost."

      :return: True if the sprite is a "speed boost," False otherwise.

   .. method:: is_bonus()

      Checks if the sprite represents a "bonus."

      :return: True if the sprite is a "bonus," False otherwise.

   .. method:: path()

      Retrieves the image path for the sprite.

      :return: The image path as a pygame Surface.
