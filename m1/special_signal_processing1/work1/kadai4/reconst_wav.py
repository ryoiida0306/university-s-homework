import numpy as np
import scipy.io.wavfile as wavfile

# 1. Read the 16-bit quantized .wav file
filename = "arayurugennzituwo"
input_wav_file = '{}.wav'.format(filename)
output_wav_file = '{}2.wav'.format(filename)
sampling_rate, data = wavfile.read(input_wav_file)

# 2. Normalize the audio to -3dBFS
peak = np.max(np.abs(data))
target_dBFS = -3.0
target_peak = 10 ** (target_dBFS / 20.0) * (2**15)
scaling_factor = target_peak / peak
data_normalized = data * scaling_factor

# 3. Reduce the quantization bit depth to 8 bits (from 16 bits)
data_normalized_8bit = np.round(data_normalized / (2**8)).astype(np.int8)

# 4. Convert back to 16-bit by scaling
data_16bit = (data_normalized_8bit.astype(np.int16)) * (2**8)

# 5. Write the processed data to a new .wav file
wavfile.write(output_wav_file, sampling_rate, data_16bit)

print("Processing complete. Output file saved as", output_wav_file)
