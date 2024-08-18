# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 09:24:27 2022

@author: iida ryo
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

d = np.array([[5,4,1,5,5],[1,2,5,4,5]])


wardLink = linkage(d.T,metric='euclidean',method='ward')
singleLink = linkage(d.T,metric='euclidean',method='single')

dendrogram(wardLink)
plt.show()
#dendrogram(singleLink)
plt.show()

print(wardLink)