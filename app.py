from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import plotly_express as px
import os

app = Flask(__name__) # creates Flask object from main fcn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/browse/', methods=['GET','POST'])
def browse():
    token = 'pk.eyJ1IjoibWF6YWJkdWwiLCJhIjoiY2trMWh1aXRsMHJhMjJxbzU0eTYzbTI5ZiJ9.DIP735c0I4CbxFHmTtNBCw'

    df = pd.read_excel('personal-well-being-borough.xlsx', sheet_name='Summary - Mean Scores', skiprows = 1)

    columns = [1, 27, 37, 38]
        
    df2 = df.iloc[list(range(0,33)),columns] # select happiness
    df2 = df2.drop([0,1])
    df2 = df2.reset_index(drop = True)
    df2["2018/19.2"]= np.array(df2["2018/19.2"], dtype=np.float64)

    ukavg = df.iloc[[50], [27]] #uk avg hapiness
    ukavg = ukavg["2018/19.2"][50]
    df2["%Difference from AVG"] = df2["2018/19.2"]

    for i in range(len(df2["%Difference from AVG"])):
        df2["%Difference from AVG"][i] = (100*(df2["%Difference from AVG"][i] - ukavg)/ukavg)

    df2.columns = ["Area", "Happiness", "Latitude", "Longitude", "%Difference from AVG"]
    fig = px.scatter_mapbox(
                            df2, 
                            lat=df2.Latitude, 
                            lon=df2.Longitude, 
                            size="Happiness",  
                            hover_name = "Area",
                            hover_data= ["Happiness", "%Difference from AVG"],
                            color_discrete_sequence=["fuchsia"],
                            color = "%Difference from AVG",
                            size_max=10, 
                            zoom=9,
                            title= "Happiness Rating per Borough"
                        )

    fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    div = fig.to_html(full_html=False)

    return render_template('browse.html', div_placeholder = div)


@app.route('/login/')
def login():
    return render_template("login.html")

@app.route('/graphs/')
def graphs():
    return render_template("graphs.html")

if __name__ == '__main__': #runs Flask app
    app.run()
