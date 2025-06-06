usuarios = []
id_usuario = 1
usuario_actual = None

def registrar_usuario(nombre, apellido, email, contraseña):
    global id_usuario

    rol = "admin" if len(usuarios) == 0 else "estandar"

    nuevo_usuario = {
        "id": id_usuario,
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "contraseña": contraseña,
        "rol": rol
    }

    usuarios.append(nuevo_usuario)
    id_usuario += 1
    print(f"Usuario registrado como '{rol}'.\n")

def iniciar_sesion(email, contraseña):
    global usuario_actual

    for u in usuarios:
        if u["email"] == email and u["contraseña"] == contraseña:
            usuario_actual = u
            print(f"Bienvenido, {u['nombre']} ({u['rol']})\n")
            return True

    print("Credenciales incorrectas.\n")
    return False

def mostrar_datos_personales():
    if usuario_actual:
        print("\n Datos del usuario:")
        print(f"Nombre: {usuario_actual['nombre']} {usuario_actual['apellido']}")
        print(f"Email: {usuario_actual['email']}")
        print(f"Rol: {usuario_actual['rol']}")
        print("-" * 40)

def cambiar_rol(email):
    for u in usuarios:
        if u["email"] == email:
            if u["rol"] == "estandar":
                u["rol"] = "admin"
            else:
                u["rol"] = "estandar"
            print(f"El rol del usuario fue cambiado a: {u['rol']}")
            return
    print("Usuario no encontrado.")


