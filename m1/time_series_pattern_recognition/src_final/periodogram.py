import numpy as np
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as sm
from makedata import ECGdata
# from acf import colum, acf_result, lag
from scipy import signal
from makedata import ECGdata

# plt.clf()
colum = 2


frequencies, power = signal.periodogram(ECGdata[:,colum], fs=1024)
# print(ECGdata.shape)
# print(frequencies.shape)
# print(power.shape)

plt.figure(figsize=(10, 5))
plt.semilogy(frequencies, power)
plt.title('Periodogram')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power/Frequency [V**2/Hz]')
plt.grid()
plt.savefig("../image/final/periodogram(colum{}).pdf".format(colum))
# plt.show()



# # FFT（高速フーリエ変換）を計算
# fft_result = np.fft.fft(acf_result)


# # frequencies, power = signal.periodogram(acf_result, fs=lag)
# # # パワースペクトルを計算
# # power_spectrum = np.abs(fft_result) ** 2

# # # 周波数軸を作成
# # freqs = np.fft.fftfreq(len(acf_result))

# # # 正の周波数のみを取得
# # positive_freqs = freqs[:len(acf_result)//2]
# # positive_power_spectrum = power_spectrum[:len(acf_result)//2]

# # ピリオドグラムのプロット
# # plt.plot(positive_freqs[:51], positive_power_spectrum[:51])
# fft_result = fft_result[:len(fft_result)//2]
# t = np.arange(0,0.5,1/lag)
# # plt.figure(figsize=(30, 5))  # グラフのサイズ指定
# plt.plot(t,fft_result.real)
# plt.xlabel('f')
# plt.ylabel('p(f)')
# plt.title("Periodogram(colum{})".format(colum))
# plt.savefig("../image/final/periodogram(colum{}).pdf".format(colum))
# # plt.show()

# # print(fft_result)