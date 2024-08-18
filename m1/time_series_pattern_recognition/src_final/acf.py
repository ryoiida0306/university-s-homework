import numpy as np
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as sm
from makedata import ECGdata

colum = 1
lag = 500
# 自己相関関数（ACF）の計算
acf_result = sm.acf(ECGdata[:,colum],nlags=lag)

# # 自己共分散関数（ACOVF）の計算
# acovf_result = sm.acovf(data)

# # クロス相関関数（CCF）の計算
# ccf_result = sm.ccf(data1, data2)

t = np.arange(0, acf_result.shape[0], 1)

# 時系列データのプロット
plt.figure(figsize=(6, 4))  # グラフのサイズ指定
plt.plot(t,acf_result)
plt.title("Ck")
plt.xlabel('lag k')
plt.ylabel('acf')
plt.grid(True)
plt.savefig("../image/final/acf{}.pdf".format(colum))
# plt.show()