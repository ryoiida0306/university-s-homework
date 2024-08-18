# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:54:26 2021

@author: taguc
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

t = np.arange(-5,5,0.1)
p = stats.t.pdf(t, df = 4 )     
plt.plot(t, p,label="t")

t0 = 2.0

plt.plot([t0, t0], [0, 0.45], 'r-')

plt.savefig("test.png")
#plt.show()
    