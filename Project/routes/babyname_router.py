
from authentication.jwthandler import  create_access_token, get_current_user
from fastapi import APIRouter, Body, HTTPException, Depends, Request,status
from models.userModels import User, Login, Token, TokenData

# from database.database import get_game_by_genre, get_anime_genre
from database.db import *
from fastapi.encoders import jsonable_encoder
from models.serviceModels import babyName
import babygenerator
import sys

babyname_router = APIRouter()
sys.setrecursionlimit(100000)

@babyname_router.post('/babynamegenerator/')
async def babynames_generator_based_on_movie_and_song(item: babyName, current_user:User = Depends(get_current_user)):
    final_nama = babygenerator.babynameGenerator(item.jenis_kelamin, item.jumlah_huruf_minimal, item.jumlah_huruf_maksimal, item.jumlah_nama, item.judul_film, item.judul_lagu, item.tahun_lagu)
    # result = babygenerator.babynameGenerator(item.judul_film, item.judul_lagu, item.tahun_lagu)
    return final_nama