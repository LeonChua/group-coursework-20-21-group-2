import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

#plotting the population density vs the price of various rooms

#connecting to sqlite database
conn = sqlite3.connect('database.sqlite')
df_housing_density = pd.read_sql('SELECT * FROM housing_density_borough;', conn, index_col='area_id')
df_housing_prices = pd.read_sql('SELECT * FROM housing_prices;', conn, index_col='area_id')
print(df_housing_density.dtypes)
print("table_2")
print(df_housing_prices.dtypes)

#creating table which has area id, population per square kilometre, housing prices
df1 = df_housing_density[['Population_per_square_kilometre']]
df2 = df_housing_prices[['one_bed_median_price']]

df = pd.merge(df1, df2, on='area_id')
df.dropna()
print(df.dtypes)

#plotting matplotlib graph

fig, ax = plt.subplots(figsize=(12, 7))

df.plot('Population_per_square_kilometre')
plt.show()