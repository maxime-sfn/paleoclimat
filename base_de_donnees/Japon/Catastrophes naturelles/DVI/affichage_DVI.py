import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Affichage:
    def __init__(self, dataName):
        self.data = pd.read_csv('donnees_DVI.csv', sep = ',')
        self.yearLabel = self.data.columns[0]
        self.dviLabel = self.data.columns[1]
        
        self.years = self.data.iloc[:, 0].tolist()
        self.dvi = self.data.iloc[:, 1].tolist()
        
    def affichageDVI(self):
        plt.scatter(self.years, self.dvi, color='b', marker='o')
        plt.plot(self.years, self.dvi, linestyle='dashed', color='gray', alpha=0.5)  # Relie les points

        plt.xlabel(f"{self.yearLabel}")
        plt.ylabel(f"DVI (Dust Veil Index)")
        plt.legend()
        plt.grid(True)

        plt.show()
        
Affichage = Affichage('donnees_DVI.csv')
Affichage.affichageDVI()