import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Affichage:
    def __init__(self, dataFilename):
        self.data = pd.read_csv(dataFilename)
        
        self.year_label = self.data.columns[0] # Get the name of the first column
        self.taille_label = self.data.columns[1]
                
        self.year = self.data.iloc[:, 0].tolist() # Convert the first column to a list
        self.taille = self.data.iloc[:, 1].tolist() # Convert the second column to a list
        
    def filterdCherryDates(self):
        cherryDates = []
        
        for date in self.cherryDates:
            if date == 0 :
                cherryDates.append(np.nan)
            else :
                cherryDates.append(date - (30 + 30 + 31 + 31))
        return cherryDates

    '''    
    def displayCherryDates(self):
        
        cherryDates = self.filterdCherryDates()
        
        plt.scatter(self.year, cherryDates, color='b', marker='x', label='Irregular points')
        plt.plot(self.year, cherryDates, linestyle='dashed', color='gray', alpha=0.5)  # Connect the points
        plt.xlabel(f"{self.year_label}")
        plt.ylabel(f"{self.doyLabel}")
        plt.title('Cherry Blossoms dates of lake suwa (DOY with beggining 01/12) ')
        plt.legend()
        plt.grid(True)
        plt.show()
    '''

    def displayTreeRings(self):

        plt.scatter(self.year, self.taille, color='b', marker='x', label='Irregular points')
        plt.plot(self.year, self.taille, linestyle='dashed', color='gray', alpha=0.5)  # Connect the points
        plt.xlabel(f"{self.year_label}")
        plt.ylabel(f"{self.taille}")
        plt.title('Tree rings depuis 820 ')
        plt.legend()
        plt.grid(True)
        plt.show()

        
        
Affichage = Affichage("donne_tree_rings_europe_reformatees.csv")
Affichage.displayTreeRings()
