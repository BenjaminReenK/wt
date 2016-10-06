import numpy as np
import scipy as sp
import math
import matplotlib.pyplot as plt
from scipy import stats

def konfidenz(arr, prozent):
  untere_grenze = np.percentile(arr, (100-prozent)/2) 
  obere_grenze = np.percentile(arr, 100-((100-prozent)/2))
  rueckgabe = np.array([untere_grenze, obere_grenze])
  return rueckgabe

def experiment(j):
  a = np.random.binomial(n=j, p=0.2, size=100)
  #a = np.sort(a)
  ausgabe = 'Sortierte Ergebnisse fuer 100 Testreihen mit {} Experimenten:\n\n{}\n'.format(j, a)
  print ausgabe

  print 'Variance'
  var = np.nanvar(a)
  print var 
  print

  print 'Standard deviation:'
  dev = np.std(a)
  print dev
  print

  print 'mean'
  mean = np.mean(a)
  print mean
  print

  print 'Confidence intervall 0.95'
  #The location (loc) keyword specifies the mean. 
  #The scale (scale) keyword specifies the standard deviation.
  confint = stats.norm.interval(0.95, loc=mean, scale=dev)
  print confint
  print

  print 'Konfidenzintevall 95% mit eigener Funktion: '
  print konfidenz(a, 95)
  print

  print 'Konfidenzintervall eigene funktion array sortiert'
  a = np.sort(a)
  print konfidenz(a, 95)
  print

  return a

e1 = experiment(10)
e2 = experiment(100)
e3 = experiment(1000)
e4 = experiment(10000)

f, axarr = plt.subplots(2, 2)
axarr[0, 0].hist(e1/10., bins=np.sqrt(10))
axarr[0, 0].set_title('n = 10')
axarr[0, 0].axis(xmin=0, xmax=15)

axarr[0, 1].hist(e2/100., bins=np.sqrt(100))
axarr[0, 1].set_title('n = 100')
#axarr[0, 1].axis(xmin=5, xmax=40)

axarr[1, 0].hist(e3/1000., bins=np.sqrt(1000))
axarr[1, 0].set_title('n = 1000')
#axarr[1, 0].axis(xmin=100, xmax=300)

axarr[1, 1].hist(e4/10000., bins=np.sqrt(10000))
axarr[1, 1].set_title('n = 10000')
#axarr[1, 1].axis(xmin=1500, xmax=2500)

for ax in axarr:  
  for x in ax:
    x.set_xlabel("# of successes in n experiments")
    x.set_ylabel("frequency of occurence")

plt.show()
#http://matplotlib.org/examples/pylab_examples/subplots_demo.html
#http://adventuresinpython.blogspot.de/2012/12/confidence-intervals-in-python.html
#https://plot.ly/matplotlib/histograms/
