import math
import numpy as np


lambda_ans = 2.0

scale = 1.0/lambda_ans

N = 100
n = 10

data = np.zeros((n,N))

# 指数分布に従う乱数を生成
for i in range(n):
    data[i] = np.random.exponential(scale, N)

# print("Exponential random numbers:", data)

