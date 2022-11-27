from fastapi import FastAPI
from database.db import engine
import uvicorn
from models import userModels
from routes.routes import user_router

app = FastAPI()
app.debug  = True

userModels.Base.metadata.create_all(engine)
app.include_router(user_router, prefix="/users")

@app.get('/')
def index():
    return {"18220047 - Dhiya Risalah Ghaida" : "Welcome to my API!"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)