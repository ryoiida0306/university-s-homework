import numpy as np
from scipy.io import wavfile

filename = "aaa2"
# 入力wavファイルの読み込み

input_wav_path = '{}.wav'.format(filename)
sample_rate, data = wavfile.read(input_wav_path)

# dataはNumPy配列に格納される
print(f'Sample Rate: {sample_rate}')
print(f'Data Type: {type(data)}')
print(f'Data Shape: {data.shape}')

# ここで必要な処理を行う（例：データの加工など）
li = 0
for i in range(len(data)) :
    if data[li] != data[i] :
        l = data[li]
        r = data[i]
        leng = i - li
        for j in range(leng) :
            data[li+j] = int(l + (r - l) * j/leng)
        li = i
        


# 出力wavファイルの保存
output_wav_path = '{}_linear_interpolation.wav'.format(filename)
wavfile.write(output_wav_path, sample_rate, data)

print(f'Output saved to: {output_wav_path}')
