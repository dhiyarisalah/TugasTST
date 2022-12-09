from fastapi import FastAPI, HTTPException, Depends, status
import uvicorn
from authentication.hashpassword import Hash
from authentication.jwthandler import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from models.userModels import User
from database.db import user_db
from routes.movie_router import movie_router
from routes.babyname_router import babyname_router

app = FastAPI(title="Integration System & Technology 2022/2023")

@app.get("/", tags=["Made with Love, 18220047 Dhiya Risalah Ghaida"])
async def greeting():
	return {"18220047 - Dhiya Risalah Ghaida" : "Welcome to my Service!"}


@app.post('/register', tags=["User"])
def create_user(request:User):
	hashed_pass = Hash.bcrypt(request.password)
	user_object = dict(request)
	user_object["password"] = hashed_pass
	user_id = user_db["users"].insert_one(user_object)
	# print(user)
	return {"User":"created"}

@app.post('/login', tags=["User"])
def login(request:OAuth2PasswordRequestForm = Depends()):
	user = user_db["users"].find_one({"username":request.username})
	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'No user found with this {request.username} username')
	if not Hash.verify(user["password"],request.password):
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'Wrong Username or password')
	access_token = create_access_token(data={"sub": user["username"] })
	return {"access_token": access_token, "token_type": "bearer"}

app.include_router(movie_router, tags=['Movies Recommendation Based on Movie Title'])
app.include_router(babyname_router, tags=['Get Your Future Baby Name(s) Based on Your Favorite Movie and Song'])
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)