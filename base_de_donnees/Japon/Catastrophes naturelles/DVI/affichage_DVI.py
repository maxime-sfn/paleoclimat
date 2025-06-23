import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Affichage:
    def __init__(self, dataName):
        self.data = pd.read_csv(dataName, sep=',')
        self.yearLabel = self.data.columns[0]
        self.dviLabel = self.data.columns[1]
        
        self.years = self.data.iloc[:, 0].tolist()
        self.dvi = self.data.iloc[:, 1].tolist()
        
    def affichageDVI(self):
        plt.style.use("seaborn-v0_8-whitegrid")
        plt.figure(figsize=(12, 6))

        # Courbe lissée
        plt.plot(self.years, self.dvi, linestyle='-', color='#3366cc', linewidth=2, label='Indice DVI')
        plt.scatter(self.years, self.dvi, color='#ff6600', s=50, alpha=0.8, edgecolors='k', label='Données')

        plt.xlabel(f"{self.yearLabel}", fontsize=12)
        plt.ylabel("DVI (Dust Veil Index)", fontsize=12)
        plt.title("Évolution de l'indice DVI au cours des années", fontsize=14, fontweight='bold')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# Utilisation
affichage = Affichage('donnees_DVI.csv')
affichage.affichageDVI()