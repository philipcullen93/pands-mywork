# Program that puts 10 random numbers into a queue(list), the
# program then outputs all the values in the queue
# then takes the numbers from the queue one at a time, prints them and the current numbers still
# in the queue. (the command pop(0) takes the first element out of a list)

# Author: Philip Cullen

import random
queue = []
numberofnumbers = 10
rangeto = 100

for n in range(0, numberofnumbers):
    queue.append(random.randint(0, rangeto))

print(f"queue is {queue}")

while len(queue) != 0:
    currentnumber = queue.pop(0)
    print(f"Current Number is {currentnumber} and the queue is {queue}")

print("The queue is now empty")
