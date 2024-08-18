import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 定数の設定
fs = 1  # サンプリング周波数 [Hz]
dt = 1 / fs  # サンプリング周期 [s]
f_in = 103 / 65536  # 入力正弦波信号周波数 [Hz]
quant_step = 1  # 量子化ステップ [V]
amp_in = 0.25  # 入力正弦波信号振幅 [V]
n = 65536  # FFTの点数
N = n * 4  # 時間軸(65536*4点分のデータを求める必要があるため，nを4倍している)
t = np.arange(0, N) / fs 
blackman_harris_window = 0.35875 - 0.48829 * np.cos(2 * np.pi * np.arange(N) / N) + 0.14128 * np.cos(2 * np.pi * 2 * np.arange(N) / N) - 0.01168 * np.cos(2 * np.pi * 3 * np.arange(N) / N)

def main():
    sinWave = amp_in * np.sin(2 * np.pi * f_in * t)
    plt.figure(figsize=(10, 5))
    plt.plot(t[-n:], sinWave[-n:])  
    plt.xlim(3*n, 3*n+1/f_in)
    plt.ylabel('Amplitude [V]')
    plt.xlabel('points')
    plt.savefig('../img/ansA_t.pdf')
    plt.show()
    plt.clf()
    plt.close()

    windowed_sinWave = sinWave[-n:] * signal.windows.blackmanharris(n)
    wsw_fft = np.fft.fft(windowed_sinWave)  # fftしてから65536点分使う，ではなく窓関数は65536*4点分，fftは65536点分
    #wsw_fft = wsw_fft[-n:]  # 最後の65536点分を使うからスライス
    wsw_fft /= n/2
    freq = np.fft.fftfreq(len(wsw_fft), d=dt)
    plt.figure(figsize=(10, 5))
    plt.plot(freq[:n//2], 20 * np.log10(np.abs(wsw_fft)[:n//2]))
    plt.xscale('log')
    plt.ylabel('Spectrum [dB]')
    plt.xlabel('Frequency [Hz, (log-scale)]')
    plt.savefig(f'../img/ansA_f.pdf')
    plt.show()
    plt.clf()
    plt.close()

if __name__ == '__main__':
    main()