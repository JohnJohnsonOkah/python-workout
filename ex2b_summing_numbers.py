"""
This program finds the average of a list a numbers
"""


def myaverage(*numbers):
    """
    This function takes in a list of numbers
    and return the average (or arithmetic mean) of the numbers.
    """

    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)
    return average


print(myaverage(1, 2, 3, 4))
