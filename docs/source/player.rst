Player Class
=============

.. py:class:: Player

   A class representing a player in the game.

   .. attribute:: settings

      The game settings for the player.

   .. attribute:: points

      The current points scored by the player.

   .. attribute:: high_score

      The highest score achieved by the player.

   .. attribute:: next_milestone

      The next milestone for scoring bonus points.

   .. method:: __init__(high_score, selected_player)

      Initializes a Player.

      :param high_score: The highest score achieved by the player.
      :param selected_player: The selected player.

   .. method:: reset(total_laps=GameSetting.LAPS_PER_LEVEL)

      Resets the player's attributes.

      :param total_laps: Total laps for the level.

   .. method:: steer(segment)

      Adjusts the player's position based on the segment.

      :param segment: The current game segment.

   .. method:: climb(segment)

      Adjusts the player's vertical position based on the segment.

      :param segment: The current game segment.

   .. method:: detect_collisions(segment)

      Detects collisions with sprites and competitors in the segment.

      :param segment: The current game segment.

   .. method:: render(window, segment)

      Renders the player on the window based on the segment.

      :param window: The game window.
      :param segment: The current game segment.

   .. method:: render_hud(window)

      Renders the player's heads-up display on the window.

      :param window: The game window.

   .. method:: render_blood(window)

      Renders blood overlay on the window.

      :param window: The game window.

   .. method:: accelerate()

      Adjusts the player's speed based on acceleration.

   .. method:: travel(track_length, window)

      Updates the player's position and attributes based on travel.

      :param track_length: The length of the track.
      :param window: The game window.

   .. method:: set_acceleration(keys)

      Sets the player's acceleration based on keyboard input.

      :param keys: The pressed keys.

   .. method:: set_direction(keys)

      Sets the player's direction based on keyboard input.

      :param keys: The pressed keys.

   .. method:: speed_percent()

      Calculates the player's speed as a percentage of the top speed.

   .. method:: direction_speed()

      Calculates the player's speed in the current direction.

   .. method:: segment_percent()

      Calculates the player's position as a percentage of the segment.

   .. method:: handle_crash()

      Handles the player's state after a crash.

   .. method:: finished()

      Checks if the player has finished the level.

   .. method:: alive()

      Checks if the player is alive.

   .. method:: __set_special_text(text, time)

      Sets special text for display.

   .. method:: __collided_with_sprite(sprite)

      Checks if the player has collided with a sprite.

   .. method:: __circular_orbit(center, radius, t)

      Calculates the position on a circular orbit.

   .. method:: __set_checkpoint()

      Sets the last checkpoint time.

   .. method:: __hit_hooker()

      Handles player's state after hitting a hooker sprite.

   .. method:: __hit_bonus()

      Handles player's state after hitting a bonus sprite.

   .. method:: __hit_speed_boost()

      Handles player's state after hitting a speed boost sprite.

   .. method:: __hit_world_object()

      Handles player's state after hitting a world object sprite.

   .. method:: __hit_competitor()

      Handles player's state after hitting a competitor sprite.

   .. method:: __fastest_lap()

      Checks if the player has set the fastest lap.

   .. method:: __run_screech()

      Plays screech sound effect.

   .. method:: __stop_screech()

      Stops the screech sound effect.

   .. method:: __game_over_overlay(window)

      Renders the game over overlay on the window.

   .. method:: __level_over_overlay(window)

      Renders the level complete overlay on the window.

