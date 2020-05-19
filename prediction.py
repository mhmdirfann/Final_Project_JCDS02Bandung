import pickle
from pandas import DataFrame,get_dummies
import pandas as pd


model = pickle.load(open('finalized_model_zomato.sav','rb'))
scaler=pickle.load(open('scaler_zomato.sav','rb'))
def prediction(data):
    dfdata = pd.DataFrame(scaler.transform(data),columns=data.columns)
    hasil = model.predict(dfdata)
    return hasil[0]
def data_zomato():
    df = pd.read_csv('ZomatoCleanedData.csv')
    return df
    

