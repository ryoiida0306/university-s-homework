import numpy as np
import matplotlib.pyplot as plt
from AirQualityData import data1,data2

# # 散布図用のデータ
# x = np.random.normal(loc=0, scale=1, size=100)
# y = np.random.normal(loc=0, scale=1, size=100)

# # 散布図の作成
plt.figure(figsize=(6, 4))
plt.scatter(data1, data2)
plt.title('Scatter Plot (AirQuality)')
plt.xlabel('PT08.S4(NO2)')
plt.ylabel('PT08.S5(O3)')
plt.grid(True)
plt.savefig('./image/Scatter.pdf')
# plt.show()