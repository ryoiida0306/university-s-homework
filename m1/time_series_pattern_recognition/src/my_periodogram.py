import numpy as np
import matplotlib.pyplot as plt
# from AirQualityData import data1,data2, fn
from CovidData import data, fn
import statsmodels.tsa.stattools as sm




# FFT（高速フーリエ変換）を計算
fft_result = np.fft.fft(data)

# パワースペクトルを計算
power_spectrum = np.abs(fft_result) ** 2

# 周波数軸を作成
freqs = np.fft.fftfreq(len(data))

# 正の周波数のみを取得
positive_freqs = freqs[:len(data)//2]
positive_power_spectrum = power_spectrum[:len(data)//2]

# ピリオドグラムのプロット
plt.plot(positive_freqs, positive_power_spectrum)
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.title("Periodogram({})".format(fn))
plt.savefig("./image/periodogram_{}.pdf".format(fn))
# plt.show()