# Forms.py

from Backend_SQL.SQLController import *

#======================================================================
def FormINSERT():
    print("\n=== Crear nuevo usuario ===")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    fecha_nac = input("Fecha de Nacimiento (YYYY-MM-DD): ")

    try:
        usuario = Usuario(
            Nombre=nombre,
            Edad=edad,
            FechaNacimiento=fecha_nac
        )
        InsertUser(usuario)
        input("\nPresiona Enter para continuar...")
    except Exception as e:
        print(f"Error: {e}")
        input("\nPresiona Enter para continuar...")
# ======================================================================
def FormSHOWALL():
    Users = ShowAllUsers()
    print("\n=== Usuarios registrados en la base de datos")
    for User in Users:
        print(f"Nombre: {User['Nombre']}")
        print(f"Edad: {User['Edad']}")
        print("-" * 30)
# ======================================================================
def FormSEARCHBYNAME():
    print("\n=== Busqueda de usuarios")
    Nombre = input("Nombre del usuario:")
    found_user = SearchByName(Nombre)

    if found_user:
        print(f"\n✓ Usuario encontrado:")
        print(f"  ID: {found_user['id']}")
        print(f"  Nombre: {found_user['Nombre']}")
        print(f"  Edad: {found_user['Edad']}")
        print(f"  Nació: {found_user['FechaNacimiento']}")
    else:
        print(f"\n✗ No se encontró usuario con nombre '{Nombre}'")

    input("\nPresiona Enter para continuar...")
# ======================================================================
def FormUPDATE():
    CleanScreen()
    print("\n=== Actualizar usuario ===")

    # Primero buscar el usuario
    id = int(input("ID del usuario a actualizar: "))

    print("\nIngresa los nuevos datos:")
    nombre = input("Nuevo nombre: ")
    edad = int(input("Nueva edad: "))
    fecha_nac = input("Nueva fecha de nacimiento (YYYY-MM-DD): ")

    try:
        usuario = Usuario(
            Nombre=nombre,
            Edad=edad,
            FechaNacimiento=fecha_nac
        )
        UpdateUser(id, usuario)
        input("\nPresiona Enter para continuar...")
    except Exception as e:
        print(f"Error: {e}")
        input("\nPresiona Enter para continuar...")
# ======================================================================
def FormDELETE():
    CleanScreen()
    print("\n=== Eliminar usuario ===")
    id = input("id del usuario a eliminar: ")  # ← String, no int
    UserFound = SearchByID(id)
    confirmar = input(f"¿Seguro que deseas eliminar a '{UserFound['Nombre']}'? (s/n): ")

    if confirmar.lower() == 's':
        try:
            DeleteUser(id)
            input("\nPresiona Enter para continuar...")
        except Exception as e:
            print(f"Error: {e}")
            input("\nPresiona Enter para continuar...")
    else:
        print("Cancelado")
        input("\nPresiona Enter para continuar...")
# ======================================================================
def CleanScreen():
    print('\033[2J\033[H', end='')
# ======================================================================
