import reflex as rx
from typing import Optional
from sqlmodel import Field

# Definimos el modelo Usuarios que representa la tabla en la base de datos
class User(rx.Model, table=True):
    __user__="user" #Este es el nombre de la tabla
    iduser: Optional[int] = Field(default=None, primary_key=True)
    name: str 
    username: str 
    password: str
    phone: str

