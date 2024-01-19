TunnelInside Class
==================

.. py:class:: TunnelInside

   A class representing the inside of a tunnel.

   .. attribute:: quantifier

      A factor used to determine the size of the tunnel inside.

   .. method:: __init__()

      Initializes a TunnelInside.

   .. method:: render(window, coords, clip, coverage)

      Renders the inside of the tunnel on the window.

      :param window: The Pygame window surface.
      :param coords: Coordinates of the tunnel.
      :param clip: Clipping information for sprites.
      :param coverage: List of coverage information.

