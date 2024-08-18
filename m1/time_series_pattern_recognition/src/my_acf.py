import numpy as np
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as sm
from AirQualityData import data1,data2, fn
from CovidData import data, fn


# 自己相関関数（ACF）の計算
acf_result = sm.acf(data)

# # 自己共分散関数（ACOVF）の計算
# acovf_result = sm.acovf(data)

# # クロス相関関数（CCF）の計算
# ccf_result = sm.ccf(data1, data2)

t = np.arange(0, acf_result.shape[0], 1)

# 時系列データのプロット
plt.figure(figsize=(6, 4))  # グラフのサイズ指定
plt.plot(t,acf_result)
plt.title(format("acf ({})".format(fn)))
plt.xlabel('lag k')
plt.ylabel('acf')
plt.grid(True)
plt.savefig("./image/acf_{}.pdf".format(fn))
# plt.show()