import pandas as pd

# Replace 'your_dataset.csv' with the path to your actual dataset file
file_path = '../data/Gira_H2.csv'

# Read the dataset
df = pd.read_csv(file_path)

# Print column names to verify
print("Columns in the dataset:", df.columns.tolist())

# Ensure that the column names used below match exactly with what's printed above
# Splitting 'designcomercial' into 'ID' and 'station'
df[['ID', 'station']] = df['desigcomercial'].str.split('-', n=1, expand=True)

# Renaming columns
df.rename(columns={'numbicicletas': 'bikes_available', 
                   'numdocas': 'total_docks', 
                   'estado': 'state'}, inplace=True)

# Extracting latitude and longitude from 'position'
df['latitude'] = df['position'].apply(lambda x: eval(x)['coordinates'][1])
df['longitude'] = df['position'].apply(lambda x: eval(x)['coordinates'][0])

# Extracting date and time from 'entity_ts'
df['date'] = pd.to_datetime(df['entity_ts']).dt.date
df['time'] = pd.to_datetime(df['entity_ts']).dt.strftime('%H:%M:%S')

# Selecting the required columns in the specified order
df = df[['ID', 'station', 'bikes_available', 'total_docks', 'state', 'latitude', 'longitude', 'date', 'time']]

# Write the cleaned data to a new CSV file
output_file = '../cleaned/gira_h2_cleaned_dataset.csv'
df.to_csv(output_file, index=False)

print(f"Cleaned dataset saved as '{output_file}'")
