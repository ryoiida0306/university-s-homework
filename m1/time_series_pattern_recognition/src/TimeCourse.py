import numpy as np
import matplotlib.pyplot as plt
# from AirQualityData import data1,data2, fn
from CovidData import data, fn

# print(data1)
# 時系列データの作成
t = np.arange(0, 1096, 1)
# x = np.arange(0, 10, 0.1)  # 0から10まで0.1刻みのデータ
# y = np.sin(t)              # サイン関数を適用

# 時系列データのプロット
plt.figure(figsize=(10, 5))  # グラフのサイズ指定
plt.plot(t,data)
plt.title(format("Time Series Data ({})".format(fn)))
plt.xlabel('Time[day]')
plt.ylabel('Number of people')
plt.grid(True)
plt.savefig("./image/Timecourse_{}.pdf".format(fn))
# plt.show()

# tsa acf acovf ccf