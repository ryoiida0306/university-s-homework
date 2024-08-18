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
from filename import fname, fpath
import math
from binary import fdata
from mydataplot import fleng, time
from ratedown import normalization, down
import scipy.io.wavfile as wavfile

downbit = 8

if __name__ == "__main__" :
    input_wav_file = fpath + ".wav"
    output_wav_file = '{}bit_reconst_{}.wav'.format(16-downbit,fname)
    sampling_rate, data = wavfile.read(input_wav_file)

    norm_data = normalization(data)
    down_data = down(norm_data,downbit).astype(np.int16)

    # data = np.zeros(len(data))
    # f = 300
    # for i in range(len(data)) :
    #     data[i] = math.sin(f*2*math.pi*i/sampling_rate)
    
    down_data = (data).astype(np.int16)

    wavfile.write(output_wav_file, sampling_rate, down_data)
