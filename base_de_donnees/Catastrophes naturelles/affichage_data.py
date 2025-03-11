import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
data = pd.read_csv('donnees DVI.csv', sep = ',')

x = data.iloc[:, 0].tolist()
y = data.iloc[:, 1].tolist()

plt.scatter(x, y, color='b', marker='o', label='Points irréguliers')
plt.plot(x, y, linestyle='dashed', color='gray', alpha=0.5)  # Relier les points

plt.xlabel('Axe X')
plt.ylabel('Axe Y')
plt.title('Affichage de points à intervalles irréguliers')
plt.legend()
plt.grid(True)

plt.show()

'''

x = np.linspace(0,180, 100)
y = np.cos((np.pi/180)*x)**2

fig, ax = plt.subplots()
ax.plot(x, y)

plt.show()