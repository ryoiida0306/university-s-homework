import numpy as np
import matplotlib.pyplot as plt
# from AirQualityData import data1,data2, fn
from makedata import ECGdata

# print(data1)
# 時系列データの作成
# t = np.arange(0, data.shape[0], 1)
# x = np.arange(0, 10, 0.1)  # 0から10まで0.1刻みのデータ
# y = np.sin(t)              # サイン関数を適用
# 時系列データのプロット
plt.figure(figsize=(10, 5))  # グラフのサイズ指定
plt.plot(ECGdata[:5001,0],ECGdata[:5001,1])
plt.title("TimeCourse")
plt.xlabel('time')
plt.ylabel('colum1')
plt.grid(True)
plt.savefig("../image/final/TimeCourse01.pdf")
# plt.show()

# tsa acf acovf ccf