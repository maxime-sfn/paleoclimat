import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data_omiwatari = pd.read_csv(rf"..\..\base_de_donnees\Japon\FreezingDates_and_OmiwatariDates\data.csv")  # Load Omiwatari dates
data_cherry = pd.read_csv(rf"..\..\base_de_donnees\Japon\CherryBlossomFloweringDates\data.csv")  # Load Cherry Blossom dates

year_omiwatari = data_omiwatari.iloc[:, 0].tolist()  # Get the first column (year)
year_cherry = data_cherry.iloc[:, 0].tolist()  # Get the first column (year)

omiwatari_dates = data_omiwatari.iloc[:, 1].tolist()  # Get the second column (Omiwatari dates)
cherry_dates = data_cherry.iloc[:, 1].tolist()  # Get the second column (Cherry Blossom dates)

filtered = [(y, d) for y, d in zip(year_omiwatari, omiwatari_dates) if d != "no" and d != "did"]
year_omiwatari, omiwatari_dates = zip(*filtered) if filtered else ([], [])
year_omiwatari = list(year_omiwatari)
omiwatari_dates = list(omiwatari_dates)

# Remove entries where cherry_dates is 0, keeping both lists aligned
year_cherry, cherry_dates = zip(*[(y, d) for y, d in zip(year_cherry, cherry_dates) if d != 0])
year_cherry = list(year_cherry)
cherry_dates = list(cherry_dates)
        
# Assuming the lists: year_omiwatari, omiwatari_dates, year_cherry, cherry_dates

# Step 1: Create DataFrames from the lists for easier manipulation
df_omiwatari = pd.DataFrame({
    'year': year_omiwatari,
    'omiwatari_doy': omiwatari_dates
})

df_cherry = pd.DataFrame({
    'year': year_cherry,
    'cherry_bloom_doy': cherry_dates
})

# Step 2: Merge the two datasets on the 'year' column
merged_df = pd.merge(df_omiwatari, df_cherry, on='year')

# Step 3: Filter out invalid omiwatari or cherry bloom dates (if not already done)
merged_df = merged_df[merged_df['omiwatari_doy'].notna() & merged_df['cherry_bloom_doy'].notna()]

# Step 4: Extract the cleaned and aligned lists of years, omiwatari dates, and cherry blossom dates
aligned_years = merged_df['year'].tolist()
aligned_omiwatari_dates = merged_df['omiwatari_doy'].tolist()
aligned_cherry_dates = merged_df['cherry_bloom_doy'].tolist()

# Now, aligned_years, aligned_omiwatari_dates, and aligned_cherry_dates have the same years
# You can use these for further analysis or model training


aligned_cherry_dates = [int(date) - 91 for date in aligned_cherry_dates]


import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Sample data: Replace this with your dataset
data = {
    "year": aligned_years,
    "omiwatari_doy": aligned_omiwatari_dates,  # from Dec 1
    "sakura_doy": aligned_cherry_dates  # from Dec 1
}
df = pd.DataFrame(data)

# Ensure the data is numeric
df['omiwatari_doy'] = pd.to_numeric(df['omiwatari_doy'], errors='coerce')  # Convert to numeric
df['sakura_doy'] = pd.to_numeric(df['sakura_doy'], errors='coerce')  # Convert to numeric
df.dropna(subset=['omiwatari_doy', 'sakura_doy'], inplace=True)  # Drop rows with NaN

# Features and target
X = df[['omiwatari_doy']].values
y = df['sakura_doy'].values

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),  # Using Input layer instead of input_dim
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),  # Adding dropout to reduce overfitting
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
history = model.fit(X_train, y_train, epochs=200, batch_size=8, validation_split=0.1)

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
plt.title("Sakura Bloom Prediction using Neural Network (Without Scaling)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Function to predict for a given input
def predict_sakura_bloom(omiwatari_doy):
    """Predict the sakura bloom date for a given omiwatari DOY."""
    input_data = np.array([[omiwatari_doy]])  # reshape input for prediction
    prediction = model.predict(input_data)
    return prediction[0][0]  # Return the predicted DOY

# Example: Predict for a new omiwatari date
new_omiwatari_doy = 50  # Replace with any new omiwatari DOY you want to predict
predicted_bloom_doy = predict_sakura_bloom(new_omiwatari_doy)
print(f"Predicted Sakura Bloom DOY for Omiwatari DOY {new_omiwatari_doy}: {predicted_bloom_doy}")

# Exporting the final predictions for all years in the dataset
df["predicted_sakura_doy"] = model.predict(df[['omiwatari_doy']]).flatten()

import ace_tools as tools; tools.display_dataframe_to_user(name="Sakura Bloom Model Predictions", dataframe=df)
