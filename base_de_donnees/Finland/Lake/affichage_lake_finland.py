import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Affichage:
    def __init__(self, dataFilename):
        self.data = pd.read_csv(dataFilename)
        
        self.year_label = self.data.columns[2] # Get the name of the first column
        self.month_label = self.data.columns[3]
        self.year_label = self.data.columns[4]
                
        self.year = self.data.iloc[:, 2].tolist() # Convert the first column to a list
        self.month = self.data.iloc[:, 3].tolist()
        self.day = self.data.iloc[:, 4].tolist()
        
        self.doy = []
        
        for i in range(len(self.month)):
            days = 0
            if self.month[i] == 4 :
                days = 31 + 28 + 31 + self.day[i]
            if self.month[i] == 5 :
                days = 31 + 28 + 31 + 30 + self.day[i]
            if self.month[i] == 6 :
                days = 31 + 28 + 31 + 30 + 31 + self.day[i]
            if self.year[i] % 4 == 0: # Si année bisextile
                days += 1
            self.doy.append(days)
            
    def displayFreezeOfDates(self):
        
        plt.scatter(self.year, self.doy, color='b', marker='.')
        plt.plot(self.year, self.doy, linestyle='dashed', color='gray', alpha=0.5)  # Connect the points
        plt.xlabel(f"Years")
        plt.ylabel(f"DOY")
        plt.title('DOY for unfreezing dates of the river TORNIONJOKI in Finland')
        plt.legend()
        plt.grid(True)
        plt.show()
        
Affichage = Affichage("data.csv")
Affichage.displayFreezeOfDates()