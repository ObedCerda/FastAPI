from fastapi import FastAPI

app = FastAPI() #Aqui llamo a una clase de FastAPI

#get es parte del protocolo HTTP y se usa para obtener datos de un servidor
@app.get("/") #esto es un decorador que toma root como la ruta root del servidor
async def root(): # Cuando se accede a un server se ncecita una funcion asincrona
    # Esta funcion se ejecuta cuando se accede a la ruta raiz
    return {"message" : "Hello, World!"}    
