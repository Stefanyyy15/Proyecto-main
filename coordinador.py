from datos import *

ruta_estudiantes_aprobados= "aprobados.json"
datos_estudiantes_aprobados= cargar_datos(ruta_estudiantes_aprobados)

ruta_estudiantes_cursando= "cursando.json"
datos_estudiantes_cursando= cargar_datos(ruta_estudiantes_cursando)

ruta_de_rutas= "rutas.json"
datos_de_rutas= cargar_datos(ruta_de_rutas)

ruta_trainers= "trainer.json"
datos_trainers= cargar_datos(ruta_trainers)

def asignar_ruta(datos_estudiantes_aprobados, datos_estudiantes_cursando):
    print("Digite el documento del camper que desea modificar: ")
    doc = input()
    if doc in datos_estudiantes_aprobados["usuarios"]:
        usuario = datos_estudiantes_aprobados["usuarios"][doc]
        usuario["Proceso"] = "Cursando"
        usuario_sin_datos = usuario.copy()
        eliminar = ["Nombres", "Apellidos", "Direccion", "Acudiente", "Telefono fijo", "Contacto"]
        for i in eliminar:
            usuario_sin_datos.pop(i, None)
            usuario_sin_datos["Notas"] = {"Quizes y Trabajos": 0, "Prueba teorica":0, "Prueba practica(Proyecto)": 0,}
        print("Elija la ruta del camper: \n1.NodeJs \n2.Java \n3.NetCore")
        ruta = int(input())
        if ruta == 1:
            if len(datos_estudiantes_cursando["Rutas"].get("NodeJs")) < 32:
                datos_estudiantes_cursando["Rutas"]["NodeJs"][doc] = usuario_sin_datos
            else:
                print("En la ruta NodeJs no caben más campers!")
        elif ruta == 2:
            if len(datos_estudiantes_cursando["Rutas"].get("Java")) < 32:
                datos_estudiantes_cursando["Rutas"]["Java"][doc] = usuario_sin_datos
            else:
                print("En la ruta Java no caben más campers!")
        elif ruta == 3:
            if len(datos_estudiantes_cursando["Rutas"].get("NetCore")) < 32:
                datos_estudiantes_cursando["Rutas"]["NetCore"][doc] = usuario_sin_datos
            else:
                print("En la ruta NetCore no caben más campers!")
            guardar_datos(datos_estudiantes_cursando, ruta_estudiantes_cursando)
            guardar_datos(datos_estudiantes_aprobados, ruta_estudiantes_aprobados)
            print("Estudiante aprobado movido exitosamente de aprobados a cursando.")
        else:
            print("El estudiante no está en proceso Cursando.")
    else:
        print("El documento no corresponde a ningún estudiante aprobado.")

def asignar_trainer(datos_trainers, datos_estudiantes_cursando):
    doc = input("Ingresa el documento del trainer: ")
    trainer = datos_trainers["Trainers"][doc]["Nombre"]
    print(trainer)
    print("1. NodeJs")
    print("2. Java")
    print("1. NetCore")
    ruta = None
    opc = int(input("Ingresa la ruta para buscar el camper: "))
    if opc == 1:
        ruta = "NodeJs"
    elif opc == 2:
        ruta = "Java"
    elif opc == 3:
        ruta = "NetCore"
    docu = input("Ingresa el documento del camper: ")

    ola = datos_estudiantes_cursando["Rutas"][ruta][docu]["trainers"] = trainer
    guardar_datos(datos_estudiantes_cursando, ruta_estudiantes_cursando)

def agregar_trainer(datos_trainers):
    bitbop={}
    print("Digite el numero de documento del trainer ")
    doc=input()
    if doc in datos_trainers:
        print("Trainer Existe!")
    else:
        bitbop["Nombre"]=input("Digite el nombre y apellido del trainer: ")
        bitbop["Edad"]=int(input("Digite la edad del trainer: "))
        datos_trainers["Trainers"][doc]=bitbop
        guardar_datos(datos_trainers, ruta_trainers)

def crear_ruta(datos_estudiantes_cursando):
    cargar_datos(ruta_estudiantes_cursando)
    vivi= {}
    name_ruta = input("Ingresa el nombre de la ruta: ")
    print("Esta seguro del nombre", name_ruta,"\n1.Si\n2.No")
    opc=int(input())
    if opc==1:
        datos_estudiantes_cursando["Rutas"][name_ruta]=vivi
    elif opc==2:
        nuevo_name_ruta = input("Ingresa el nombre de la ruta: ")
        datos_estudiantes_cursando["Rutas"][nuevo_name_ruta]=vivi
        print("Ruta añadida exitosamente!")
    guardar_datos(datos_estudiantes_cursando, ruta_estudiantes_cursando)

def definir_riesgo(datos_estudiantes_cursando):
    try:
        datos_estudiantes_cursando = cargar_datos(ruta_estudiantes_cursando)
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return
    print("1. NodeJs")
    print("2. Java")
    print("3. NetCore")
    try:
        opc = int(input("Ingresa la ruta para buscar el camper: "))
    except Exception:
        print("Opción no válida!")
        return
    ruta = None
    if opc == 1:
        ruta = "NodeJs"
    elif opc == 2:
        ruta = "Java"
    elif opc == 3:
        ruta = "NetCore"
    else:
        print("Opción no válida!")
        return
    doc = input("Digite el documento del camper que desea modificar el riesgo: ")
    
    if ruta in datos_estudiantes_cursando["Rutas"]:
        if doc in datos_estudiantes_cursando["Rutas"][ruta]:
            try:
                opi = int(input("¿El camper está en riesgo?\n1. Sí\n2. No\nOpción: "))
            except Exception:
                print("Opción no válida!")
                return
            if opi == 1:
                datos_estudiantes_cursando["Rutas"][ruta][doc]["Riesgo"] = True
            elif opi == 2:
                datos_estudiantes_cursando["Rutas"][ruta][doc]["Riesgo"] = False
            else:
                print("Opción no válida!")
                return
            guardar_datos(datos_estudiantes_cursando, ruta_estudiantes_cursando)
            print("Riesgo actualizado correctamente.")
        else:
            print(f"El documento {doc} no existe en la ruta {ruta}.")
    else:
        print(f"La ruta {ruta} no existe en los datos.")

def leer_registrados(datos_estudiantes_registrados):
    for i,a in datos_estudiantes_registrados["usuarios"].items():
        print(f"")
