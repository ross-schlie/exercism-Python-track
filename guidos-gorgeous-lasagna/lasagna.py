"""exercism lasagna module."""

EXPECTED_BAKE_TIME = 40 # how many minutes the lasagna should bake in the oven
PREPARATION_TIME = 2 #the time it takes to prepare a single layer

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """
    Return elapsed preparation time based on the number of layers.

    :param number_of_layers: int number of layers added to the lasagna.
    :return: int time to make lasagna derived from 'PREPARATION_TIME'.

    This function takes a number representing the number of layers
    and calculates the time spent preparing the lasagna.
    """

    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    :param number_of_layers: int the number of layers added to the lasagna.
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int sum of your preparation time and the time the lasagna has already spent baking in the oven

    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
