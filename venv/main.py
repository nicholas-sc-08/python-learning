from fastapi import FastAPI

app = FastAPI()

users = [{"id": 1, "name": "teste", "email": "teste@gmail.com", "senha": "1234567"}]

@app.get("/")
async def home():
    return { "message": "Hello Python" }

@app.get("/users")
async def getUsers():
    return users