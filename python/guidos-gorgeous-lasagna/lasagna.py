"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time




def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based on the number of layers.

        :param number_of_layers: int - number of layers of the lasagna.
        :return: int - time of preparation (in minutes) derived from 'PREPARATION_TIME'.

        Function that take the time of preparation of one layers and provides the total
        time of preparation of all lasagna.
        """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time you have been cooking.

            :param number_of_layers: int - number of layers of the lasagna.
            :param elapsed_bake_time: int - baking time already elapsed.
            :return: int - total time of cooking.

            Function that returns the amount of time you have been cooking the lasagna.
            """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time