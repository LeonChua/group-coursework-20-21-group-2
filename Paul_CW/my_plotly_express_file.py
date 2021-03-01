import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Load the file into a pandas DataFrame
crimeFile = '../Approved_datasets/MPS Borough Level Crime (most recent 24 months) (1).csv'

df = pd.read_csv(crimeFile, header=0)
print(df)

boroughs = ["Brent", "Haringey", "Camden"]
boroughs.sort()
date = "202010"

# Calculate totals
df1 = df[df['LookUp_BoroughName'] == boroughs[0]]
data1 = df1[date]

df2 = df[df['LookUp_BoroughName'] == boroughs[1]]
data2 = df2[date]

df3 = df[df['LookUp_BoroughName'] == boroughs[2]]
data3 = df3[date]
# wanted to keep graph easy to read to limited to only 3 boroughs at a time.

print(df1)

# the data for October 2020 adapted from https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
frames = [df1, df2, df3]
data = pd.concat(frames)

print(data)

data.set_index(['MajorText', 'MinorText'])


# make a list of all "major" crimes from dataframe

crimes = data['MajorText'].drop_duplicates()
print(crimes)
crimes = crimes.values.tolist()

print(crimes)

# graph from https://plotly.com/python/bar-charts/
fig = px.bar(data, x="LookUp_BoroughName", y='202010', color="MajorText",
             title="Bar chart breakdown of crimes per borough",
             labels={
                 "LookUp_BoroughName": "Boroughs",
                 "202010": "Number of crimes",
                 "MajorText": "Crime Key",
             },
             )
fig.show()