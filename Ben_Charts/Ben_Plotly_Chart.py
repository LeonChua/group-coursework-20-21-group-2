# Is there a correlation between how happy people in London are and the amount of income they earn?
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

wellbeing = '../Approved_datasets/personal-well-being-borough (2).xlsx'
rental = '../Approved_datasets/privaterentalmarketstatistics11122020.xls'
df = pd.read_excel(wellbeing, sheet_name='Summary - Mean Scores', skiprows=[0, 2], index_col=1)
df2 = pd.DataFrame(df, columns=['2018/19.2'])
df3 = df2.dropna()
unwanted_rows = list(range(33, 47))
df4 = df3.drop(df3.index[unwanted_rows])
happiness = df4.drop(df4.index[0])

df = pd.read_excel(rental, sheet_name='Table2.7', skiprows=[0, 1, 2, 3, 4], index_col=3)
df2 = df.loc['Camden':'Waltham Forest']
df3 = df2[~df2.index.str.contains("Outer London")]
df4 = df3[~df3.index.str.contains("City of London")]
df5 = df4.drop(columns=['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'All categories', 'Unnamed: 5', 'Unnamed: 6',
                        'Unnamed: 8'], axis=1)
rent = df5.sort_index()

frames = [happiness, rent]
df6 = pd.concat(frames, axis=1)
final = df6.rename(columns={"2018/19.2": "Happiness", "Unnamed: 7": "Median Rent"})
Boroughs = final.index.tolist()

fig = px.scatter(final, x='Median Rent', y='Happiness', title='Is there a correlation between how happy people in '
                                                              'London are and the amount of income they earn?',
                                                            color=Boroughs)

# Create a Dash app (if you use a stylesheet in the assets folder you will need to use __name__ in the constructor).
app = dash.Dash(__name__)

# Create the app layout and add the bar chart to it
app.layout = html.Div(children=[
    html.H1('COMP0034 Coursework 1 Ben Li Chart #2'),

    dcc.Graph(figure=fig, style={'width': '90vh', 'height': '90vh'}),

])

# Run the web app server
if __name__ == '__main__':
    app.run_server(debug=False, port=8050)