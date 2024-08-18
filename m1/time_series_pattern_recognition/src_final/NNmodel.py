##### Exercise(6) example
##### (c) G.Tanaka @ NITech

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import torch
import torch.nn as nn
import torch.nn.functional as func
import torch.optim as optim
import torch.utils.data as data
from makedata import ECGdata

# np.random.seed(0)
    
# # import data (y.year)
# data_y = sm.datasets.get_rdataset('y.year')
# y = np.array(data_y.data.value).reshape(-1,1)
# month = np.array(data_y.data.time).reshape(-1,1)

colum = 1
N = 500
y = ECGdata[:,colum].reshape(-1,1)
loadparam = 0
checkpoint = 1000
# y = pd.Series(y)

# divide into training and test data
train_ratio = N/len(y)
len_train = int(train_ratio*len(y))
len_test = len(y)-int(train_ratio*len(y))
s_train = y[:len_train]
s_test = y[len_train:]

# transform dataset to a tensor form for applying torch tools
def transform_dataset(dataset, lookback):
    X, y = [], []
    for i in range(len(dataset)-lookback):
        feature = dataset[i:i+lookback]
        target = dataset[i+1:i+lookback+1]
        X.append(feature)
        y.append(target)
    return torch.tensor(X).float(), torch.tensor(y).float()

lookback = 3  # window size
X_train, y_train = transform_dataset(s_train, lookback=lookback)
X_test, y_test = transform_dataset(s_test, lookback=lookback)

# set RNN model
class set_model(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=1, hidden_size=20, num_layers=1, batch_first=True)
        self.dropout = nn.Dropout(0.5)
        self.linear = nn.Linear(20, 1)
        self.relu = nn.ReLU()
    def forward(self, x):
        x, _ = self.lstm(x)
        x = self.dropout(x)
        batch_size, seq_len, hidden_size = x.size()
        x = x.reshape(batch_size * seq_len, hidden_size)
        x = self.linear(x)
        x = x.reshape(batch_size, seq_len, -1)
        x = self.relu(x)
        return x

# create model and determine the evaluation measure
model = set_model()
optimizer = optim.Adam(model.parameters())
loss_fn = nn.MSELoss()
loader = data.DataLoader(data.TensorDataset(X_train, y_train), shuffle=True, batch_size=8)

# training
if loadparam :
    model.load_state_dict(torch.load('parameters/NN/model_{}_{}.pth'.format(colum,checkpoint)))
    optimizer.load_state_dict(torch.load('parameters/NN/optimizer_{}_{}.pth'.format(colum,checkpoint)))
    model.eval()

n_epochs = 1001
for epoch in range(n_epochs):
    if loadparam :
        break
    model.train()
    for X_batch, y_batch in loader:
        y_pred = model(X_batch)
        loss = loss_fn(y_pred, y_batch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    # validation
    if epoch % 100 != 0:
        continue
    torch.save(model.state_dict(), 'parameters/NN/model_{}_{}.pth'.format(colum,epoch))
    torch.save(optimizer.state_dict(), 'parameters/NN/optimizer_{}_{}.pth'.format(colum,epoch))
    model.eval()
    with torch.no_grad():
        y_pred = model(X_train)
        train_rmse = np.sqrt(loss_fn(y_pred, y_train))
        y_pred = model(X_test)
        test_rmse = np.sqrt(loss_fn(y_pred, y_test))
    print("Epoch %d: train RMSE %.4f, test RMSE %.4f" % (epoch, train_rmse, test_rmse))
model.eval()

with torch.no_grad():
    # shift train predictions for plotting
    train_plot = np.ones_like(y) * np.nan
    y_pred = model(X_train)
    y_pred = y_pred[:, -1, :]
    train_plot[lookback:len_train] = model(X_train)[:, -1, :]
    # shift test predictions for plotting
    test_plot = np.ones_like(y) * np.nan
    test_plot[len_train+lookback:len(y)] = model(X_test)[:, -1, :]

# plot
plt.figure(figsize=(100, 5))  # グラフのサイズ指定
plt.plot(y, color='gray', label='Data')
plt.plot(train_plot, c='C0', label='Prediction (train)')
plt.plot(test_plot, c='C3', label='Prediction (test)')
plt.xlabel('$n$')
plt.title('y (yearly)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.savefig("../image/final/LSTM{}.pdf".format(colum), bbox_inches='tight')
# plt.show()


plt.figure()
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