import sys
up_path = "../"
sys.path.append(up_path)


from filename import fname, fpath
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# WAVファイルの読み込み
sample_rate, data = wavfile.read("{}.wav".format(fpath))

data = data[:500]
# 音声データの時間軸を計算
time = np.arange(0, len(data)) / sample_rate

# プロット
plt.figure(figsize=(10, 4))
plt.plot(time, data)
plt.title('Waveform')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.savefig("../figure/{}.pdf".format(fname))

# plt.show()
