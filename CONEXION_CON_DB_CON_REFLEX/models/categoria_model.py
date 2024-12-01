import reflex as rx
from typing import Optional
from sqlmodel import Field

# Definicion del modelo de datos de Categoria para su correspondiente
# tabla


class Categoria(rx.Model, table=True):
    __tablename__= "tablacategorias" #Este es el nombre de la tabla
    idcategoria: Optional[int] = Field(default=None, primary_key=True)
    nombrecategoria: str
    departamento: str
