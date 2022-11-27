from sqlalchemy import Column, Integer, String
from database.db import Base
from pydantic import BaseModel, EmailStr
from typing import Optional


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String)
    email = Column(String)
    password = Column(String)

    class Config:
        schema_extra = {
            "Contoh": {
                "nama": "John Doe",
                "email": "JohnDoe@mail.com",
                "password": "Password123",
            }
        }


class UserSchema(BaseModel):
    nama: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "Contoh": {
                "nama": "John Doe",
                "email": "JohnDoe@mail.com",
                "password": "Password123",
            }
        }


class ShowUser(BaseModel):
    email: EmailStr
    nama: str

    class Config:
        orm_mode = True
        schema_extra = {
            "Contoh": {
                "nama": "John Doe",
                "email": "JohnDoe@mail.com",
                "password": "Password123",
            }
        }


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None



