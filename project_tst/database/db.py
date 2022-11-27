# from fastapi import FastAPI
# from pymongo import MongoClient
# import os
# from typing import Optional

# var_mongopass = os.getenv("dhiyarisalah")
# var_url = f'mongodb+srv://dhiyarisalah:password12345@cluster0.884hnst.mongodb.net/?retryWrites=true&w=majority'

# client = MongoClient(var_url)



from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseSettings

SQLALCHEMY_DATABASE_URL = 'sqlite:///./projecttst.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False}, echo=True)

session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    SECRET_KEY: Optional[str] = "default"
    ALGORTIM: Optional[str] = "HS256"

    class Config:
        env_file = ".env"
