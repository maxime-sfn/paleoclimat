import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Affichage:
    def __init__(self, dataFilename):
        self.data = pd.read_csv(dataFilename)
        
        self.year_label = self.data.columns[0] # Get the name of the first column
        self.doyLabel = self.data.columns[1]
                
        self.year = self.data.iloc[:, 0].tolist() # Convert the first column to a list
        self.cherryDates = self.data.iloc[:, 1].tolist() # Convert the second column to a list
        
    def filterdCherryDates(self):
        cherryDates = []
        
        for date in self.cherryDates:
            if date == 0 :
                cherryDates.append(np.nan)
            else :
                cherryDates.append(date - (30 + 30 + 31))
        return cherryDates
        
    def displayCherryDates(self):
        
        cherryDates = self.filterdCherryDates()
        
        plt.scatter(self.year, cherryDates, color='b', marker='x', label='Cheery blossom')
        plt.plot(self.year, cherryDates, linestyle='dashed', color='gray', alpha=0.5)  # Connect the points
        plt.xlabel(f"{self.year_label}")
        plt.ylabel(f"DOY from December 1st")
        plt.title('Cherry Blossoms dates of sakuras in Tokyo (DOY with beggining 01/12) ')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    def displayCherryDatesChunks(self, chunk_size=200):
        cherryDates = self.filterdCherryDates()
        
        min_year, max_year = min(self.year), max(self.year)
        num_chunks = (max_year - min_year) // chunk_size + 1

        for i in range(num_chunks):
            start_year = min_year + i * chunk_size
            end_year = start_year + chunk_size

            # Filter data for this chunk
            indices = [j for j, y in enumerate(self.year) if start_year <= y < end_year]
            years_chunk = [self.year[j] for j in indices]
            dates_chunk = [cherryDates[j] for j in indices]

            if not years_chunk:  # Skip empty chunks
                continue

            # Create a new figure for each chunk
            plt.figure(figsize=(10, 5))
            plt.scatter(years_chunk, dates_chunk, color='b', marker='x', label='Cherry Blossoms')
            plt.plot(years_chunk, dates_chunk, linestyle='dashed', color='gray', alpha=0.5)
            plt.xlabel(self.year_label)
            plt.ylabel("DOY from Dec 1st")
            plt.title(f'Cherry Blossom Dates in Tokyo (DOY with beggining 01/12) ({start_year}-{end_year-1})')
            plt.legend()
            plt.grid(True)

            # Show and wait before plotting the next figure
            plt.show()
        
Affichage = Affichage("data.csv")
Affichage.displayCherryDates()
Affichage.displayCherryDatesChunks()