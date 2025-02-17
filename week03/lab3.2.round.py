# rounds a number
# be careful of round, it rounds to the nearest even number
# e.g. 4.5 rounds to 4
# but 5.5 rounds to 6
# don't use it when accuracy is essential
# Author: Philip Cullen

numbertoround = float(input("Enter a float number: "))
roundednumber = round(numbertoround)
print("{} rounded is {}".format(numbertoround, roundednumber))