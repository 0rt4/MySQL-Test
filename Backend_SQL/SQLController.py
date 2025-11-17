from pydantic import BaseModel, Field
from datetime import datetime
import mysql.connector


class Usuario(BaseModel):
    Nombre: str
    Edad: int
    FechaNacimiento: str
    FechaCreacion: datetime = Field(default_factory=datetime.now)

def ConectarDB():
    return mysql.connector.connect(
        unix_socket="/home/orta/Documentos/Proyectos/MySQL-Test/.mysql/mysql.sock",
        user="root",
        database="Users"
    )

def InsertarUser(Usuario:Usuario):
    conexion = ConectarDB()
    cursor = conexion.cursor()

    query = """
    INSERT INTO Usuarios (Nombre, Edad, FechaNacimiento, FechaCreacion)
    VALUES (%s, %s, %s, %s)
    """
    data = (
        Usuario.Nombre,
        Usuario.Edad,
        Usuario.FechaNacimiento,
        Usuario.FechaCreacion
    )

    cursor.execute(query,data)
    conexion.commit()

    print(f"✓ Usuario Registrado N° {cursor.lastrowid}")
    cursor.close()
    conexion.close()

