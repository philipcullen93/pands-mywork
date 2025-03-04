# read in two numbers and multiple them together
# Author: Philip Cullen

# Previous method:

# num1 = int(input("Enter a Number: "))
# num2 = int(input("Enter a second number: "))

# answer = num1 * num2
# print(f"Answer is {answer}")

# Function Method

def readnum(message = "Enter a number: "):
    num = False
    while (not num):
        try:
            num = int(input(message))
        except ValueError:
            print("Not a number")
    return num

num1 = readnum()
num2 = readnum("Enter second number:")

answer = num1 * num2
print(f"The answer is {answer}")

       