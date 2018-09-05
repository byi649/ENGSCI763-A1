import random
import numpy as np

average = []

for i in range(1000):

    random_set = [random.random() for x in range(10)]
    random_set.sort()

    orders = random_set[2], random_set[4], random_set[6]
    average.append((random_set[2] + random_set[4] + random_set[6]) / 3.0)

np.savetxt("list.csv", average)
