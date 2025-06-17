import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
import csv
from time_series import CherryData, Years

# === Constantes ===
R = 8.314  # J/mol·K
Ts = 288.2  # K (température de référence)
Ea = 56000  # J/mol (énergie d'activation)
D = 164  # Jour de début d’accumulation
DTS_target = 30  # Seuil cumulé empirique

# === Fonctions ===
def daily_dts(T_C):
    T_K = T_C + 273.15
    return np.exp(Ea * (T_K - Ts) / (R * T_K * Ts))

def cumulative_dts(T_C, DOY):
    days = DOY - D
    return np.sum([daily_dts(T_C) for _ in range(days)]) if days > 0 else 0

def estimate_temperature_from_doy(DOY):
    def equation(T): return cumulative_dts(T, DOY) - DTS_target
    try:
        sol = root_scalar(equation, bracket=[0, 20], method='brentq')
        return sol.root if sol.converged else np.nan
    except ValueError:
        return np.nan

# === Reconstruction de température ===
estimated_temperatures = [estimate_temperature_from_doy(doy) for doy in CherryData]

# === Premier graphique : reconstruction brute ===
plt.figure(figsize=(12, 6))
plt.plot(Years, estimated_temperatures, 'x', color='blue', label="Reconstruction")
plt.xlabel("Année", fontsize=16)
plt.ylabel("Température moyenne estimée (°C)", fontsize=16)
plt.title("Reconstruction par modèle d’Arrhenius", fontsize=20)
plt.grid(True)
plt.tick_params(axis='both', labelsize=14)
plt.legend(fontsize=14)
plt.tight_layout()
plt.show()

# === Fonction de lissage améliorée ===
def lissage(x, y, nb_annee, save_csv=False, csv_filename="smoothed_data.csv"):
    def moving_average(data, window_size):
        return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

    y_smoothed = moving_average(y, nb_annee)
    x_smoothed = x[nb_annee - 1:]

    # Enregistrement CSV si demandé
    if save_csv:
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Year', 'SmoothedTemperature'])
            writer.writerows(zip(x_smoothed, y_smoothed))

    # Affichage graphique
    plt.figure(figsize=(12, 6))
    plt.plot(x_smoothed, y_smoothed, linewidth=2, label=f"Lissage ({nb_annee} ans)")
    plt.xlabel("Année", fontsize=16)
    plt.ylabel("Température moyenne estimée (°C)", fontsize=16)
    plt.title(f"Lissage sur {nb_annee} ans — Reconstruction Arrhenius", fontsize=20)
    plt.grid(True)
    plt.tick_params(axis='both', labelsize=14)
    plt.legend(fontsize=14)
    plt.tight_layout()
    plt.show()

# === Graphiques de lissage ===
lissage(Years, estimated_temperatures, 10, save_csv=True, csv_filename="lissage_10_years.csv")
lissage(Years, estimated_temperatures, 20)
lissage(Years, estimated_temperatures, 30)
lissage(Years, estimated_temperatures, 40)
