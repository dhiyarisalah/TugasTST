from fastapi import FastAPI, HTTPException, Depends, status
import uvicorn
from authentication.hashpassword import Hash
from authentication.jwthandler import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from models.userModels import User
from database.db import user_db
from routes.movie_router import movie_router
from routes.babyname_router import babyname_router
from routes.quotes_router import quotes_router

description = """
## This API will help you do awesome stuff. 🎬 🎵
Enjoy!

Note : Mohon bersabar dalam menjalankan beberapa service :)
"""

tags_metadata = [
    {
        "name": "Made with Love, 18220047 Dhiya Risalah Ghaida",
        "description": "",
	},
    {
        "name": "User",
        "description": "User berisi endpoint yang berkaitan dengan user. User dapat membuat akun dan login untuk **mendapatkan token**. Token digunakan untuk mengakses service yang disediakan. Adapun durasi token adalah **30 hari**.",
	},
    {
        "name": "Movies Recommender",
        "description": "Movie Recommender berisi endpoint yang dapat men-generate **rekomendasi film** untuk user berdasarkan **judul film**.",
    },
    {
        "name": "Baby Name Generator",
        "description": "Baby Name Generator berisi endpoint yang dapat **men-generate nama bayi** berdasarkan input yang dimasukkan oleh pengguna. Input yang perlu dimasukkan antara lain **jenis kelamin, jumlah huruf minimal, jumlah huruf maksimal, jumlah nama yang ingin diberikan, judul film, judul lagu, dan tahun lagu**. Hasil yang diberikan merupakan hasil pengolahan informasi dari Movie Recommender dan Music Recommender",
        "externalDocs": {
            "description": "Gabungan 2 API (Music Generator)",
            "url": "https://musicrecommendationtst.azurewebsites.net/"
        },
    },
    {
        "name": "Quotes Generator",
        "description": "Quotes Generator berisi endpoint yang dapat memberikan informasi **mood, quotes, dan rekomendasi film** berdasarkan input pengguna. Input yang perlu dimasukkan antara lain **judul lagu dan tahun lagu**. Hasil yang diberikan merupakan hasil pengolahan informasi dari Movies Recommender dan Music Recommender",
        "externalDocs": {
            "description": "Gabungan 2 API (Music Generator)",
            "url": "https://musicrecommendationtst.azurewebsites.net/"
        },
    },
    
]

app = FastAPI(title="Integration System & Technology 2022/2023", openapi_tags= tags_metadata, description=description)

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

app.include_router(movie_router, tags=['Movies Recommender'])
app.include_router(babyname_router, tags=['Baby Name Generator'])
app.include_router(quotes_router, tags=["Quotes Generator"])
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)