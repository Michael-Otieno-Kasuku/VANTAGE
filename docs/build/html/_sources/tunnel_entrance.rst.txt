TunnelEntrance Class
====================

.. py:class:: TunnelEntrance

   A class representing the entrance of a tunnel.

   .. attribute:: quantifier

      A factor used to determine the size of the tunnel entrance.

   .. attribute:: colour

      The color of the tunnel entrance.

   .. method:: __init__(colour)

      Initializes a TunnelEntrance.

      :param colour: The color of the tunnel entrance.

   .. method:: render(window, segment)

      Renders the tunnel entrance on the window.

      :param window: The Pygame window surface.
      :param segment: The game segment associated with the tunnel entrance.
