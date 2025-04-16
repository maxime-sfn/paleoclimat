import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Affichage:
    def __init__(self):
        self.data = pd.read_csv('natural_disaster_data.csv', sep=',')
        self.yearLabel = self.data.columns[0]
        self.categories = self.data.columns[1:].tolist()
        self.years = self.data.iloc[:, 0].tolist()
        self.values = [self.data[col].tolist() for col in self.categories]
        
    def affichageDVI(self):
        bar_width = 0.1  # Largeur des barres
        x = np.arange(len(self.years))  # Position des années sur l'axe x
        
        plt.figure(figsize=(12, 6))
        for i, (category, values) in enumerate(zip(self.categories, self.values)):
            plt.bar(x + i * bar_width, values, width=bar_width, label=category)
        
        plt.xlabel(f"{self.yearLabel}")
        plt.ylabel("Occurrences")
        plt.xticks(x + (bar_width * (len(self.categories) / 2)), self.years, rotation=45)
        plt.legend()
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.title("Occurrences des catastrophes naturelles par année")
        
        plt.show()
        
Affichage = Affichage()
Affichage.affichageDVI()