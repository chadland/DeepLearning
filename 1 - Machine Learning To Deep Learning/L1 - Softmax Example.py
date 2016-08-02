# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 12:43:25 2016

@author: christerhadland
"""

"""Softmax."""


import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    "Create empty list"    
    scoresNp = np.asarray(x)
    softmax=(np.exp(x)/np.sum(np.exp(scoresNp),axis=0))
    "sum(math.exp(scores))"
    return softmax

print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()

