import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from regression import temperature_reconstruite
from time_series import Temp_data, Years

pred_temp = temperature_reconstruite[271:]
years_focus = Years[271:]

def square_error(a,b):
    out = 0
    for i in range(len(a)):
        out += (a[i]-b[i])**2
    out = np.sqrt(out)
    return out

def list_of_error(a,b):
    out = []
    for i in range(len(a)):
        out.append(abs(a[i]-b[i]))
    return out

print(square_error(pred_temp,Temp_data))

err = list_of_error(pred_temp,Temp_data)

plt.scatter(years_focus, pred_temp, color='b', marker='x')
plt.plot(years_focus, err, color='gray', alpha=0.5)
plt.scatter(years_focus,Temp_data,color='r', marker='o')
plt.xlabel(f"years")
plt.ylabel("temperature")
plt.title(f'Regression error comparison')
plt.show()