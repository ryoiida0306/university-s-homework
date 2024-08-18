# csvモジュールを使ってCSVファイルから1行ずつ読み込む
import csv
import numpy as np
import matplotlib.pyplot as plt

# CSVファイルのパス
fn = "AirQualityUCI"
file_path = "./data/"+ fn +".csv"

# データの読み込み
data = np.genfromtxt(file_path, delimiter=';', skip_header=1, dtype=None, encoding=None)

# データの表示
# print(data)
# output_file = "myfile.txt"
# np.savetxt(output_file, data, delimiter=';', fmt='%s')
# print(data[0][10])
# print(data[9356][10])

cpdata = np.zeros((1000,17))
# print(cpdata.shape)

for i in range(1000):
    for j in range(17):
        if j == 0 : continue
        if j == 1 : continue
        if j == 2 : continue
        if j == 5 : continue
        if j >= 12 : continue
        # print(data[0][0])
        # print(j)
        cpdata[i][j] = data[i][j];
        if data[i][j] == -200:
            if i > 0:
                cpdata[i][j] = cpdata[i-1][j]
# data2 = data[:, 7]

data1 = cpdata[:, 10]
data2 = cpdata[:, 11]