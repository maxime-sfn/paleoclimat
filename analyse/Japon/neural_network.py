from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from regression import temperature_reconstruite
from time_series import CherryDataTest, Years


train_X = temperature_reconstruite[767:]
train_Y = CherryDataTest


#cross validation
grid = GridSearchCV(MLPClassifier(solver='adam', hidden_layer_sizes=(1)),{'alpha': 10.0 ** -np.arange(1, 5)}, cv = 3)
grid.fit(train_X,train_Y)
print(grid.best_params_)