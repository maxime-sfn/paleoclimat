import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from time_series import Temp_data, Years, Lake_data, Lake_training_data

# Define the non-linear regression model (for example, inverse model)
def model(params, lake_data):
    a, b, c = params
    return a / (lake_data - b) + c

# Define the RSS function to minimize
def rss(params, temp_data, doy_data):
    predicted_doy = model(params, temp_data)
    residuals = doy_data - predicted_doy
    return np.sum(residuals ** 2)

result = minimize(rss, [100,0,80], args=(Lake_training_data, Temp_data), method='Nelder-Mead')

fitted_params = result.x

temperature_reconstruite = [model(fitted_params,x) for x in Lake_data]

np.savetxt(rf'..\corelation\finalnd.csv', temperature_reconstruite.reshape(1, -1), delimiter=',', fmt='%d')

plt.scatter(Years, temperature_reconstruite, color='b', marker='x')
plt.plot(Years, temperature_reconstruite, linestyle='dashed', color='gray', alpha=0.5)
plt.xlabel(f"years")
plt.ylabel("temperature")
plt.title(f'regression')
plt.show()