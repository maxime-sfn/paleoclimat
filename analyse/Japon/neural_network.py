import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import GridSearchCV
from time_series import KyotoTemperature, CherryDataTest, Years, CherryData

# Input: cherry dates, Output: March temperatures
train_X = np.array(CherryDataTest).reshape(-1, 1)
train_Y = np.array(KyotoTemperature).reshape(-1)

# Model training
def train_model(X, Y):
    param_grid = {'alpha': 10.0 ** -np.arange(1, 5)}
    grid = GridSearchCV(
        MLPRegressor(solver='adam', hidden_layer_sizes=(8,), max_iter=10000),
        param_grid,
        cv=3
    )
    grid.fit(X, Y)
    return grid.best_estimator_

# Train the model
model = train_model(train_X, train_Y)

data_X = np.array(CherryData).reshape(-1,1)

# Reconstruct March temperature from cherry blossom data
temperature_reconstructed = model.predict(data_X)

print(len(temperature_reconstructed))
print(len(Years))



import matplotlib.pyplot as plt

plt.plot(Years, temperature_reconstructed, label='Predicted Temperature', linestyle='--')
plt.xlabel('Year')
plt.ylabel('March Mean Temperature (°C)')
plt.title('Reconstructed March Temperature from Cherry Blossom DOY')
plt.legend()
plt.show()