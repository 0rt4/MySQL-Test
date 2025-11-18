# SQLController.py

from pydantic import BaseModel, Field
from datetime import datetime
import mysql.connector

# ======================================================================
class Usuario(BaseModel):
    Nombre: str
    Edad: int
    FechaNacimiento: str
    FechaCreacion: datetime = Field(default_factory=datetime.now)
# ======================================================================
def ConnectToBD():
    return mysql.connector.connect(
        unix_socket="/home/orta/Documentos/Proyectos/MySQL-Test/.mysql/mysql.sock",
        user="root",
        database="Users"
    )
# ======================================================================
def InsertUser(Usuario:Usuario):
    connection = ConnectToBD()
    cursor = connection.cursor()

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
    connection.commit()

    print(f"✓ Usuario Registrado N° {cursor.lastrowid}")
    cursor.close()
    connection.close()
# ======================================================================
def ShowAllUsers():
    connection = ConnectToBD()
    cursor = connection.cursor(dictionary=True)

    query = """
            SELECT * FROM Usuarios
            """
    cursor.execute(query)

    Usuarios= cursor.fetchall()
    cursor.close()
    connection.close()

    return Usuarios
# ======================================================================
def SearchByName(nombre: str):  # ← Solo string, no Usuario
    connection = ConnectToBD()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM Usuarios WHERE Nombre = %s"  # ← Faltaba "Nombre ="

    cursor.execute(query, (nombre,))  # ← Tupla con un elemento
    user_found = cursor.fetchone()

    cursor.close()
    connection.close()

    return user_found  # Retorna dict o None
# ======================================================================
def SearchByID(id:int):
    connection = ConnectToBD()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM Usuarios WHERE id = %s"

    cursor.execute(query,(id,))
    UserFound = cursor.fetchone()

    cursor.close()
    connection.close()

    return UserFound
# ======================================================================
def UpdateUser(id_usuario: int, usuario: Usuario):  # ← Necesitas ID + datos nuevos
    connection = ConnectToBD()
    cursor = connection.cursor()

    query = """
        UPDATE Usuarios
        SET Nombre = %s, Edad = %s, FechaNacimiento = %s
        WHERE id = %s
    """
    # ← NO actualizamos FechaCreacion, eso se mantiene

    data = (
        usuario.Nombre,
        usuario.Edad,
        usuario.FechaNacimiento,
        id_usuario  # ← El WHERE va al final
    )

    cursor.execute(query, data)
    connection.commit()

    print(f"✓ Usuario {id_usuario} actualizado")
    cursor.close()
    connection.close()
# ======================================================================
def DeleteUser(id):  # ← Solo string, no Usuario
    connection = ConnectToBD()
    cursor = connection.cursor()

    query = "DELETE FROM Usuarios WHERE id = %s"  # ← Faltaba WHERE

    cursor.execute(query, (id,))
    connection.commit()

    print(f"✓ Usuario '{id}' eliminado")
    cursor.close()
    connection.close()