from ..models.categoria_model import Categoria
from .connect_db import connect
from sqlmodel import Session, select


# Este procedimiento muestra el contenido de la tabla
# categorias.
def select_all_categoria():
    engine = connect()
    with Session(engine) as session:
        query = select(Categoria)
        return session.exec(query).all()
