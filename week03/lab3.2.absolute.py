# give the absolute value of a number

# Author: Philip Cullen

# In the question, number is ambiguous but the
# output implies that we should be dealing with floats
# so I am casting the input to a float

number = float(input("Enter a number: "))
absolutevalue = abs(number)
print("The absolute value of {} is {}".format(number, absolutevalue))
