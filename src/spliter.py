import pandas as pd

def split_csv(input_file, output_files):
    # Read the input CSV file
    data = pd.read_csv(input_file)
    
    # Calculate the size of each split
    split_size = len(data) // len(output_files)
    
    # Split the data and save to new files
    for i, output_file in enumerate(output_files):
        if i < len(output_files) - 1:
            data_split = data.iloc[i*split_size:(i+1)*split_size]
        else:
            # Ensure the last file includes any remaining rows
            data_split = data.iloc[i*split_size:]
        data_split.to_csv(output_file, index=False)

# Usage
input_csv = '../cleaned/final_dataset.csv'
output_csvs = ['../cleaned/data_1.csv', '../cleaned/data_2.csv', '../cleaned/data_3.csv']
split_csv(input_csv, output_csvs)
