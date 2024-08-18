import sys
up_path =  "../"
kadai1_path = "../kadai1/"
kadai2_path = "../kadai2/"
sys.path.append(up_path)
sys.path.append(kadai1_path)
sys.path.append(kadai2_path)

import numpy as np
import matplotlib.pyplot as plt
from filename import fname
from binary import fdata
from mydataplot import fleng, time

downbit = 8 #or 12

def normalization(data) :
    full_scale = 32767
    minus_3dbfs = full_scale / np.sqrt(2)

    # 正規化
    normal_scale = minus_3dbfs/data.max()
    norm_data = (data*normal_scale).astype(int)
    return norm_data

def down(data, downbit) :
    size = 1 << downbit
    down_data = (data/size).astype(int)
    down_data = down_data*size

    return down_data

if __name__ == "__main__" :
    norm_data = normalization(fdata)
    down_data = down(norm_data, downbit)
    data_short = down_data[:fleng]

    plt.figure(figsize=(10,4))
    plt.plot(time,data_short)
    plt.title("Waveform of First 100ms")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.savefig("../figure/dataplot_{}bit_{}.pdf".format(16-downbit,fname))
