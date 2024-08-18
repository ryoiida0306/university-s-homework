# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 03:35:28 2022

@author: iida ryo
"""

import numpy as np
import matplotlib.pyplot as plt

#標準化する関数
def standard(a) :
    a = a - np.average(a)
    Saa = a@a
    Va = Saa/(len(a)-1)
    return a/np.sqrt(Va)

#データをグラフにプロットする関数
def dataplot(dataname,data) :
    plt.figure(num = None,figsize=(6,4),dpi = 80,)
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    for i in range(len(data.T[0])) :
        plt.plot()
        plt.plot(data[i][0],data[i][1],marker = ".",color = "blue") 
    plt.savefig(dataname)
    
jpn = np.array([86,71,42,62,96,39,50,78,51,89],dtype = np.int)
eng = np.array([79,75,43,58,97,33,53,66,44,92],dtype = np.int)
math = np.array([67,78,39,98,61,45,64,52,76,93],dtype = np.int)
sci = np.array([68,84,44,95,63,50,72,47,72,91],dtype = np.int)


#標準化
Ujpn = standard(jpn)
Ueng = standard(eng)
Umath = standard(math)
Usci = standard(sci)

u = np.array([Ujpn,Ueng,Umath,Usci])
print(Ujpn)
print(u)


#相関係数行列の計算
R = u@u.T/(len(jpn)-1)
print(R)

#固有値固有ベクトルの計算
w,v = np.linalg.eig(R)

#print(w)
print(v)

#給与率80％以上を目指す
v = v.T
signal = np.zeros(len(w))
W = np.array([])
V = np.array([[]]).reshape((0,4))
sumW = 0
for n in range(4) :
    max = -1001001001
    maxI = 0
    for i, tmp in enumerate(w):
        if signal[i] == 1 :
            continue
        if max<tmp :
            maxI = i
            max = tmp
    signal[maxI] = 1
    W = np.insert(W,len(W),w[maxI],axis = 0)
    V = np.insert(V,len(V),v[maxI],axis = 0)
    sumW += w[maxI]/len(w)
    
    #print(signal)
    #print(sumW)
    if sumW>0.8 :
        break

#print(u)

#print(u.T@V.T)

#主成分分析
dataplot("主成分分析結果.pdf",u.T@V.T)

#因子負荷量の計算
W = np.sqrt(W)
r = W*V.T
#print(W)
#print(V.T)
#print(r)
#print(r.T[0])
dataplot("因子負荷量.pdf",r)


