#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Nov 2021
# This is a guessing game

from random import randint


def main():
    # This function inputs guess and outputs if correct or not

    # generate random number
    NUM = randint(0, 9)

    # input
    try:
        guess = int(input("Enter guess(0-9): "))
    except ValueError:
        print(f"Input must be integer")
        return

    # process/output
    if guess == NUM:
        print("You guessed correctly!")
    else:
        print(f"Incorrect, the number was {NUM}.")

    # output finished
    print("Thanks for playing.")
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
