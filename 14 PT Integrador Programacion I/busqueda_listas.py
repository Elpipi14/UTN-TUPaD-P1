import time
import random

# Generamos una lista simulada de 1 millón de productos
productos = [f"producto{i}" for i in range(1, 1_000_001)]

# Elegimos un producto que esté al final para forzar el peor caso en búsqueda lineal
producto_buscado = "producto1000000"

# --- Algoritmo 1: Búsqueda Lineal ---
def busqueda_lineal(lista, objetivo):
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False

# --- Algoritmo 2: Búsqueda Binaria ---
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return False

# --- Medimos el tiempo de ejecución de cada algoritmo ---
def medir_tiempo(funcion, lista, objetivo):
    inicio = time.time()
    resultado = funcion(lista, objetivo)
    fin = time.time()
    return resultado, fin - inicio

# Prueba de búsqueda lineal
resultado1, tiempo1 = medir_tiempo(busqueda_lineal, productos, producto_buscado)

# Para búsqueda binaria debemos ordenar la lista
productos_ordenados = sorted(productos)
resultado2, tiempo2 = medir_tiempo(busqueda_binaria, productos_ordenados, producto_buscado)

# Mostramos los resultados
print(f"Búsqueda Lineal: Resultado = {resultado1}, Tiempo = {tiempo1:.6f} segundos")
print(f"Búsqueda Binaria: Resultado = {resultado2}, Tiempo = {tiempo2:.6f} segundos")
