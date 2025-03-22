# this program generates 10 random numbers from 0 to 100
# prints them out
# then prints the top 3

# a list is used to store and
# manipulate the numbers

#author: Philip Cullen

import random

howmany = 10
tophowmany = 3
rangefrom = 0
rangeto = 100

numbers = []

for i in range(0,howmany) :
    numbers.append(random.randint(rangefrom,rangeto))
print(f"{howmany} random number \t {numbers}")

topones = numbers.copy()

topones.sort(reverse = True)
print(f"The top three numbers are {tophowmany} are \t\t {topones[0:tophowmany]}")