import random
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

# Función para obtener un set de datos
def obtener_datos():
    print("\n1. Ingresar datos manualmente")
    print("2. Usar datos automáticos")
    opcion = input(Fore.CYAN + "Selecciona una opción: ")

    if opcion == '1':
        datos = input(Fore.YELLOW + "Ingresa los datos separados por coma (ej: 3,7,1,4): ")
        try:
            lista = [int(x.strip()) for x in datos.split(",") if x.strip()]
            return lista
        except ValueError:
            print(Fore.RED + "Error: ingrese solo números enteros.")
            return obtener_datos()
    elif opcion == '2':
        cantidad = random.randint(5, 20)
        lista = random.sample(range(1, 100), cantidad)
        print(Fore.GREEN + f"Set de datos automático generado ({cantidad} elementos): {lista}")
        return lista
    else:
        print(Fore.RED + "Opción inválida. Intenta nuevamente.")
        return obtener_datos()

# Algoritmo de búsqueda lineal
def busqueda_lineal():
    datos = obtener_datos()
    try:
        objetivo = int(input(Fore.YELLOW + "Ingresa el número que deseas buscar: "))
    except ValueError:
        print(Fore.RED + "Error: ingresa un número entero.")
        return

    for i, valor in enumerate(datos):
        if valor == objetivo:
            print(Fore.GREEN + f"Número encontrado en la posición {i}.")
            return
    print(Fore.RED + "Número no encontrado.")

# Algoritmo de ordenamiento: Burbuja
def ordenamiento_burbuja():
    datos = obtener_datos()
    print(Fore.YELLOW + f"Datos originales: {datos}")

    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]

    print(Fore.GREEN + f"Datos ordenados: {datos}")

# Menú principal
def menu():
    while True:
        print(Fore.CYAN + "\n=== MENÚ PRINCIPAL ===")
        print("1. Algoritmo de Búsqueda")
        print("2. Algoritmo de Ordenamiento")
        print("3. Salir")
        opcion = input(Fore.CYAN + "Selecciona una opción: ")

        if opcion == '1':
            busqueda_lineal()
        elif opcion == '2':
            ordenamiento_burbuja()
        elif opcion == '3':
            print(Fore.GREEN + "Saliendo del programa.")
            break
        else:
            print(Fore.RED + "Opción inválida. Intenta nuevamente.")

# Ejecutar el programa
menu()
