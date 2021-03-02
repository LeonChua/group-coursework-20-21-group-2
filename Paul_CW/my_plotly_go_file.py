import plotly.graph_objects as go
import pandas as pd


class WellbeingChart:
    """Create the Wellbeing Radar chart to be used in the dashboard"""

    def __init__(self):
        self.create_radar_chart("Brent", "Camden")
        self.allareas = []

    def create_radar_chart(self, borough1, borough2):
        # Select Boroughs Wanted
        boroughs = [borough1, borough2]

        # Load the file into a pandas DataFrame
        wellbeing = '../Approved_datasets/personal-well-being-borough (2).xlsx'
        df = pd.read_excel(wellbeing, sheet_name='Summary - Mean Scores', skiprows=0, header=[0, 1])

        print(df)
        # from https://stackoverflow.com/questions/45128523/pandas-multiindex-how-to-select-second-level-when-using-columns
        # and https://www.kite.com/python/answers/how-to-drop-a-level-from-a-multi-level-column-index-in-a-pandas-dataframe-in-python
        df2 = df.xs('2018/19', axis=1, level=1, drop_level=False)
        df2.columns = df2.columns.droplevel(level=1)
        areas = df.xs('Area', axis=1, level=1, drop_level=False)
        areas.columns = areas.columns.droplevel(level=0)

        # Convert Areas into list for callback
        self.allareas = areas["Area"].to_list()

        # from https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
        df3 = pd.concat([areas, df2.reindex(areas.index)], axis=1)

        # Drop"City of London"
        df3.drop(0)

        # Extract only London Boroughs
        df3 = df3[0: 33]

        print(df3)

        df3 = df3.set_index("Area")

        # Plot graph
        # from https://plotly.com/python/radar-chart/
        categories = df2.columns.to_list()

        fig = go.Figure()

        for borough in boroughs:
            fig.add_trace(go.Scatterpolar(
                r=df3.loc[borough].to_list(),
                theta=categories,
                fill='toself',
                name=borough
            ))

        fig.update_layout(
            title="Radar Chart - Comparing the wellbeing of 2 boroughs",
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=True
        )

        return fig