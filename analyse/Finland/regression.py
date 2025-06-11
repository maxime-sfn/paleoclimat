import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from time_series import Temp_data, Years, Lake_data, Lake_training_data

# Define the non-linear regression model
def model(params, lake_data):
    a, b, c = params
    return a / (lake_data - b) + c

# Define RSS to minimize
def rss(params, temp_data, doy_data):
    predicted_doy = model(params, temp_data)
    residuals = doy_data - predicted_doy
    return np.sum(residuals ** 2)

# Fit the model
result = minimize(rss, [100, 0, 80], args=(Lake_training_data, Temp_data), method='Nelder-Mead')
fitted_params = result.x

# Reconstruct temperature
temperature_reconstruite = np.array([model(fitted_params, x) for x in Lake_data])

# Build DataFrame
df = pd.DataFrame({
    'Year': Years,
    'Temp': temperature_reconstruite
})

# 10-year smoothing
df['Temp_Smooth10'] = df['Temp'].rolling(window=10, center=True).mean()

# === First Graph: Original reconstruction ===
plt.figure(figsize=(12, 6))
plt.scatter(df['Year'], df['Temp'], color='b', marker='x', label='Reconstructed')
plt.plot(df['Year'], df['Temp'], linestyle='dashed', color='gray', alpha=0.5)
plt.xlabel("Years", fontsize=16)
plt.ylabel("Temperature (°C)", fontsize=16)
plt.title("Reconstructed Temperature", fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.legend(fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()

# === Second Graph: 10-year smoothed ===
plt.figure(figsize=(12, 6))
plt.plot(df['Year'], df['Temp_Smooth10'], color='r', linewidth=2, label='10-year Smooth')
plt.xlabel("Years", fontsize=16)
plt.ylabel("Temperature (°C)", fontsize=16)
plt.title("10-Year Smoothed Temperature", fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.legend(fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()
