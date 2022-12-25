# Program that scrapes data from a table using Pandas

import pandas as pd

url = 'https://simple.m.wikipedia.org/wiki/List_of_U.S._state_capitals'

tables = pd.read_html(url)

tables[0]

# Select the desired column or indes
dataframe = tables[0, 1, 3]

# Creates a heading for the table
dataframe.head()

# Convert dataset to CSV file
dataframe.to_csv('us_state_capitals')