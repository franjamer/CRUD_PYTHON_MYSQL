""" Definimos el modelo Usuarios que representa la tabla en la base de datos"""
import reflex as rx
from typing import Optional
from sqlmodel import Field

# Esta será la clase encargada de mapear mi base de datos
# concretamente la tabla User.
class User(rx.Model, table=True):
    __user__="user" #Este es el nombre de la tabla
    iduser: Optional[int] = Field(default=None, primary_key=True)
    name: str 
    username: str 
    password: str
    phone: str
# En la definicion de los datos de la tabla, los nombres de los 
# campos deben ser iguales a los de la db a la que nos conectamos

# Este modelo se adaptará a cada tabla que tengamos en nuestra db, 
# adaptandolas a sus correspondientes datos, pero lo que no cambiará 
# es la estructura general.
# Se recomienda crear un fichero de modelo, como este por cada tabla.
