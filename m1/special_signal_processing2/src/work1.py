import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import windows, lfilter

# 定数の設定
fs = 1  # サンプリング周波数 1 Hz
f_input = 103 / 65536  # 入力正弦波信号周波数
A = 0.25  # 入力正弦波信号振幅
N = 65536  # FFT の点数
quantization_step = 1  # 量子化ステップ

# 時間軸の作成
t = np.arange(0, N) / fs

# (a) 入力正弦波信号
input_signal = A * np.sin(2 * np.pi * f_input * t)

# (b) 入力正弦波信号の量子化
quantized_signal = np.round(input_signal / quantization_step) * quantization_step

# (c) ∆Σ変調A-D変換器の1ビット出力
# ブロック図に基づくデルタシグマ変調器の実装
def delta_sigma_modulator(input_signal):
    N = len(input_signal)
    output_signal = np.zeros(N)
    integrator1 = 0
    integrator2 = 0
    for n in range(N):
        integrator1 += input_signal[n] - output_signal[n - 1]
        integrator2 += integrator1 - output_signal[n - 1]
        output_signal[n] = 1 if integrator2 >= 0 else -1
    return output_signal

delta_sigma_output = delta_sigma_modulator(input_signal)

# (d) ∆Σ変調A-D変換器の出力信号に64 tapの移動平均フィルタを3段通過
# 過渡応答特性の影響を避けるために、65536×4点分のデータを使用
extended_signal = np.tile(delta_sigma_output, 4)
moving_average_filter = np.ones(64) / 64
filtered_signal = lfilter(moving_average_filter, 1, extended_signal)
filtered_signal = lfilter(moving_average_filter, 1, filtered_signal)
filtered_signal = lfilter(moving_average_filter, 1, filtered_signal)

# 最後の65536点分を抽出
filtered_signal = filtered_signal[-65536:]

# ブラックマン–ハリス窓関数の適用
window = windows.blackmanharris(N)
print(filtered_signal.shape, window.shape)
windowed_signal = filtered_signal * window

# FFTの計算
def calculate_fft(signal, fs):
    N = len(signal)
    fft_result = np.fft.fft(signal, N)
    fft_freq = np.fft.fftfreq(N, 1/fs)
    fft_amplitude = np.abs(fft_result) / N
    return fft_freq[:N // 2], 20 * np.log10(fft_amplitude[:N // 2])

freq_input, amp_input = calculate_fft(input_signal, fs)
freq_quantized, amp_quantized = calculate_fft(quantized_signal, fs)
freq_delta_sigma, amp_delta_sigma = calculate_fft(delta_sigma_output, fs)
freq_filtered, amp_filtered = calculate_fft(windowed_signal, fs)

# グラフの描画
plt.figure(figsize=(14, 10))

# (a) 入力正弦波信号
plt.subplot(4, 2, 1)
plt.plot(t, input_signal)
plt.title('Input Sine Wave Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [V]')

plt.subplot(4, 2, 2)
plt.semilogx(freq_input, amp_input)
plt.title('Input Sine Wave Signal - Frequency Spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')

# (b) 量子化信号
plt.subplot(4, 2, 3)
plt.plot(t, quantized_signal)
plt.title('Quantized Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [V]')

plt.subplot(4, 2, 4)
plt.semilogx(freq_quantized, amp_quantized)
plt.title('Quantized Signal - Frequency Spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')

# (c) ∆Σ変調出力
plt.subplot(4, 2, 5)
plt.plot(t, delta_sigma_output)
plt.title('Delta-Sigma Modulated 1-bit Output')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [V]')

plt.subplot(4, 2, 6)
plt.semilogx(freq_delta_sigma, amp_delta_sigma)
plt.title('Delta-Sigma Modulated 1-bit Output - Frequency Spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')

# (d) フィルタ通過後の信号
plt.subplot(4, 2, 7)
plt.plot(t, filtered_signal)
plt.title('Filtered Signal After 3-stage Moving Average')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [V]')

plt.subplot(4, 2, 8)
plt.semilogx(freq_filtered, amp_filtered)
plt.title('Filtered Signal - Frequency Spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')

plt.tight_layout()
plt.savefig('work1.pdf')
# plt.show()
