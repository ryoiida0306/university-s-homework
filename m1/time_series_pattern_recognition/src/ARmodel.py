import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

np.random.seed(0)

# set parameters of AR(2) model
# Note: check the model expression in Appendix of the material
ar = np.r_[1, -0.9*np.sqrt(3), .81, -.1]
ma = np.r_[1]

# generate model and data
arma_process = sm.tsa.ArmaProcess(ar, ma)
N = 250  # number of samples
y = arma_process.generate_sample(N)

# division of data (70% for training, 30% for testing)
train_ratio = 0.7
len_train = int(train_ratio*len(y))
len_test = len(y)-len_train
y_train = y[:len_train]
y_test = y[len_train:]

# sample autocovariance
C = sm.tsa.stattools.acovf(y_train,nlag=3)

# Yule-Walker equation (Ta=s)
T = np.array([[C[0], C[1], C[2]], [C[1], C[0], C[1]], [C[2], C[1], C[0]]])
s = np.array([C[1], C[2], C[3]]).reshape(3,1)
a = np.dot(np.linalg.inv(T), s)
sigma2 = C[0]-a[0]*C[1]-a[1]*C[2]-a[2]*C[3]
sigma = np.sqrt(sigma2)
print('Estimated a: ', a)
print('Estimated sigma: ', sigma)

# estimation
y_est = [y[0],y[1],y[2]]  # initial condition
for n in range(3,len_train):
    tmp = a[0][0]*y[n-1] + a[1][0]*y[n-2] + a[2][0]*y[n-3]  # using observation
    y_est.append(tmp)

# prediction
y_pred = [y[len_train-3], y[len_train-2], y[len_train-1]]  # initial condition
for n in range(3,len(y)-len_train):
    tmp = a[0][0]*y_pred[n-1] + a[1][0]*y_pred[n-2] + a[2][0]*y_pred[n-3]
    y_pred.append(tmp)

# prediction error (RMSE)
SE = [(y_test[i]-y_pred[i])**2 for i in range(len(y)-len_train)]
RMSE = np.sqrt(np.mean(SE))
print('RMSE = ', RMSE)
    
# plot
# plt.figure(figsize=(10, 4))  # グラフのサイズ指定
plt.plot(y, color='gray', label='Data')
plt.plot(y_est[:len_train], 'b-', label='Estimation')
plt.plot(np.arange(len_train,len(y)), y_pred, 'r-', label='Prediction')
plt.xlabel('n')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.savefig("../image/AR(3).pdf", bbox_inches='tight')
# plt.show()