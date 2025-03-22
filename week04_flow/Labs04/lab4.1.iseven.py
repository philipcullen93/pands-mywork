# this program allows the user to input a number
# the program then tells the user if the number is odd or even

# author: Philip Cullen

number = int(input("Enter an interger: "))
if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")