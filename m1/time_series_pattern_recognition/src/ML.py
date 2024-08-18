# import math
import numpy as np
import matplotlib.pyplot as plt
from makedata import data, n, N


plt.figure(figsize=(6, 4))  # グラフのサイズ指定
lamb = np.arange(0, 5, 0.1)
for i in range(n):
    def f(x) :
        return N * np.log(x) - x * data[i].sum()
    vf = np.vectorize(f)
    liklehood = vf(lamb)
    plt.plot(lamb,liklehood)
# plt.title()
plt.xlabel('lambda')
plt.ylabel('likelihood')
plt.grid(True)
plt.savefig("../image/likelihood.pdf")
# plt.show()

   

