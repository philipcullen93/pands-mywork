# this program reads in a string and strips
# any leading or trailing spaces.
# it also converts all the letters to lowercase
# it then outputs the length of the original string
# and the normalised one.

# author: Philip Cullen

rawstring = input("Please input a string: ")
normalisedstring = rawstring.strip().lower()

lengthofrawstring = len(rawstring)
lengthofnormalisedstring = len(normalisedstring)

print(f"That string normalised is: {normalisedstring}")
print(f"We reduced the input string from {lengthofrawstring} to {lengthofnormalisedstring} characters")