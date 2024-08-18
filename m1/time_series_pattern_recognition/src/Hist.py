import numpy as np
import matplotlib.pyplot as plt
from AirQualityData import data1,data2

# # ヒストグラム用のデータ
# data = np.random.normal(loc=0, scale=1, size=1000)  # 平均0、標準偏差1の正規分布から1000個のサンプルを生成

# # ヒストグラムの作成
plt.figure(figsize=(6, 4))
plt.hist(data1, bins=30, edgecolor='black')
plt.title('Histogram (AirQuality)')
plt.xlabel('PT08.S4(NO2)')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('./image/Hist.pdf')
# plt.show()