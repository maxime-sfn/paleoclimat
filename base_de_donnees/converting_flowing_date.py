import pandas as pd

chemin_csv = "/home/gaspard/paleoclimat/base_de_donnees/Full_flowering_dates_sakura_kyoto.csv"

df = pd.read_csv(chemin_csv, encoding='utf-8')

for i in range (2,len(df)): 
    if df.iloc[i,1]==0:
        pass
    elif df.iloc[i,1] < 400:
        df.iloc[i,1] = (df.iloc[i,1] - 300 + (31+28+31) - 122)%365
    else:
        df.iloc[i,1] = (df.iloc[i,1]- 400 + (31+28+31+30) -122)%365

# Chemin vers le nouveau fichier CSV
nouveau_chemin_csv = "/home/gaspard/paleoclimat/base_de_donnees/Full_flowering_dates_sakura_kyoto_updated.csv"

# Enregistrer les modifications dans un nouveau fichier CSV
df.to_csv(nouveau_chemin_csv, index=False, encoding='utf-8')
