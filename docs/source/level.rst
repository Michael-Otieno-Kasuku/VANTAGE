Level Class
===========

.. py:class:: Level

   A class representing a game level.

   .. attribute:: name

      The name of the level.

   .. attribute:: slug

      The unique identifier (slug) of the level.

   .. attribute:: song

      The background music for the level.

   .. attribute:: laps

      The number of laps in the level.

   .. attribute:: backgrounds

      List of background images for the level.

   .. attribute:: palettes

      The color palettes for the level.

   .. attribute:: finished

      A boolean indicating whether the level is finished.

   .. attribute:: segments

      List of game segments in the level.

   .. attribute:: competitors

      List of competitor objects in the level.

   .. method:: __init__(details)

      Initializes a Level.

      :param details: Details about the level.

   .. method:: build()

      Builds the level by reading track and sprite information.

   .. method:: add_segment(curve, start_y=0, end_y=0)

      Adds a game segment to the level.

      :param curve: The curvature of the segment.
      :param start_y: The starting y-coordinate of the segment.
      :param end_y: The ending y-coordinate of the segment.

   .. method:: add_sprite(segment, name, x, y=0.0)

      Adds a sprite to a specific game segment.

      :param segment: The game segment to which the sprite is added.
      :param name: The name of the sprite.
      :param x: The x-coordinate of the sprite.
      :param y: The y-coordinate of the sprite.

   .. method:: add_polygon(segment, klass, when="pre", args=[])

      Adds a polygon to a game segment.

      :param segment: The game segment to which the polygon is added.
      :param klass: The class of the polygon.
      :param when: The timing of the polygon (either "pre" or "post").
      :param args: Additional arguments for the polygon.

   .. method:: insert_bonuses()

      Inserts bonus sprites into random segments of the level.

   .. method:: add_speed_boost(position, offset)

      Adds speed boost sprites to the level.

      :param position: The position of the speed boost.
      :param offset: The offset of the speed boost.

   .. method:: add_competitor(position, offset, name, speed)

      Adds a competitor to the level.

      :param position: The position of the competitor.
      :param offset: The offset of the competitor.
      :param name: The name of the competitor.
      :param speed: The speed of the competitor.

   .. method:: add_tunnel(start, end)

      Adds a tunnel to the level.

      :param start: The starting index of the tunnel.
      :param end: The ending index of the tunnel.

   .. method:: track_length()

      Calculates the total length of the track.

   .. method:: find_segment(position)

      Finds the game segment at a given position.

      :param position: The position to find the segment for.

   .. method:: offset_segment(i)

      Returns the game segment at the specified offset.
