from authentication.jwthandler import  create_access_token, get_current_user
from fastapi import APIRouter, Body, HTTPException, Depends, Request,status
from models.userModels import User, Login, Token, TokenData
from database.db import *
from fastapi.encoders import jsonable_encoder
from models.serviceModels import musicItem
import quotes

import sys

quotes_router = APIRouter()
sys.setrecursionlimit(100000)

@quotes_router.post("/mood_generator/")
async def generate_mood(item: musicItem, current_user:User = Depends(get_current_user)):
    songs = quotes.get_music_mood(item.name, item.year)
    return songs

@quotes_router.post("/quotes_generator/")
async def generate_quotes(item: musicItem, current_user:User = Depends(get_current_user)):
    songs = quotes.get_quotes(quotes.get_music_mood(item.name, item.year)['mood'], "only_quotes")
    return songs

@quotes_router.post("/quotes_movie_generator/")
async def generate_quotes_movie(item: musicItem, current_user:User = Depends(get_current_user)):
    songs = quotes.get_quotes(quotes.get_music_mood(item.name, item.year)['mood'], "all")
    return songs

@quotes_router.post("/generate_all_by_lyrics/")
async def generate_all_by_lyrics(item: musicItem, current_user:User = Depends(get_current_user)):
    all = quotes.get_all(item.name, item.year, target="lyrics")
    return all