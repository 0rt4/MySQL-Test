from Backend_SQL.SQLController import InsertarUser, Usuario

def FormUser():
    return {
        'Nombre': input("Nombre: "),
        'Edad': int(input("Edad: ")),
        'FechaNacimiento': input("Fecha de Nacimiento: ")
    }

def SendToDB(Nombre,Edad,FechaNac):
    try:
        usuario = Usuario(
            Nombre=Nombre,
            Edad=Edad,
            FechaNacimiento=FechaNac
        )
        InsertarUser(usuario)
    except Exception as e:
        print(f"Error: {e}")

def RunCLI():
    print("Captura de usuarios para la base de datos")
    print("Deseas agregar un usuario?")
    Resp= input("S/N:  ")

    while Resp == "S":
        data = FormUser()
        SendToDB(data ['Nombre'],data ['Edad'],data ['FechaNacimiento'])
        print("Deseas agregar otro usuario?")
        Resp= input("S/N:  ")
