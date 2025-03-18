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
        
        plt.scatter(self.year, freezingDates, color='b', marker='x', label='Freezing dates')
        plt.plot(self.year, freezingDates, linestyle='dashed', color='gray', alpha=0.5)  # Connect the points
        plt.xlabel(f"{self.year_label}")
        plt.ylabel(f"{self.freezingDates_label}")
        plt.title('Freezing dates of lake suwa (DOY with beggining 01/12) ')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    def displayFreezingDatesChunks(self, chunk_size=200):
        cherryDates = self.freezingDatesFilterd()
        
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
            plt.scatter(years_chunk, dates_chunk, color='b', marker='x', label='Freezing dates')
            plt.plot(years_chunk, dates_chunk, linestyle='dashed', color='gray', alpha=0.5)
            plt.xlabel(self.year_label)
            plt.ylabel("DOY from Dec 1st")
            plt.title(f'Freezing dates of lake suwa (DOY with beggining 01/12) ({start_year}-{end_year-1})')
            plt.legend()
            plt.grid(True)

            # Show and wait before plotting the next figure
            plt.show()
        
    def displayOmiwatariDates(self):
        
        omiwatariDates = self.omiwatariDatesFilterd()
        
        plt.scatter(self.year, omiwatariDates, color='b', marker='x', label='Omiwatari points')
        plt.plot(self.year, omiwatariDates, linestyle='dashed', color='gray', alpha=0.5)  # Connect the points
        plt.xlabel(f"{self.year_label}")
        plt.ylabel(f"Duration of the lake freezing period (days)")
        plt.title('Omiwatari dates of lake suwa (DOY with beggining 01/12) ')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    def displayOmiwatariDatesChunks(self, chunk_size=200):
        cherryDates = self.omiwatariDatesFilterd()
        
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
            plt.scatter(years_chunk, dates_chunk, color='b', marker='x', label='Omiwatari dates')
            plt.plot(years_chunk, dates_chunk, linestyle='dashed', color='gray', alpha=0.5)
            plt.xlabel(self.year_label)
            plt.ylabel("DOY from Dec 1st")
            plt.title(f'Omiwatari dates of lake suwa (DOY with beggining 01/12) ({start_year}-{end_year-1})')
            plt.legend()
            plt.grid(True)

            # Show and wait before plotting the next figure
            plt.show()
        
    def displayFreezingDatesAndOmiwatariDatesLength(self):
        
        freezingDates = self.freezingDatesFilterd()
        omiwatariDates = self.omiwatariDatesFilterd()
        
        freezingDuration = []
        
        for i in range(len(self.year)):
            freezingDuration.append(omiwatariDates[i] - freezingDates[i])
            
        
        plt.scatter(self.year, freezingDuration, color='b', marker='x', label='Irregular points')
        plt.plot(self.year, freezingDuration, linestyle='dashed', color='gray', alpha=0.5)  # Connect the points
        plt.xlabel(f"{self.year_label}")
        plt.ylabel(f"Duration of the lake freezing period (days)")
        plt.title('Omiwatari dates of lake suwa (DOY with beggining 01/12) ')
        plt.legend()
        plt.grid(True)
        plt.show()



Affichage = Affichage(rf"data.csv")
Affichage.displayFreezingDates()
Affichage.displayOmiwatariDates()
Affichage.displayFreezingDatesAndOmiwatariDatesLength()
Affichage.displayFreezingDatesChunks()
Affichage.displayOmiwatariDatesChunks()