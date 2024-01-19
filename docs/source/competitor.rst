Competitor Class
================

.. py:class:: Competitor

   A class representing a competitor in the game.

   .. attribute:: position

      The z-position of the competitor.

   .. attribute:: offset

      The offset of the competitor.

   .. attribute:: offset_y

      The y-offset of the competitor.

   .. attribute:: sprite

      The sprite information for the competitor.

   .. attribute:: speed

      The speed of the competitor.

   .. attribute:: engine_sfx

      The sound effect for the competitor's engine.

   .. method:: __init__(position, offset, name, speed)

      Initializes a Competitor.

      :param position: The z-position of the competitor.
      :param offset: The offset of the competitor.
      :param name: The name of the competitor's sprite.
      :param speed: The speed of the competitor.

   .. method:: travel(track_length)

      Updates the z-position of the competitor based on its speed.

      :param track_length: The length of the track.

   .. method:: play_engine(player_position)

      Plays or stops the engine sound based on the player's position.

      :param player_position: The z-position of the player.

   .. method:: path()

      Retrieves the image path for the competitor's sprite.

      :return: The image path as a pygame Surface.

   .. method:: __engine_volume(player_position)

      Calculates the volume of the engine sound based on the player's position.

      :param player_position: The z-position of the player.

      :return: The calculated volume.
