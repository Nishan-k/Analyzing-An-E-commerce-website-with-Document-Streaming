import pandas as pd
import json
import numpy as np



# TODO:1 Read the CSV file:
df = pd.read_csv("./data/test.csv")

# TODO:2 Add a new column in the existing DF for the JSON representation of all the CSV file per record:
df['json'] = df.to_json(orient='records', lines=True).splitlines()

# Only retrieving the column with JSON representation:
df_json = df['json']

# TODO:3 Save the JSON data in a text file:
with open("./data/output.txt", 'a') as output:
    for line in df_json:
        output.write(line + '\n')
