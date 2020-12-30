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

    number = random.randint(0, 10)
    trial = 0

    while guessed_num := input("Guess the number: "):

        trial += 1

        try:
            guessed_num = int(guessed_num)
            if guessed_num > number:
                print(f"Your guess {guessed_num} is too high")
                if trial == 3:
                    print("You didn't guess correctly \N{cross mark}")
                    break
            elif guessed_num < number:
                print(f"Your guess {guessed_num} is too low")
                if trial == 3:
                    print("You didn't guess correctly \N{cross mark}")
                    break
            else:
                print(f"Just right! The number is {guessed_num} \N{check mark}")
                break
        except ValueError:
            print("Invalid input")


guessing_game()
