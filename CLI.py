# CLI.py

from Backend_SQL.Forms import *

def Menu():
    CleanScreen()
    print("╔════════════════════════════════════╗")
    print("║   GESTIÓN DE USUARIOS - MYSQL      ║")
    print("╠════════════════════════════════════╣")
    print("║  1. Crear usuario                  ║")
    print("║  2. Ver todos los usuarios         ║")
    print("║  3. Buscar usuario por Nombre      ║")
    print("║  4. Actualizar usuario             ║")
    print("║  5. Eliminar usuario               ║")
    print("║  6. Salir                          ║")
    print("╚════════════════════════════════════╝")
    print()

def RunCLI():
    while True:
        Menu()
        option = int(input("Selecciona una opción"))
        if option == 1:
            FormINSERT()
        elif option == 2:
            FormSHOWALL()
        elif option == 3:
            FormSEARCHBYNAME()
        elif option == 4:
            FormUPDATE()
        elif option == 5:
            FormDELETE()
        elif option == 6:
            CleanScreen()
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")
            input("\nPresiona Enter para continuar...")
            CleanScreen()


