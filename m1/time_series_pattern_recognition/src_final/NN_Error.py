from NNmodel import s_test,test_plot,colum,y
import matplotlib as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import torch
import torch.nn as nn
import torch.nn.functional as func
import torch.optim as optim
import torch.utils.data as data
from makedata import ECGdata


print(y.shape)
print(test_plot.shape)
error = (test_plot - y) * (test_plot - y)
# plot
plt.figure(figsize=(100, 5))  # グラフのサイズ指定
plt.plot(error, c='C3', label='Error')
plt.xlabel('$n$')
plt.title('y (yearly)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.savefig("../image/final/Error{}.pdf".format(colum), bbox_inches='tight')
# plt.show()