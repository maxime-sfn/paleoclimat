import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load data
data = pd.read_csv("data.csv")

# Convert to datetime
data['Date'] = pd.to_datetime(data.iloc[:, 0], format="%m/%d/%Y")
data['Year'] = data['Date'].dt.year
data['DayOfYear'] = data['Date'].dt.dayofyear

# Pivot to a heatmap format
pivot_table = data.pivot(index='DayOfYear', columns='Year', values="Kyoto")

# Plot heatmap
plt.figure(figsize=(15, 6))
sns.heatmap(pivot_table, cmap="coolwarm", cbar=True)
plt.xlabel("Year")
plt.ylabel("Day of Year")
plt.title("Daily Temperature Heatmap in Kyoto (1955-2021)")
plt.show()