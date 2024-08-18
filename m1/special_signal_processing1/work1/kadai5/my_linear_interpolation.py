import sys
up_path = "../"
kadai1_path = "../kadai1/"
kadai2_path = "../kadai2/"
kadai3_path = "../kadai3/"
sys.path.append(up_path)
sys.path.append(kadai1_path)
sys.path.append(kadai2_path)
sys.path.append(kadai3_path)

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from filename import fname, fpath
from binary import fdata
from mydataplot import fleng, time
from ratedown import normalization, down

downbit = 8
if __name__ == "__main__" :
    # 1. Read the 16-bit quantized .wav file
    input_wav_file = fpath + ".wav"
    output_wav_file = '{}bit_reconst_linear_interpolation_{}.wav'.format(16-downbit,fname)
    sampling_rate, data = wavfile.read(input_wav_file)

    norm_data = normalization(data)
    down_data = down(norm_data,downbit).astype(np.int16)

    li = 0
    for ri in range(len(down_data)) :
        if down_data[li] != down_data[ri] :
            l = down_data[li]
            r = down_data[ri]
            leng = ri - li
            for j in range(leng) :
                down_data[li+j] = int(l + (r - l) * j/leng)
            li = ri
        


    # 5. Write the processed data to a new .wav file
    wavfile.write(output_wav_file, sampling_rate, down_data)

    print("Processing complete. Output file saved as", output_wav_file)
