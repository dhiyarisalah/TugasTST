from database.db import get_db
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.userModels import UserSchema, ShowUser, Token
from sqlalchemy.orm import Session
from typing import List
from authentication.authenticate import authenticate
from pydantic import EmailStr

from controller import userController

user_router = APIRouter(
    tags=["User"],
)

@user_router.post("/Register")
def sign_user_up(request: UserSchema, db: Session = Depends(get_db)) -> dict:
    return userController.sign_up(request, db)

@user_router.post("/Login", response_model=Token)
def sign_user_in(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> dict:
    return userController.sign_in(request, db)


@user_router.get("/user", response_model=List[ShowUser])
def get_user_list(db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return userController.get_all_user(db)


@user_router.get("/{id}", response_model=ShowUser)
def get_a_user(id: int, db: Session = Depends(get_db), user: str = Depends(authenticate)) -> dict:
    return userController.get_user(id, db)