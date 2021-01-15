"""
This program sums up numbers in a list together with
an optional argument (the starting point - an extra number)
"""


def mysum(numbers, extra=0):
    """
    This function takes in a list (containing numbers)
    and an optional argument (an extra number)

    then it return the sum of the numbers in the list and the extra number.
    """

    total = extra

    for num in numbers:
        total += num
    return total


print(mysum([1, 2, 3], 4))
