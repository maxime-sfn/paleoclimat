import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data_omiwatari = pd.read_csv(rf"..\..\base_de_donnees\Japon\FreezingDates_and_OmiwatariDates\data.csv")  # Load Omiwatari dates
data_cherry = pd.read_csv(rf"..\..\base_de_donnees\Japon\CherryBlossomFloweringDates\data.csv")  # Load Cherry Blossom dates

year_omiwatari = data_omiwatari.iloc[:, 0].tolist()  # Get the first column (year)
year_cherry = data_cherry.iloc[:, 0].tolist()  # Get the first column (year)

omiwatari_dates = data_omiwatari.iloc[:, 1].tolist()  # Get the second column (Omiwatari dates)
cherry_dates = data_cherry.iloc[:, 1].tolist()  # Get the second column (Cherry Blossom dates)

for i in range(len(year_omiwatari)):
    if omiwatari_dates[i] == "no" or omiwatari_dates[i] == "did":
        omiwatari_dates.remove(omiwatari_dates[i])
        year_omiwatari.remove(year_omiwatari[i])
        



# Sample data: Replace this with your dataset
data = {
    "year": [1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827],
    "omiwatari_doy": [38, 43, 54, 41, 48, 50, 52, 50],  # from Dec 1
    "sakura_doy": [216, 231, 224, 228, 229, 236, 234, 234]  # from Dec 1
}
df = pd.DataFrame(data)

# Features and target
X = df[['omiwatari_doy']].values
y = df['sakura_doy'].values

# Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Define the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_dim=1),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
history = model.fit(X_train, y_train, epochs=100, batch_size=8, validation_split=0.2)

# Evaluate the model
loss = model.evaluate(X_test, y_test)
print(f"Test loss: {loss}")

# Predictions
y_pred = model.predict(X_test)

# Plotting the results
plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, label="True values", color='blue')
plt.scatter(X_test, y_pred, label="Predicted values", color='red')
plt.xlabel("Omiwatari DOY (from Dec 1)")
plt.ylabel("Sakura Bloom DOY (from Dec 1)")
plt.title("Sakura Bloom Prediction using Neural Network")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import ace_tools as tools; tools.display_dataframe_to_user(name="Sakura Bloom Model Predictions", dataframe=pd.DataFrame({"Year": df["year"], "True Sakura DOY": df["sakura_doy"], "Predicted Sakura DOY": model.predict(scaler.transform(df[['omiwatari_doy']])).flatten()}))
