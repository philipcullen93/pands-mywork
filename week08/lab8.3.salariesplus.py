import random
import numpy as np
# it is a good idea to have your absolute values set into variables at the beginning of your program

minsalary = 20000
maxsalary = 80000
number_of_entries = 10

salaries = np.random.randint(minsalary, maxsalary, number_of_entries)
salaries_plus = salaries + 5000
print(salaries_plus)