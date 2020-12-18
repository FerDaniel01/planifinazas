from fastapi import FastAPI
from fastapi import HTTPException
import db

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [

    "http://localhost:8081",
    "https://planifinanzas-front.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


@app.get("/transacciones/")
async def obtener_transacciones():
    transacciones = db.obtener_Transaciones()
    return transacciones

@app.post("/transacciones/agregar/")
async  def agregar_transaccion(transaccion:db.Transaccion):
    agregada_exitosamente=db.agregar_transaccion(transaccion)
    if agregada_exitosamente:
        return {"mensaje":"Transacción agregada exitosamente"}
    else:
        raise  HTTPException(status_code=400, detail="Erros, el id de la transaccion y existe ")
