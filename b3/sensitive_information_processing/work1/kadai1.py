# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

x = np.array([9,7,4,6],dtype = np.int) 
y = np.array([10,8,4,6],dtype = np.int) 

x = x - np.average(x)
y = y - np.average(y)

Sxx = x@x
Syy = y@y
Sxy = x@y

Cxy = Sxy/(len(x)-1)

rxy = Sxy/(np.sqrt(Sxx*Syy))
print("Sxy =",Sxy)
print("Cxy =",Cxy)
print("rxy =",rxy)