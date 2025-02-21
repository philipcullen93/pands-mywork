# the program randomly picks a number between 0 and 100
# program asks user to guess a number
# the program prompts the user to keep guessing numbers
# until they guess the correct one
# this program also tells the user if their guess is
# too high or
# too low

# author: Philip Cullen

import random

numbertoguess = random.randint(0,100)

guess = int(input("Please guess a number between 0 and 100: "))

while guess != numbertoguess :
    if guess < numbertoguess :
        print("Too Low")
    else:
        print("Too High")
    guess = int(input("Please guess again: "))

print(f"Well Done! The number was {numbertoguess}")