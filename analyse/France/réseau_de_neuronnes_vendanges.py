import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

temp_df = pd.read_csv("Temp_Moyenne_mesurées_Beaune_1850_2024.csv")
vend_df = pd.read_csv("Vendanges_beaune_1355_2018.csv")
temp_df = temp_df.rename(columns={temp_df.columns[0]: "year", temp_df.columns[1]: "temperature"})
vend_df = vend_df.rename(columns={vend_df.columns[0]: "year", vend_df.columns[1]: "vendanges_julian"})
temp_df = temp_df[temp_df['year'].between(1850, 2024)].dropna()
vend_df = vend_df[vend_df['year'].between(1355, 2024)].dropna()
merged_df = pd.merge(temp_df, vend_df, on="year")
train_df = merged_df[merged_df['year'] >= 1875]
test_df = merged_df[merged_df['year'] < 1875]

X_train = train_df[['vendanges_julian']].values
y_train = train_df['temperature'].values
X_test = test_df[['vendanges_julian']].values
y_test = test_df['temperature'].values
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

def construire_modele(neurones_par_couche, activation='relu'):
    model = Sequential()
    model.add(Dense(neurones_par_couche[0], activation=activation, input_shape=(1,)))
    for n in neurones_par_couche[1:]:
        model.add(Dense(n, activation=activation))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

configurations = {
    "1 couche (8)": [8],
    "2 couches (8,8)": [8, 8],
    "2 couches (6,6)": [6,6], 
    "2 couches (4,4)": [4,4],
    "2 couches (16,8)": [16, 8],
    "3 couches (8,8,8)": [8, 8, 8],
    "3 couches (6,6,6)": [6, 6, 6],  # ← celle qu'on va tester avec différents batchs
    "3 couches (4,4,4)": [4, 4, 4],
}

resultats = {}

for nom_config, structure in configurations.items():
    
    # Cas spécial : tester 3 batch_sizes uniquement pour la config (6,6,6)
    if nom_config == "3 couches (6,6,6)":
        for batch in [32,64]:
            modele = construire_modele(structure, activation='relu')
            modele.fit(X_train_scaled, y_train, epochs=500, batch_size=batch, verbose=0)
            y_pred = modele.predict(X_test_scaled).flatten()
            rmse = np.sqrt(mean_squared_error(y_test, y_pred))
            resultats[f"{nom_config} — batch={batch}"] = rmse
            print(f"{nom_config} — batch={batch} → RMSE = {rmse:.3f}")

            # Tracé du graphique de prédiction vs réalité
            plt.figure(figsize=(10, 4))
            plt.plot(test_df['year'], y_test, label="Réalité")
            plt.plot(test_df['year'], y_pred, label="Prédiction", linestyle="--")
            plt.title(f"{nom_config} — batch={batch} — Prédiction (1850-1874)")
            plt.xlabel("Année")
            plt.ylabel("Température (°C)")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.show()
    
    else:
        # Cas général pour les autres architectures avec batch par défaut (32)
        modele = construire_modele(structure, activation='relu')
        modele.fit(X_train_scaled, y_train, epochs=500, verbose=0)
        y_pred = modele.predict(X_test_scaled).flatten()
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))    
        resultats[nom_config] = rmse
        print(f"{nom_config} → RMSE = {rmse:.3f}")

        # Tracé du graphique
        plt.figure(figsize=(10, 4))
        plt.plot(test_df['year'], y_test, label="Réalité")
        plt.plot(test_df['year'], y_pred, label="Prédiction", linestyle="--")
        plt.title(f"{nom_config} — Prédiction (1850-1874)")
        plt.xlabel("Année")
        plt.ylabel("Température (°C)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()