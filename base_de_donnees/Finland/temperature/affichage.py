import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Affichage:
    def __init__(self, dataFilename):
        self.data = pd.read_csv(dataFilename)
        
        self.year_label = self.data.columns[0] # Get the name of the first column
        self.average_may_temp_label = self.data.columns[1]
                
        self.year = self.data.iloc[:, 0].tolist() # Convert the first column to a list
        self.avg_temp_may = self.data.iloc[:, 1].tolist() # Convert the second column to a list
        
    def displayAvgTemperatureMayFinland(self):
                
        plt.scatter(self.year, self.avg_temp_may, color='b', marker='x', label='Cheery blossom')
        plt.plot(self.year, self.avg_temp_may, linestyle='dashed', color='gray', alpha=0.5)  # Connect the points
        plt.xlabel(f"{self.year_label}")
        plt.ylabel(f"average_may_temperature")
        plt.title('Average May temperatures in Kemi-Tornio Airport')
        plt.show()
        
Affichage = Affichage("data.csv")
Affichage.displayAvgTemperatureMayFinland()