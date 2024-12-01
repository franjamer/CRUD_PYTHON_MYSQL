"""
Métodos de servicio.Es decir son los 
métodos que pasan la información a 
nuestras páginas.
"""
from ..repository.user_repository import select_all, select_user_by_email,create_user,delete_user
from ..models.user_model import User

# metodos que ya sirven la informacion a nuestras páaginas
# Aqí tambien se hace la lógica de negocio.
# así como las validaciones.     


def select_all_user_service():
    users = select_all()
    print(users)
    return users


def select_user_by_email_service(email: str):
    if (len(email) != 0):
        users=select_user_by_email(email)
        print(f"Usuarios encontrados con email{email}:",users)
        return users 
    else:
        return select_all()


def create_user_service(username:str,password:str,phone:str,name:str):
    # validacion
    user = select_user_by_email(username)
    if(len(user)==0):
        user_save=User(username=username, password=password,phone=phone,name=name )
        return create_user(user_save)
    else:
        print("el usuario ya existe")
        raise BaseException("El usuario ya existe")

def delete_user_service(email: str):
    return delete_user(email=email)

