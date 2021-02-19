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

df3 = df2.drop(columns=['201911', '201912', '202001', '202002', '202003', '202004', '202005', '202006', '202007',
                        '202008', '202009', '202010'], axis=1)

df4 = df3[~df3.MinorText.str.contains("Business")]
df5 = df4[~df4.MajorText.str.contains("Miscellaneous")]
df6 = df5[~df5.MajorText.str.contains("Vehicle")]
df7 = df6[~df6.MajorText.str.contains("Drug")]
df8 = df7[~df7.LookUp_BoroughName.str.contains("Airport")]

aggregation_functions = {'NumberofCrimes': 'sum', 'LookUp_BoroughName': "first", 'MajorText': 'first'}
df9 = df8.groupby(['LookUp_BoroughName', 'MajorText']).aggregate(aggregation_functions)

ArsonFrame = df9[df9['MajorText'] == 'Arson and Criminal Damage']
Arson = ArsonFrame['NumberofCrimes'].tolist()

BurglaryFrame = df9[df9['MajorText'] == 'Burglary']
Burglary = BurglaryFrame['NumberofCrimes'].tolist()

Possession_of_WeaponsFrame = df9[df9['MajorText'] == 'Possession of Weapons']
Possession_of_Weapons = Possession_of_WeaponsFrame['NumberofCrimes'].tolist()

Public_Order_OffencesFrame = df9[df9['MajorText'] == 'Public Order Offences']
Public_Order_Offences = Public_Order_OffencesFrame['NumberofCrimes'].tolist()

RobberyFrame = df9[df9['MajorText'] == 'Robbery']
Robbery = RobberyFrame['NumberofCrimes'].tolist()

SexualFrame = df9[df9['MajorText'] == 'Sexual Offences']
Sexual = SexualFrame['NumberofCrimes'].tolist()

TheftFrame = df9[df9['MajorText'] == 'Theft']
Theft = TheftFrame['NumberofCrimes'].tolist()

ViolenceFrame = df9[df9['MajorText'] == 'Violence Against the Person']
Violence = ViolenceFrame['NumberofCrimes'].tolist()

boroughs = ArsonFrame['LookUp_BoroughName'].tolist()

fig, ax = plt.subplots(figsize=(20, 20))
ind = np.arange(len(boroughs))

p1 = plt.bar(ind, Arson)
p2 = plt.bar(ind, Burglary, bottom=Arson)
p3 = plt.bar(ind, Possession_of_Weapons, bottom=Burglary)
p4 = plt.bar(ind, Public_Order_Offences, bottom=Possession_of_Weapons)
p5 = plt.bar(ind, Robbery, bottom=Public_Order_Offences)
p6 = plt.bar(ind, Sexual, bottom=Robbery)
p7 = plt.bar(ind, Theft, bottom=Sexual)
p8 = plt.bar(ind, Violence, bottom=Theft)

plt.xlabel('Boroughs of London')
plt.ylabel('Number of Crimes')
plt.xticks(ind, boroughs, rotation='vertical')
plt.yticks(np.arange(0, 50000, step=5000))
plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0]), ('Arson and Criminal Damage', 'Burglary',
                                                                      'Possession of Weapons', 'Public Order Offences',
                                                                      'Robbery', 'Sexual Offences', 'Theft',
                                                                      'Violent Crimes'))

plt.savefig('Ben_matplotlib_graph.jpg')
plt.show()