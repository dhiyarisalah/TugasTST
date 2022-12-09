from pymongo import MongoClient
# from models.model import game_schema
from bson.objectid import ObjectId
import re
import json

mongodb_uri = "mongodb+srv://root:sandi@projecttst.ew4fyct.mongodb.net/?retryWrites=true&w=majority"
port = 8000
client = MongoClient(mongodb_uri, port)
user_db = client["User"]