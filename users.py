from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()  # Aquí llamo a una clase de FastAPI

#Ingresa a venv
#inicia server con fastapi dev users.py

#Paranop rellenar todo a mano se hac elo siguiente

class User(BaseModel):
    id : int
    name: str
    surname : str
    url : str
    age : int 

users_fake_db = [User(id = 1, name="Obed", surname="Cerda", url="obedcerda.com", age=30),
                 User(id = 2, name="Juan", surname="Perez", url="juanperez.com", age=25),
                 User(id = 3, name="Maria", surname="Lopez", url="marialopez.com", age=28)]

@app.get("/usersjson")
async def users_json():
    return [{"name" : "Obed", "surname" : "Cerda", "url": "obedcerda.com", "age": 30},
            {"name" : "Juan", "surname" : "Perez", "url": "juanperez.com", "age": 25},
            {"name" : "Maria", "surname" : "Lopez", "url": "marialopez.com", "age": 28}]

@app.get("/users")
async def user():
    return users_fake_db

@app.get("/users{id}")
async def user(id : int):
    user = filter(lambda user: user.id == id, users_fake_db)
    return list(user)[0]

