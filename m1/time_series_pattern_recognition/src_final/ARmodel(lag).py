import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from makedata import ECGdata
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
import pandas as pd

colum = 1

datalength = 5000
lag = 200  # ラグの数を200に設定
ECGdata = ECGdata[:datalength,...]
y = ECGdata[:,colum]

N = 3000
train_ratio = N/datalength
len_train = int(train_ratio*len(y))
len_test = len(y)-len_train
y_train = y[:len_train]
y_test = y[len_train:]


# ARモデルのフィッティング
model = AutoReg(y_train, lags=lag).fit()

# トレーニングデータに対する予測
pred_train = model.predict(start=lag, end=len_train-1, dynamic=False)

# テストデータに対する予測
pred_test = model.predict(start=len_train, end=len(ECGdata)-1, dynamic=False)

# 異常スコアの計算 (MSE)
anomaly_score_train = mean_squared_error(y_train[lag:], pred_train)
anomaly_score_test = mean_squared_error(y_test[:len(pred_test)], pred_test)

# 異常スコアの計算 (MSE)を手動で計算
anomaly_score_train = np.mean((y_train[lag:] - pred_train) ** 2)
anomaly_score_test = np.mean((y_test[:len(pred_test)] - pred_test) ** 2)

# 閾値の設定
# threshold = anomaly_score_train
threshold = 0.5

# 異常検知
anomalies = (y_test[:len(pred_test)] - pred_test) ** 2 > threshold

# プロット
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# 元のデータと予測データのプロット
ax1.plot(y, color='gray', label='Data')
ax1.plot(np.arange(lag, len_train), pred_train, c='C0', label='Prediction (train)')
ax1.plot(np.arange(len_train, len_train + len(pred_test)), pred_test, c='C3', label='Prediction (test)')
ax1.set_ylabel('Value')
ax1.set_title('Time Series Data')
ax1.legend(loc='upper left')

# 異常スコアのプロット
ax2.plot(np.arange(len_train, len_train + len(pred_test)), (y_test[:len(pred_test)] - pred_test) ** 2, color='blue', label='Anomaly Score')
ax2.axhline(threshold, color='red', linestyle='--', label='Threshold')
ax2.fill_between(np.arange(len_train, len_train + len(pred_test)), (y_test[:len(pred_test)] - pred_test) ** 2, threshold, where=anomalies, color='red', alpha=0.5, label='Anomalies')
ax2.set_ylabel('Anomaly Score')
ax2.set_xlabel('Time')
ax2.set_title('Anomaly Detection')
ax2.legend(loc='upper left')
plt.savefig("../image/final/AR({})0{}.pdf".format(lag,colum), bbox_inches='tight')
# plt.show()