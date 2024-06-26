#Guardar y cargar datos en json
import json 

def cargar_datos(archivo):
    try:
        with open(archivo, "r") as file:
            user = json.load(file)
            print("Datos cargados") 
            return user
    except Exception as a:
        print("Error al cargar los datos", a )


def guardar_datos(datos, archivo):
    try:
        datos = dict(datos)
        thing = json.dumps(datos, indent=4)
        file = open(archivo, "w")
        file.write(thing)
        file.close()
        print("Datos cargados") 
    except Exception:
        print("Error al cargar los datos", Exception) 