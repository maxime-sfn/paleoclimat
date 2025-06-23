import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Affichage:
    def __init__(self, dataName):
        self.data = pd.read_csv(dataName, sep=',')
        self.yearLabel = self.data.columns[0]
        self.labels = self.data.columns[1:]  # Toutes les catastrophes sauf l'année

        self.years = self.data[self.yearLabel].tolist()
        # Calcul de la somme de toutes les catastrophes naturelles par année
        self.total_per_year = self.data[self.labels].sum(axis=1).tolist()

    def affichageTotalCatastrophes(self):
        plt.style.use("seaborn-v0_8-whitegrid")
        plt.figure(figsize=(12, 6))
        plt.plot(self.years, self.total_per_year, color='#e74c3c', linewidth=2.5, marker='o', markersize=5, label='Total catastrophes')
        
        plt.xlabel(self.yearLabel, fontsize=12)
        plt.ylabel("Nombre total de catastrophes", fontsize=12)
        plt.title("Évolution annuelle du nombre total de catastrophes naturelles", fontsize=14, fontweight='bold')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

# Utilisation
affichage = Affichage('natural_disaster_data.csv')
affichage.affichageTotalCatastrophes()
