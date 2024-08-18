# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 09:24:27 2022

@author: iida ryo
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

# 日本語のフォントを設定
# （windowsでは動くけど，macだとどう？）
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

####################################
# 散布図を描画する関数
# x,y: データ
# xlabel : x軸のラベル
# ylabel : y軸のラベル
# dlabel : データ点のラベル
####################################
def drawScatter(x,y,xlabel,ylabel,dlabel):     
    
    # グラフの消去（必要に応じて利用）
    # plt.clf();
    
    # グラフのサイズを設定
    plt.figure(figsize=(7.0, 7.0))

    # グラフの軸ラベル等の設定
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)

    # ラベル位置のマージン
    m = 0.001

    for (i,j,k) in zip(x,y,dlabel):
        
        # プロットを描画
        plt.plot(i,j,'o')
        
        # ラベルを描画
        plt.annotate(k, xy=(i+m, j+m))
    
    plt.show()




#標準化する関数
def standard(a) :
    a = a - np.average(a)
    Saa = a@a
    Va = Saa/(len(a)-1)
    return a/np.sqrt(Va)

fn = "data_lec04_nagoya1.csv"
d = np.loadtxt(fn,delimiter=',')
d = d.T

u = np.zeros((6,15))
#標準化
for n in range(6):
    u[n] = standard(d[n])

#相関係数行列の計算
R = u@u.T/(len(u[0])-1)

#固有値固有ベクトルの計算
w,v = np.linalg.eig(R)

#給与率80％以上を目指す
v = v.T
signal = np.zeros(len(w))
W = np.array([])
V = np.array([[]]).reshape((0,6))
sumW = 0
for n in range(6) :
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

X=u.T@V.T

print(X)

n = 52
dlabel = range(0,n+1)  

#dlabel = ["tikusa","higasi","kita","nisi","nakamura","naka","mizuho","atuta","nakagawa","minato","minami","moriyama","midori","meitou","tenpaku"]

drawScatter(X.T[0],X.T[1],"x","y",dlabel)



wardLink = linkage(X,metric='euclidean',method='ward')
singleLink = linkage(X,metric='euclidean',method='single')

dendrogram(wardLink)
plt.show()
#dendrogram(singleLink)
plt.show()