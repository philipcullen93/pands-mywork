FILENAME = "count.txt"

def readnumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

def writenumber(number):
    with open (FILENAME,"wt") as f:
        # convert string to int/numbers
        f.write(str(number))

num = readnumber()
num += 1
print(f"We have run this program {num} times")
writenumber(num)