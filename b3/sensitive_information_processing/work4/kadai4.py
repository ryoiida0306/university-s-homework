# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:27:25 2022

@author: iida ryo
"""

import numpy as np
import matplotlib.pyplot as plt

def dataplot(dataname,data) :
    plt.figure(num = None,figsize=(6,4),dpi = 80,)
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    for i in range(len(data.T[0])) :
        plt.plot()
        plt.plot(data[i][0],data[i][1],marker = ".",color = "blue") 
    plt.savefig(dataname)
    
    
A = np.array([[0,1,1],[0,1,0],[0,0,1],[1,0,1]],dtype = np.int);

B = np.zeros((len(A[0]),len(A[0])));

C = np.zeros((len(A.T[0]),len(A.T[0])));

#Bの作成
for i in range(len(A[0])):
    for j in range(len(A.T[0])):
        if A[j][i] == 1:
            B[i][i] += 1;
            C[j][j] += 1;


B12 = np.zeros((len(A[0]),len(A[0])));


for i in range(len(A[0])):
    B12[i][i] = 1/np.sqrt(B[i][i]);

C_inv = np.linalg.inv(C)

#print(B12)
#print(C_inv)



H = B12@A.T@C_inv@A@B12;

#print(H);

w,v = np.linalg.eig(H)

#print(w)
#print(v)

v = v.T
signal = np.zeros(len(w))
                
W = np.array([])
V = np.array([[]]).reshape((0,len(A.T)))
sumW = 0;
for n in range(len(w)) :
    max = -1001001001
    maxI = 0
    for i, tmp in enumerate(w):
        if signal[i] == 1 :
            continue
        if tmp == 1:
            continue
        if max<tmp :
            maxI = i
            max = tmp
    if max == -1001001001 :
        break
    signal[maxI] = 1
    W = np.insert(W,len(W),w[maxI],axis = 0)
    V = np.insert(V,len(V),v[maxI],axis = 0)
    sumW += w[maxI]/len(w)
    
    #print(signal)
    #print(maxI)
    if sumW>0.8 :
        break
V = V.T
#print(W)
#print(V)

W12 = np.zeros(len(W))
for i in range(len(W)):
    W12[i] = np.sqrt(W[i])
    

x = B12@V
y = C_inv@A@V/W12
#print(x)
#print(y) 

dataplot("x_plot.png",x)
dataplot("y_plot.png",y)

print("A=\n",A)
print("B=\n",B)
print("C=\n",C)
print("Bの-1/2乗=\n",B12)
print("Cの逆行列=\n",C_inv)
print("H=\n",H)
print("第一第二成分固有値=\n",W)
print("第一第二成分固有ベクトル=\n",V)
print("第一第二固有ベクトル=\n",V)
print("x=\n",x)
print("y=\n",y)
