import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# === Chargement et prétraitement ===
data_omiwatari = pd.read_csv(r"..\..\base_de_donnees\Japon\FreezingDates_and_OmiwatariDates\data.csv")
data_cherry    = pd.read_csv(r"..\..\base_de_donnees\Japon\CherryBlossomFloweringDates\data.csv")

# Clean Omiwatari
omi = data_omiwatari.rename(columns={data_omiwatari.columns[0]:'year',
                                     data_omiwatari.columns[1]:'omiwatari_doy'})
omi = omi[~omi['omiwatari_doy'].isin(['no','did'])]

# Clean Cherry
cherry = data_cherry.rename(columns={data_cherry.columns[0]:'year',
                                     data_cherry.columns[1]:'cherry_bloom_doy'})
cherry = cherry[cherry['cherry_bloom_doy'] != 0]

# Merge & adjust
df = pd.merge(omi, cherry, on='year')
df['adjusted_cherry_bloom_doy'] = df['cherry_bloom_doy'] - 91

# === Random train split, test on all ===
X_full = df[['omiwatari_doy']].values
y_full = df['adjusted_cherry_bloom_doy'].values

# 80% of the data at random for training; we ignore the “test” split here
X_train, _, y_train, _ = train_test_split(
    X_full, y_full, train_size=0.8, random_state=42
)

# Fit scaler on training only
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Transform the entire dataset for evaluation
X_full_scaled  = scaler.transform(X_full)

# === Model builder ===
def construire_modele(neurones, activation='relu'):
    model = Sequential()
    model.add(Dense(neurones[0], activation=activation, input_shape=(1,)))
    for n in neurones[1:]:
        model.add(Dense(n, activation=activation))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

configs = {
    "2 couches (8,8)":   [8,  8],
    "2 couches (16,8)":  [16, 8]
}

for name, struct in configs.items():
    model = construire_modele(struct)
    model.fit(X_train_scaled, y_train, epochs=500, batch_size=32, verbose=0)
    
    # Predict on the full dataset
    y_pred_full = model.predict(X_full_scaled).flatten()
    
    for i in range(len(y_pred_full)):
        y_pred_full[i] = int(y_pred_full[i])
    
    # Compute RMSE on the **entire** dataset
    rmse = np.sqrt(mean_squared_error(y_full, y_pred_full))
    print(f"{name} → RMSE (full data) = {rmse:.3f}")
    
    # Plot
    plt.figure(figsize=(10,4))
    plt.plot(df['year'], df['adjusted_cherry_bloom_doy'], label='Réalité (Tous)',    linestyle='-',  color='orange')
    plt.plot(df['year'], y_pred_full,                             label='Prédiction (Tous)', linestyle='--', color='blue')
    plt.title(f"{name} — Prédiction vs Réalité sur l'ensemble des données")
    plt.xlabel("Année")
    plt.ylabel("Date de floraison ajustée des cerisiers (DOY)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
