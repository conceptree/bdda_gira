import pandas as pd

# Load the datasets
df_01 = pd.read_csv('../cleaned/gira_h1_cleaned_dataset.csv')
df_02 = pd.read_csv('../cleaned/gira_h2_cleaned_dataset.csv')

# Concatenate the datasets
concatenated_df = pd.concat([df_01, df_02])

# Optionally, sort by date if the datasets are not already sorted
# Replace 'date_column_name' with the name of your date column
concatenated_df.sort_values(by='date', inplace=True)

# Reset the index of the concatenated dataset
concatenated_df.reset_index(drop=True, inplace=True)

# Save the concatenated dataset to a new CSV file
concatenated_df.to_csv('../cleaned/gira_final.csv', index=True, index_label="index")

print("Concatenated dataset saved.")
