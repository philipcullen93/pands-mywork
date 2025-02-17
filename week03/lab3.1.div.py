# program that reads in two numbers and
# outputs the integer answer and remainder
# Author: Philip Cullen

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
answer = x//y
remainder = x%y
print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))