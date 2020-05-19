from flask import Flask,render_template,request
from data import price_range,boolean,restonew
from prediction import prediction
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from prediction import data_zomato
from math import sin, cos, sqrt, atan2, radians
import plotly
import plotly.express as px
import json
from plots import data_cheap,data_mapaverage,data_expensive,data_avgcostcountry,data_pctrest


## translate Flask to python object
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index_prediction():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
        for i in data:
            if data[i]=='Yes':
                data[i]=1
            elif data[i]=='No':
                data[i]=0
        data['Price range'] = int(data['Price range'])
        data['Aggregate rating'] = float(data['Aggregate rating'])
        data['Votes'] = int(data['Votes'])
        data=pd.DataFrame(data,index=[0])
        hasil = prediction(data)
        return render_template('result.html', hasil_prediction=round(hasil,2))
    return render_template('prediction.html',data_location=sorted(price_range),
    data_boolean=sorted(boolean))
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/Visualization')
def visualization():
    data=data_cheap()
    data2=data_mapaverage()
    data3=data_expensive()
    data4=data_avgcostcountry()
    data5=data_pctrest()

    return render_template('visualization.html',data=data,data2=data2,data3=data3,data4=data4,data5=data5)
@app.route('/recommend',methods=['GET','POST'])
def recommend():
    if request.method == "POST":
        data1 = request.form
        data1 = data1.to_dict()
        cb_Cuisines=pd.read_csv('ZomatoDataforRecommend.csv')
        cv= CountVectorizer()
        cv_genres_result=cv.fit_transform(cb_Cuisines.Cuisines)
        cos_sin_cuisine=cosine_similarity(cv_genres_result)
        cv_Location=cv.fit_transform(cb_Cuisines['Location'])
        cos_sin_loc=cosine_similarity(cv_Location)
        cos_sin_loc_cuisine=(cos_sin_loc*0.70)+(cos_sin_cuisine*0.30)
        def get_recomendation_restaurantbyloccuisine(title='Jahanpanah',location='AgraCantt,Agra,India'):
            index_to_search=cb_Cuisines[(cb_Cuisines['Restaurant Name']==title)&(cb_Cuisines['Location']==location)].index[0]
            Resto_similar=pd.Series(cos_sin_loc_cuisine[index_to_search])
            index_similar=Resto_similar.sort_values(ascending=False).head(6).index
            recommendation=cb_Cuisines.loc[index_similar]
            recommendation.reset_index(drop=True,inplace=True)
            dist=[]

            for i in range(len(recommendation)):
                # approximate radius of earth in km
                R = 6373.0

                lat1 = radians(recommendation['Latitude'][0])
                lon1 = radians(recommendation['Longitude'][0])
                lat2 = radians(recommendation['Latitude'][i])
                lon2 = radians(recommendation['Longitude'][i])

                dlon = lon2 - lon1
                dlat = lat2 - lat1

                a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))

                distance = R * c

                dist.append(round(distance,2))
            recommendation['Distance Approximate(Km)']=dist
            recommendation=recommendation[['Restaurant Name','Cuisines','City','Country','Average Cost for two ($USD)','Aggregate rating','Votes','Distance Approximate(Km)']].loc[1:6]
            recommendation['Votes']=recommendation['Votes'].astype(np.int64)
            return recommendation
        data1split=data1['Recommendation'].split('|')
        result=get_recomendation_restaurantbyloccuisine(data1split[0],data1split[1])
        return render_template('resultrecomm.html', hasilrecomm=result)


    return render_template('recommendation.html',listrestaurant=sorted(restonew))

if __name__ == '__main__':
    app.run(debug=True, port=1100)