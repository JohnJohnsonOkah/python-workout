"""
This program sums up numbers in the list of object
"""


def mysum(*args):
    """
    This function takes in an arbitrary number of arguments
    (argument could be of any type)

    and returns the sum of all that can be converted to an int.
    """

    total = 0

    for i in args:
        try:
            i = int(i)
        except ValueError:
            i = 0

        total += i
    return total


print(mysum(2, 12, 6, "2"))
