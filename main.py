import numpy as np
import pandas as pd
import os

# Get a list of all CSV files
csv_files = [os.path.join('data', file) for file in os.listdir('data')]

# Create an empty dictionary that will consist of crypto dataframes
dataframes = {}

# Loop through each CSV file and create a dataframe
for file in csv_files:
    # Extract dataframe name from file name (without the extension)
    df_name = os.path.splitext(os.path.basename(file))[0]
    # Read the CSV file into a dataframe and store it in the dictionary
    dataframes[df_name] = pd.read_csv(file)
    
# Now, we have a dictionary where keys are dataframe names and values are dtaframes
# We can access each dataframe using its name, e.g., dataframes['filename']
