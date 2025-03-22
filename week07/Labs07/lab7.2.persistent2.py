
FILENAME = "count.txt"

def writenumber(number):
    with open (FILENAME,"wt") as f:
        # convert string to int/numbers
        f.write(str(number))

# test
writenumber(3)