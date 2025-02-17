# program to subtract one number from another

# input reads in a string so we need to convert it into an integer
# Author: Philip Cullen

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
answer = x - y
print("{} minus {} is {}".format(x, y, answer))

# if 'hello' is enetered an error occurs because 'hello' is a string not an integer.
# if 12.5 is enetered an error occurs becasue 12.5 is a float not an integer.