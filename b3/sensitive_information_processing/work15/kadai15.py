# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 15:08:12 2022

@author: iida ryo
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

if __name__ == "__main__":
    print()
    
fn = "data_test14_1.csv"
D1 = np.loadtxt(fn,delimiter=',')
fn = "data_test14_2.csv"
D2 = np.loadtxt(fn,delimiter=',')

D1 = D1.T
D2 = D2.T

myu1 = np.mean(D1,axis=1)
myu2 = np.mean(D2,axis=1)
print(myu1)
print(myu2)

myu = (myu1+myu2)/2
print(myu)

A = D1.T-myu1
S1 = A.T@A

B = D2.T-myu2
S2 = B.T@B
print(S1)
print(S2)

sigma = (S1[0,0]+S2[0,0])/(np.size(D1[0,:])-1+np.size(D2[0,:])-1)

print()
z = ((myu1[0]-myu2[0])/sigma)*(D1-myu[0])
print(z)

print()
delta = myu1-myu2
print(delta)

print()
sigma11 = (S1[0,0]+S2[0,0])/(np.size(D1[0,:])-1+np.size(D2[0,:])-1)
sigma12 = (S1[0,1]+S2[0,1])/(np.size(D1[0,:])-1+np.size(D2[0,:])-1)
sigma21 = (S1[1,0]+S2[1,0])/(np.size(D1[0,:])-1+np.size(D2[0,:])-1)
sigma22 = (S1[1,1]+S2[1,1])/(np.size(D1[0,:])-1+np.size(D2[0,:])-1)
print(sigma11)
print(sigma12)
print(sigma21)
print(sigma22)

print()
sigma = np.array([[sigma11,sigma12],[sigma21,sigma22]])
sigma_inv=np.linalg.inv(sigma)
print(sigma_inv)

print()
delta_new=delta.T@sigma_inv@delta

mis_probability=1-stats.norm.cdf(delta_new, delta_new/2, np.sqrt(delta_new))
print('誤判別の確率',mis_probability)
print('判別効率',delta_new)
