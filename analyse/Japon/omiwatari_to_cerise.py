import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# === Chargement des données ===
data_omiwatari = pd.read_csv(rf"..\..\base_de_donnees\Japon\FreezingDates_and_OmiwatariDates\data.csv")
data_cherry = pd.read_csv(rf"..\..\base_de_donnees\Japon\CherryBlossomFloweringDates\data.csv")

# === Prétraitement des données ===
# Extraire les années et les dates d'Omiwatari et de floraison des cerisiers
year_omiwatari = data_omiwatari.iloc[:, 0].tolist()
year_cherry = data_cherry.iloc[:, 0].tolist()
omiwatari_dates = data_omiwatari.iloc[:, 1].tolist()
cherry_dates = data_cherry.iloc[:, 1].tolist()

# Filtrer les années et dates valides
filtered = [(y, d) for y, d in zip(year_omiwatari, omiwatari_dates) if d != "no" and d != "did"]
year_omiwatari, omiwatari_dates = zip(*filtered) if filtered else ([], [])
year_omiwatari = list(year_omiwatari)
omiwatari_dates = list(omiwatari_dates)

# Retirer les entrées où les dates de floraison sont nulles (0)
year_cherry, cherry_dates = zip(*[(y, d) for y, d in zip(year_cherry, cherry_dates) if d != 0])
year_cherry = list(year_cherry)
cherry_dates = list(cherry_dates)

# Créer des DataFrames pour faciliter la manipulation
df_omiwatari = pd.DataFrame({
    'year': year_omiwatari,
    'omiwatari_doy': omiwatari_dates
})

df_cherry = pd.DataFrame({
    'year': year_cherry,
    'cherry_bloom_doy': cherry_dates
})

# Fusionner les deux DataFrames sur la colonne "year"
merged_df = pd.merge(df_omiwatari, df_cherry, on='year')

# Ajuster les dates de floraison des cerisiers (ajustement de 91 jours pour aligner les deux phénomènes)
merged_df['adjusted_cherry_bloom_doy'] = merged_df['cherry_bloom_doy'].apply(lambda x: int(x) - 91)

# === Séparation des données : entraînement (années récentes) et test (années plus anciennes) ===
train_df = merged_df[merged_df['year'] >= 1600]  # Sélectionner les années récentes pour l'entraînement
test_df = merged_df[merged_df['year'] < 1600]   # Sélectionner les années anciennes pour le test

X_train = train_df[['omiwatari_doy']].values
y_train = train_df['adjusted_cherry_bloom_doy'].values
X_test = test_df[['omiwatari_doy']].values
y_test = test_df['adjusted_cherry_bloom_doy'].values

# === Standardisation des variables explicatives ===
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# === Définition d'une fonction de construction de modèle générique ===
def construire_modele(neurones_par_couche, activation='relu'):
    model = Sequential()
    model.add(Dense(neurones_par_couche[0], activation=activation, input_shape=(1,)))
    for n in neurones_par_couche[1:]:
        model.add(Dense(n, activation=activation))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

# === Dictionnaire de configurations à tester (nombre de couches et neurones) ===
configurations = {
    "2 couches (8,8)": [8, 8],
    "2 couches (16,8)": [16, 8],
    "3 couches (8,8,8)": [8, 8, 8],
}

# === Dictionnaire pour stocker les RMSE des différents modèles ===
resultats = {}

# === Boucle d'entraînement et d'évaluation ===
for nom_config, structure in configurations.items():
    
    modele = construire_modele(structure, activation='relu')
    modele.fit(X_train_scaled, y_train, epochs=500, batch_size=32, verbose=0)
    
    # Prédiction sur le jeu de données d'entraînement
    y_train_pred = modele.predict(X_train_scaled).flatten()
    
    # Prédiction sur le jeu de données de test
    y_test_pred = modele.predict(X_test_scaled).flatten()

    # Prédiction sur l'ensemble des données après entraînement
    X_all_scaled = scaler.transform(merged_df[['omiwatari_doy']].values)
    y_all_pred = modele.predict(X_all_scaled).flatten()

    # Calculer le RMSE
    rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))  # RMSE sur le test uniquement
    resultats[nom_config] = rmse
    print(f"{nom_config} → RMSE = {rmse:.3f}")

    # Tracé du graphique : Prédictions sur l'ensemble des données (entraînement et test)
    plt.figure(figsize=(10, 4))
    plt.plot(merged_df['year'], merged_df['adjusted_cherry_bloom_doy'], label="Réalité (Tous)", linestyle='-', color='orange')
    plt.plot(merged_df['year'], y_all_pred, label="Prédiction (Tous)", linestyle="--", color='blue')
    plt.title(f"{nom_config} — Prédiction vs Réalité sur l'ensemble des données")
    plt.xlabel("Année")
    plt.ylabel("Date de floraison ajustée des cerisiers (DOY)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
