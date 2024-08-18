# import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# from makedata import data, n, N
from ML import data, n, N

def maximum_liklehood(x) :
    return N/x.sum()

lambdata = np.zeros(n)

for i in range(n) :
    lambdata[i] = maximum_liklehood(data[i])


plt.figure(figsize=(6, 4))  # グラフのサイズ指定
plt.hist(lambdata, bins=5, edgecolor='black')
# plt.title()
plt.xlabel('lambda')
plt.xlim(1,3)
plt.ylabel('Number of pieces')
plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
# plt.grid(True)
plt.savefig("../image/MLHist.pdf")
# plt.show()

   