import pandas as pd

# Load the full dataset
input_file = 'liag_freeze_thaw_table.csv'  # Replace with your actual file name
df = pd.read_csv(input_file)

# Loop through each unique lakecode and save a separate CSV
for lakecode in df['lakecode'].unique():
    lake_df = df[df['lakecode'] == lakecode]
    lake_df.to_csv(f'{lakecode}.csv', index=False)
