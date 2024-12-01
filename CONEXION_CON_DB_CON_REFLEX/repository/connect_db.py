"""Creación de la conexion a la base de datos"""
# Va a tener los datos de conexion con la base de datos
# Instrucciones de sqlmodel 
# para mysql la libreria a importar es pymysql
from sqlmodel import create_engine
def connect():
    # Configuración del motor de conexión a la base de datos
    engine = create_engine(
        "mysql+pymysql://root:root@localhost:3306/base_vscode_python")
    return engine


