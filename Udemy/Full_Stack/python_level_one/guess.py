"""
Simple guessing game where the user is asked to guess a three digit
number. The computer will then give you hints if you're wrong or tell
you that you're right
"""

import random

COMP_NUM = random.randint(100, 1000)

def main():
    # prompt user to guess
    print("Guess which 3 digit number I'm thinking of:")

    # set game loop
    while True:
        guess = input()

        # check if user input is an integer
        try:
            guess = int(guess)
        except:
            print("That's not a number!")
            return False

        # check if user input is a 3 digit number
        if guess not in range(100, 1000):
            print("That's not a 3 digit number")
            return False

        # check if user guess matches COMP_NUM
        if guess == COMP_NUM:
            print("You got it! The number was {}".format(COMP_NUM))
            return False
        elif guess > COMP_NUM:
            print("Nope. Guess lower.")
        else:
            print("Nope. Guess higher.")

    # quit the game
    quit()

if __name__ == '__main__':
    main()
