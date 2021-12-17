#  Generate a random number between 1 and 9 (including 1 and 9).
#  Ask the user to guess the number,
#  then tell them whether they guessed too low, too high, or exactly right.

import random

def guess(x):
    my_number = random.randint(1, 10)
    guess = 0

    while guess != my_number:
        guess = int(input("guess my number: "))
        if guess > my_number:
            print("my number is lower")
        elif guess < my_number:
            print("my number is higher")
        else:
            print("Well Done! You guessed my number! ")

print(guess(8))

