import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 定数の設定
fs = 1  # サンプリング周波数 [Hz]
dt = 1 / fs  # サンプリング周期 [s]
tap = 64  # 移動平均フィルタのタップ数
f_in = 103 / 65536  # 入力正弦波信号周波数 [Hz]
quant_step = 1  # 量子化ステップ [V]
amp_in = 0.25  # 入力正弦波信号振幅 [V]
n = 65536  # FFTの点数
N = n * 4  # 時間軸(65536*4点分のデータを求める必要があるため，nを4倍している)
t = np.arange(0, N) / fs  
blackman_harris_window = 0.35875 - 0.48829 * np.cos(2 * np.pi * np.arange(N) / N) + 0.14128 * np.cos(2 * np.pi * 2 * np.arange(N) / N) - 0.01168 * np.cos(2 * np.pi * 3 * np.arange(N) / N)

def main():
    sinWave = amp_in * np.sin(2 * np.pi * f_in * t)
    y = np.zeros_like(sinWave)
    v1 = np.zeros_like(sinWave)
    v2 = np.zeros_like(sinWave)
    # デルタシグマ変調の計算
    for i in range(1, N):
        v1[i] = sinWave[i] + v1[i-1] - y[i-1]
        v2[i] = v1[i] + v2[i-1] - y[i-1]
        y[i] = np.sign(v2[i])

    # 64tapの移動平均フィルタを3回通す
    out1 = np.zeros_like(sinWave)
    out2 = np.zeros_like(sinWave)
    out3 = np.zeros_like(sinWave)
    for i in range(tap, N):
        out1[i] = sum(y[i-tap:i]) / tap
    for i in range(tap, N):
        out2[i] = sum(out1[i-tap:i]) / tap
    for i in range(tap, N):
        out3[i] = sum(out2[i-tap:i]) / tap
    
    plt.figure(figsize=(10, 5))
    plt.plot(t[-n:], out3[-n:])  # プロットするグラフの時間軸を65536で割る必要はあるのか．サンプリング周波数が1Hzだから1秒に1点しか出ないから割る必要なさそうだけど，とりあえず．あと波形が密集しているけど正しいのか．
    plt.xlim(3*n, 3*n+1/f_in)
    plt.ylabel('Amplitude [V]')
    plt.xlabel('points')
    plt.savefig('../img/ansD_t.pdf')
    plt.show()
    plt.clf()
    plt.close()

    windowed_out = out3[-n:] * signal.windows.blackmanharris(n)
    wo_fft = np.fft.fft(windowed_out)
    #sliced_wyfft = wy_fft[-n:]  # 最後の65536点分を使うからスライス
    wo_fft /= n/2
    freq = np.fft.fftfreq(len(wo_fft), d=dt)
    plt.figure(figsize=(10, 5))
    plt.plot(freq[:n//2], 20 * np.log10(np.abs(wo_fft)[:n//2]))
    plt.xscale('log')
    plt.ylabel('Spectrum [dB]')
    plt.xlabel('Frequency [Hz, (log-scale)]')
    plt.savefig(f'../img/ansD_f.pdf')
    plt.show()
    plt.clf()
    plt.close()


if __name__ == '__main__':
    main()