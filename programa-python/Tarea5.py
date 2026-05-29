# =========================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# CURSO: FUNDAMENTOS DE PROGRAMACIÓN
# FASE 5 - EVALUACIÓN FINAL POA
#
# PROBLEMA 1:
# Evaluación del compromiso de sesiones de clientes
#
# Autor: [Jhonatan Hernandez Jimenez]
# =========================================================


# =========================================================
# MATRIZ DE DATOS
# Formato:
# [ID Cliente, Duración (segundos), Eventos Clics]
# =========================================================

sesiones = [
    ["CLI001", 250, 12],
    ["CLI002", 45, 2],
    ["CLI003", 120, 5],
    ["CLI004", 300, 15],
    ["CLI005", 80, 1],
    ["CLI006", 190, 9]
]


# =========================================================
# FUNCIÓN:
# Clasifica el compromiso de una sesión
# =========================================================

def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# =========================================================
# FUNCIÓN:
# Validar datos de la sesión
# =========================================================

def validar_datos(duracion, clics):

    if duracion < 0 or clics < 0:
        return False

    return True


# =========================================================
# FUNCIÓN:
# Generar informe completo
# =========================================================

def generar_informe(matriz_sesiones):

    # Contadores
    total_alto = 0
    total_medio = 0
    total_bajo = 0

    print("\n====================================================")
    print("      INFORME DE COMPROMISO DE SESIONES")
    print("====================================================\n")

    # Encabezados
    print(f"{'CLIENTE':<12}{'DURACIÓN':<15}{'CLICS':<10}{'NIVEL'}")
    print("----------------------------------------------------")

    # Recorrido de la matriz
    for sesion in matriz_sesiones:

        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        # Validación de datos
        if validar_datos(duracion, clics):

            # Clasificación
            clasificacion = clasificar_compromiso(duracion, clics)

            # Contadores
            if clasificacion == "Alto":
                total_alto += 1

            elif clasificacion == "Medio":
                total_medio += 1

            else:
                total_bajo += 1

            # Mostrar información
            print(f"{id_cliente:<12}{duracion:<15}{clics:<10}{clasificacion}")

        else:
            print(f"{id_cliente:<12} DATOS INVÁLIDOS")

    # =====================================================
    # RESUMEN GENERAL
    # =====================================================

    print("\n====================================================")
    print("                 RESUMEN GENERAL")
    print("====================================================")

    print(f"Sesiones con compromiso ALTO  : {total_alto}")
    print(f"Sesiones con compromiso MEDIO : {total_medio}")
    print(f"Sesiones con compromiso BAJO  : {total_bajo}")

    total_sesiones = total_alto + total_medio + total_bajo

    print(f"\nTotal de sesiones analizadas  : {total_sesiones}")

    print("====================================================")


# =========================================================
# FUNCIÓN:
# Agregar nueva sesión manualmente
# =========================================================

def agregar_sesion():

    print("\n======================================")
    print("        REGISTRO DE NUEVA SESIÓN")
    print("======================================")

    id_cliente = input("Ingrese el ID del cliente: ")

    try:
        duracion = int(input("Ingrese la duración en segundos: "))
        clics = int(input("Ingrese la cantidad de clics: "))

        if validar_datos(duracion, clics):

            nueva_sesion = [id_cliente, duracion, clics]

            sesiones.append(nueva_sesion)

            print("\nSesión registrada correctamente.")

        else:
            print("\nError: Los valores no pueden ser negativos.")

    except ValueError:
        print("\nError: Debe ingresar valores numéricos.")


# =========================================================
# FUNCIÓN:
# Menú principal
# =========================================================

def menu():

    while True:

        print("\n====================================================")
        print("        SISTEMA DE ANÁLISIS DE SESIONES")
        print("====================================================")

        print("1. Mostrar informe de sesiones")
        print("2. Agregar nueva sesión")
        print("3. Salir")

        opcion = input("\nSeleccione una opción: ")

        # Opción 1
        if opcion == "1":
            generar_informe(sesiones)

        # Opción 2
        elif opcion == "2":
            agregar_sesion()

        # Opción 3
        elif opcion == "3":

            print("\nPrograma finalizado correctamente.")
            break

        # Opción inválida
        else:
            print("\nOpción inválida. Intente nuevamente.")


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

menu()