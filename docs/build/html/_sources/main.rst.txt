Project proposal
================

SRS
===

SDS
===

vantage module
==============
It contains all the classes used to develop VANTAGE(An Arcade Car Racing Game developed using PyGame).

Here are all the python ``libraries`` and ``modules`` used in this project.

.. code-block:: python
    
    import math
    import csv
    from pygame import Color
    import os
    import pygame
    import sys
    from pygame.locals import *
    from pygame.font import Font
    import json
    import datetime as dt
    from enum import Enum
    import random

1. LevelGenerator class
-----------------------  
Contains the following static helper functions for generating the level files.

.. py:function:: ease_in(a , b, p):

    Eases into a value between a and b using a quadratic easing function.

    :param a: Starting value.
    :type a: float
    :param b: Ending value.
    :type b: float
    :param p: Progress between 0 and 1.
    :type p: float
    :return: Eased value.
    :rtype: float




.. py:function:: ease_out(a, b, p):

    Eases into and out of a value between a and b using a cosine easing function.

    :param a: Starting value.
    :type a: float
    :param b: Ending value.
    :type b: float
    :param p: Progress value between 0 and 1.
    :type p: float
    :return: Eased value.
    :rtype: float

.. py:function:: ease_in_out(a, b, p):

    Eases into and out of a value between a and b using a cosine easing function.

    :param a: Starting value.
    :type a: float
    :param b: Ending value.
    :type b: float
    :param p: Progress value between 0 and 1.
    :type p: float
    :return: Eased value.
    :rtype: float
    
.. py:function:: add_corner(enter, hold, exit, curve, start_y=0, height=0):

    Generate a series of corner segments with specified parameters.

    :param enter: Number of segments to ease into the corner.
    :type enter: int
    :param hold: Number of segments to hold the corner.
    :type hold: int
    :param exit: Number of segments to ease out of the corner.
    :type exit: int
    :param curve: Corner curvature.
    :type curve: float
    :param start_y: Starting y-coordinate.
    :type start_y: float
    :param height: Peak height of the corner.
    :type height: float
    :return: List of corner segments.
    :rtype: list

.. py:function:: add_hill(enter,hold,exit,height,start_y):

    Generates a series of hill segments with specified parameters.
    
    :param enter: Number of segments to ease into the hill.
    :type enter: int
    :param hold: Number of segments to hold the hill.
    :type hold: int
    :param exit: Number of segments to ease out of the hill.
    :type exit: int
    :param height: Peak height of the hill segment.
    :type height: float
    :param start_y: Starting y-coordinate.
    :type start_y: float
    :return: List of hill segments.
    :rtype: list
    
.. py:function:: straight(length,y):

    Generates a series of straight segments.
    
    :param length: Length of the straight segment.
    :type length: int
    :param y: Y-coordinate for the straight segment.
    :type y: float
    :return: List of straight segments.
    :rtype: list
    
.. py:function:: last_y(segments):

    Generates the Y-Coordinate of the last fragment.
    
    :param segments: List of segments.
    :type segments: list
    :returns: Y-coordinate of the last segment.
    :rtype: float
    
.. py:function:: write(path, segments):

    Writes the segments to a CSV file of the specified path.
    
    :param path: File path of the CSV file.
    :type path: str
    :param segments: List of segments to write to the file.
    :type segments: list
    :returns: Nothing.
    :rtype: None
    
2. Melbourne class
------------------
Generates track segments for the Melbourne level and writes them to a CSV file.

This class includes straight segments, hills, corners, and writes the resulting track data to a CSV file for use in the game.

**Segments:**

- Straight segments

- Hills with varying parameters (height, length)

- Corners with different radii and banking angles.

**Usage:**
Invoke
:py:func:`Melbourne.create()` to generate and save the track segments for the Melbourne Level.

**Output:**
The generated track segments are saved to a CSV file  ``assets/tracks/melbourne.csv``.

**Note:**
This class uses the static methods of the 
:py:class:`LevelGenerator` class for track segment generation.

.. py:function:: create():

    Generates track segments for the Melbourne level and writes them to a CSV file.

3. GoldCoast class
------------------
Generate track segments for the Goldcoast level and store them in a CSV file.

    This class includes straight segments, corners, hills, and a combination of these to form
    a diverse and challenging track for the game.

    **Segments:**
    
    - Straight segments of varying lengths
    
    - Corners of different radii, banking angles, and directions.
    
    - Hills with varying parameters (height, length)

    **Usage:**
    An object of this class is used to generate the track segments for level two.

    **Output:**
    The generated track segments are saved to a CSV file  ``assets/tracks/goldcoast.csv``

    **Note:**
    This class makes use of the :py:class:`LevelGenerator` class for track segment generation.
    
    .. py:function:: create():
        
        Generate track segments for the Goldcoast level and store them in a CSV file.

        This method creates a series of track segments using the LevelGenerator class and saves
        the resulting track data to a CSV file ``assets/tracks/goldcoast``.

        :return: None

4. GameSetting class
--------------------
Contains all the constants used in the game.

5. Background class
-------------------
Represents a single scrollable background in a level.

    **Attributes:**
    
    - `image` (pygame.Surface): The background image.
    
    - `parallax_speed` (float): The speed at which the background scrolls relative to the player's movement.
    
    - `y` (int): The vertical position of the background.
    
    - `width` (int): The width of the background image.
    
    - `height` (int): The height of the background image.
    
    - `curvature` (float): The curvature of the background based on the difference between its width and the screen width.
    
    - `scale_height` (bool): If True, scales the height of the background to fill the visible area.
    
    - `visible_height` (int): The height of the visible area to be filled when scaling is turned on.
    
    .. py:function:: __init__(name, parallax_speed, scale_height=False, convert=False):
    
        Initializes a Background object.

        **Parameters:**
        
        - `name` (str): The filename (without extension) of the background image.
        
        - `parallax_speed` (float): The speed at which the background scrolls relative to the player's movement.
        
        - `scale_height` (bool): If True, scales the height of the background to fill the visible area.
        
        - `convert` (bool): If True, converts the image to the same pixel format as the display surface.
     
     .. py:function:: step(curve, speed_percent):
     
        Moves the background one step to simulate turning.

        **Parameters:**
        
        - `curve` (float): The curvature of the road.
        
        - `speed_percent` (float): The percentage of the player's speed.

        **Returns:**
        
        None
        
     .. py:function:: render(window):
     
        Draws the image to the window.

        **Parameters:**
        
        - `window` (pygame.Surface): The surface to draw the background on.

        **Returns:**
        
        None
     
6. Util class
-------------
    Contains helper methods that are used to control the game.

    .. py:function:: try_quit(e):
    
        Quit the game if a QUIT event is detected or if the ESC key is pressed in fullscreen mode.

        **Parameters:**
        
        - `e` (pygame.event.Event): The event object.
        
    .. py:function:: limit(v, low, high):
    
        Returns v, limited to the specified low/high threshold.

        **Parameters:**
        
        - `v`: The value to be limited.
        
        - `low`: The lower threshold.
        
        - `high`: The upper threshold.

        **Returns:**
        
        int: The limited value.
    
    .. py:function:: render_text(text, window, font, color, position):
    
          Renders a font and blits it to the given window.

        **Parameters:**
        
        - `text` (str): The text to render.
        
        - `window` (pygame.Surface): The window surface to render on.
        
        - `font` (pygame.font.Font): The font to use for rendering.
        
        - `color` (tuple): The RGB color tuple for the text.
        
        - `position` (tuple): The (x, y) coordinates to blit the text.

        **Returns:**
        
        pygame.Surface: The rendered text surface.
        
    .. py:function:: middle(surface, x_offset=0, y_offset=0, x=-1, y=-1):
    
        Returns a tuple of X,Y coordinates that represents the center position for the given surface.
        x_offset and y_offset will offset the appropriate axis by N pixels.
        Passing in a value for x or y will override the calculated value.

        **Parameters:**
        
        - `surface` (pygame.Surface): The surface for which to calculate the center position.
        
        - `x_offset` (int): The offset to apply to the X-axis.
        
        - `y_offset` (int): The offset to apply to the Y-axis.
        
        - `x` (int): The overridden X-coordinate value.
        
        - `y` (int): The overridden Y-coordinate value.

        **Returns:**
        
        tuple: The (x, y) coordinates representing the center position.

7. WorldObject class
--------------------
Represents a scalable object in the game world.

    **Attributes:**
    
    - `quantifier` (int): A factor determining the dimensions of the world object.
    
    - `rendered_area` (list): A list containing the rendered area coordinates [start, end].

    **Methods:**
    
    - `__init__(quant=3)`: Initializes a WorldObject instance with a quantifier factor.
    
    - `non_renderable()`: Checks if the object is renderable.
    
    - `screen_dim(dimension, screen_pos)`: Computes the dimension of the object on the screen.
    
    - `render(window, segment)`: Renders the object to the window with appropriate scaling and clipping.

    **Parameters:**
    
    - `quant` (int): An optional parameter to set the quantifier factor during initialization.
    
    .. py:function:: __init__(quant=3):
    
        Initializes a WorldObject instance with a quantifier factor.

        **Parameters:**
        
        - `quant` (int): An optional parameter to set the quantifier factor during initialization.
        
     .. py:function:: non_renderable():
     
        Checks if the object is renderable.

        **Returns:**
        
        bool: True if the object is not renderable, False otherwise.
     
     .. py:function:: screen_dim(dimension, screen_pos):
     
        Computes the dimension of the object on the screen.

        **Parameters:**
        
        - `dimension` (str): The dimension to compute ("width" or "height").
        
        - `screen_pos` (float): The screen position factor.

        **Returns:**
        
        int: The computed dimension.
     
     .. py:function:: render(window, segment):
     
        Renders the object to the window with appropriate scaling and clipping.

        **Parameters:**
        
        - `window` (pygame.Surface): The window surface to render on.
        
        - `segment` (Segment): The segment representing the portion of the road.

        **Returns:**
        
        None
     
8. Competitor class
-------------------
Represents a single competitor car in a level.

    **Attributes:**
    
    - `position` (float): The current Z position of the competitor on the track.
    
    - `offset` (float): The horizontal offset of the competitor on the track.
    
    - `offset_y` (float): The vertical offset of the competitor on the screen.
    
    - `sprite` (dict): Information about the competitor's sprite, including the file path.
    
    - `speed` (float): The speed of the competitor.
    
    - `engine_sfx` (pygame.mixer.Sound): The sound effect for the competitor's engine.

    **Methods:**
    
    - `__init__(self, position, offset, name, speed)`: Initializes a Competitor object.
    
    - `travel(self, track_length)`: Updates the Z position of the competitor based on its speed.
    
    - `play_engine(self, player_position)`: Plays or stops the engine sound based on the distance from the player.
    
    - `path(self)`: Returns the image of the competitor.
    
    - `__engine_volume(self, player_position)`: Returns a value between 0.0 and 1.0 indicating the engine volume from the player's perspective.

    **Parameters:**
    
    - `position` (float): The starting Z position of the competitor on the track.
    
    - `offset` (float): The horizontal offset of the competitor on the track.
    
    - `name` (str): The name of the competitor's sprite.
    
    - `speed` (float): The speed of the competitor.
    
    .. py:function:: __init__(position, offset, name, speed):
        
        Initializes a Competitor object.

        **Parameters:**
        
        - `position` (float): The starting Z position of the competitor on the track.
        
        - `offset` (float): The horizontal offset of the competitor on the track.
        
        - `name` (str): The name of the competitor's sprite.
        
        - `speed` (float): The speed of the competitor.
        
    .. py:function:: travel(track_length):
        
        Updates the Z position of the competitor based on its speed.

        **Parameters:**
        
        - `track_length` (float): The total length of the track.

        **Returns:**
        
        None
        
    .. py:function:: play_engine(player_position):
    
        Plays or stops the engine sound based on the distance from the player.

        **Parameters:**
        
        - `player_position` (float): The Z position of the player on the track.

        **Returns:**
        
        None
        
    .. py:function:: path():
    
        Returns the image of the competitor.

        **Parameters:**
        
        None

        **Returns:**
        
        pygame.Surface: The image of the competitor.
        
    .. py:function:: __engine_volume(player_position):
    
        Returns a value between 0.0 and 1.0 indicating the engine volume from the player's perspective.

        **Parameters:**
        
        - `player_position` (float): The Z position of the player on the track.

        **Returns:**
        
        float: The engine volume.
        
9. CountDown class
------------------
Plays a countdown before the level starts.

    **Attributes:**
    
    - `level_number` (int): The number of the current level.
    
    - `level_name` (str): The name of the current level.
    
    - `remaining` (int): The remaining time in the countdown.
    
    - `finished` (bool): Indicates if the countdown has finished.
    
    - `text_font` (pygame.font.Font): The font for regular text.
    
    - `cd_font` (pygame.font.Font): The font for the countdown text.

    **Methods:**
    
    - `__init__(self, level_number, level_name)`: Initializes a CountDown object.
    
    - `progress(self, window)`: Displays and progresses the countdown.

    **Parameters:**
    
    - `level_number` (int): The number of the current level.
    
    - `level_name` (str): The name of the current level.
    
    .. py:function:: __init__(level_number, level_name):
    
        Initializes a CountDown object.

        **Parameters:**
        
        - `level_number` (int): The number of the current level.
        
        - `level_name` (str): The name of the current level.
        
    .. py:function:: progress(window):
    
        Displays and progresses the countdown.

        **Parameters:**
        
        - `window` (pygame.Surface): The window surface to render the countdown.

        **Returns:**
        
        None
        
10. Credit class
----------------
Plays the credits sequence at the end of the game.

    **Attributes:**
    
    - `finished` (bool): Indicates if the credits sequence has finished.

    **Methods:**
    
    - `__init__(self)`: Initializes a Credits object.
    
    - `progress(self, window)`: Progresses the credits sequence.
    
    .. py:function:: __init__():
    
        Initializes a Credits object.
        
    .. py::function:: progress(window):
    
        Progresses the credits sequence.

        **Parameters:**
        
        - `window` (pygame.Surface): The window surface to render the credits.

        **Returns:**
        
        None

11. HighScore class
-------------------
Wrapper over the high scores file.

    **Attributes:**
    
    - `high_scores` (list): List of high scores, each represented as a pair of date and score.

    **Methods:**
    
    - `__init__(self)`: Initializes a HighScores object, reading and sorting high scores from the file.
    
    - `is_high_score(self, score)`: Checks if the given score qualifies to be on the high score list.
    
    - `minimum_score(self)`: Returns the minimum score required to be on the high score list.
    
    - `add_high_score(self, score)`: Adds the given score to high scores, replacing the lowest score if necessary.
    
    .. py:function:: __init__():
    
        Initializes a HighScore object, reading and sorting high scores from the file.

        **Returns:**
        
        None
        
     .. py:function:: is_high_score(score):
     
        Checks if the given score qualifies to be on the high score list.

        **Parameters:**
        
        - `score` (int): The score to be checked.

        **Returns:**
        
        bool: True if the score is a high score, False otherwise.
        
    .. py:function:: minimum_score():
    
        Returns the minimum score required to be on the high score list.

        **Returns:**
        
        int: The minimum score.
        
    .. py:function:: add_high_score(score):
    
        Adds the given score to high scores, replacing the lowest score if necessary.

        **Parameters:**
        
        - `score` (int): The score to be added.

        **Returns:**
        
        None
        
    .. py:function:: __sort():
    
        Sorts the high scores list in descending order based on scores.

        **Returns:**
        
        None
        
    .. py:function:: __write_high_scores():
    
        Writes the high scores to the file in JSON format.

        **Returns:**
        
        None
    
    .. py:function:: __read_high_scores():
    
        Reads the high scores from the file in JSON format.

        **Returns:**
        
        list: List of high scores, each represented as a pair of date and score.
        
     .. py: function:: __scores_only():
     
        Extracts and returns the scores from the list of high scores.

        **Returns:**
        
        list: List of scores.
        
12. PlayerStatus class
----------------------
Represents the current status of the player.

13. Player class
----------------
Represents the player in the game world.

    **Attributes:**
    
    - `settings` (dict): Player settings based on the selected player.
    
    - `points` (float): Current points accumulated by the player.
    
    - `high_score` (float): Highest score achieved by the player.
    
    - `next_milestone` (float): Points needed for the next milestone.
    
    - `status` (PlayerStatus): Current status of the player (alive, game over, or level over).
    
    - `level_over_lag` (int): Counter for the level completion overlay display.
    
    - `x` (float): X-coordinate of the player's position.
    
    - `y` (float): Y-coordinate of the player's position.
    
    - `position` (float): Current position of the player on the track.
    
    - `lap_percent` (float): Percentage of the current lap completed.
    
    - `direction` (int): Steering direction (-1 for left, 1 for right).
    
    - `acceleration` (float): Current acceleration factor.
    
    - `speed` (float): Current speed of the player.
    
    - `speed_boost` (float): Speed boost factor.
    
    - `animation_frame` (int): Current frame for player animation.
    
    - `new_lap` (bool): Flag indicating if a new lap has started.
    
    - `lap_bonus` (float): Bonus time awarded for completing laps.
    
    - `time_bonus` (float): Bonus points awarded for remaining time.
    
    - `lap` (int): Current lap number.
    
    - `total_laps` (int): Total number of laps in the level.
    
    - `lap_time` (float): Time taken to complete the current lap.
    
    - `lap_margin` (float): Difference between the fastest lap and the current lap time.
    
    - `blood_alpha` (int): Alpha value for blood splatter overlay.
    
    - `in_tunnel` (bool): Flag indicating if the player is in a tunnel.
    
    - `fastest_lap` (float): Fastest lap time achieved by the player.
    
    - `checkpoint` (float): Time interval for checkpoints.
    
    - `time_left` (float): Remaining time for the current lap.
    
    - `last_checkpoint` (datetime): Timestamp of the last checkpoint.
    
    - `crashed` (bool): Flag indicating if the player has crashed.
    
    - `special_text` (list): Information about special text to display.
    
    - `screech_sfx` (pygame.mixer.Sound): Sound object for screech effect.

    **Methods:**
    
    - `__init__(self, high_score, selected_player)`: Initializes a Player object.
    
    - `reset(total_laps=GameSetting.LAPS_PER_LEVEL)`: Resets player variables for the start of a new level.
    
    - `steer(segment)`: Updates x to simulate steering.
    
    - `climb(segment)`: Updates y to simulate hill and valley ascension.
    
    - `detect_collisions(segment)`: Detects and handles player collisions with sprites.
    
    - `render(window, segment)`: Renders the player sprite to the given surface.
    
    - `render_hud(window)`: Renders a Head-Up display on the active window.
    
    - `render_blood(window)`: Renders a blood splatter if the player has killed someone.
    
    - `accelerate()`: Updates speed at the appropriate acceleration level.
    
    - `travel(track_length, window)`: Updates position, reflecting how far the player has traveled since the last frame.
    
    - `set_acceleration(keys)`: Updates the acceleration factor depending on world conditions.
    
    - `set_direction(keys)`: Updates the direction the player is going, accepts a key-map.
    
    - `speed_percent()`: Calculates the current speed as a percentage of the top speed.
    
    - `direction_speed()`: Calculates the speed based on the direction and player's speed percentage.
    
    - `segment_percent()`: Returns a value between 0 and 1 indicating how far through the current segment the player is.
    
    - `handle_crash()`: Proceeds the player through the crash state.
    
    - `finished()`: Checks if the level completion overlay display is finished.
    
    - `alive()`: Checks if the player is alive.
    
    - `__set_special_text(text, time)`: Defines the special text to show and for how long.
    
    - `__collided_with_sprite(sprite)`: Checks if the player has collided with a sprite.
    
    - `__circular_orbit(center, radius, t)`: Returns the X/Y coordinate for a given time in a circular orbit.
    
    - `__set_checkpoint()`: Sets the checkpoint timestamp to the current time.
    
    - `__hit_hooker()`: Handles collisions with hooker sprites.
    
    - `__hit_bonus()`: Handles collisions with bonus sprites.
    
    - `__hit_speed_boost()`: Handles collisions with speed boost sprites.
    
    - `__hit_world_object()`: Handles collisions with world object sprites.
    
    - `__hit_competitor()`: Handles collisions with competitor sprites.
    
    - `__fastest_lap()`: Checks if the current lap is the fastest lap.
    
    - `__run_screech()`: Starts the screech sound effect.
    
    - `__stop_screech()`: Stops the screech sound effect.
    
    - `__game_over_overlay(window)`: Displays the game over overlay on the window.
    
    - `__level_over_overlay(window)`: Displays the level completion overlay on the window.

14. PlayerSelect class
----------------------
Manages the player selection screen.

    **Attributes:**
    
    - `selected` (int): Index of the currently selected player.
    
    - `finished` (bool): Indicates whether the player selection process is finished.
    
    - `player_chosen` (bool): Indicates whether a player has been chosen.
    
    - `selection_colour` (int): Index to alternate the color of the player selection box.
    
    - `background` (pygame.Surface): Background image for the player selection screen.
    
    - `fonts` (dict): Dictionary containing fonts for different text elements.

    **Methods:**
    
    - `__init__(self)`: Initializes a PlayerSelect object.
    
    - `progress(self, window)`: Displays and progresses through the player selection screen.
    
    - `finalise_selection(self, player)`: Finalizes the player selection with sound effects.
    
    - `normalise(self, v, low, high)`: Normalizes a value within a given range.
    
    .. py:function:: __init__():
    
        Initializes a PlayerSelect object.
        
    .. py:function:: progress(window):
    
        Displays and progresses through the player selection screen.

        **Args:**
        
        - `window` (pygame.Surface): The surface to display the player selection on.
        
    .. py:function:: finalise_selection(window):
     
        Finalizes the player selection with sound effects.

        **Args:**
        
        - `player`: The selected player.
        
    .. py:function:: normalise(v, low, high):
     
        Normalizes a value within a given range.

        **Args:**
        
        - `v`: The value to normalize.
        
        - `low`: The lower bound of the range.
        
        - `high`: The upper bound of the range.

        **Returns:**
        
        - Normalized value.

15. Segment class
-----------------
Represents a single segment in a level.

    **Attributes:**
    
    - `index` (int): Index of the segment within the level.
    
    - `curve` (float): Curvature factor of the segment.
    
    - `sprites` (list): List of sprites present in the segment.
    
    - `competitors` (list): List of competitor objects present in the segment.
    
    - `pre_polygons` (list): List of polygons rendered before the sprites.
    
    - `post_polygons` (list): List of polygons rendered after the sprites.
    
    - `clip` (list): Clipping information for rendering.
    
    - `in_tunnel` (bool): Indicates whether the segment is inside a tunnel.
    
    - `tunnel_end` (bool): Indicates whether the segment marks the end of a tunnel.
    
    - `speed_boost` (bool): Indicates whether the segment contains a speed boost.
    
    - `palette` (dict): Color palette for rendering the segment.
    
    - `top` (dict): Information about the top line of the segment.
    
    - `bottom` (dict): Information about the bottom line of the segment.

    **Methods:**
    
    - `__init__(self, palette, index, curve, start_y, end_y)`: Initializes a Segment object.
    
    - `project(self, camera_x, curve, curve_delta, position, player_y)`: Projects the segment lines to 2D coordinates.
    
    - `should_ignore(self, segment)`: Checks if the segment should be ignored during rendering.
    
    - `render_grass(self, window)`: Renders the grass for the segment.
    
    - `render_road(self, window)`: Renders the road for the segment.
    
    - `render_polygons(self, window, full_clip)`: Renders polygons/shapes for the segment.
    
    - `render_world_objects(self, window)`: Renders sprites/competitors for the segment.
    
    - `render_tunnel_roof(self, window, highest_y)`: Renders the tunnel roof.
    
    - `render_left_tunnel(self, window)`: Renders the left tunnel wall.
    
    - `render_right_tunnel(self, window)`: Renders the right tunnel wall.
    
    - `remove_sprite(self, sprite)`: Removes a sprite permanently from the segment.
    
    .. py:function:: project(camera_x, curve, curve_delta, position, player_y):
    
        Modifies the segment lines in place, projecting them to 2D coordinates.

        **Args:**
        
        - `camera_x`: Current camera X position.
        
        - `curve`: Current curve factor.
        
        - `curve_delta`: Delta change in curve.
        
        - `position`: Current position.
        
        - `player_y`: Player's Y position.
        
    .. py:function:: should_ignore(segment):
     
        Returns true if this segment will be projected behind a hill, or behind us, etc.

        **Args:**
        
        - `segment`: The segment to compare with.

        **Returns:**
        
        - True if the segment should be ignored; otherwise, False.
        
    .. py:function:: render_grass(window):
    
        Renders the grass for this segment to the given surface.

        **Args:**
        
        - `window` (pygame.Surface): The surface to render the grass on.
        
    .. py:function:: render_road(window):
    
        Renders the road for this segment to the given surface.

        **Args:**
        
        - `window` (pygame.Surface): The surface to render the road on.
        
    .. py:function:: render_polygons(window, full_clip):
    
        Renders the polygons/shapes (if any) for this segment to the given surface.
        These are rendered after the track, but before the sprites.

        **Args:**
        
        - `window` (pygame.Surface): The surface to render the polygons on.
        
        - `full_clip` (bool): Whether to apply full clipping.
        
    .. py:function:: render_world_objects(window):
    
        Renders the sprites/competitors (if any) for this segment to the given surface.

        **Args:**
        
        - `window` (pygame.Surface): The surface to render the sprites on.
        
    .. py:function:: render_tunnel_roof(window, highest_y):
    
        Renders the tunnel roof, accounting for the exit hole if it's visible.

        **Args:**
        
        - `window` (pygame.Surface): The surface to render the tunnel roof on.
        
        - `highest_y`: The highest Y position.
        
    .. py:function:: render_left_tunnel(window):
    
        Renders the left tunnel wall.

        **Args:**
        
        - `window` (pygame.Surface): The surface to render the left tunnel wall on.
        
    .. py:function:: render_right_tunnel(window):
    
        Renders the right tunnel wall.

        **Args:**
        
        - `window` (pygame.Surface): The surface to render the right tunnel wall on.    
        
    .. py:function:: remove_sprite(sprite):
    
        Permanently removes the given sprite from this segment.

        **Args:**
        
        - `sprite`: The sprite to be removed.
                    
    .. py:function:: __project_line(line, camera_x, camera_z, player_y):
    
        Projects a 3D world position into 2D coordinates for the given line.

        **Args:**
        
        
        - `line`: The line to project ("top" or "bottom").
        
        - `camera_x`: Current camera X position.
        
        - `camera_z`: Current camera Z position.
        
        - `player_y`: Player's Y position.
            
    .. py:function:: __initialize_line(self, y, height):
    
        Initializes a line with world coordinates.

        **Args:**
        
        - `y`: Y-coordinate.
        
        - `height`: Height of the line.

        **Returns:**
        
        - Dictionary containing world coordinates.
        
16. Sprite class
----------------
Represents a single sprite in a level.

    **Attributes:**
    
    - `name` (str): The name of the sprite.
    
    - `x` (int): The x-coordinate offset.
    
    - `y` (int): The y-coordinate offset.
    
    - `offset` (int): The x-coordinate offset.
    
    - `offset_y` (int): The y-coordinate offset.
    
    - `sprite` (dict): The sprite information from the settings module.
    
    - `hit` (bool): A flag indicating whether the sprite has been hit.

    **Methods:**
    
    - `__init__(self, name, x, y)`: Initializes a Sprite instance.
    
    - `is_hooker(self)`: Check if the sprite is a "hooker" type.
    
    - `is_speed_boost(self)`: Check if the sprite is a "speed_boost" type.
    
    - `is_bonus(self)`: Check if the sprite is a "bonus" type.
    
    - `path(self)`: Get the file path of the sprite image, considering hit status for "hooker" type.
    
    .. py:function:: __init__(name, x, y):
    
        Initialize a Sprite instance.

        **Args:**
        
        - `name` (str): The name of the sprite.
        
        - `x` (int): The x-coordinate offset.
        
        - `y` (int): The y-coordinate offset.
        
    .. py:function:: is_hooker():
    
        Check if the sprite is of type "hooker".

        **Returns:**
        
        - bool: True if the sprite is a "hooker," False otherwise.
        
    .. py:function:: is_speed_boost():
    
        Check if the sprite is of type "speed_boost".

        **Returns:**
        
        - bool: True if the sprite is a "speed_boost," False otherwise.
        
    .. py:function:: is_bonus():
    
        Check if the sprite is of type "bonus".

        **Returns:**
        
        - bool: True if the sprite is a "bonus," False otherwise.
        
    .. py:function:: path():
    
        Get the file path of the sprite image, considering hit status for "hooker" type.

        **Returns:**
        
        - pygame.Surface: The loaded image of the sprite.
        
17. TitleScreen class
---------------------
Plays a title screen and waits for the user to insert a coin.

    **Attributes:**
    
    - `finished` (bool): Indicates if the title screen has finished playing.
    
    - `ready` (bool): Indicates if the user can insert a coin.
    
    - `background` (pygame.Surface): The background image of the title screen.
    
    - `logo_a` (pygame.Surface): The first logo image for the title screen.
    
    - `logo_b` (pygame.Surface): The second logo image for the title screen.
    
    - `bg_offset` (int): The vertical offset of the background image.
    
    - `font` (pygame.font.Font): The font used for displaying text.
    
    - `state` (int): The current state of the title screen (0, 1, or 2).
    
    - `frame` (int): The current frame count.
    
    - `logo_a_off` (int): The horizontal offset of the first logo image.
    
    - `logo_b_off` (int): The horizontal offset of the second logo image.

    **Methods:**
    
    - `__init__(self)`: Initialize a TitleScreen instance.
    
    - `progress(self, window)`: Progress through the title screen animation and handle user input.
    
    - `state_0_step(self, window)`: Perform animations and actions for state 0 of the title screen.
    
    - `state_1_step(self, window)`: Perform animations and actions for state 1 of the title screen.
    
    - `state_2_step(self, window)`: Perform animations and actions for state 2 of the title screen.
    
    .. py:function:: __init__():
    
        Initialize a TitleScreen instance.
        
    .. py:function:: progress():
    
        Progress through the title screen animation and handle user input.

        **Args:**
        
        - `window` (pygame.Surface): The window surface to render on.
        
    .. py:function:: state_0_step():
    
        Perform animations and actions for state 0 of the title screen.

        **Args:**
        
        - `window` (pygame.Surface): The window surface to render on.
        
    .. py:function:: state_1_step():
    
        Perform animations and actions for state 1 of the title screen.

        **Args:**
        
        - `window` (pygame.Surface): The window surface to render on.
        
    .. py:function:: state_2_step():
    
        Perform animations and actions for state 2 of the title screen.

        Args:
        - `window` (pygame.Surface): The window surface to render on.
        
18. TunnelEntrance class
------------------------
Represents a Tunnel Entrance polygon as we approach it.

    **Attributes:**
    
    - `quantifier` (int): A factor determining the dimensions of the tunnel entrance.
    
    - `colour` (tuple): The RGB color tuple representing the color of the tunnel entrance.

    **Methods:**
    
    - `__init__(self, colour)`: Initializes a TunnelEntrance instance.
    
    - `render(self, window, segment)`: Render the tunnel entrance on the window surface.
    
    .. py:function:: __init__(colour):
    
        Initialize a TunnelEntrance instance.

        **Args:**
        
        - `colour` (tuple): The RGB color tuple representing the color of the tunnel entrance.
        
    .. py:function:: render(window, segment):
    
        Render the tunnel entrance on the window surface.

        **Args:**
        
        - `window` (pygame.Surface): The window surface to render on.
        
        - `segment` (Segment): The road segment containing information about the current state.
        
19. TunnelInside class
----------------------
Represents a Tunnel inside (walls, roof) polygon as we approach it.

    **Attributes:**
    
    - `quantifier` (int): A factor to adjust the rendering of the tunnel geometry.

    **Methods:**
    
    - `__init__(self)`: Initializes a TunnelInside instance.
    
    - `render(self, window, coords, clip, coverage)`: Renders the tunnel inside, including roof, left wall, and right wall.

    **Parameters:**
    
    - `window` (pygame.Surface): The surface to render the tunnel inside on.
    
    - `coords` (dict): Dictionary containing screen coordinates for rendering.
    
    - `clip` (list): List of segments with clipping information for the tunnel.
    
    - `coverage` (list): List of segments with coverage information for the tunnel.

    **Details:**
    
    - The tunnel inside is rendered based on the provided screen coordinates, clipping segments,and coverage segments.Therendering includes the roof, left wall, and right wall of the tunnel.
    
    .. py:function:: __init__():
    
        Initializes a TunnelInside instance.
        
    .. py:function:: render(window, coords, clip, coverage):
    
        Renders the tunnel inside, including roof, left wall, and right wall.

        **Args:**
        
        - `window` (pygame.Surface): The surface to render the tunnel inside on.
        
        - `coords` (dict): Dictionary containing screen coordinates for rendering.
        
        - `clip` (list): List of segments with clipping information for the tunnel.
        
        - `coverage` (list): List of segments with coverage information for the tunnel.
        
20. Level class
---------------
Represents a level in the game world.

    **Attributes:**
    
    - `name` (str): The name of the level.
    
    - `slug` (str): The identifier for the level.
    
    - `song` (str): The song associated with the level.
    
    - `laps` (int): The number of laps required to complete the level.
    
    - `backgrounds` (list): List of background objects for the level.
    
    - `palettes` (dict): Color palettes used in the level.
    
    - `finished` (bool): Indicates whether the level has been completed.
    
    - `segments` (list): List of segments composing the level.
    
    - `competitors` (list): List of competitor objects in the level.

    **Methods:**
    
    - `__init__(self, details)`: Initializes a Level object with the provided details.
    
    - `build(self)`: Reads the level file and builds the level by populating the segments array.
    
    - `add_segment(self, curve, start_y=0, end_y=0)`: Creates a new segment and adds it to the segments array.
    
    - `add_sprite(self, segment, name, x, y=0.0)`: Adds a sprite to the given segment.
    
    - `add_polygon(self, segment, klass, when="pre", args=[])`: Adds a non-sprite renderable object to the given segment.
    
    - `insert_bonuses(self)`: Adds bonuses into the track at random places.
    
    - `add_speed_boost(self, position, offset)`: Inserts sprites for speed boosts at the correct locations.
    
    - `add_competitor(self, position, offset, name, speed)`: Adds a competitor sprite to the given segment.
    
    - `add_tunnel(self, start, end)`: Marks the appropriate segments as part of a tunnel.
    
    - `track_length(self)`: Returns the total length of the level track.
    
    - `find_segment(self, position)`: Returns the appropriate segment given a Z position.
    
    - `offset_segment(self, i)`: Returns a segment by index, wrapping back to the beginning if past the end.
    
21. Game class
--------------
Provides the game flow.

    **Attributes:**
    
    - `window` (pygame.Surface): The main game window.
    
    - `clock` (pygame.time.Clock): The game clock.
    
    - `paused` (bool): Indicates if the game is currently paused.
    
    - `waiting` (bool): Indicates if the game is in a waiting state.
    
    - `selected_player` (int): Index of the selected player.
    
    - `player` (Player): The player object.
    
    - `level` (Level): The level object.
    
    - `high_scores` (hs.HighScores): The high scores object.

    **Methods:**
    
    - `__init__(self, window, clock)`: Initializes a Game object.
    
    - `play(self)`: Manages the game flow.
    
    - `wait(self)`: Displays high scores until a new player is ready.
    
    - `__game_cycle(self)`: Executes a cycle of the game, updating player, level, and game state.
    
    - `__pause_cycle(self)`: Pauses the game, displaying a 'Paused' message.
    
    - `__progress(self, screen, fps)`: Advances the provided screen with the given frames per second.
    
    - `__title_screen(self)`: Displays the title screen.
    
    - `__countdown(self, level_number)`: Displays the countdown screen for the given level.
    
    - `__player_select(self)`: Displays the player selection screen.
    
    - `__credits_screen(self)`: Displays the credits screen.
    
22. GameLauncher class
----------------------
Vantage- Main Game Loop

    **Initialization:**
    
    - Pygame engine is initialized.
    
    - Game window caption is set to "VANTAGE"
    
    - Fullscreen mode is configured based on the settings.
    
    - Pygame clock for controlling frames per second (FPS) is created.
    
    - Game instance is initialized with the game window and clock.

    **Main Game Loop:**
    
    - The loop continues indefinitely, alternating between waiting for a new player and playing the game.
    
    - If the game is waiting for a new player, the 'wait' method of the game instance is called to display high scores until a new player is ready.
    
    - If not waiting, the 'play' method of the game instance is called to manage the overall game flow.

    **Note:** The game loop continues indefinitely until the program is manually terminated.

