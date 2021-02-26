# Is there a correlation between how anxious people feel living in a borough to the amount of crime experienced in that borough?

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Importing Data and Cleaning
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

list=[Arson, Burglary, Possession_of_Weapons, Public_Order_Offences, Robbery, Sexual, Theft, Violence]

dff = pd.DataFrame(list, index=['Arson', 'Burglary', 'Possession of Weapons', 'Public Order Offences', 'Robbery',
                                 'Sexual Offences', 'Theft', 'Violent Crimes'], columns=boroughs, dtype=float)

#App Layout
app.layout = html.Div([
    html.H1("Ben's Plot #3", style={'text-align': 'left'}),
    html.Div([
        dcc.Dropdown(
            id='select_borough',
            options=[
                    {'label': 'Barking and Dagenham', 'value': 'Barking and Dagenham'},
                    {'label': 'Barnet', 'value': 'Barnet'},
                    {'label': 'Bexley', 'value': 'Bexley'},
                    {'label': 'Brent', 'value': 'Brent'},
                    {'label': 'Bromley', 'value': 'Bromley'},
                    {'label': 'Camden', 'value': 'Camden'},
                    {'label': 'Croyden', 'value': 'Croyden'},
                    {'label': 'Ealing', 'value': 'Ealing'},
                    {'label': 'Enfield', 'value': 'Enfield'},
                    {'label': 'Greenwich', 'value': 'Greenwich'},
                    {'label': 'Hackney', 'value': 'Hackney'},
                    {'label': 'Hammersmith and Fulham', 'value': 'Hammersmith and Fulham'},
                    {'label': 'Haringey', 'value': 'Haringey'},
                    {'label': 'Harrow', 'value': 'Harrow'},
                    {'label': 'Havering', 'value': 'Havering'},
                    {'label': 'Hillindon', 'value': 'Hillindon'},
                    {'label': 'Hounslow', 'value': 'Hounslow'},
                    {'label': 'Islington', 'value': 'Islington'},
                    {'label': 'Kensington and Chelsea', 'value': 'Kensington and Chelsea'},
                    {'label': 'Kingston Upon Thames', 'value': 'Kingston Upon Thames'},
                    {'label': 'Lambeth', 'value': 'Lambeth'},
                    {'label': 'Lewisham', 'value': 'Lewisham'},
                    {'label': 'Merton', 'value': 'Merton'},
                    {'label': 'Newham', 'value': 'Newham'},
                    {'label': 'Redbridge', 'value': 'Redbridge'},
                    {'label': 'Richmond Upon Thames', 'value': 'Richmond Upon Thames'},
                    {'label': 'Southwark', 'value': 'Southwark'},
                    {'label': 'Sutton', 'value': 'Sutton'},
                    {'label': 'Tower Hamlets', 'value': 'Tower Hamlets'},
                    {'label': 'Waltham Forest', 'value': 'Waltham Forest'},
                    {'label': 'Wandsworth', 'value': 'Wandsworth'},
                    {'label': 'Westminster', 'value': 'Westminster'}
                 ],
                 optionHeight=35,
                 multi=False,
                value='Barking and Dagenham',
                 searchable=True,
                 search_value='',
                 placeholder='Please select...',
                 clearable=True,
                 style={'width': "40%"}
                 )
    ]),

    html.Div([
        dcc.Graph(id='crime_pie')
    ]),

])

@app.callback(
    Output(component_id='crime_pie', component_property='figure'),
    [Input(component_id='select_borough', component_property='value')]
)
def update_graph(select_borough):
    labels = dff.index.tolist()
    figure = px.pie(dff, names=labels, values=select_borough, title='Breakdown of Crimes in London Boroughs')
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
