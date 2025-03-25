import random
import numpy as np
import matplotlib.pyplot as plt

minsalary = 20000
maxsalary = 80000
number_of_entries = 100

np.random.seed(1)
salaries = np.random.randint(minsalary, maxsalary, number_of_entries)

plt.hist(salaries)
plt.show()