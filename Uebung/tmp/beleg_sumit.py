import collections
import math
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt

# Bernoulli trail == 1 experiment
ns = [10, 100, 1000, 10000, 100000]
count = 100
probability = 0.2
interval = .95
mapp = {}

for n in ns:
	mapp[n] = [np.random.binomial(n=n, p=probability) for i in range(count)]

mapp = collections.OrderedDict(sorted(mapp.items()))
print(mapp)

def getCI(list):
	mean = np.average(list)
	std = np.std(list)
	bounds = t.interval(interval, len(list) - 1)
	ci = [mean + critival * std / math.sqrt(len(list)) for critival in bounds]
	#return (std, np.var(list), ci[0], ci[1])
	return ci

# print mapp
for k, v in mapp.items():
	tt = getCI(v)
	print ('Key: %d, Std: %f, Variance: %f, KI %f - %f ' % (k, np.std(v), np.var(v), tt[0], tt[1]))

"""
for x in mapp.keys():
	plt.hist(mapp[x])
	plt.show()
"""
