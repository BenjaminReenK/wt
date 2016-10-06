import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def makeExperiment(n):
    estimates = np.zeros(100)
    positiveOutcomes = np.zeros(100)
    positiveOutcomes


    for i in range (0, 100):
        positiveOutcomes[i] = np.random.binomial(n, p=0.2)
        estimates[i] = positiveOutcomes[i] / n
    return positiveOutcomes, estimates

def getVariance(values, average):
    sum = 0
    for i in range (0, 100):
        sum += (values[i] - average) * (values[i] - average)
    return sum / 100

def b(n):
    print ("\nn=" + str(n))
    positiveOutcomes, estimatedPs = makeExperiment(n)
    positiveOutcomes
    estimatedPs
    var = getVariance(estimatedPs, np.sum(estimatedPs) / 100)
    print("variance: " + str(var))
    print("standard deviation: " + str(np.sqrt(var)))

    mean = getMean(estimatedPs)
    sd = getStandardDeviation(estimatedPs, mean)
    lb = np.percentile(estimatedPs, 2.5)
    ub = np.percentile(estimatedPs, 97.5)
    print("confidence interval: "+ str(lb) + " - " + str(ub))
    return estimatedPs, mean, sd

def getMean(values):
    sum = 0
    for i in range(0, 100):
        sum += values[i]
    return sum / 100

def getStandardDeviation(values, mean):
    sum = 0
    for i in range(0, 100):
        sum += (values[i] - mean) * (values[i] - mean)
    return sum / 100


print("\nb.1)")

p_10, mean_10, sd_10 = b(10)
p_100, mean_100, sd_100 = b(100)
p_1000, mean_1000, sd_1000 = b(1000)
p_10000, mean_10000, sd_10000 = b(10000)

print("\n")

titles = ["n = 10", "n = 100", "n = 1000", "n = 10000"]

n_bins = 50

plt.subplot(221)
plt.hist(p_10, bins=n_bins, normed=True)
plt.title("n = 10")
plt.xlabel("estimated p")
plt.ylabel("how many times was p the estimated probability")
plt.xlim([0, 1])

plt.subplot(222)
plt.hist(p_100, bins=n_bins, normed=True)
plt.title("n = 100")
plt.xlabel("estimated p")
plt.ylabel("how many times was p the estimated probability")
plt.xlim([0, 1])

plt.subplot(223)
plt.hist(p_1000, bins=n_bins, normed=True)
plt.title("n = 1000")
plt.xlabel("estimated p")
plt.ylabel("how many times was p the estimated probability")
plt.xlim([0, 1])

plt.subplot(224)
plt.hist(p_10000, bins=n_bins, normed=True)
plt.title("n = 10000")
plt.xlabel("estimated p")
plt.ylabel("how many times was p the estimated probability")
plt.xlim([0, 1])

plt.show()


print ("\n4)\nDer Studie vertraue ich nicht, weil nur 100 Befragungen in jedem Bundesland eine viel zu kleine Stichprobe darstellen, um repraesentativ zu sein. In dieser Simulation ist zu erkennen, dass die geschaetze Wahrscheinlichkeit mit der realen Wahrscheinlichkeit immer besser uebereinstimmt, je mehr Versuche durchgefuehrt werden.")

