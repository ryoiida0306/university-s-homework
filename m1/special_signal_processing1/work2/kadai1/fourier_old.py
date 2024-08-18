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
t = config.t
n = config.n

def brackman_window(t,T) :
    return 0.42 - 0.5*math.cos(2*math.pi*t/T) + 0.08*math.cos(4*math.pi*t/T)

def my_fourier(norm_data, sampling_rate, start_iter, t, n) :

    Fs = sampling_rate
    N = int(Fs * t)

    data_from_window = np.zeros(len(norm_data))
    for i in range(N) :
        data_from_window[i] = norm_data[i+start_iter]*brackman_window(i,N)
    
    An = np.zeros(N)
    Bn = np.zeros(N)

    for i in range(N) :
        for j in range(N) :
            An[i] += data_from_window[j] * math.cos(2*math.pi/Fs*i*j)
            Bn[i] += data_from_window[j] * math.sin(2*math.pi/Fs*i*j)
        An[i] *= 2/N
        Bn[i] *= 2/N

    An_short = An[:n]
    Bn_short = Bn[:n]

    return An_short, Bn_short

def plot(Xn, Xn_name,fname, sampling_rate, t) :
    Ts = int(sampling_rate * t)
    time = np.arange(0,n)
    plt.figure(figsize=(10,4))
    markerline, stemlines, baseline = plt.stem(time, Xn, use_line_collection=True)
    markerline.set_markersize(1)

    # plt.plot(time,Xn)
    plt.title("{}".format(Xn_name))
    plt.xlabel("Hz")
    plt.ylabel("{}".format(Xn_name))
    plt.grid()
    plt.savefig("../figure/{}_{}.pdf".format(fname,Xn_name))

    plt.figure()

if __name__ == "__main__" :
    # 1. Read the 16-bit quantized .wav file
    input_wav_file = fpath + ".wav"
    sampling_rate, data = wavfile.read(input_wav_file)

    norm_data = data/np.max(data)

    An, Bn = my_fourier(norm_data, sampling_rate, start_iter, t, n)
    
    plot(An, "An", fname, sampling_rate, t)
    plot(Bn, "Bn", fname, sampling_rate, t)

    Hn = np.sqrt(An*An + Bn*Bn)
    plot(Hn, "Hn", fname, sampling_rate, t)

    # max_time = len(data)
    # fleng = int(max_time*sampling_rate)
    


    # 5. Write the processed data to a new .wav file
    # wavfile.write(output_wav_file, sampling_rate, down_data)

    # print("Processing complete. Output file saved as", output_wav_file)
