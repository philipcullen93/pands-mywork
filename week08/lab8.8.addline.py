import random
import numpy as np
import matplotlib.pyplot as plt

minsalary = 20000
maxsalary = 80000
number_of_entries = 100

np.random.seed(1)
salaries = np.random.randint(minsalary, maxsalary, number_of_entries)
ages = np.random.randint(low = 21, high = 65, size = number_of_entries)
plt.scatter(ages, salaries)

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = 'r')
plt.show()
