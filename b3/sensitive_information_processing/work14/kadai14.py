# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 15:08:12 2022

@author: iida ryo
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats



fn = "data_test14_1.csv"
D1 = np.loadtxt(fn,delimiter=',')
fn = "data_test14_2.csv"
D2 = np.loadtxt(fn,delimiter=',')
"""
D1 = np.array([[50,69,93,76,88],[15.5,18.4,26.4,22.9,18.9]])
D2 = np.array([[43,56,38,21,25],[16.9,21.6,12.2,16.0,10.5]])
D1 = D1.T
D2 = D2.T
"""
myu1 = np.mean(D1,axis = 0)
myu2 = np.mean(D2,axis = 0)
#print(myu1)
#print(myu2)
A1 = D1-myu1
A2 = D2-myu2
S1 = A1.T@A1
S2 = A2.T@A2
#print(S1)
#print(S2)

myu = (myu1+myu2)/2
S = (S1+S2)/(len(D1)-1+len(D2)-1)
print("S=",S)
S_inv  = np.linalg.inv(S)



x = np.array([10,10])

z = (myu1-myu2)@S_inv@(x-myu)
print("z=",z)

#z>0 -> 1に属する