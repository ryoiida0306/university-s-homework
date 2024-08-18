import sys
up_path = "../"
kadai1_path = "../kadai1/"
sys.path.append(kadai1_path)
sys.path.append(up_path)

import numpy as np
import matplotlib.pyplot as plt
from filename import fname
from binary import fdata

sampling_rate = 16000
max_time = 0.1
fleng = int(max_time*sampling_rate)
time = np.linspace(0,max_time,fleng)
fdata_short = fdata[:fleng].copy()
if __name__ == "__main__" :
    plt.figure(figsize=(10,4))
    plt.plot(time,fdata_short)
    plt.title("Waveform of First 100ms")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.savefig("../figure/dataplot_{}.pdf".format(fname))
