import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from time_series import CherryDataTest, KyotoTemperature, CherryData, Years

# Define the non-linear regression model (for example, inverse model)
def model(params, cherry_data):
    a, b, c = params
    return a / (cherry_data - b) + c

# Define the RSS function to minimize
def rss(params, temp_data, doy_data):
    predicted_doy = model(params, temp_data)
    residuals = doy_data - predicted_doy
    return np.sum(residuals ** 2)

def lisser_et_afficher(data, y, abscisse): #y correspondant à la durée de lissages
    
    taille = len(data)
    data_moyenne = np.zeros(taille)


    for i in range(taille):
        if i >= y:
            somme = 0
            for x in range(i - y, i):
                somme += float(data[x])
            data_moyenne[i] = (1 / y) * somme
        else:
            somme = 0
            for x in range(i+1):
                somme += float(data[x])
            data_moyenne[i] = (1/(i+1)) * somme

    # Affichage courbe lissée seule
    plt.figure(figsize=(18, 6))
    plt.plot(abscisse, data_moyenne, label='Moyenne mobile', color='blue')
    plt.title("Courbe lissée")
    plt.xticks(rotation=60)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

result = minimize(rss, [100,0,80], args=(CherryDataTest, KyotoTemperature), method='Nelder-Mead')

fitted_params = result.x

temperature_reconstruite = [model(fitted_params,x) for x in CherryData]

lisser_et_afficher(temperature_reconstruite,10,Years)

plt.scatter(Years, temperature_reconstruite, color='b', marker='x')
plt.plot(Years, temperature_reconstruite, linestyle='dashed', color='gray', alpha=0.5)
plt.xlabel(f"years")
plt.ylabel("temperature")
plt.title(f'non-linear regression')
plt.show()