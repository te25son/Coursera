"""
Remix of the guessing game where the user is not involvedselfself.
The computer picks a random number, then tries to guess it's own number.
How many times does it take it to guess its number.
"""

import random

COMP_NUM = random.randint(100, 1000)

def main():
    # define number range for computer to guess
    game_list = list(range(100, 1000))

    # count how many times the computer guesses
    count = 1

    # prompt user to guess
    print("Guess which 3 digit number I'm thinking of:")

    # set game loop
    while True:
        # initial guess of the computer
        guess = round(max(game_list) - ((max(game_list) - min(game_list)) / 2))

        print(guess)

        # check if user guess matches COMP_NUM
        if guess == COMP_NUM:
            print("You got it! The number was {}".format(COMP_NUM))
            print("It took the computer {} attempts".format(count))
            return False
        elif guess > COMP_NUM:
            print("Nope. Guess lower.")
            game_list = game_list[:game_list.index(guess)]
            count += 1
        else:
            print("Nope. Guess higher.")
            game_list = game_list[game_list.index(guess) + 1:]
            count += 1


if __name__ == '__main__':
    main()
