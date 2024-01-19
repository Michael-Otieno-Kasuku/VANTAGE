LevelGenerator Class
====================

.. py:class:: LevelGenerator

   A class for generating level segments for a game.

   .. method:: ease_in(a, b, p)

      Static method to calculate eased-in value between a and b based on parameter p.

   .. method:: ease_out(a, b, p)

      Static method to calculate eased-out value between a and b based on parameter p.

   .. method:: ease_in_out(a, b, p)

      Static method to calculate eased-in-out value between a and b based on parameter p.

   .. method:: add_corner(enter, hold, exit, curve, start_y=0, height=0)

      Static method to generate level segments for a corner.

   .. method:: add_hill(enter, hold, exit, height, start_y)

      Static method to generate level segments for a hill.

   .. method:: add_straight(length, y)

      Static method to generate level segments for a straight path.

   .. method:: last_y(segments)

      Static method to get the last y-coordinate from a list of level segments.

   .. method:: write(path, segments)

      Static method to write level segments to a CSV file.

   Example usage:

   .. code-block:: python

      # Import the LevelGenerator class
      from your_module import LevelGenerator

      # Example usage
      segments = LevelGenerator.add_corner(3, 2, 3, 0.5)
      LevelGenerator.write("path/to/file.csv", segments)

