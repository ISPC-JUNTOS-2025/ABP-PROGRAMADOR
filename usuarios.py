usuarios = []
id_usuario = 1
usuario_actual = None


def iniciar_sesion(email, contraseña):
    global usuario_actual

    for u in usuarios:
        if u["email"] == email and u["contraseña"] == contraseña:
            usuario_actual = u
            print(f"Bienvenido, {u['nombre']} ({u['rol']})\n")
            return True

    print("Credenciales incorrectas.\n")
    return False




