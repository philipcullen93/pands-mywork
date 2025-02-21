# # program asks user to pick a number
# the program prompts the user to keep guessing numbers
# until they guess the right one
# this program also tells the user if their guess is
# too high or
# too low

# author: Philip Cullen

numbertoguess = 21
guess = int(input("Please guess a number between 0 and 30: "))
while guess != numbertoguess :
    if guess < numbertoguess :
        print("Too Low")
    else:
        print("Too High")
    guess = int(input("Please guess again: "))

print(f"Well Done! The number was {numbertoguess}")
        