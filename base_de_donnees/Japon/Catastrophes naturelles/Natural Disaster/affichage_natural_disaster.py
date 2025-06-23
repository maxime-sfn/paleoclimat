import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Affichage:
    def __init__(self, dataName):
        self.data = pd.read_csv(dataName, sep=',')
        self.yearLabel = self.data.columns[0]
        self.labels = self.data.columns[1:]  # toutes les colonnes sauf la première

        self.years = self.data.iloc[:, 0].tolist()
        self.series = {label: self.data[label].tolist() for label in self.labels}

    def affichageDVI(self):
        plt.style.use("seaborn-v0_8-whitegrid")
        plt.figure(figsize=(14, 7))

        # Liste de couleurs distinctes
        colors = [
            "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",
            "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22"
        ]

        for idx, (label, values) in enumerate(self.series.items()):
            # Filtrer les années et valeurs non nulles
            filtered_years = [year for year, val in zip(self.years, values) if val > 0]
            filtered_values = [val for val in values if val > 0]

            if filtered_years:  # S'assurer qu'il y a quelque chose à afficher
                plt.plot(
                    filtered_years,
                    filtered_values,
                    label=label.replace("_", " ").capitalize(),
                    color=colors[idx % len(colors)],
                    linewidth=2,
                    marker='o',
                    markersize=5,
                    alpha=0.8
                )

        plt.xlabel(self.yearLabel, fontsize=12)
        plt.ylabel("Nombre d'événements", fontsize=12)
        plt.title("Évolution des catastrophes naturelles au fil des années", fontsize=14, fontweight='bold')
        plt.legend(title="Type de catastrophe", loc='upper left', bbox_to_anchor=(1.02, 1))
        plt.grid(True)
        plt.tight_layout()
        plt.show()

# Utilisation
affichage = Affichage('natural_disaster_data.csv')
affichage.affichageDVI()