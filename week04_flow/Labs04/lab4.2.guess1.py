# program asks user to pick a number
# the program prompts the user to keep guessing numbers
# until they guess the right one

# author: Philip Cullen

numbertoguess = 42

guess = int(input("Please guess a number: "))
while guess != numbertoguess :
    print("Wrong")
    guess = int(input("Please guess again: "))

print(f"Well done! The number was {numbertoguess}")