import sys
up_path = "../"
kadai1_path = "../kadai1"
sys.path.append(up_path)
sys.path.append(kadai1_path)

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from filename import fname, fpath
from fourier import my_fourier, plot
import config


start_iter = config.start_iter
N = config.N
lag = config.lag
max_f = config.max_f
delta_f = config.delta_f


def my_LPF(data, lag) :

    sumdata = np.zeros(len(data)+1)
    for i in range(len(data)) :
        sumdata[i+1] = sumdata[i] + data[i]
    
    y = np.zeros(len(data)-lag+1)
    for i in range(len(y)) :
        y[i] = sumdata[i+lag] - sumdata[i]
    y/=lag

    return y


if __name__ == "__main__" :
    input_wav_file = fpath + ".wav"
    sampling_rate, data = wavfile.read(input_wav_file)
    y = my_LPF(data,lag)
    norm_y = y/np.max(y)
    Af, Bf = my_fourier(norm_y, sampling_rate, start_iter, N, max_f, delta_f)
    Hf = np.sqrt(Af*Af + Bf*Bf)
    plot(Af, "An_LPF", fname, max_f, delta_f)
    plot(Bf, "Bn_LPF", fname, max_f, delta_f)
    plot(Hf, "Hn_LPF", fname, max_f, delta_f)

