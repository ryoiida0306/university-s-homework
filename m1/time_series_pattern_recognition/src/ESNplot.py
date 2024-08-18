import numpy as np
import matplotlib.pyplot as plt

# print(data1)
# 時系列データの作成
sr = np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,0.975,1.0,1.05,1.1,1.2])
data = np.array([
    0.2532749752568612,
    0.29359297042252114,
    0.22577142876203793,
    0.21976913273438098,
    0.20963736587631587,
    0.20343961028868232,
    0.19330095362258093,
    0.17749874329411125,
    0.1667970679141231,
    0.14778558623164637,
    0.13575652265747876,
    0.13314660523354796,
    0.13279504012960902,
    0.1421733047152143,
    0.1999493696526488,
    0.4264729309248273,
    ])
# x = np.arange(0, 10, 0.1)  # 0から10まで0.1刻みのデータ
# y = np.sin(t)              # サイン関数を適用

# 時系列データのプロット
# plt.figure(figsize=(10, 5))  # グラフのサイズ指定
plt.plot(sr,data)
plt.title("ESNmodel")
plt.xlabel('spectral radius')
plt.ylabel('RMSE')
# plt.grid(True)
plt.savefig("../image/ESN/ESNplot.pdf")
# plt.show()

# tsa acf acovf ccf