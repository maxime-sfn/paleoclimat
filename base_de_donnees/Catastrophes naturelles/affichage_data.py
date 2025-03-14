import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('donnees_DVI.csv', sep = ',')

x_label = data.columns[0]
y_label = data.columns[1]

x = data.iloc[:, 0].tolist()
y = data.iloc[:, 1].tolist()

plt.scatter(x, y, color='b', marker='o', label='Points irréguliers')
plt.plot(x, y, linestyle='dashed', color='gray', alpha=0.5)  # Relier les points

plt.xlabel(f"AXE x : {x_label}")
plt.ylabel(f"AXE y : {y_label}")
plt.title('Affichage de points à intervalles irréguliers')
plt.legend()
plt.grid(True)

plt.show()