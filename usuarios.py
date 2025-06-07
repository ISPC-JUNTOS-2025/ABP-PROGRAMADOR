def iniciar_sesion(email_usuario, contraseña_usuario):
    try:
        # 1 - Validar que no estén vacíos
        if email_usuario.strip() == '' or contraseña_usuario.strip() == '':
            raise ValueError("El email y la contraseña no pueden estar vacíos.")
        
        # 2 - Validar formato del email
        utilidades.verificar_email(email_usuario)

        # 3 - Buscar usuario en la lista
        usuario_encontrado = None
        for u in lista_de_usuarios:
            if u["Email"] == email_usuario:
                usuario_encontrado = u
                break

        if not usuario_encontrado:
            raise ValueError("No se encontró un usuario con ese email.")

        # 4 - Encriptar la contraseña ingresada para compararla
        contraseña_encriptada_ingresada = utilidades.encriptar_contraseña(contraseña_usuario)

        if usuario_encontrado["Contraseña"] != contraseña_encriptada_ingresada:
            raise ValueError("La contraseña es incorrecta.")

        # 5 Desencriptar contraseña original
        contraseña_desencriptada = utilidades.desencriptar_contraseña(usuario_encontrado["Contraseña"])

        print(f"Inicio de sesión exitoso. Bienvenido, {usuario_encontrado['Nombre']}.")
         

        return usuario_encontrado

    except ValueError as error:
        print(f"Error: {error}")
        return None

































def iniciar_sesion(email_usuario, contraseña_usuario):
    try:
        # Verifica que no estén vacíos
        if email_usuario.strip() == "" or contraseña_usuario.strip() == "":
            raise ValueError("El email y la contraseña no pueden estar vacíos.")

        # Buscar el usuario
        usuario_encontrado = next((u for u in lista_de_usuarios if u["Email"] == email_usuario), None)

        if not usuario_encontrado:
            raise ValueError("No se encontró un usuario con ese email.")

        # Encriptar la contraseña ingresada para compararla
        contraseña_encriptada = utilidades.encriptar_contraseña(contraseña_usuario)

        if usuario_encontrado["Contraseña"] != contraseña_encriptada:
            raise ValueError("La contraseña es incorrecta.")

        print(f"Inicio de sesión exitoso. Bienvenido, {usuario_encontrado['Nombre']}.")
        return usuario_encontrado

    except ValueError as error:
        print(f"Error: {error}")
        return None




