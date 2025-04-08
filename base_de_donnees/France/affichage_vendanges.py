import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dates_vendanges_complete_1484_1879.csv")

plt.figure(figsize=(12, 6))
plt.plot(df['Annee'], df['Valeur'], marker='o')
plt.title("Dates des vendanges (1484-1879), Moyenne: France du Nord-Est, Suisse Romane et Region sud-Rhenane")
plt.xlabel("Année")
plt.ylabel("Nombre de jours après le 1 Septembre")
plt.grid(True)
plt.tight_layout()
plt.show()

min_year = df['Annee'].min()
max_year = df['Annee'].max()
segments = list(range(min_year, max_year + 1, 100))

for start in segments:
    end = min(start + 99, max_year)
    segment_df = df[(df['Annee'] >= start) & (df['Annee'] <= end)]
    
    plt.figure(figsize=(10, 4))
    plt.plot(segment_df['Annee'], segment_df['Valeur'], marker='o')
    plt.title(f"Dates des vendanges ({start}-{end})")
    plt.xlabel("Année")
    plt.ylabel("Nombre de jours après le 1 Septembre")
    plt.grid(True)
    plt.tight_layout()
    plt.show()