from menu import *
from camper import *
from datos import *
from coordinador import *
from trainer import *

ruta_estudiantes_registrados= "registrados.json"
datos_estudiantes_registrados= cargar_datos(ruta_estudiantes_registrados)

ruta_estudiantes_aprobados= "aprobados.json"
datos_estudiantes_aprobados= cargar_datos(ruta_estudiantes_aprobados)

ruta_estudiantes_cursando= "cursando.json"
datos_estudiantes_cursando= cargar_datos(ruta_estudiantes_cursando)

ruta_de_rutas= "rutas.json"
datos_de_rutas= cargar_datos(ruta_de_rutas)

ruta_trainers= "trainer.json"
datos_trainers= cargar_datos(ruta_trainers)

while True:
        menu_principal()
        opc = pedir_opc()
        
        if opc == 1:
            registrar_camper(datos_estudiantes_registrados)
        elif opc == 2:
            main_menu()
            opc = pedir_opc()
            if opc == 1:
                menu_camper()
                opc = pedir_opc()
                if opc==1:
                    ver_notas()
                elif opc==2:
                    print("Horario")
            elif opc==2:
                menu_trainer()
                opc= pedir_opc()
                if opc==1:
                    print("Horario")
                if opc==2:
                    modificar_notas(datos_estudiantes_cursando)
            elif opc==3:
                menu_coordinador()
                opc= pedir_opc()
                if opc==1:
                    modificar_camper(datos_estudiantes_registrados)
                    aprobar_camper(datos_estudiantes_registrados, datos_estudiantes_aprobados)
                elif opc==2:
                    asignar_ruta(datos_estudiantes_aprobados, datos_estudiantes_cursando)
                elif opc==3:
                    crear_ruta(datos_estudiantes_cursando)  
                elif opc==4:
                    agregar_trainer(datos_trainers)
                elif opc==5:
                    asignar_trainer(datos_trainers, datos_estudiantes_cursando)
                elif opc==6:
                    definir_riesgo(datos_estudiantes_cursando)
        elif opc==3:
            pruebas_admision(datos_estudiantes_registrados)
        else:
            print("Opción no válida.")



        guardar_datos(datos_estudiantes_registrados, ruta_estudiantes_registrados)
        guardar_datos(datos_estudiantes_aprobados, ruta_estudiantes_aprobados)
        guardar_datos(datos_estudiantes_cursando, ruta_estudiantes_cursando)
        guardar_datos(datos_de_rutas, ruta_de_rutas)
        guardar_datos(datos_trainers, ruta_trainers)

