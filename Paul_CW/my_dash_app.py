# animate existing plotly chart by year, and design intuitive borough selection

# imports necessary for dash app
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import base64
import os

from Paul_CW.my_dash_app_chart import CrimeChart
from Paul_CW.my_dash_app_data import CrimeData
from Paul_CW.my_dash_app_px_chart2 import CrimePlotlyChart
from Paul_CW.my_plotly_go_file import WellbeingChart

# Run dataset preparation program

data = CrimeData()
area1 = "Brent"
area2 = "Haringey"
area3 = "Camden"
data.process_data(area1, area2, area3)

# Build figures
cr = CrimeChart(data)
fig3 = cr.create_chart()

crpx = CrimePlotlyChart()
fig2 = crpx.create_px_chart()

# Build Radar Chart
wb = WellbeingChart()
fig4 = wb.create_radar_chart("Brent", "Camden")

# code from #https://github.com/plotly/dash/issues/71 (continued below)
image_filename = 'chart1.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

# Adapted from week 4 + 5 exercises
# create dash app
app = dash.Dash(external_stylesheets=[dbc.themes.LUX])

# Create the app layout and add the marimekko chart to it
app.layout = dbc.Container(fluid=True, children=[
    html.H1('Plotly dash charts'),
    # Adapted from week 5
    dbc.Row([
        dbc.Col(children=[
            html.H2('Chart 1'),
            # code from https://github.com/plotly/dash/issues/71
            dbc.FormGroup([
                html.Img(src='chart1.png')
            ])
        ])
    ]),
    dbc.Row([
        dbc.Col(children=[
            html.H2('Chart 2')
        ])
    ]),
    dbc.Row([
        dbc.Col(children=[
            dcc.Graph(figure=fig2),
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
    dbc.Row([
        dbc.Col(children=[
            html.H2('Chart 2')
        ])
    ]),
    dbc.Row([
        # Add the first column here. This is for the area selector and the statistics panel.
        dbc.Col(width=3, children=[
            dbc.FormGroup([
                html.H4("Select Areas"),
                # dash-core-components (dcc) provides a dropdown
                dcc.Dropdown(id="area_select_radar1", options=[{"label": x, "value": x} for x in wb.allareas],
                             value="Barking and Dagenham"),
                dcc.Dropdown(id="area_select_radar2", options=[{"label": x, "value": x} for x in wb.allareas],
                             value="Camden"),
            ]),

        ]),
        # Add the second column here. This is for the figure.
        dbc.Col(width=9, children=[

            html.H4("Radar Chart"),
            html.Div(id="radar-chart"),
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
    fig3 = cr.create_chart()
    panel = html.Div([
        dcc.Graph(figure=fig3),

    ])
    return panel

@app.callback(Output("radar-chart", "children"), [Input("area_select_radar1", "value"),
                                                   Input("area_select_radar2", "value")])
def render_output_panel(area_select_radar1, area_select_radar2):
    fig4 = wb.create_radar_chart(area_select_radar1, area_select_radar2)
    panel = html.Div([
        dcc.Graph(figure=fig4),

    ])
    return panel

# Run the web app server
if __name__ == '__main__':
    app.run_server(debug=False, port=8050)