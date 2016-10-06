#!/bin/python

#assignment 1 differences of infidelity 
import numpy as np  
from scipy import stats
import matplotlib.pyplot as plt

def bin_trials(n,k,p):
    positive_out = []
    for i in range(0,k):
        positive_out.append(np.random.binomial(n, p) )
        #print("positive out: ", positive_out[i], "maximum likelihood: " , positive_out[i]/n)

    #print(positive_out)
    return positive_out

def arith_mean(arr):
    return np.mean(arr)
    
def variance(arr):
    return np.var(arr)

def std_deviation(arr):
    return np.std(arr)

#def plot_nigga():
    
    
def n_var(n):
    print("n = " , n)
    lst_of_pos_trials = bin_trials(n, 100, 0.2)
    mean = arith_mean(lst_of_pos_trials)
    print("aithmetic mean: ", mean)
    mu = 0.2 * n
    print("estimate value (mu): ", mu)
    var = n*0.2*(1-0.2)
    print("std variance: ",var)
    var_std = variance(lst_of_pos_trials)
    print("variance: ", var_std)    
    sigma = np.sqrt(var)
    print("deviation (sigma): ", sigma) 
    sigma = std_deviation(lst_of_pos_trials)   
    print("std deviation (sigma): ", sigma)
    res = stats.norm.interval(0.95, loc=mu, scale=sigma/np.sqrt(n))
    print("Confidence Interval: ", res)
    
    return (mean, sigma)
    
def main():
    mean_10, sigma_10 = n_var(10)
    print(mean_10, sigma_10)
    mean_100, sigma_100 = n_var(100)
    mean_1000, sigma_1000 = n_var(1000)
    mean_10000, sigma_10000 =n_var(10000)
    
    data = [np.random.normal(mean_10, sigma_10, 100),
    np.random.normal(mean_100, sigma_100, 100), np.random.normal(mean_1000,
    sigma_1000, 100), np.random.normal(mean_10000, sigma_10000, 100)]
    
    titles = ["n = 10", "n = 100", "n = 1000", "n = 10000"]
    
    plt.subplots_adjust(hspace=.4)
    plt.hist((data[0], data[1], data[2], data[3]), bins=[0.05, 0.05, 0.15,
    0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95], normed=True, label=titles)
    
    plt.legend()
    plt.show()    
    
    
main()
