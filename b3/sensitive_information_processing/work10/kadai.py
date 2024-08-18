# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 00:37:13 2022

@author: iida ryo
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


X = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [51, 38, 57, 51, 53,
             77, 63, 69, 72, 73], [16, 4, 16, 11, 4, 22, 5, 5, 2, 1]])
X = X.T
y = np.array([3.0, 3.2, 3.3, 3.9, 4.4, 4.5, 4.5, 5.4, 5.4, 6.0])

x = np.array([[51, 38, 57, 51, 53, 77, 63, 69, 72, 73],
             [16, 4, 16, 11, 4, 22, 5, 5, 2, 1]])
x = x.T
#print(X)
#print(y)
n = len(X)
p = len(X.T)-1

beta = np.linalg.inv(X.T@X)@X.T@y
y_hat = X@beta

#print(beta)
#print(np.cov(y_hat, y))
Cov = np.cov(y_hat, y)
Syhyh = Cov[0, 0]
Syy = Cov[1, 1]
Syyh = Cov[0, 1]
R_2 = Syyh*Syyh/Syy/Syhyh
R_2_star = 1-(1-R_2)*(n-1)/(n-p-1)
#print(R_2_star)

y0 = y-np.mean(y)
Syy0 = y0.T@y0

xM1 = np.array([51, 38, 57, 51, 53, 77, 63, 69, 72, 73])
ones = np.array([1,1,1,1,1,1,1,1,1,1])
XM1 = np.array([ones,xM1])
XM1 = XM1.T
#print(XM1)
betaM1 = np.linalg.inv(XM1.T@XM1)@XM1.T@y
y_hatM1 = XM1@betaM1
eM1 = y-y_hatM1
SeM1 = eM1.T@eM1
#print(SeM1)
#print(Syy0)
F_0M1 = ((Syy0-SeM1)/((n-1)-(n-2)))/(SeM1/(n-2))
#print(F_0M1)

CovM1 = np.cov(y_hatM1, y)
SyhyhM1 = CovM1[0, 0]
SyyM1 = CovM1[1, 1]
SyyhM1 = CovM1[0, 1]
R_2M1 = SyyhM1*SyyhM1/SyyM1/SyhyhM1
R_2_starM1 = 1-(1-R_2M1)*(n-1)/(n-p-1)
print(R_2_starM1)


XM2 = X;
betaM2 = np.linalg.inv(XM2.T@XM2)@XM2.T@y
y_hatM2 = XM2@betaM2
eM2 = y-y_hatM2
SeM2 = eM2.T@eM2
print(betaM2)
print(SeM2)
F_0M2 = ((SeM1-SeM2)/((n-2)-(n-3)))/(SeM2/(n-3))
print(F_0M2)






#print(y_hat)
e = y-y_hat
Se = e.T@e
Ve = Se/(n-p-1)
standard_e = e/np.sqrt(Ve)
#print(e)
#print(standard_e)

x = x.T
x_means = [x[0].mean(), x[1].mean()]
x = x.T
x0 = x - x_means
S = x0.T@x0
#print(S)
S_inv = np.linalg.inv(S)
#print(S_inv)
#S11 = S[0,0]
#S12 = S[0,1]
#S22 = S[1,1]
Dk = (n-1)*x0@S_inv@x0.T
Dk = np.diag(Dk)
#print(Dk)
hkk = 1/n + Dk/(n-1)
#print(hkk)
#print("if hkk >", 2.5*hkk.mean(), "the hkk is exception")
#print(2.5*(p+1)/n)

X_sample = np.array([1,70,10])
x_sample = np.array([70,10])
y_sample = X_sample@beta
#print(y_sample)

x0_sample = x_sample - x_means
D_0 = (n-1)*x0_sample.T@S_inv@x0_sample
#print(D_0)

t0,t1 = stats.t.interval(alpha = 0.95,df =7)
#print(y_sample+t0*np.sqrt((1/n+D_0/(n-1))*Ve))
#print(y_sample+t1*np.sqrt((1/n+D_0/(n-1))*Ve))
#print(y_sample+t0*np.sqrt((1+1/n+D_0/(n-1))*Ve))
#print(y_sample+t1*np.sqrt((1+1/n+D_0/(n-1))*Ve))






