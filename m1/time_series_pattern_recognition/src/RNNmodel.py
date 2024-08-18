##### Exercise(6) example
##### (c) G.Tanaka @ NITech

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import torch
import torch.nn as nn
import torch.nn.functional as func
import torch.optim as optim
import torch.utils.data as data

np.random.seed(0)
    
# import data (sunspot.year)
data_sunspot = sm.datasets.get_rdataset('sunspot.year')
sunspot = np.array(data_sunspot.data.value).reshape(-1,1)
month = np.array(data_sunspot.data.time).reshape(-1,1)

# divide into training and test data
train_ratio = 0.9
len_train = int(train_ratio*len(sunspot))
len_test = len(sunspot)-int(train_ratio*len(sunspot))
s_train = sunspot[:len_train]
s_test = sunspot[len_train:]

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
        self.lstm = nn.LSTM(input_size=1, hidden_size=50, num_layers=1, batch_first=True)
        self.linear = nn.Linear(50, 1)
    def forward(self, x):
        x, _ = self.lstm(x)
        x = self.linear(x)
        return x

# create model and determine the evaluation measure
model = set_model()
optimizer = optim.Adam(model.parameters())
loss_fn = nn.MSELoss()
loader = data.DataLoader(data.TensorDataset(X_train, y_train), shuffle=True, batch_size=8)

# training
n_epochs = 1000
for epoch in range(n_epochs):
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
    model.eval()
    with torch.no_grad():
        y_pred = model(X_train)
        train_rmse = np.sqrt(loss_fn(y_pred, y_train))
        y_pred = model(X_test)
        test_rmse = np.sqrt(loss_fn(y_pred, y_test))
    print("Epoch %d: train RMSE %.4f, test RMSE %.4f" % (epoch, train_rmse, test_rmse))

with torch.no_grad():
    # shift train predictions for plotting
    train_plot = np.ones_like(sunspot) * np.nan
    y_pred = model(X_train)
    y_pred = y_pred[:, -1, :]
    train_plot[lookback:len_train] = model(X_train)[:, -1, :]
    # shift test predictions for plotting
    test_plot = np.ones_like(sunspot) * np.nan
    test_plot[len_train+lookback:len(sunspot)] = model(X_test)[:, -1, :]

# plot
plt.plot(sunspot, color='gray', label='Data')
plt.plot(train_plot, c='C0', label='Prediction (train)')
plt.plot(test_plot, c='C3', label='Prediction (test)')
plt.xlabel('$n$')
plt.title('Sunspot (yearly)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.savefig("../image/LSTM.pdf", bbox_inches='tight')
# plt.show()