import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Affichage:
    def __init__(self, dataFilename):
        self.data = pd.read_csv(dataFilename, sep=';', encoding='utf-8')
        # La première colonne contient les décennies
        self.decades = self.data.iloc[:, 0].tolist()
        self.decades = [int(d) for d in self.decades]  # Convertir les décennies en entiers
        print(self.decades)
        # Les colonnes suivantes contiennent les tailles des anneaux pour chaque année de la décennie
        self.yearly_sizes = self.data.iloc[:, 1:]
        
        # Transformer les données pour obtenir une liste d'années et de tailles correspondantes
        self.years = []
        self.sizes = []
        for i, decade in enumerate(self.decades):
            for j in range(10):  # Chaque décennie contient 10 années
                year = decade + j
                size = self.yearly_sizes.iloc[i, j]
                self.years.append(year)
                self.sizes.append(size)
        print(self.years,self.sizes)
    def displayTreeRingsChunks(self, chunk_size=200):
        
        plt.figure(figsize=(10, 5))
        plt.scatter(self.years, self.sizes, color='b', marker='x', label='Ring size')
        plt.plot(self.years, self.sizes, linestyle='none', color='gray', alpha=0.5)
        plt.xlabel("Year")
        plt.ylabel("Ring size (mm)")
        plt.title("Tree Ring Sizes of Cypress Over Time near Suwa, Japan")
        plt.legend()
        plt.grid(True)
        plt.show()

        
Affichage = Affichage("dendrochronology_suwa.csv")
Affichage.displayTreeRingsChunks()