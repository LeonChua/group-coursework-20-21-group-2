import pandas as pd
import matplotlib.pyplot as plt

# Load the xlsx file into a pandas DataFrame and skip the first line which contains the logo
rentFile = '../Approved_datasets/privaterentalmarketstatistics11122020.xls'
wellbeing = '../Approved_datasets/personal-well-being-borough (2).xlsx'

df = pd.read_excel(rentFile, sheet_name='Table2.7', skiprows=6)

# Show the columns in the spreadsheet and the first few rows of data
print(df.columns)
print(df.head(3))
