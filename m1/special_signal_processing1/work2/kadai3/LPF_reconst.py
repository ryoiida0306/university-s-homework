import sys
up_path = "../"
kadai1_path = "../kadai1"
kadai2_path = "../kadai2"
sys.path.append(up_path)
sys.path.append(kadai1_path)
sys.path.append(kadai2_path)

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from filename import fname, fpath
from fourier import my_fourier, plot
from LPF import my_LPF
import config

lag = config.lag


if __name__ == "__main__" :
    input_wav_file = fpath + ".wav"
    output_wav_file = "{}_LPF_reconst.wav".format(fname)
    sampling_rate, data = wavfile.read(input_wav_file)
    y = my_LPF(data,lag)
    y_ = np.zeros(lag-1)
    y_con = np.concatenate((y,y_)).astype(np.int16)
    wavfile.write(output_wav_file, sampling_rate, y_con)


