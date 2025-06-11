import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# === Chargement des données ===
temp_df = pd.read_csv("Temp_Moyenne_mesurées_Beaune_1850_2024.csv")
vend_df = pd.read_csv("Vendanges_beaune_1355_2018.csv")

# === Renommage des colonnes ===
temp_df = temp_df.rename(columns={temp_df.columns[0]: "year", temp_df.columns[1]: "temperature"})
vend_df = vend_df.rename(columns={vend_df.columns[0]: "year", vend_df.columns[1]: "vendanges_julian"})

# === Filtrage des années utiles et suppression des valeurs manquantes ===
temp_df = temp_df[temp_df['year'].between(1850, 2024)].dropna()
vend_df = vend_df[vend_df['year'].between(1355, 2018)].dropna()

# === Fusion des deux jeux de données pour l'entraînement
merged_df = pd.merge(temp_df, vend_df, on="year")
train_df = merged_df[merged_df['year'] >= 1875]

# === Données d'entraînement
X_train = train_df[['vendanges_julian']].values
y_train = train_df['temperature'].values

# === Standardisation
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# === Données à prédire : toutes les années avec vendanges
X_all_years = vend_df[['vendanges_julian']].values
X_all_scaled = scaler.transform(X_all_years)

# === Modèle (6,6,6)
model = Sequential()
model.add(Dense(6, activation='relu', input_shape=(1,)))
model.add(Dense(6, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# === Entraînement
model.fit(X_train_scaled, y_train, epochs=500, batch_size=32, verbose=0)

# === Prédiction
Y = model.predict(X_all_scaled).flatten()
X = vend_df['year'].values

print(X)
print(Y)

# === Affichage (facultatif)
plt.figure(figsize=(12, 6))
plt.plot(X, Y, label="Température prédite (1355–2018)", color="blue")
plt.plot(train_df['year'], train_df['temperature'], label="Mesures réelles (1875–2018)", color="red", linestyle="--")
plt.xlabel("Année")
plt.ylabel("Température (°C)")
plt.title("Reconstruction de la température (1355–2018) par réseau de neurones")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
