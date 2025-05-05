"""import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import GridSearchCV
from time_series import KyotoTemperature, CherryDataTest, Years, CherryData
import matplotlib.pyplot as plt
from regression import temperature_reconstruite, lisser_et_afficher
# Input: cherry dates, Output: March temperatures
train_X = np.array(CherryDataTest).reshape(-1, 1)
train_Y = np.array(KyotoTemperature).reshape(-1)

# Model training
def train_model(X, Y):
    param_grid = {'alpha': 10.0 ** -np.arange(1, 5)}
    grid = GridSearchCV(
        MLPRegressor(solver='adam', hidden_layer_sizes=(4), max_iter=10000),
        param_grid,
        cv=3
    )
    grid.fit(X, Y)
    return grid.best_estimator_

# Train the model
model = train_model(train_X, train_Y)

# Stockage de l'évolution de l'erreur (loss curve)
error_evolution = model.loss_curve_

# Affichage de l'évolution de l'erreur
plt.figure()
plt.plot(error_evolution)
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Evolution of Training Error (Loss)')
plt.show()


data_X = np.array(CherryData).reshape(-1,1)

# Reconstruct March temperature from cherry blossom data
temperature_reconstructed = model.predict(data_X)

lisser_et_afficher(temperature_reconstructed,10,Years)

plt.plot(Years, temperature_reconstructed, label='Predicted Temperature with Neural Network', linestyle='--', color="b")
#plt.plot(Years, temperature_reconstruite, label='Predicted Temperature with Regression', linestyle='-',color='g')
plt.xlabel('Year')
plt.ylabel('March Mean Temperature (°C)')
plt.title('Reconstructed March Temperature from Cherry Blossom DOY')
plt.legend()
plt.show()"""

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from time_series import KyotoTemperature, CherryDataTest, Years, CherryData
from regression import temperature_reconstruite, lisser_et_afficher

# Préparation des données
train_X = np.array(CherryDataTest).reshape(-1, 1)
train_Y = np.array(KyotoTemperature).reshape(-1, 1)
data_X = np.array(CherryData).reshape(-1, 1)

# Convertir en tenseurs torch
train_X_tensor = torch.tensor(train_X, dtype=torch.float32)
train_Y_tensor = torch.tensor(train_Y, dtype=torch.float32)
data_X_tensor = torch.tensor(data_X, dtype=torch.float32)

# Définition du modèle
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.hidden = nn.Linear(1, 1)
        self.relu = nn.ReLU()
        self.output = nn.Linear(1, 1)

    def forward(self, x):
        x = self.hidden(x)
        x = self.relu(x)
        x = self.output(x)
        return x

model = SimpleNN()

# Définition de la fonction de perte et de l'optimiseur
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Liste pour stocker l'évolution de l'erreur
error_evolution = []

# Boucle d'entraînement
num_epochs = 1000
for epoch in range(num_epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(train_X_tensor)
    loss = criterion(outputs, train_Y_tensor)
    loss.backward()
    optimizer.step()

    error_evolution.append(loss.item())

# Affichage de l'évolution de l'erreur
plt.figure()
plt.plot(error_evolution)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Evolution of Training Error (Loss)')
plt.show()

# Prédiction sur les nouvelles données
model.eval()
with torch.no_grad():
    predictions = model(data_X_tensor).numpy().flatten()

# Tracé et lissage comme avant
lisser_et_afficher(predictions, 40, Years)

plt.plot(Years, predictions, label='Predicted Temperature with Neural Network (PyTorch)', linestyle='--', color="b")
plt.plot(Years, temperature_reconstruite, label='Predicted Temperature with Regression', linestyle='-', color='g')
plt.xlabel('Year')
plt.ylabel('March Mean Temperature (°C)')
plt.title('Reconstructed March Temperature from Cherry Blossom DOY (PyTorch)')
plt.legend()
plt.show()