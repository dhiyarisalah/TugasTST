from requests import request
import json
from datetime import datetime
import pandas as pd
from pandas import json_normalize 
from scrap_data import *

url_movie = "https://movierecommender123.azurewebsites.net/login"
data = {
    "username": "string",
    "password": "string"
}
response_movie = request("POST", url_movie, data=data)
access_token = response_movie.json()["access_token"]
token_type = response_movie.json()["token_type"]
#Membuat request
url_movie = f"https://movierecommender123.azurewebsites.net/movierecommendation/"
headers = {
    "accept": "application/json",
    "Authorization": token_type + " " + access_token, 
    "Content-Type": "application/json"
}
params = {
    "judul_film": "Avatar"
} 
response_movie = request("POST", url_movie, headers=headers, json = params)
result_movie= response_movie.json()
print(result_movie)
judul = result_movie["Title"]

list_of_dict_values = list(judul.values())
df_movie = pd.DataFrame (list_of_dict_values, columns = ['Film'])

df_movie['Year'] = df_movie['Film'].str[-5:-1].astype(int)

df1_movie = df_movie['Year']
