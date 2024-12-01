from ..models.user_model import User
from .connect_db import connect
from sqlmodel import Session, select

# Métodos

def select_all():
    # Conexión a la base de datos
    engine = connect()
    with Session(engine) as session:
        # Ejecutamos la consulta para obtener todos los usuarios
        query = select(User)
        # devuelve una lista de todos los usuarios que tengamos en nuestra tabla de la base de datos
        return session.exec(query).all()

def select_user_by_email(email: str):
    engine = connect()
    with Session(engine) as session:
        query = select(User).where(User.username == email)
        return session.exec(query).all()

# Método para crear un nuevo usuario
def create_user(user: User):
    engine = connect()
    with Session(engine) as session:
        # añadimos nuevo usuario
        session.add(user)
    # pasamos los datos a la tabla
        session.commit()
    # devuelve lista de los datos nuevos en el navegador
        query = select(User)
    # devuelve lista de usuarios ya actualizada
        return session.exec(query).all()

# Metodo para eliminar un usuario
def delete_user(email:str):
    engine = connect()
    with Session(engine) as session:
        query= select(User).where(User.username==email)
        user_delete = session.exec(query).one()
        session.delete(user_delete)
        session.commit()
        query=select(User)
        return session.exec(query).all()
