"""
This program is a guessing game that generates a random numbers
and allows you to guess the number.
"""

import random


def guessing_game():
    """
    This function does the following:
    - generates a random number
    - accepts a guess from user
    - tells user if their guess was higher, lower or correct
    """

    # Generates a random number
    number = random.randint(0, 100)

    # Accepts a guess from user
    try:
        guessed_num = int(input("Guess the number: "))
    except ValueError:
        print("Your input is invalid")
        return

    # Determine if user guess is higher, lower or correct
    while guessed_num != number:
        if guessed_num > number:
            print("Too high")
        elif guessed_num < number:
            print("Too low")
        try:
            guessed_num = int(input("Try again: "))
        except ValueError:
            print("Your input is invalid")
            return
    print("Just right")


guessing_game()
