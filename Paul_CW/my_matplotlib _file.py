import pandas as pd
import matplotlib.pyplot as plt

# Load the xlsx file into a pandas DataFrame and skip the first 6 lines
rentFile = '../Approved_datasets/privaterentalmarketstatistics11122020.xls'
wellbeing = '../Approved_datasets/personal-well-being-borough (2).xlsx'

df = pd.read_excel(rentFile, sheet_name='Table2.7', skiprows=6)

#### DATA PROCESSING
# Show the columns in the spreadsheet and the first few rows of data
print(df.columns)
print(df)

df2 = df[['Area', 'Median']]

# Select only London Boroughs
# https://stackoverflow.com/questions/43193880/how-to-get-row-number-in-dataframe-in-pandas
start = df[df['Area'] == 'LONDON'].index[0]
end = df[df['Area'] == 'SOUTH EAST'].index[0]

df2 = df.loc[start:end-1]

# Remove LONDON, Inner London and Outer London Entries
# https://datatofish.com/rows-with-nan-pandas-dataframe/
df3 = df2.loc[~df2['LA Code1'].isna()]

# Sort in alphabetical order
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
df4 = df3.sort_values(by=['Area'])

# Select Median Price Column only
#median_rent = df4['Median']
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.set_index.html
median_rent = df4.set_index('Area')[['Median']]

print(median_rent)


# Load the xlsx file into a pandas DataFrame
df = pd.read_excel(wellbeing, sheet_name='Summary - Mean Scores', skiprows=0, index_col=[1])

# Show the columns in the spreadsheet and the first few rows of data
print(df.columns)
print(df)

# Select Happiness section
# https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html
# 'Unnamed: 9' = Life Satisfaction, 'Unnamed: 18' = Worthwhile, 'Unnamed: 27' = Happiness, 'Unnamed: 36' = Anxiety
df2 = df[['Unnamed: 9']]

# Select London Boroughs only
happiness = df2.loc['City of London': 'Westminster'].dropna()
happiness = happiness.rename(columns = {'Unnamed: 9': 'Happiness'})

print(happiness)

# Combine both dataframes
# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

data = pd.concat([happiness, median_rent.reindex(happiness.index)], axis = 1).reindex(happiness.index)

# Sort data by increasing rent
# https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
data = data.sort_values(by=['Median'], ascending=True)

try:
    # Drop City of London
    data = data.drop(['City of London'])
    print(data)
except:
    print("No City of London")


#### PLOT DATA

fig, axes = plt.subplots(figsize=(12, 6))
axes.scatter(data[['Median']], data[['Happiness']])
axes.set_ylim([0, 10]) # Range chosen to better represent results and reflect the options given (0-10)
axes.set_xlabel('Median Monthly Rent Price (£)')
axes.set_ylabel('Life Satisfaction (Arbitrary Units from 0-10)')
# "Monthly Rent Price" more concise than "Median Monthly Rent price"
axes.set_title('Graph of Life Satisfaction against Monthly Rent Price for each London Borough')
# https://stackoverflow.com/questions/8209568/how-do-i-draw-a-grid-onto-a-plot-in-python
axes.xaxis.grid()
axes.yaxis.grid()
plt.show()
# in your report, explain how you chose your graph (using interactive char chooser), and how you avoided chartjunk
# why did you not use a line graph?
"""

fig2, axes2 = plt.subplots(figsize=(12, 6))
axes2 = data['Median'].plot.bar(x=0, y=2, width=1.0)
plt.show()

data = data.sort_values(by=['Happiness'], ascending=True)

fig3, axes3 = plt.subplots(figsize=(12, 6))
axes3 = data['Happiness'].plot.bar(x=0, y=2, width=1.0)
plt.show()

"""
# export figure to png/jpeg
fig.savefig('chart1.jpeg', transparent=True, bbox_inches='tight')