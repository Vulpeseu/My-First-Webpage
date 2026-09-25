"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME = 40

print(EXPECTED_BAKE_TIME)
    


#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(y):
    """
    yep
    """
    bake_time_remaining = EXPECTED_BAKE_TIME - y
    return bake_time_remaining
"""Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
"""
        
    



#TODO (student): Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(a):
    """Validate function.__doc__ exists for each function.
Check the attribute dictionary of each listed function
for the presence of a __doc__ key.

:return: unexpectedly None error when __doc__ key is missing.
"""
    return a * 2

        

#TODO (student): define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(a, elapsed_time_in_minutes):
    """Validate function.__doc__ exists for each function.
Check the attribute dictionary of each listed function
for the presence of a __doc__ key.

:return: unexpectedly None error when __doc__ key is missing.
"""
    return 2 * a +  elapsed_time_in_minutes
    


# TODO (student): Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
