from datos import *

ruta_estudiantes_aprobados = "aprobados.json"
datos_estudiantes_aprobados = cargar_datos(ruta_estudiantes_aprobados)

ruta_estudiantes_cursando = "cursando.json"
datos_estudiantes_cursando = cargar_datos(ruta_estudiantes_cursando)


def modificar_notas(datos_estudiantes_cursando):
    cargar_datos(ruta_estudiantes_cursando)
    print("Digite el documento del trainer: ")
    doc=input()
    print ("¿En que ruta esta?\n1.NodeJs\n2.Java\n3.NetCore")
    opc=int(input())
    if opc==1:
        notas = datos_estudiantes_cursando["Rutas"]["NodeJs"][doc].get("Notas")
        nombre= datos_estudiantes_aprobados["usuarios"][doc].get("Nombres")
        print("Estan son las notas de:", nombre)
        for clave, valor in notas.items():
            print (clave, valor )
        datos_estudiantes_cursando["Rutas"]["NodeJs"][doc]["Notas"]["Quizes y Trabajos"]=int(input("Digite la nota: "))
        datos_estudiantes_cursando["Rutas"]["NodeJs"][doc]["Notas"]["Prueba teorica"]=int(input("Digite la nota: "))
        datos_estudiantes_cursando["Rutas"]["NodeJs"][doc]["Notas"]["Prueba practica(Proyecto)"]=int(input("Digite la nota: "))
        guardar_datos(datos_estudiantes_cursando, ruta_estudiantes_cursando)
        for clave, valor in notas.items():
            print (clave, valor )
    elif opc==2:
        notas = datos_estudiantes_cursando["Rutas"]["Java"][doc].get("Notas")
        nombre= datos_estudiantes_aprobados["usuarios"][doc].get("Nombres")
        print("Estan son las notas de:", nombre)
        for clave, valor in notas.items():
            print (clave, valor )
        datos_estudiantes_cursando["Rutas"]["Java"][doc]["Notas"]["Quizes y Trabajos"]=int(input("Digite la nota: "))
        datos_estudiantes_cursando["Rutas"]["Java"][doc]["Notas"]["Prueba teorica"]=int(input("Digite la nota: "))
        datos_estudiantes_cursando["Rutas"]["Java"][doc]["Notas"]["Prueba practica(Proyecto)"]=int(input("Digite la nota: "))
        guardar_datos(datos_estudiantes_cursando, ruta_estudiantes_cursando)
        for clave, valor in notas.items():
            print (clave, valor )
    elif opc==3:
        notas = datos_estudiantes_cursando["Rutas"]["NetCore"][doc].get("Notas")
        nombre= datos_estudiantes_aprobados["usuarios"][doc].get("Nombres")
        print("Estan son las notas de:", nombre)
        for clave, valor in notas.items():
            print (clave, valor )
        datos_estudiantes_cursando["Rutas"]["NetCore"][doc]["Notas"]["Quizes y Trabajos"]=int(input("Digite la nota: "))
        datos_estudiantes_cursando["Rutas"]["NetCore"][doc]["Notas"]["Prueba teorica"]=int(input("Digite la nota: "))
        datos_estudiantes_cursando["Rutas"]["NetCore"][doc]["Notas"]["Prueba practica(Proyecto)"]=int(input("Digite la nota: "))
        guardar_datos(datos_estudiantes_cursando, ruta_estudiantes_cursando)
        for clave, valor in notas.items():
            print (clave, valor )    
    else:
        print("Valor no valido!")

