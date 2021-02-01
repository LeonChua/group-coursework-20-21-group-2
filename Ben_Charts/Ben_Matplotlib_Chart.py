# What are the differences in the types of crime committed between two different boroughs?

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

crime = '../Approved_datasets/MPS Borough Level Crime (most recent 24 months) (1).csv'


df = pd.read_csv(crime)
df2 = pd.DataFrame(df, columns=['MajorText', 'MinorText', 'LookUp_BoroughName', '201911', '201912', '202001', '202002',
                                '202003', '202004', '202005', '202006', '202007', '202008', '202009', '202010'])

df2['NumberofCrimes'] = df2['201911'] + df2['201912'] + df2['202001'] + df2['202002'] + df2['202003'] + df2['202004'] \
                        + df2['202005'] + df2['202006'] + df2['202007'] + df2['202008'] + df2['202009'] + df2['202010']

df3 = df2.drop(columns = ['201911', '201912', '202001', '202002',
                          '202003', '202004', '202005', '202006', '202007', '202008', '202009', '202010'], axis = 1)

df4 = df3[~df3.MinorText.str.contains("Business")]
df5 = df4[~df4.MajorText.str.contains("Miscellaneous")]
df6 = df5[~df5.MajorText.str.contains("Vehicle")]
df7 = df6[~df6.MajorText.str.contains("Drug")]
df8 = df7[~df7.LookUp_BoroughName.str.contains("Airport")]

aggregation_functions = {'LookUp_BoroughName': 'first', 'MajorText': 'first', 'NumberofCrimes': 'sum'}
df9 = df8.groupby(df8['LookUp_BoroughName']).aggregate(aggregation_functions)

boroughs = ['Barking and Dagenham', 'Barnet', 'Bexley', 'Brent', 'Bromley', 'Camden', 'Croydon', 'Ealing',
                  'Enfield', 'Greenwich', 'Hackney', 'Hammersmith', 'Haringey', 'Harrow', 'Havering', 'Hilingdon',
                  'Hounslow', 'Islington', 'Kensington and Chelsea', 'Kingston Upon Thames', 'Lambeth', 'Lewisham',
            'Merton', 'Newham', 'Redbridge', 'Richmond Upon Thames', 'Southwark', 'Sutton', 'Tower Hamlets',
            'Waltham Forest', 'Wandsworth', 'Westminster']

numberofcrimes = df9['NumberofCrimes']

fig, ax = plt.subplots(figsize=(20, 20))
ypos = np.arange(len(boroughs))
plt.xticks(ypos, boroughs, rotation='vertical')
plt.yticks(np.arange(0, 50000, step=5000))
plt.xlabel('Boroughs of London')
plt.ylabel('Number of Crimes')
ax.set_title('Comparison of Number of Crimes in Different London Boroughs')
plt.bar(ypos, numberofcrimes)
plt.savefig('Ben_matplotlib_graph.jpg')

plt.show()