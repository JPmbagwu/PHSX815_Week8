#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:44:45 2023

@author: johnpaulmbagwu
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def cone(xx):
    x, y = xx
    tmp1 = (x - 5.)**2
    tmp2 = y**2
    return np.sqrt(tmp1 + tmp2) - 100.

result = minimize(cone, [-1., 1.2], method='BFGS')

print('Minimum:', result.fun)
print('x:', result.x[0])
print('y:', result.x[1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(3, 7, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt((X - 5.)**2 + Y**2) - 100.

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
