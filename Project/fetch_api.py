from requests import request
import json
from datetime import datetime
import pandas as pd
from pandas import json_normalize 
from scrap_data import *


def fetchData (judul_film, judul_lagu, tahun_lagu):
    url_movie = "https://movierecommender123.azurewebsites.net/token"
    data = {
        "username": "string",
        "password": "string"
    }
    response_movie = request("POST", url_movie, data=data)
    access_token = response_movie.json()["access_token"]
    token_type = response_movie.json()["token_type"]

    #Membuat request
    url_movie = f"https://movierecommender123.azurewebsites.net/movierecommendation"
    headers = {
        "accept": "application/json",
        "Authorization": token_type + " " + access_token, 
        "Content-Type": "application/json"
    }

    # x = input()
    params = {
        "name": judul_film
    }

    response_movie = request("POST", url_movie, headers=headers, json = params)
    result_movie= response_movie.json()
    judul = result_movie["Title"]

    list_of_dict_values = list(judul.values())
    df_movie = pd.DataFrame (list_of_dict_values, columns = ['Film'])

    df_movie['Year'] = df_movie['Film'].str[-5:-1].astype(int)

    df1_movie = df_movie['Year']

    listTahun_movie = df1_movie.to_numpy()
        
    #API Music Recommender
    url_music = "https://musicrecommendationtst.azurewebsites.net/token"
    data = {
        "username": "divya",
        "password": "mysecret"
    }
    response_music = request("POST", url_music, data=data)

    #Akses token
    access_token = response_music.json()["access_token"]
    token_type = response_music.json()["token_type"]

    # Membuat request
    url_music = f"https://musicrecommendationtst.azurewebsites.net/musicrecommendation"
    headers = {
        "accept": "application/json",
        "Authorization": token_type + " " + access_token, 
        "Content-Type": "application/json"
    }
    # song = str(input("Input song title: "))
    # year = int(input("Input song year: "))
    params = {
        "name": judul_lagu,
        "year": tahun_lagu 
    }
    response_music = request("POST", url_music, headers=headers, json=params)
    result_music = response_music.json()

    df_music= pd.DataFrame.from_dict(result_music, orient="columns")

    df1_music = df_music['year']
    listTahun_music = df1_music.to_numpy()

    averageYear = (sum(listTahun_movie+listTahun_music))//20
    return averageYear
    # scrapDataBoy(averageYear)
    # scrapDataGirl(averageYear)

# fetchData ("Avatar", "Ocean & Engines", 2022)