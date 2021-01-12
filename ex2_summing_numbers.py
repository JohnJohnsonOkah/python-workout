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
        total = total + i
    print(total)


mysum(2, 5, 6)
