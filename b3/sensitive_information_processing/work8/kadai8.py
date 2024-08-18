# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 16:29:43 2022

@author: iida ryo
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
#import statistics
#import math

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
        
    


fn = "data_lec08_homework.csv"
A = np.loadtxt(fn,delimiter=',')


x = A.T[0]
y = A.T[1]
#print(x)

xlabel = "身長"
ylabel = "体重"
n = len(x)     
dlabel = range(1,n)
#drawScatter(x,y,xlabel,ylabel,dlabel)

x_ave = x.mean(axis = 0)
y_ave = y.mean(axis = 0)

xy_Sigma = np.cov(x,y,bias = True)

x_pvar = xy_Sigma[0][0]
y_pvar = xy_Sigma[1][1]
xy_cov = xy_Sigma[0][1]


#print(x_pvar)
#print(y_pvar)
#print(xy_cov)
print("単回帰の推定式：\n y = ",xy_cov/x_pvar,"x",y_ave-xy_cov/x_pvar*x_ave)

Se = y_pvar-xy_cov/x_pvar*xy_cov

R_2 = 1-Se/y_pvar

print("寄与率R^2=",R_2)

#定義域を165から185とする

X = np.array([165,185])
Y = np.array([xy_cov/x_pvar*X[0]+y_ave-xy_cov/x_pvar*x_ave,xy_cov/x_pvar*X[1]+y_ave-xy_cov/x_pvar*x_ave])

plt.plot(X,Y)
plt.scatter(x,y , color = "red")

print(xy_cov*len(x))
print(Se)
print(1-Se*(len(x)-1)/y_pvar/(len(x)-2))



