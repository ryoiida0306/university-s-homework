##### Exercise(5) example
##### (c) G.Tanaka @ NITech

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# import data (sunspot.year)
data_sunspot = sm.datasets.get_rdataset('sunspot.year')
y = data_sunspot.data.value
month = data_sunspot.data.time

# divide into training and test data
train_ratio = 0.9
len_train = int(train_ratio*len(y))
len_test = len(y)-int(train_ratio*len(y))
y_train = y[:len_train]
y_test = y[len_train:]


m = 10
# fit the model
model = sm.tsa.statespace.SARIMAX(y_train, trend='n', order=(m,0,1))
results = model.fit(disp=False)


path = "../logs/lecture5.log"
with open(path,'a') as f :
    f.write("m = {}\n".format(m))
    f.write("{}\n".format(results.summary()))  # check the information of the fitted model
    f.write("AIC = {}\n".format(results.aic))

# prediction (in training period)
y_pred_train = results.get_prediction()
y_pred_train_mean = y_pred_train.predicted_mean
y_pred_train_ci = y_pred_train.conf_int()

# prediction (in test period)
y_pred_test = results.get_forecast(len_test)
y_pred_test_mean = y_pred_test.predicted_mean
y_pred_test_ci = y_pred_test.conf_int()

# prediction error (RMSE)
SE = [(y_test.iloc[i]-y_pred_test_mean.iloc[i])**2 for i in range(len_test)]
RMSE = np.sqrt(np.mean(SE))
with open(path,'a') as f :
    f.write("RMSE = {}\n\n".format(RMSE))

# draw
plt.plot(np.arange(len(y)), y, color='gray', label='Data')
plt.plot(np.arange(len_train), y_pred_train_mean, color='C0', label='Prediction (train)')
plt.fill_between(np.arange(len_train), y_pred_train_ci.iloc[:,0], y_pred_train_ci.iloc[:,1], color='C0', label='Confidence interval', alpha=.2)
plt.plot(np.arange(len_train,len(y)), y_pred_test_mean, color='C3', label='Prediction (test)')
plt.fill_between(np.arange(len_train,len(y)), y_pred_test_ci.iloc[:,0], y_pred_test_ci.iloc[:,1], color='C3', label='Confidence interval', alpha=.2)
plt.xlabel('Year ($n$)')
plt.ylabel('Counts')
plt.title('Sunspot (yearly)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.savefig("../image/SS/ARMA({},1).pdf".format(m), bbox_inches='tight')
# plt.show()