from datetime import datetime
from dispositivos import devolver_lista_de_dispositivos

lista_de_dispositivos = devolver_lista_de_dispositivos()
lista_de_automatizaciones = [
    {
        "Id Dispositivo": 1,
        "Tipo Dispositivo": "luces",
        "Nombre Dispositivo": "luces".lower(),
        "Estado Dispositivo": True,
        "Estado Automatizacion": True, 
        "Fecha de Creacion": "08-06-2025 14:30:15"
    },
    {
        "Id Dispositivo": 2,
        "Tipo Dispositivo": "luces",
        "Nombre Dispositivo": "luces cocina".lower(),
        "Estado Dispositivo": True,
        "Estado Automatizacion": True, 
        "Fecha de Creacion": "17-03-2024 09:05:42"
    }
    ]


def activar_automatizacion_encender_luces():
    try:
        for dispositivo in lista_de_dispositivos:
            if dispositivo["Nombre Dispositivo"] == "luces".lower() and dispositivo["Estado Dispositivo"] == False:
                dispositivo["Estado Dispositivo"] = True
                dispositivo["Estado Automatizacion"] = True
                lista_de_automatizaciones.append(dispositivo)
                return print("automatizacion encendido de luces activada")
            raise ValueError("Las luces ya estan encendidas")
        raise ValueError("No se han detectado luces a encender")
    except ValueError as error:
        print(f"Error: {error}")


def desactivar_automatizacion_encender_luces():
    try:
        for dispositivo in lista_de_dispositivos:
            if dispositivo["Nombre Dispositivo"] == "luces".lower() and dispositivo["Estado Dispositivo"] == True:
                dispositivo["Estado Dispositivo"] = False
                return print("automatizacion encendido de luces desactivada")

            if dispositivo["Nombre Dispositivo"] != "luces".lower():
                raise ValueError("no existe el dispositivo luces")

            if dispositivo["Estado Dispositivo"] == False:
                raise ValueError("las luces ya se encuentran apagadas")
    except ValueError as error:
        print(f"Error: {error}")


def consultar_automatizaciones_activas():
    try:
        for automatizacion in lista_de_automatizaciones:
            if automatizacion["Estado Automatizacion"] == False:
                raise ValueError("No hay automatizaciones activas")
            print(f"Tipo de dispositivo: {automatizacion["Tipo Dispositivo"]}")
            print(f"Nombre del dispositivo: {automatizacion["Nombre Dispositivo"]}")
            print(f"Estado Automatizacion:" + " Encendido" if automatizacion["Estado Automatizacion"] else "Apagado")
            print("-" * 40)
    except ValueError as error:
        print(f"Error: {error}")
              

def menu_automatizaciones():
    while True:
        print(" " * 10)     
        print("*******************************")
        print("*       SmartHome Menu        *")
        print("*         Activacion          *")
        print("*   automatización de Luces   *")
        print("*******************************")
        print("1. Activar Automatizacion")
        print("2. Desactivar Automatizacion")
        print("3. Salir")  
        print(" " * 10)                                             

        opcion_menu = input("Seleccione una opción (1-3): ")

        match opcion_menu:
            case "1":
                activar_automatizacion_encender_luces()
                pass

            case "2":
                desactivar_automatizacion_encender_luces()
                pass

            case "3":
                print("Volver SmartHome Menu")
                break
            
            case _:
                print("Opcion Invalida")