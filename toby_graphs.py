import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

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



#plotting matplotlib graph

fig, ax = plt.subplots(figsize=(12, 7))

ax.set_title('Population per square kilometer against median housing prices')
plt.xlabel('Population per square kilometre')
plt.ylabel('Price (£)')

ax.scatter(df['Population_per_square_kilometre'], df['room_median_price'])
ax.scatter(df['Population_per_square_kilometre'], df['studio_median_price'])
ax.scatter(df['Population_per_square_kilometre'], df['one_bed_median_price'])
ax.scatter(df['Population_per_square_kilometre'], df['two_bed_median_price'])
ax.scatter(df['Population_per_square_kilometre'], df['three_bed_median_price'])
ax.scatter(df['Population_per_square_kilometre'], df['four_plus_bed_median_price'])
ax.set_ylim([0, 5000])

labels = 'room_median_price' , 'studio_median_price', 'one_bed_median_price', 'two_bed_median_price', 'three_bed_median_price', 'four_plus_bed_median_price'
plt.legend(labels=labels)
plt.savefig('matplotlib_graph_toby.jpg')
plt.show()

