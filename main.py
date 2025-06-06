import dispositivos
import usuarios

def menu_usuario_estandar():
    while True:
        print("""
=== Menú Usuario Estándar ===
1. Consultar datos personales
2. Ver dispositivos
3. Activar automatización
0. Cerrar sesión
""")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                usuarios.mostrar_datos_personales()
            case "2":
                dispositivos.listar_dispositivos()
            case "3":
                dispositivos.automatizacion_encender_luces()
            case "0":
                break
            case _:
                print("Opción inválida.")

def menu_usuario_admin():
    while True:
        print("""
=== Menú Administrador ===
1. Ver dispositivos
2. Crear dispositivo
3. Eliminar dispositivo
4. Cambiar rol de un usuario
5. Consultar automatización
0. Cerrar sesión
""")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                dispositivos.listar_dispositivos()
            case "2":
                tipo = input("Tipo de dispositivo: ")
                nombre = input("Nombre del dispositivo: ")
                dispositivos.crear_dispositivo(tipo, nombre)
            case "3":
                nombre = input("Nombre del dispositivo a eliminar: ")
                dispositivos.eliminar_dispositivo_por_nombre(nombre)
            case "4":
                email = input("Email del usuario a cambiar de rol: ")
                usuarios.cambiar_rol(email)
            case "5":
                dispositivos.automatizacion_encender_luces()
            case "0":
                break
            case _:
                print("Opción inválida.")

def menu_principal():
    while True:
        print("""
=== SmartHome ===
1. Registrar usuario
2. Iniciar sesión
0. Salir
""")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                email = input("Email: ")
                contraseña = input("Contraseña: ")
                usuarios.registrar_usuario(nombre, apellido, email, contraseña)

            case "2":
                email = input("Email: ")
                contraseña = input("Contraseña: ")
                if usuarios.iniciar_sesion(email, contraseña):
                    if usuarios.usuario_actual["rol"] == "admin":
                        menu_usuario_admin()
                    else:
                        menu_usuario_estandar()
            case "0":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción inválida.")

menu_principal()

        
