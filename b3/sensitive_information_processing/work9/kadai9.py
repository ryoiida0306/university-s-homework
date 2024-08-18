# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 14:54:26 2021

@author: taguc
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

#課題1
#(1)
"""
t = np.arange(-5,5,0.1)
p = stats.t.pdf(t, df = 4 )     
plt.plot(t, p,label="t")

t0 = 2.0

#plt.plot([t0, t0], [0, 0.45], 'r-')

plt.savefig("自由度4のt分布.png")
#plt.show()
   
plt.close()
 
 #(2)

t = np.arange(-5,5,0.1)
p = stats.t.pdf(t, df = 5 )     
plt.plot(t, p,label="t")
plt.savefig("自由度5のt分布.png")
plt.close()
p = stats.t.pdf(t, df = 50 )     
plt.plot(t, p,label="t")
plt.savefig("自由度50のt分布.png")
plt.close()
p = stats.t.pdf(t, df = 100 )     
plt.plot(t, p,label="t")
plt.savefig("自由度100のt分布.png")
plt.close()
p = stats.t.pdf(t, df = 1000 )     
plt.plot(t, p,label="t")
plt.savefig("自由度1000のt分布.png")
plt.close()
 #(3)
 
 
t = np.arange(-5,5,0.1)
p = stats.t.pdf(t, df = 9 )     
plt.plot(t, p,label="t")

t0,t1 = stats.t.interval(alpha = 0.95,df = 9)

plt.plot([t0, t0], [0, 0.45], 'r-')
plt.plot([t1, t1], [0, 0.45], 'r-')

plt.savefig("自由度9のt分布95%.png")
#plt.show()
   
plt.close()

#(4)
"""
data = np.array([3,4,2,9,6,7,5,6,5,4]) 
myu = 3

E = np.mean(data)
V = np.var(data)
test_t = (E - myu)/np.sqrt(V/len(data))

t = np.arange(-5,5,0.1)
p = stats.t.pdf(t, df = len(data)-1 )     
plt.plot(t, p,label="t")

t0,t1 = stats.t.interval(alpha = 0.95,df = len(data)-1)

plt.plot([t0, t0], [0, 0.45], 'r-')
plt.plot([t1, t1], [0, 0.45], 'r-')
plt.plot([test_t, test_t], [0, 0.45], 'r-')

plt.savefig("t検定.png")
#plt.show()

plt.close()
if(t0<test_t or test_t<t1):
    print("帰無仮説を棄却し、H_1が成立")
else:
    print("帰無仮説は棄却できない")
    
print(myu+t0*np.sqrt(V/len(data)),"≦µ≦",myu+t1*np.sqrt(V/len(data)))

"""
#課題2
data = np.array([[2.2,4.1,5.5,1.9,3.4,2.6,4.2,3.7,4.9,3.2],[71,81,86,72,77,73,80,81,85,74]],dtype = np.float16)


x = data[0]
y = data[1]
#print(x)

xlabel = "含有率"
ylabel = "収率"
n = len(x)     
dlabel = range(1,n)
#drawScatter(x,y,xlabel,ylabel,dlabel)

x_ave = x.mean(axis = 0)
y_ave = y.mean(axis = 0)

xy_Sigma = np.cov(x,y,bias = True)

x_pvar = xy_Sigma[0][0]
y_pvar = xy_Sigma[1][1]
xy_cov = xy_Sigma[0][1]
Sxx = x_pvar*len(data[0])
Syy = y_pvar*len(data[0])
Sxy = xy_cov*len(data[0])

beta1=xy_cov/x_pvar
beta0 =y_ave-xy_cov/x_pvar*x_ave
#print("単回帰の推定式：\n y = ",beta1,"x",beta0)

Se = Syy-Sxy/Sxx*Sxy

R_2 = 1-Se/y_pvar

#print("寄与率R^2=",R_2)


X = np.array([0,8])
Y = np.array([xy_cov/x_pvar*X[0]+y_ave-xy_cov/x_pvar*x_ave,xy_cov/x_pvar*X[1]+y_ave-xy_cov/x_pvar*x_ave])

plt.plot(X,Y)
plt.scatter(x,y , color = "red")
plt.savefig("回帰分析.png")
plt.close()

#(1)

Ve = Se/(len(data[0])-2)

myu = 0

test_t = (beta1 - myu)/np.sqrt(Ve/x_pvar)

t = np.arange(-5,5,0.1)
p = stats.t.pdf(t, df = len(data[0])-2 )     
plt.plot(t, p,label="t")

t0,t1 = stats.t.interval(alpha = 0.95,df = len(data[0])-2)

plt.plot([t0, t0], [0, 0.45], 'r-')
plt.plot([t1, t1], [0, 0.45], 'r-')
plt.plot([test_t, test_t], [0, 0.45], 'r-')

plt.savefig("t検定_beta1.png")
#plt.show()

plt.close()
if(t0<test_t or test_t<t1):
    print("帰無仮説を棄却し、H_1が成立")
else:
    print("帰無仮説は棄却できない")

print(beta1+t0*np.sqrt(Ve/x_pvar),"≦beta1≦",beta1+t1*np.sqrt(Ve/x_pvar))


#(2)

y_hat = beta1 * x +beta0
E = y-y_hat
standardE = E/np.sqrt(Ve)
 
hkk = 1/len(data[0])+(x-x_ave)*(x-x_ave)/Sxx
print("予測値=",y_hat)
print("標準残差=",standardE)
print("テコ比=",hkk)


#(3)

data = np.array([[12,12,11,7,8,9,14,11],[22,24,21,19,19,22,24,23]],dtype = np.float16)


x = data[0]
y = data[1]
#print(x)

xlabel = "含有率"
ylabel = "収率"
n = len(x)     
dlabel = range(1,n)
#drawScatter(x,y,xlabel,ylabel,dlabel)

x_ave = x.mean(axis = 0)
y_ave = y.mean(axis = 0)

xy_Sigma = np.cov(x,y,bias = True)

x_pvar = xy_Sigma[0][0]
y_pvar = xy_Sigma[1][1]
xy_cov = xy_Sigma[0][1]
Sxx = x_pvar*len(data[0])
Syy = y_pvar*len(data[0])
Sxy = xy_cov*len(data[0])

beta1=xy_cov/x_pvar
beta0 =y_ave-xy_cov/x_pvar*x_ave
#print("単回帰の推定式：\n y = ",beta1,"x",beta0)

Se = Syy-Sxy/Sxx*Sxy

R_2 = 1-Se/y_pvar



X = np.array([6,15])
Y = np.array([xy_cov/x_pvar*X[0]+y_ave-xy_cov/x_pvar*x_ave,xy_cov/x_pvar*X[1]+y_ave-xy_cov/x_pvar*x_ave])

plt.plot(X,Y)
plt.scatter(x,y , color = "red")
plt.savefig("問題4_回帰分析.png")
plt.close()


Ve = Se/(len(data[0])-2)

myu = 0

test_t = (beta1 - myu)/np.sqrt(Ve/x_pvar)

t = np.arange(-5,5,0.1)
p = stats.t.pdf(t, df = len(data[0])-2 )     
plt.plot(t, p,label="t")

t0,t1 = stats.t.interval(alpha = 0.95,df = len(data[0])-2)

plt.plot([t0, t0], [0, 0.45], 'r-')
plt.plot([t1, t1], [0, 0.45], 'r-')
plt.plot([test_t, test_t], [0, 0.45], 'r-')

plt.savefig("課題4_t検定_beta1.png")
#plt.show()

plt.close()


y_hat = beta1 * x +beta0
E = y-y_hat
standardE = E/np.sqrt(Ve)
 
hkk = 1/len(data[0])+(x-x_ave)*(x-x_ave)/Sxx

print("(1)")
print("寄与率R^2=",R_2)
print("自由度調節済み寄与率=",1-Se*(len(x)-1)/y_pvar/(len(x)-2))
print("(2)")
if(t0<test_t or test_t<t1):
    print("帰無仮説を棄却し、H_1が成立")
else:
    print("帰無仮説は棄却できない")

print(beta1+t0*np.sqrt(Ve/x_pvar),"≦beta1≦",beta1+t1*np.sqrt(Ve/x_pvar))
print("(3)")
print("標準残差=",standardE)
print("テコ比=",hkk)
 
"""
 
 
 
 