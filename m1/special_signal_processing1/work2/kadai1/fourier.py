import sys
up_path = "../"
sys.path.append(up_path)

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
from filename import fname, fpath
import config


start_iter = config.start_iter
N = config.N
max_f = config.max_f
delta_f = config.delta_f

def brackman_window(t,T) :
    return 0.42 - 0.5*math.cos(2*math.pi*t/T) + 0.08*math.cos(4*math.pi*t/T)

def my_fourier(norm_data, sampling_rate, start_iter, N, max_f, delta_f) :

    Fs = sampling_rate

    data_from_window = np.zeros(len(norm_data))
    for i in range(N) :
        data_from_window[i] = norm_data[i+start_iter]*brackman_window(i,N)
    
    Af = np.zeros(int(max_f/delta_f + 1))
    Bf = np.zeros(int(max_f/delta_f + 1))

    for f in range(len(Af)) :
        for j in range(N) :
            Af[f] += data_from_window[j] * math.cos(2*math.pi/Fs*f*delta_f*j)
            Bf[f] += data_from_window[j] * math.sin(2*math.pi/Fs*f*delta_f*j)
        Af[f] *= 2/N
        Bf[f] *= 2/N
    return Af, Bf

def plot(Xn, Xn_name, fname, max_f, delta_f) :
    frequency = np.arange(0,max_f,delta_f)
    Xn = Xn[:len(frequency)]
    plt.figure(figsize=(10,4))
    plt.plot(frequency,Xn)
    plt.title("{}".format(Xn_name))
    plt.xlabel("frequency[Hz]")
    plt.ylabel("{}".format(Xn_name))
    plt.grid()
    plt.savefig("../figure/{}_{}.pdf".format(fname,Xn_name))
    plt.figure()


if __name__ == "__main__" :
    input_wav_file = fpath + ".wav"
    sampling_rate, data = wavfile.read(input_wav_file)
    norm_data = data/np.max(data)
    Af, Bf = my_fourier(norm_data, sampling_rate, start_iter, N, max_f, delta_f)
    Hf = np.sqrt(Af*Af + Bf*Bf)
    plot(Af, "An", fname, max_f, delta_f)
    plot(Bf, "Bn", fname, max_f, delta_f)
    plot(Hf, "Hn", fname, max_f, delta_f)