
from authentication.jwthandler import  create_access_token, get_current_user
from fastapi import APIRouter, Body, HTTPException, Depends, Request,status
from models.userModels import User, Login, Token, TokenData

# from database.database import get_game_by_genre, get_anime_genre
from database.db import *
from fastapi.encoders import jsonable_encoder
from models.serviceModels import movieItem
import itemRecommender
import sys


movie_router = APIRouter()
sys.setrecursionlimit(100000)

# @movie_router.post('/getMovieGenre/')
# async def get_movie_genre(movie_name: movieItem, current_user:User = Depends(get_current_user)):
#     res = itemRecommender.get_movie_recommendation_item_based(movie_name.judul_film)
#     return res

@movie_router.post('/movierecommendation/')
async def movies_recommender_from_movie(movie_name: movieItem, current_user:User = Depends(get_current_user)):
    df = itemRecommender.get_movie_recommendation_item_based(movie_name.judul_film)
    return df


