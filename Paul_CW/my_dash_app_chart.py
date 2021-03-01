import plotly.graph_objects as go
import numpy as np


class CrimeChart:
    """Create the crime Marimekko chart to be used in the dashboard"""

    def __init__(self, data):
        self.data = data

    def create_chart(self):
        crimes = self.data.crimes_list
        data = self.data.reduceddata
        widths = self.data.widths
        boroughs = self.data.areas
        fig = go.Figure()
        for crime in crimes:
            numbers = data[data['MajorText'] == crime].groupby('LookUp_BoroughName').sum()['202010']
            area = widths * numbers
            area = area.round(0)  # numbers rounded up for clarity + rounding errors
            numbers = (numbers * 100).round(1)  # convert to percentage for graph clarity vs decimal points
            print(numbers)
            crimelist = np.array([crime, crime, crime])
            fig.add_trace(go.Bar(
                name=crime,
                y=numbers,
                x=np.cumsum(widths) - widths,
                width=widths,  # customize width here
                offset=0,
                customdata=np.transpose([boroughs, area, crimelist]),
                texttemplate="%{y} x %{width} =<br>%{customdata[1]}",
                textposition="inside",
                textangle=0,
                textfont_color="white",
                hovertemplate="<br>".join([
                    "Crime: %{customdata[2]}",  # added crimes (customdata[2]) so that it is easier to identify
                    "Borough: %{customdata[0]}",
                    "Total crimes: %{width}",
                    "Percentage of total crimes: %{y}",
                    "Amount committed: %{customdata[1]} <extra></extra>",
                    # <extra> removes grey secondary box https://plotly.com/python/reference/#scatter-hovertemplate
                ])
            ))

        fig.update_xaxes(
            tickangle=0, #ensure tick angle is at zero
            tickvals=np.cumsum(widths) - widths / 2,
            ticktext=["%s<br>%d" % (l, w) for l, w in zip([s + "<br>Crimes" for s in boroughs], widths)]
            # add crimes to bar labels for graph clarity
        )

        fig.update_yaxes(ticksuffix="%")

        fig.update_xaxes(range=[0, widths.sum()])
        fig.update_yaxes(range=[0, 100])

        fig.update_layout(
            yaxis_title="Percentage of crime committed out <br> of all crimes in each borough",
            xaxis_title="Total Number of Major Crimes",
            title_text="Marimekko Chart - Percentage breakdown of crimes, area is proportional to total crimes",
            barmode="stack",
            uniformtext=dict(mode="hide", minsize=10),
        )

        return fig
