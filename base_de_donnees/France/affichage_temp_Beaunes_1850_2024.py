import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Temp_Moyenne_mesurées_Beaune_1850_2024.csv")
df = df[["Year", "Annual"]]
df["Annual"] = df["Annual"] + 11

plt.figure(figsize=(14, 6))
plt.plot(df["Year"], df["Annual"])
plt.title("Températures moyennes annuelles à Beaune (1850-2024)")
plt.xlabel("Année")
plt.ylabel("Température moyenne (°C)")
plt.grid(True)
plt.show()