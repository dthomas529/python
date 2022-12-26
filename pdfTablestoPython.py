# This program extracts a table from a pdf using Tabula and Pandas
import tabula

tables = tabula.read_pdf('sample.pdf', pages='all')

print(tables[0])

# this prints the type of table
print(type(tables[0]))

dataframe = tables[0]
print(dataframe[dataframe.Age > 30])
