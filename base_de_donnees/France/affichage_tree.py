import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Affichage:
    def __init__(self, dataFilename):
        self.data = pd.read_csv(dataFilename)
        print(self.data.columns[0])
        print(self.data.columns[1])
        self.year_label = self.data.columns[0] # Get the name of the first column
        self.taille_label = self.data.columns[1]
                
        self.year = self.data.iloc[:, 0].tolist() # Convert the first column to a list
        self.year = [int(y) for y in self.year] # Convert the years into integers
        self.taille = self.data.iloc[:, 1].tolist() # Convert the second column to a list

    def displayTreeRingsChunks(self, chunk_size=200):
        
        # min_year, max_year = min(self.year), max(self.year)
        min_year, max_year = 1820, max(self.year)
        num_chunks = (max_year - min_year) // chunk_size + 1

        for i in range(num_chunks):
            start_year = min_year + i * chunk_size
            end_year = start_year + chunk_size

            # Filter data for this chunk
            indices = [j for j, y in enumerate(self.year) if start_year <= y < end_year]
            years_chunk = [self.year[j] for j in indices]
            dates_chunk = [self.taille[j] for j in indices]

            if not years_chunk:  # Skip empty chunks
                continue

            # Create a new figure for each chunk
            plt.figure(figsize=(10, 5))
            plt.scatter(years_chunk, dates_chunk, color='b', marker='x', label='Ring size')
            plt.plot(years_chunk, dates_chunk, linestyle='dashed', color='gray', alpha=0.5)
            plt.xlabel("Year")
            plt.ylabel("Ring size (mm)")
            #plt.title(f'Tree rings size since 820 ({start_year}-{end_year-1})')
            plt.title(f'Tree rings size ({start_year}-1959)')
            plt.legend()
            plt.grid(True)

            # Show and wait before plotting the next figure
            plt.show()

    def displayTreeRings(self):

        plt.scatter(self.year, self.taille, color='b', marker='x', label='Irregular points')
        plt.plot(self.year, self.taille, linestyle='dashed', color='gray', alpha=0.5)  # Connect the points
        plt.xlabel(f"Year")
        plt.ylabel(f"Ring size (mm)")
        #plt.title('Tree rings size since 820 ')
        plt.title('Tree rings size')
        plt.legend()
        plt.grid(True)
        plt.show()

        
        
Affichage = Affichage("donne_tree_rings_europe_reformatees.csv")
Affichage.displayTreeRings()
Affichage.displayTreeRingsChunks()