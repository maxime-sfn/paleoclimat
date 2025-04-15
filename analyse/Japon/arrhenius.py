import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
from time_series import CherryData, Years

# Constants
R = 8.314  # J/mol·K
Ts = 288.2  # K (reference temperature)
Ea = 56000  # J/mol (activation energy)
D = 164  # Start day of accumulation (DOY 42 = 11 Feb because date of start was 01 september)
DTS_target = 30  # Empirical cumulative threshold (from the paper)

# Function to compute daily DTS from a temperature in Celsius
def daily_dts(T_C):
    T_K = T_C + 273.15
    return np.exp(Ea * (T_K - Ts) / (R * T_K * Ts))

# Function to compute cumulative DTS for a given T_C and DOY
def cumulative_dts(T_C, DOY):
    days = DOY - D
    if days <= 0:
        return 0
    return np.sum([daily_dts(T_C) for _ in range(days)])

def estimate_temperature_from_doy(DOY):
    def equation(T):
        return cumulative_dts(T, DOY) - DTS_target

    # Debug: print function values at the bracket edges
    f0 = equation(0)
    f20 = equation(20)
    print(f"DOY: {DOY}, f(0): {f0:.2f}, f(20): {f20:.2f}")

    try:
        sol = root_scalar(equation, bracket=[0, 20], method='brentq')
        return sol.root if sol.converged else np.nan
    except ValueError:
        return np.nan


# Estimate temperatures
estimated_temperatures = [estimate_temperature_from_doy(doy) for doy in CherryData]

# Plot
plt.plot(Years, estimated_temperatures, 'x', color='blue')
plt.xlabel("Year")
plt.ylabel("Estimated March Mean Temperature (°C)")
plt.title("Temperature Reconstruction Using Arrhenius Model")
plt.grid(True)
plt.show()
