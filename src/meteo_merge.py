import pandas as pd

# Assuming the concatenated dataset is available at the given path
concatenated_path = '../cleaned/gira_final.csv'  # Update this with the actual file path
concatenated_df = pd.read_csv(concatenated_path)

# Load the meteorological data
meteo_path = './Lx_Meteo.csv'
meteo_df = pd.read_csv(meteo_path)

# Ensure date formats are aligned (modify if necessary)
concatenated_df['date'] = pd.to_datetime(concatenated_df['date'])
meteo_df['datetime'] = pd.to_datetime(meteo_df['datetime'])

# Merge the datasets on the date column
merged_df = pd.merge(concatenated_df, meteo_df[['datetime', 'feelslike', 'temp', 'precip']], 
                     left_on='date', right_on='datetime', how='left')

# Drop the extra 'datetime' column if not needed
merged_df.drop('datetime', axis=1, inplace=True)

# Save the merged dataset
merged_df.to_csv('../cleaned/final_dataset.csv', index=False)

print("Final merged dataset saved.")
