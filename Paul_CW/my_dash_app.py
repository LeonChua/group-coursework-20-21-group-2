# animate existing plotly chart by year, and design intuitive borough selection

# imports necessary for dash app
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

# imports necessary for plotting
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Load data
DATA_DIRECTORY = "Approved_datasets"
crimeFile = os.path.join("..", DATA_DIRECTORY, 'MPS Borough Level Crime (most recent 24 months) (1).csv')

df = pd.read_csv(crimeFile, header=0)
print(df)

boroughs = ["Brent", "Haringey", "Camden"]
boroughs.sort()
date = "202010"

# Calculate totals
df1 = df[df['LookUp_BoroughName'] == boroughs[0]]
data1 = df1[date]
total1 = data1.sum()

df2 = df[df['LookUp_BoroughName'] == boroughs[1]]
data2 = df2[date]
total2 = data2.sum()

df3 = df[df['LookUp_BoroughName'] == boroughs[2]]
data3 = df3[date]
total3 = data3.sum()
# wanted to keep graph easy to read to limited to only 3 boroughs at a time.


# widths = total number of cases
widths = np.array([total1, total2, total3])

# convert dataframes into percentages for x axis
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.divide.html
df1[date] = df1[date].truediv(total1)
df2[date] = df2[date].truediv(total2)
df3[date] = df3[date].truediv(total3)


print(df1)

# the data for October 2020 adapted from https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
# Put filtered data together into one frame
frames = [df1, df2, df3]
data = pd.concat(frames)

print(data)

data.set_index(['MajorText', 'MinorText'])


# make a list of all "major" crimes from dataframe

crimes = data['MajorText'].drop_duplicates()
crimes = crimes.values.tolist()

# Make graph
# graph adapted from https://plotly.com/python/bar-charts/

fig = go.Figure()
for crime in crimes:
    numbers = data[data['MajorText'] == crime].groupby('LookUp_BoroughName').sum()['202010']
    area = widths*numbers
    area = area.round(0) # numbers rounded up for clarity + rounding errors
    numbers = (numbers * 100).round(1) # convert to percentage for graph clarity vs decimal points
    print(numbers)
    crimelist = np.array([crime, crime, crime])
    fig.add_trace(go.Bar(
        name=crime,
        y=numbers,
        x=np.cumsum(widths) - widths,
        width=widths,  # customize width here
        offset=0,
        customdata=np.transpose([boroughs, area, crimelist]),
        texttemplate="%{y}% x %{width} =<br>%{customdata[1]}",
        textposition="inside",
        textangle=0,
        textfont_color="white",
        hovertemplate="<br>".join([
            "Crime: %{customdata[2]}",  # added crimes (customdata[2]) so that it is easier to identify
            "Borough: %{customdata[0]}",
            "Total crimes: %{width}",
            "Percentage of total crimes: %{y}",
            "Amount committed: %{customdata[1]} <extra></extra>", # <extra> removes grey secondary box https://plotly.com/python/reference/#scatter-hovertemplate
        ])
    ))

fig.update_xaxes(
    tickvals=np.cumsum(widths)-widths/2,
    ticktext= ["%s<br>%d" % (l, w) for l, w in zip([s + " Crimes" for s in boroughs], widths)] # add crimes to bar labels for graph clarity
)

fig.update_yaxes(ticksuffix="%")

fig.update_xaxes(range=[0,widths.sum()])
fig.update_yaxes(range=[0,100])

fig.update_layout(
    yaxis_title="Percentage of crime committed out of all crimes in each borough",
    xaxis_title="Total Number of Major Crimes",
    title_text="Marimekko Chart - Percentage breakdown of crimes, area is proportional to total crimes",
    barmode="stack",
    uniformtext=dict(mode="hide", minsize=10),
)

# Adapted from week 4 exercises
# create dash app
app = dash.Dash(__name__)

# Create the app layout and add the marimekko chart to it
app.layout = html.Div(children=[

    html.H1('Plotly dash charts'),

    dcc.Graph(figure=fig)
])

# Run the web app server
if __name__ == '__main__':
    app.run_server(debug=False, port=8050)