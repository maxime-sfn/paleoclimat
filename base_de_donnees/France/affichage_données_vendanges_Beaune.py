import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv("Vendanges_beaune.csv", skiprows=1, names=["Année", "Jour"])

# Nettoyage
df = df[pd.to_numeric(df["Année"], errors="coerce").notnull()]
df = df[pd.to_numeric(df["Jour"], errors="coerce").notnull()]
df["Année"] = df["Année"].astype(int)
df["Jour"] = df["Jour"].astype(int)

# Graphique global - avec traits
plt.figure(figsize=(18, 6))
plt.plot(df["Année"], df["Jour"], marker='o', linestyle='-', alpha=0.7)
plt.title("Vendanges à Beaune (Jour de l'année) - Global avec traits", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Jour de l'année", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

# Graphique global - points seuls
plt.figure(figsize=(18, 4))
plt.scatter(df["Année"], df["Jour"], s=15, color='orange')
plt.title("Vendanges à Beaune (Jour de l'année) - Points seuls", fontsize=16)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Jour de l'année", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

# Graphiques siècle par siècle
min_year = (df["Année"].min() // 100) * 100
max_year = ((df["Année"].max() // 100) + 1) * 100

for start_year in range(min_year, max_year, 100):
    end_year = start_year + 100
    df_period = df[(df["Année"] >= start_year) & (df["Année"] < end_year)]
    
    if df_period.empty:
        continue
    
    plt.figure(figsize=(14, 4))
    plt.plot(df_period["Année"], df_period["Jour"], marker='o', linestyle='-', alpha=0.7)
    plt.title(f"Vendanges à Beaune - {start_year} à {end_year - 1}", fontsize=14)
    plt.xlabel("Année", fontsize=11)
    plt.ylabel("Jour de l'année", fontsize=11)
    plt.grid(True)
    plt.tight_layout()
    plt.show()