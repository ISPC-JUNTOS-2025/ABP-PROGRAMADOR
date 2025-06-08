import usuarios
import dispositivos
import automatizaciones
import rol_enum

def menu_usuario(user):
    while True:
        print("\n--- Menú Usuario ---")
        print("1. Consultar datos personales")
        print("2. Activar automatización")
        print("3. Consultar dispositivos")
        print("4. Cerrar sesión")
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                usuarios.consultar_datos_personales(user["Email"])
            case "2":
                automatizaciones.menu_automatizaciones()
            case "3":
                dispositivos.listar_dispositivos()
            case "4":
                break
            case _:
                print("Opción inválida")

def menu_admin():
    while True:
        print("\n--- Menú Admin ---")
        print("1. Consultar automatizaciones")
        print("2. Gestionar dispositivos")
        print("3. Cambiar rol a usuarios")
        print("4. Cerrar sesión")
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                automatizaciones.consultar_automatizaciones_activas()
            case "2":
                menu_gestion_dispositivos()
            case "3":
                nombre_usuario = input("Ingrese el nombre del usuario: ")
                usuarios.cambiar_rol_usuario(nombre_usuario)
            case "4":
                break
            case _:
                print("Opción inválida")


def menu_gestion_dispositivos():
    while True:
        print("\n--- Gestión de Dispositivos ---")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Buscar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                tipo = input("Tipo de dispositivo: ")
                nombre = input("Nombre del dispositivo: ")
                dispositivos.crear_dispositivo(tipo, nombre)
            case "2":
                dispositivos.listar_dispositivos()
            case "3":
                nombre = input("Nombre a buscar: ")
                dispositivos.buscar_dispositivo_por_nombre(nombre)
            case "4":
                nombre = input("Nombre a eliminar: ")
                dispositivos.eliminar_dispositivo_por_nombre(nombre)
            case "5":
                break
            case _:
                print("Opción inválida.")

def main():
    while True:
        print("\n=== SmartHome ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                nombre = input("Nombre: ")
                email = input("Email: ")
                contraseña = input("Contraseña: ")
                usuarios.registrar_usuario(nombre, email, contraseña)

            case "2":
                email = input("Email: ")
                contraseña = input("Contraseña: ")
                user = usuarios.iniciar_sesion(email, contraseña)
                if user:
                    if user["Rol"] == rol_enum.Roles.ADMINISTRADOR:
                        menu_admin()
                    else:
                        menu_usuario(user)

            case "3":
                print("Saliendo del sistema. ¡Hasta luego!")
                break

            case _:
                print("Opción inválida.")

main()
