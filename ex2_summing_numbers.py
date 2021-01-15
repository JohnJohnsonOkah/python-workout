"""
This program sums up numbers without the inbuilt sum() function
"""


def mysum(*args):
    """
    This function takes in an arbitrary number of arguments
    and returns the sum of all.
    """
    total = 0
    for i in args:
        total += i
    return total


print(mysum(2, 12, 6))
