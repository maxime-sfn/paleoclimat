import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from time_series import KyotoTemperature, CherryDataTest, Years


train_X = np.array(KyotoTemperature).reshape(-1, 1)
train_Y = np.array(CherryDataTest).reshape(-1, 1)

def train_model(X,Y):
    grid = GridSearchCV(MLPClassifier(solver='adam', hidden_layer_sizes=(8)),{'alpha': 10.0 ** -np.arange(1, 5)}, cv = 3)
    grid.fit(X,Y)
    model = grid.best_estimator_
    return model

model = train_model(train_X,train_Y)

temperature_reconstruite = model.predict(train_Y)