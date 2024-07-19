def ingresar_calificaciones():
    nombre = input("Ingrese el nombre del alumno: ")
    eval_continua1 = float(input("Ingrese la calificación de Evaluación Continua 1: "))
    eval_continua2 = float(input("Ingrese la calificación de Evaluación Continua 2: "))
    practica = float(input("Ingrese la calificación de Práctica: "))
    eval_final = float(input("Ingrese la calificación de Evaluación Final: "))
    
    promedio = (eval_continua1 + eval_continua2 + practica + eval_final) / 4
    return nombre, eval_continua1, eval_continua2, practica, eval_final, promedio

def guardar_en_archivo(alumno):
    with open("calificaciones.txt", "a") as file:
        file.write(f"{alumno[0]}, {alumno[1]}, {alumno[2]}, {alumno[3]}, {alumno[4]}, {alumno[5]}")

def mostrar_lista():
    try:
        with open("calificaciones.txt", "r") as file:
            print("Lista de Alumnos:")
            print("=================")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Aún no hay alumnos registrados.")

def eliminar_alumno():
    nombre_buscar = input("Ingrese el nombre del alumno que desea eliminar: ")
    try:
        with open("calificaciones.txt", "r") as file:
            lines = file.readlines()
        with open("calificaciones.txt", "w") as file:
            encontrado = False
            for line in lines:
                if nombre_buscar not in line.split(",")[0].strip():
                    file.write(line)
                else:
                    encontrado = True
            if encontrado:
                print(f"Se ha eliminado al alumno {nombre_buscar} correctamente.")
            else:
                print(f"No se encontró al alumno {nombre_buscar} en la lista.")
    except FileNotFoundError:
        print("Aún no hay alumnos registrados.")

def menu():
    while True:
        print("seleccione el que desee ejecutar:")
        print("1. Ingresar nuevas calificaciones")
        print("2. Mostrar lista de alumnos")
        print("3. eliminar alumno del registro de notas")
        print("4. salir")
        opcion = input("Seleccione una opción (1/2/3/4): ")
        
        if opcion == "1":
            alumno = ingresar_calificaciones()
            guardar_en_archivo(alumno)
            print("Calificaciones ingresadas correctamente.")
        elif opcion == "2":
            mostrar_lista()
        elif opcion == "3":
            eliminar_alumno()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("accion denegada.")
menu()
