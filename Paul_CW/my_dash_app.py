# animate existing plotly chart by year, and design intuitive borough selection

# imports necessary for dash app
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import os

from Paul_CW.my_dash_app_chart import CrimeChart
from Paul_CW.my_dash_app_data import CrimeData

# Run dataset preparation program

data = CrimeData()
area1 = "Brent"
area2 = "Haringey"
area3 = "Camden"
data.process_data(area1, area2, area3)

# Build figures
cr = CrimeChart(data)
fig1 = cr.create_chart()

# Adapted from week 4 + 5 exercises
# create dash app
app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

# Create the app layout and add the marimekko chart to it
app.layout = dbc.Container(fluid=True, children=[
    html.H1('Plotly dash charts'),
    # Adapted from week 5
    dbc.Row([
        dbc.Col(children=[
            html.H2('Chart 1')
        ])
    ]),
    dbc.Row([
        dbc.Col(children=[
            html.H2('Chart 2')
        ])
    ]),
    dbc.Row([
        dbc.Col(children=[
            html.H2('Chart 3')
        ])
    ]),
    dbc.Row([
        # Add the first column here. This is for the area selector and the statistics panel.
        dbc.Col(width=3, children=[
            dbc.FormGroup([
                html.H4("Select Areas"),
                # dash-core-components (dcc) provides a dropdown
                dcc.Dropdown(id="area_select1", options=[{"label": x, "value": x} for x in data.allareas],
                             value="Barking and Dagenham"),
                dcc.Dropdown(id="area_select2", options=[{"label": x, "value": x} for x in data.allareas],
                             value="Camden"),
                dcc.Dropdown(id="area_select3", options=[{"label": x, "value": x} for x in data.allareas],
                             value="Westminster"),
            ]),

        ]),
        # Add the second column here. This is for the figure.
        dbc.Col(width=9, children=[

            html.H4("Crime Breakdown"),
            html.Div(id="crime-graph"),
            #dcc.Graph(figure=fig1),

        ]),
    ]),
])

from dash.dependencies import Output, Input


@app.callback(Output("crime-graph", "children"), [Input("area_select1", "value"),
                                                   Input("area_select2", "value"), Input("area_select3", "value")])
def render_output_panel(area_select1, area_select2, area_select3):
    data.process_data(area_select1, area_select2, area_select3)
    cr = CrimeChart(data)
    fig1 = cr.create_chart()
    panel = html.Div([
        dcc.Graph(figure=fig1),

    ])
    return panel

# Run the web app server
if __name__ == '__main__':
    app.run_server(debug=False, port=8050)