# this program prints out a random fruit
# Author: Philip Cullen

import random
fruits = ('apples', 'oranges', 'bananas', 'pears')

# we want a random number between 0 and length-1
index = random.randint(0, len(fruits)-1)
fruit = fruits[index]
print("A random fruit: {}". format(fruit))