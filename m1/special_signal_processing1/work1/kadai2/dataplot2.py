import wave
import numpy as np
import matplotlib.pyplot as plt

def read_wav_file(filename):
    with wave.open(filename, 'rb') as wf:
        num_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        num_frames = wf.getnframes()

        # 最初の100msのフレーム数を計算
        duration = 0.1  # 100ms
        frames_to_read = int(framerate * duration)

        # フレームの読み込み
        frames = wf.readframes(frames_to_read)

        # 16ビットの量子化されたデータを int16 の数値に変換
        data = np.frombuffer(frames, dtype=np.int16)

        # フルスケール振幅
        full_scale = 32767

        # -3dBFS の振幅
        minus_3dbfs = full_scale / np.sqrt(2)

        normal_scale = minus_3dbfs/data.max()

        data = (data*normal_scale).astype(int)

        # print(data.max())


    return data, num_channels, sampwidth, framerate

def plot_waveform(data, framerate, duration):
    time = np.linspace(0, duration, num=len(data))
    plt.figure(figsize=(10, 4))
    plt.plot(time, data)
    plt.title("Waveform of First 100ms")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.savefig("./figure/3.pdf")
    # plt.show()

# 使用例
filename = 'aaa.wav'
data, num_channels, sampwidth, framerate = read_wav_file(filename)

# 最初の100msの波形をプロット
plot_waveform(data, framerate, 0.1)
