from datetime import datetime
import utilidades 
import rol_enum 

lista_de_usuarios = [{
            "id usuario": 1,
            "Nombre": "dana",
            "Email": "dana@gmail.com",
            "Contraseña": "+-=¿¡6",
            "Rol": rol_enum.Roles.ADMINISTRADOR,
            "Fecha de creacion": "08-06-2025 12:08:01"
            },
            {
            "id usuario": 2,
            "Nombre": "luciana",
            "Email": "lu28@gmail.com",
            "Contraseña": "l&l&-0-¡",
            "Rol": rol_enum.Roles.USUARIO,
            "Fecha de creacion": "08-06-2025 13:08:01"
            }
        ]

id_usuario = 3

def registrar_usuario(nombre_de_usuario,email_usuario,contraseña_de_usuario):
    global id_usuario
    
    try:
        if nombre_de_usuario == " " or nombre_de_usuario == "":
            raise ValueError("El nombre no puede estar vacio")
        if contraseña_de_usuario == " " or contraseña_de_usuario == "":
            raise ValueError("La contraseña no puede estar vacia")
        utilidades.verificar_email(email_usuario)
        contraseña_encriptada = utilidades.encriptar_contraseña(contraseña_de_usuario)
        usuario = {
            "id usuario" : id_usuario,
            "Nombre" : nombre_de_usuario,
            "Email" : email_usuario,
            "Contraseña" : contraseña_encriptada,
            "Rol" : rol_enum.Roles.USUARIO,
            "Fecha de creacion" :  datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        lista_de_usuarios.append(usuario)
        id_usuario += 1
        return print(usuario)
    except ValueError as error:
        print(f"Error: {error}")


def iniciar_sesion(email_usuario, contraseña_usuario):
    try:
        if contraseña_usuario == ' ' or email_usuario == '':
            raise ValueError("El email o la contraseña no pueden estar vacíos.")
        
        utilidades.verificar_email(email_usuario)

        usuario_encontrado = None
        for usuario in lista_de_usuarios:
            if usuario["Email"] == email_usuario:
                usuario_encontrado = usuario

        if not usuario_encontrado:
            raise ValueError("Email o contraseña incorrectos")

        contraseña_encriptada_ingresada = utilidades.encriptar_contraseña(contraseña_usuario)

        if usuario_encontrado["Contraseña"] != contraseña_encriptada_ingresada:
            raise ValueError("Email o contraseña incorrectos")

        print(f"Inicio de sesión exitoso. Bienvenido, {usuario_encontrado['Nombre']}.")
        return usuario_encontrado

    except ValueError as error:
        print(f"Error: {error}")
        return None
    

def consultar_datos_personales(email_usuario):
    try:
        for usuario in lista_de_usuarios:
            if email_usuario == usuario["Email"]: 
                print("\n--- DATOS PERSONALES ---")
                print(f"Nombre: {usuario['Nombre']}")
                print(f"Email: {usuario['Email']}")
                return 
        raise ValueError("No se encontro un usuario con ese email") 
    except ValueError as error:
        print(f"Error: {error}")


def cambiar_rol_usuario(nombre_usuario):
    try:
        for usuario in lista_de_usuarios: 
            if usuario["Nombre"] == nombre_usuario:
                usuario["Rol"] = rol_enum.Roles.ADMINISTRADOR
                print(f"{usuario['Nombre']} ahora es ADMINISTRADOR")
                return
        raise ValueError("No se encontro el usuario: " + nombre_usuario)
    except ValueError as error:
        print(f"Error: {error}")
        

