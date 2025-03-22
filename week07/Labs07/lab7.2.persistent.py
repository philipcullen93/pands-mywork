# This program that counts how many times it was run

# Author: Philip Cullen

# This function reads in a number from a file that already exists (count.txt)

FILENAME = "count.txt"
def readnumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
    
# test run
num = readnumber()
print(num)

