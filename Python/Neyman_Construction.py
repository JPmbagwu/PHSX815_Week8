#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 22:20:10 2023

@author: johnpaulmbagwu
"""

import numpy as np
import matplotlib.pyplot as plt

def coin_flip(p, n):
    """
    Simulates n coin flips with probability of heads equal to p.
    Returns the number of heads obtained.
    """
    return np.random.binomial(n, p)


# True values of p to vary
p_values = np.linspace(0, 1, 101)

# Number of experiments to simulate for each true value of p
n_experiments = 1000

# Number of coin flips per experiment
n_flips = 10

# Simulate experiments for each true value of p
results = []
for p in p_values:
    experiments = [coin_flip(p, n_flips) for _ in range(n_experiments)]
    results.append(experiments)

# Plot the Neyman construction
plt.figure(figsize=(8,6))
plt.scatter(p_values, np.mean(results, axis=1))
plt.errorbar(p_values, np.mean(results, axis=1), yerr=np.std(results, axis=1)/np.sqrt(n_experiments), fmt='none')
plt.plot(p_values, p_values, linestyle='--', color='gray')
plt.xlabel('True value of p')
plt.ylabel('Measured value of p')
plt.title('Neyman construction for coin flip model')
plt.show()
