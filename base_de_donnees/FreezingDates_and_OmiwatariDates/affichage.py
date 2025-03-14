import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Affichage:
    def __init__(self, dataFilename):
        self.data = pd.read_csv(dataFilename)
        
        self.year_label = self.data.columns[0] # Get the name of the first column
        self.freezingDates_label = self.data.columns[1] # Get the name of the second column
        self.omiwatariDates_label = self.data.columns[2] # Get the name of the third column

        self.year = self.data.iloc[:, 0].tolist() # Convert the first column to a list
        self.freezingDates = self.data.iloc[:, 1].tolist() # Convert the second column to a list
        self.omiwatariDates = self.data.iloc[:, 2].tolist() # Convert the third column to a list

    def freezingDatesFilterd(self):
        freezingDates = []
        for date in self.freezingDates:
            if date != "no" and date != "did":
                freezingDates.append(int(date))
            else:
                freezingDates.append(np.nan)
        return freezingDates
    
    def omiwatariDatesFilterd(self):
        omiwatariDates = []
        for date in self.omiwatariDates:
            if date != "no" and date != "did":
                omiwatariDates.append(int(date))
            else:
                omiwatariDates.append(np.nan)
        return omiwatariDates

    def displayFreezingDates(self):
        
        freezingDates = self.freezingDatesFilterd()
        
        plt.scatter(self.year, freezingDates, color='b', marker='x', label='Irregular points')
        plt.plot(self.year, freezingDates, linestyle='dashed', color='gray', alpha=0.5)  # Connect the points
        plt.xlabel(f"{self.year_label}")
        plt.ylabel(f"{self.freezingDates_label}")
        plt.title('Freezing dates of lake suwa (DOY with beggining 01/12) ')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    def displayOmiwatariDates(self):
        
        omiwatariDates = self.omiwatariDatesFilterd()
        
        plt.scatter(self.year, omiwatariDates, color='b', marker='x', label='Irregular points')
        plt.plot(self.year, omiwatariDates, linestyle='dashed', color='gray', alpha=0.5)  # Connect the points
        plt.xlabel(f"{self.year_label}")
        plt.ylabel(f"{self.freezingDates_label}")
        plt.title('Omiwatari dates of lake suwa (DOY with beggining 01/12) ')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    def displayFreezingDatesAndOmiwatariDatesLength(self):
        
        freezingDates = self.freezingDatesFilterd()
        omiwatariDates = self.omiwatariDatesFilterd()
        
        freezingDuration = []
        
        for i in range(len(self.year)):
            freezingDuration.append(omiwatariDates[i] - freezingDates[i])
            print(omiwatariDates[i] - freezingDates[i])
        
        plt.scatter(self.year, freezingDuration, color='b', marker='x', label='Irregular points')
        plt.plot(self.year, freezingDuration, linestyle='dashed', color='gray', alpha=0.5)  # Connect the points
        plt.xlabel(f"{self.year_label}")
        plt.ylabel(f"Duration of the lake freezing period")
        plt.title('Omiwatari dates of lake suwa (DOY with beggining 01/12) ')
        plt.legend()
        plt.grid(True)
        plt.show()



Affichage = Affichage(rf"data.csv")
#Affichage.displayFreezingDates()
#Affichage.displayOmiwatariDates()
Affichage.displayFreezingDatesAndOmiwatariDatesLength()