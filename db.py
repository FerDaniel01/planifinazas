from pydantic import BaseModel


class Transaccion(BaseModel):
    id: int
    fechaTransaccion:str
    categoria: str
    valor: float
    formaPago:str
    descripcion: str

transaciones = {
    1: Transaccion (id=1 , fechaTransaccion = "20-11-2020", categoria="Alimentación",valor=200000, formaPago="tarjeta_débito", descripcion= "Almuerzo restaurante Carne de Res"),
    2: Transaccion (id=2 , fechaTransaccion = "22-11-2020", categoria="Vestuario",valor=980000, formaPago="tajerta_crédito", descripcion= "Uniformes dotación trabajadores"),
    3: Transaccion (id=3 , fechaTransaccion = "01-12-2020", categoria="Viveres",valor=600000, formaPago="efectivo", descripcion= "Mercado mensual familiar"),



}

def obtener_Transaciones():
    #haga lo que tenga que hacer para conectarse a la base de datos y obtner todas las ordenes
    lista_transacciones=[]

    for e in transaciones:
        lista_transacciones.append(transaciones[e])
    return lista_transacciones


def agregar_transaccion(transaccion: Transaccion):
    if transaccion.id in transaciones:
        return False
    else:
        transaciones[transaccion.id]= transaccion
        return True