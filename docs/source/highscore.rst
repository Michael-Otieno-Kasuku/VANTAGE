HighScore Class
===============

.. py:class:: HighScore

   A class for handling high scores in the game.

   .. attribute:: high_scores

      The list of high scores.

   .. method:: __init__()

      Initializes a HighScore object.

   .. method:: is_high_score(score)

      Checks if a given score is a high score.

      :param score: The score to be checked.

      :return: True if it's a high score, False otherwise.

   .. method:: minimum_score()

      Retrieves the minimum high score.

      :return: The minimum high score.

   .. method:: add_high_score(score)

      Adds a new high score to the list.

      :param score: The score to be added.

   .. method:: __sort()

      Sorts the high scores in descending order.

   .. method:: __write_high_scores()

      Writes the high scores to a JSON file.

   .. method:: __read_high_scores()

      Reads the high scores from a JSON file.

      :return: The list of high scores.

   .. method:: __scores_only()

      Retrieves only the scores from the list of high scores.

      :return: The list of scores.

