import time
from colorama import init, Fore, Style
import json

# Inicializar colorama
init(autoreset=True)

# Cargar contactos precargados desde un archivo JSON
def cargar_contactos_precargados():
    with open('contactos.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Cargar contactos manualmente desde el input
def cargar_contactos_manualmente():
    contactos = []
    cantidad = int(input("¿Cuántos contactos querés ingresar? "))
    for i in range(cantidad):
        print(f"\nContacto #{i+1}")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        contactos.append({"nombre": nombre, "telefono": telefono})
    return contactos

# Algoritmo Bubble Sort para ordenar contactos alfabéticamente por nombre
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["nombre"].lower() > lista[j + 1]["nombre"].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Búsquedas
def busqueda_lineal(lista, nombre):
    for contacto in lista:
        if contacto["nombre"].lower() == nombre.lower():
            return contacto
    return None

def busqueda_binaria(lista, nombre):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = lista[medio]["nombre"].lower()
        if actual == nombre.lower():
            return lista[medio]
        elif actual < nombre.lower():
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

def buscar_por_telefono(lista, numero):
    for contacto in lista:
        if contacto["telefono"] == numero:
            return contacto
    return None

def mostrar_contactos(lista):
    for contacto in lista:
        print(Fore.YELLOW + f"{contacto['nombre']} - {contacto['telefono']}")

# Función principal de la aplicación
def main():
    modo = obtener_modo_ingreso()
    
    if modo == "s":
        contactos = cargar_contactos_manualmente()
    else:
        contactos = cargar_contactos_precargados()
        print(Fore.GREEN + "\n✅ Usando lista de contactos precargados.")
    
    while True:
        print(Fore.CYAN + "\n📱 GESTOR DE CONTACTOS")
        print(Fore.CYAN + "----------------------")

        print(Fore.MAGENTA + "\n📋 Lista de contactos ingresados:")
        mostrar_contactos(contactos)

        # Ordenar y mostrar
        bubble_sort(contactos)
        print(Fore.MAGENTA + "\n📚 Lista ordenada alfabéticamente:")
        mostrar_contactos(contactos)

        # Buscar por nombre
        nombre_buscado = input(Fore.CYAN + "\n🔍 Ingresá un nombre para buscar: ")

        inicio = time.perf_counter()
        res_lineal = busqueda_lineal(contactos, nombre_buscado)
        tiempo_lineal = time.perf_counter() - inicio
        res_binaria = busqueda_binaria(contactos, nombre_buscado)
        tiempo_binaria = time.perf_counter() - inicio

        print(Fore.CYAN + "\n📊 Resultados de búsqueda por nombre:")
        if res_lineal:
            print(Fore.GREEN + f"🔎 Lineal: {res_lineal} ({tiempo_lineal:.14f} segundos)")
        else:
            print(Fore.RED + "❌ No se encontró con búsqueda lineal.")

        if res_binaria:
            print(Fore.GREEN + f"🔎 Binaria: {res_binaria} ({tiempo_binaria:.14f} segundos)")
        else:
            print(Fore.RED + "❌ No se encontró con búsqueda binaria.")

        if tiempo_binaria > 0:
            relacion = tiempo_lineal / tiempo_binaria
            print(Fore.BLUE + f"\n📈 Relación de rendimiento (lineal/binaria): {relacion:.2f} a 1")
        else:
            print(Fore.RED + "\n⚠️ No se puede calcular la relación (tiempo de búsqueda binaria es 0)")

        # Buscar por teléfono
        telefono_buscado = input(Fore.CYAN + "\n📞 Ingresá un número para buscar por teléfono: ")
        res_telefono = buscar_por_telefono(contactos, telefono_buscado)

        print(Fore.CYAN + "\n📲 Resultado de búsqueda por teléfono:")
        if res_telefono:
            print(Fore.GREEN + f"✅ Encontrado: {res_telefono}")
        else:
            print(Fore.RED + "❌ No se encontró ese número.")

        opcion = input(Fore.CYAN + "\n¿Querés realizar otra operación? (s para seguir / cualquier otra tecla para salir): ").lower()
        if opcion != "s":
            print(Fore.CYAN + "\n👋 ¡Hasta la próxima!")
            break

# Validar opción de ingreso
def obtener_modo_ingreso():
    while True:
        modo = input("¿Querés ingresar los contactos manualmente? (s/n): ").lower()
        if modo in ["s", "n"]:
            return modo
        else:
            print(Fore.RED + "⚠️ Ingresá una opción válida: 's' para sí o 'n' para no.")

# Punto de entrada
main()
