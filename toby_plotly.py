import pandas as pd
import sqlite3
import plotly.express as px

#plotting the crime rates for different crimes

#connecting to sqlite database
conn = sqlite3.connect('database.sqlite')
df_crime = pd.read_sql('SELECT * FROM crime_rates_per_borough;', conn, index_col=None)

# only want certain crimes that relate to the students as we don't need to know all crimes committed

mean = df_crime.mean(axis=1)

df = df_crime.iloc[:,:3]
df['Mean_last_24_months'] = mean

df = df[df.MinorText == (df.iloc[1, 1] or df.iloc[3, 1] or df.iloc[5,1] or df.iloc[8,1] or df.iloc[22,1] or df.iloc[31,1] or df.iloc[34,1] or df.iloc[36,1] or df.iloc[37,1] or df.iloc[40,1] or df.iloc[45,1] or df.iloc[46,1])]

fig = px.scatter(df, x='MinorText', y='Mean_last_24_months')
fig.show()

print(df.head())