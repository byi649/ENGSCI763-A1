import random
import numpy as np

sim = []
simanti = []
for i in range(1000):

    randlist = [random.random() for x in range(10000)]
    fx = [100 if x > 0.9 else 0 for x in randlist]

    sim.append(sum(fx)/len(fx))

    randlistanti = [random.random() for x in range(5000)]
    randlistanti = randlistanti + [1 - x for x in randlistanti]
    fxanti = [100 if x > 0.9 else 0 for x in randlistanti]

    simanti.append(sum(fxanti)/len(fxanti))

print(np.var(sim), np.var(simanti))