import pandas as pd
import sqlite3
import plotly.express as px

#plotting the population density vs the price of various rooms

#connecting to sqlite database
conn = sqlite3.connect('database.sqlite')
df_housing_density = pd.read_sql('SELECT * FROM housing_density_borough;', conn, index_col='area_id')
df_housing_prices = pd.read_sql('SELECT * FROM housing_prices;', conn, index_col='area_id')

#creating table which has area id, population per square kilometre, housing prices
df1 = df_housing_density[['Population_per_square_kilometre']]
df2 = df_housing_prices
del df2['area_name']
df = pd.merge(df1, df2, on='area_id')

# removing unwanted rows
df = df[df.room_median_price != '']

fig = px.scatter(df, x="Population_per_square_kilometre", y="one_bed_median_price", trendline="ols")
fig.show()