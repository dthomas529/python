# Program that scrapes data from a table using Pandas

import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_national_capitals'

tables = pd.read_html(url)

tables[1]

# Select the desired column or indes
dataframe = = tables[1]

# Creates a heading for the table
dataframe.head()

# Convert dataset to CSV file
dataframe.to_csv('national_world_capitals')