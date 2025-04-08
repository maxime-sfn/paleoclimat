import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from regression import temperature_reconstruite
from time_series import KyotoTemperature, Years

pred_temp = temperature_reconstruite[767:]
years_focus = Years[767:]

print(len(pred_temp))
print(len(KyotoTemperature))

def square_error(a,b):
    out = 0
    for i in range(len(a)):
        out += (a[i]-b[i])**2
    out = np.sqrt(out)
    return out

def list_of_error(a,b):
    out = []
    for i in range(len(a)):
        out.append((a[i]-b[i])**2)
    return out

print(square_error(pred_temp,KyotoTemperature))

err = [pred_temp[i] - KyotoTemperature[i] for i in range(len(pred_temp))]

plt.scatter(years_focus, pred_temp, color='b', marker='x')
plt.plot(years_focus, err, linestyle='dashed', color='gray', alpha=0.5)
plt.scatter(years_focus,KyotoTemperature,color='r', marker='o')
plt.xlabel(f"years")
plt.ylabel("temperature")
plt.title(f'Regression error comparison')
plt.show()
