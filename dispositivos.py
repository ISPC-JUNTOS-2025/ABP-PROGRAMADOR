from datetime import datetime



id_dispositivo = 1


def crear_dispositivo(tipo_dispositivo, nombre_dispositivo):
    global id_dispositivo

    nuevo_dispositivo = {
        "Id": id_dispositivo,
        "Tipo Dispositivo": tipo_dispositivo,
        "Nombre Dispositivo": nombre_dispositivo,
        "Estado": False, 
        "Fecha de Creacion": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    dispositivos.append(nuevo_dispositivo)
    id_dispositivo += 1

    return nuevo_dispositivo


def buscar_dispositivo_por_nombre(nombre_dispositivo):
    for dispositivo in dispositivos:
        if dispositivo["Nombre Dispositivo"].lower() == nombre_dispositivo.lower():
            print("Id:", dispositivo["Id"])
            print("Tipo Dispositivo:", dispositivo["Tipo Dispositivo"])
            print("Nombre Dispositivo:", dispositivo["Nombre Dispositivo"])
            print("Estado:", "Encendido" if dispositivo["Estado"] else "Apagado")
            print("Fecha de Creacion:", dispositivo["Fecha de Creacion"])
            print("-" * 40)
            return 

    print(f"No se encontró el dispositivo: {nombre_dispositivo}")


def listar_dispositivos():
    if not dispositivos:
        print("No se ha encontrado ningún dispositivo")
        return
    
    for dispositivo in dispositivos:
        print("Id:", dispositivo["Id"])
        print("Tipo Dispositivo:", dispositivo["Tipo Dispositivo"])
        print("Nombre Dispositivo:", dispositivo["Nombre Dispositivo"])
        print("Estado:", "Encendido" if dispositivo["Estado"] else "Apagado")
        print("Fecha de Creacion:", dispositivo["Fecha de Creacion"])
        print("-" * 40)  


def eliminar_dispositivo_por_nombre(nombre_dispositivo):
    for i in dispositivos:
        if i["Nombre Dispositivo"] == nombre_dispositivo:
            dispositivos.remove(i)
            return print(f"El dispositivo: {i["Nombre Dispositivo"]}, ha sido eliminado")

    return print(f"No se encontro el dispositivo: {nombre_dispositivo}")


def automatizacion_encender_luces():
    print("movimiento detectado en entrada principal")

    for i in dispositivos:
        if i["Nombre Dispositivo"] == "luces".lower() and i["Estado"] == False:
            i["Estado"] = True
            return print("luces entrada principal encendidas")
            

    return print("No se han detectado luces a encender")    
