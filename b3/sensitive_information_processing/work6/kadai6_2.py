# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:27:25 2022

@author: iida ryo
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from mpl_toolkits.mplot3d import Axes3D

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
        

####################################
# ３次元の散布図を描画する関数
# x,y,z: データ
# xlabel : x軸のラベル
# ylabel : y軸のラベル
# zlabel : z軸のラベル
# dlabel : データ点のラベル
####################################
def drawScatter3D(x,y,z,xlabel,ylabel,zlabel,dlabel):     

    # グラフの消去（必要に応じて利用）
    # plt.clf();
    
    fig = plt.figure(figsize=(7.0, 7.0))
    ax = Axes3D(fig)
    
    # X,Y,Z軸にラベルを設定
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    
    # 散布図を描画
    ax.plot(x,y,z,marker="o",linestyle='None')
    
    # ラベル位置のマージン
    m = 0.001
    
    # ラベルを描画
    for i, j, k , l in zip(x, y, z, dlabel):
        ax.text(i+m, j+m, k+m, l, None)
    
    plt.show()


def dataplot(dataname,data) :
    plt.figure(num = None,figsize=(6,4),dpi = 80,)
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    for i in range(len(data.T[0])) :
        plt.plot()
        plt.plot(data[i][0],data[i][1],marker = ".",color = "blue") 
    plt.savefig(dataname)
    
    
fn = "data_lec06-2.csv"
A = np.loadtxt(fn,delimiter=',')

Fx = A.sum(axis = 0)
Fy = A.sum(axis = 1)

B = np.diag(Fx)
C = np.diag(Fy)

Bri = np.diag(Fx**(-0.5))
Ci = np.diag(1/Fy)

H = Bri@A.T@Ci@A@Bri

w,v = np.linalg.eig(H)
sort_index = np.argsort(w)[::-1]

sort_w = w[sort_index]
sort_v = v[:,sort_index]

ccr = np.cumsum(sort_w[1:])/np.sum(sort_w[1:])

x = Bri @ sort_v
y = (sort_w**(-0.5))*(Ci@A@x)


 #　各プロットにつけるラベル
#dlabel = ["A","B","C"]
var_label = ["ソフトウェア工学","パターン認識","画像情報処理","電気電子回路","言語処理工学","音声情報処理","メディアセンシング"];

# 各プロットにサンプル番号（1～n）のラベルを付ける場合
n = 52
sample_label = range(1,n+1)        

# テストしたいラベルを選択
dlabel = var_label
#dlabel = sample_label

# 2次元プロット（各プロットに任意のラベルを付ける）
drawScatter(x.T[1],x.T[2],"x","y",var_label)    
drawScatter(y.T[1],y.T[2],"x","y",sample_label)    
print(x)
print(y)
print(ccr)
