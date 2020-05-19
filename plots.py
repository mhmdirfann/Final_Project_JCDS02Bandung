import plotly
import plotly.express as px
import json
from prediction import data_zomato
import pandas as pd
import plotly.graph_objects as go
def data_cheap():
   df = data_zomato()
   fig = px.bar(df.sort_values(by='Average Cost for two ($USD)',ascending=True).head(5), y='Average Cost for two ($USD)', x='Restaurant Name',hover_data=['Country','City'])
   fig.update_layout(title="Top 5 cheapest restaurant on Zomato")
   fig_json = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder) # converting plotly to json file
   return fig_json
def data_expensive():
   df = data_zomato()
   fig = px.bar(df.sort_values(by='Average Cost for two ($USD)',ascending=False).head(5), y='Average Cost for two ($USD)', x='Restaurant Name',hover_data=['Country','City'])
   fig.update_layout(title="Top 5 most expensive restaurant on Zomato")
   fig_json = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder) # converting plotly to json file
   return fig_json
def data_avgcostcountry():
   df = data_zomato()
   dfCountryAvgCost=pd.DataFrame({'Country':df.groupby(['Country'])['Average Cost for two ($USD)'].mean().index,'Average Cost for two ($USD)':df.groupby(['Country'])['Average Cost for two ($USD)'].mean().values})
   fig = px.bar(dfCountryAvgCost.sort_values(by=['Average Cost for two ($USD)']), y='Average Cost for two ($USD)', x='Country')
   fig.update_layout(title="Average Cost for Two by Country")
   fig_json = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder) # converting plotly to json file
   return fig_json

def data_pctrest():
   df = data_zomato()
   df_counts=df.Country.value_counts()
   x=df_counts.values
   y=df_counts.keys()
   fig = px.pie(df_counts, values=x, names=y, title='Percentage restaurant by Country')   
   fig_json = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder) # converting plotly to json file
   return fig_json
def data_mapaverage():
   df = data_zomato()
   fig = go.Figure(go.Densitymapbox(lat=df.Latitude, lon=df.Longitude, z=df['Average Cost for two ($USD)'],radius=10))
   fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
   fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
   fig_json = json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder) # converting plotly to json file
   return fig_json