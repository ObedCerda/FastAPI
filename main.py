from fastapi import FastAPI

app = FastAPI() #Aqui llamo a una clase de FastAPI

#get es parte del protocolo HTTP y se usa para obtener datos de un servidor
@app.get("/") #esto es un decorador que toma root como la ruta root del servidor
async def root(): # Cuando se accede a un server se ncecita una funcion asincrona
    # Esta funcion se ejecuta cuando se accede a la ruta raiz
    return {"message" : "¡Hello, World!"}    

@app.get("/url")
async def url():
    return { "url": "https://github.com/obedcerda" }

class User(BaseModel):
    id: int
    name : str  = "Obed Cerda"
    signup_ts: datetime | None = None #  can be date | or none
    friends: list[int] = []

external_data= {
    "id": 1234,
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user = User(**external_data) # Pydantic valida los datos y crea un objeto User
print(user) # Imprime el objeto User creado
