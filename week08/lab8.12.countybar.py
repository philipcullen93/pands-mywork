# demonstration of how to make a pie plot of the unique occurances in an array.

import random
import numpy as np
import matplotlib.pyplot as plt

# make the array of occurances
possible_counties = ["wicklow", "kildare", "louth", "dublin", "carlow"]

# pick 100 randomly from possible counties with the frequency set as p.
counties = np.random.choice(
    possible_counties,
    p = [0.1, 0.3, 0.2, 0.12, 0.28],
    size = (100)
)

unique, counts = np.unique(counties, return_counts = True)
#plt.pie(counts, labels = unique)
#plt.show()

plt.bar(unique, counts)
plt.show()

