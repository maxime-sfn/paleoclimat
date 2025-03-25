import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Affichage:
    def __init__(self, dataName):
        self.data = pd.read_csv('natural_disaster_data.csv', sep = ',')
        self.yearLabel = self.data.columns[0]
        self.stormLabel = self.data.columns[1]
        self.floodLabel = self.data.columns[2]
        self.long_rainLabel = self.data.columns[3]
        self.thunder_stormLabel = self.data.columns[4]
        self.whirl_windLabel = self.data.columns[5]
        self.droughtLabel = self.data.columns[6]
        self.hail_stormLabel = self.data.columns[7]
        self.heavy_snowLabel = self.data.columns[8]
        self.frostLabel = self.data.columns[9]

        self.years = self.data.iloc[:, 0].tolist()
        self.storm = self.data.iloc[:, 1].tolist()
        self.flood = self.data.iloc[:, 2].tolist()
        self.long_rain = self.data.iloc[:, 3].tolist()
        self.thunder_storm = self.data.iloc[:, 4].tolist()
        self.whirl_wind = self.data.iloc[:, 5].tolist()
        self.drought = self.data.iloc[:, 6].tolist()
        self.hail_storm = self.data.iloc[:, 7].tolist()
        self.heavy_snow = self.data.iloc[:, 8].tolist()
        self.frost = self.data.iloc[:, 9].tolist()
        
    def affichageDVI(self):
        
        plt.scatter(self.years, self.storm, color='b', marker='o', label='storm')
        plt.plot(self.years, self.storm, linestyle='dashed', color='gray', alpha=0.5)

        plt.scatter(self.years, self.flood, color='b', marker='o', label='flood')
        plt.plot(self.years, self.flood, linestyle='dashed', color='gray', alpha=0.5)

        plt.scatter(self.years, self.long_rain, color='b', marker='o', label='long rain')
        plt.plot(self.years, self.long_rain, linestyle='dashed', color='gray', alpha=0.5)

        plt.scatter(self.years, self.thunder_storm, color='b', marker='o', label='thunder storm')
        plt.plot(self.years, self.thunder_storm, linestyle='dashed', color='gray', alpha=0.5)

        plt.scatter(self.years, self.whirl_wind, color='b', marker='o', label='whirl wind')
        plt.plot(self.years, self.whirl_wind, linestyle='dashed', color='gray', alpha=0.5)

        plt.scatter(self.years, self.drought, color='b', marker='o', label='drought')
        plt.plot(self.years, self.drought, linestyle='dashed', color='gray', alpha=0.5)

        plt.scatter(self.years, self.hail_storm, color='b', marker='o', label='hail storm')
        plt.plot(self.years, self.hail_storm, linestyle='dashed', color='gray', alpha=0.5)

        plt.scatter(self.years, self.heavy_snow, color='b', marker='o', label='heavy snow')
        plt.plot(self.years, self.heavy_snow, linestyle='dashed', color='gray', alpha=0.5)

        plt.scatter(self.years, self.frost, color='b', marker='o', label='frost')
        plt.plot(self.years, self.frost, linestyle='dashed', color='gray', alpha=0.5)
        

        plt.xlabel(f"{self.yearLabel}")
        plt.legend()
        plt.grid(True)

        plt.show()
        
Affichage = Affichage('donnees_DVI.csv')
Affichage.affichageDVI()