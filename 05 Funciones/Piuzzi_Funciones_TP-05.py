# Lógica principal del TP de Funciones.
# Se importan funciones desde Modulos_Funciones para resolver las actividades.
# Aclaración: los `int()` están en el input para mantener las funciones reutilizables.

from Modulos_Funciones import (imprimir_hola_mundo, saludar_usuario, informacion_personal, resultado_area_perimetro, segundos_a_horas, tabla_multiplicar, operaciones_basicas, calcular_imc, celsius_a_fahrenheit, calcular_promedio)

# 1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# # Codigo:
print(imprimir_hola_mundo())



# 2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y 
# devuelva un saludo personalizado.

# # Codigo:
usuario = input("Ingrese su nombre: ")
saludar_usuario(usuario)



# 3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# # Codigo
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su pais: ")
informacion_personal(nombre, apellido, edad, residencia)



# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# # Codigo:
seguir = "s"
while seguir.lower() == "s":
    radio = float(input("Ingrese el radio del cirulo: "))
    resultado_area_perimetro(radio)
    seguir = input("Querés seguir calculando ? (s/n): ")


# 5) Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# # Codigo:
segundos = int(input("Ingrese la cantidad de segundo: "))
segundos_a_horas(segundos)



# # 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# # Codigo:
numero = int(input("Ingrese un número para saber su tabla de multiplicación: "))
tabla_multiplicar(numero)



# # 7)Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

# # Codigo:
seguir = "s"
while seguir.lower() == "s":
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    operaciones_basicas(a, b)
    seguir = input("Querés calcular seguir calculando imc? (s/n): ")


# # 8)Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# # Codigo:
seguir = "s"
while seguir.lower() == "s":
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros (ejemplo_1.6m): "))
    calcular_imc(peso, altura)
    seguir = input("Querés calcular seguir calculando imc? (s/n): ")



# # 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# # Codigo:
seguir = "s"
while seguir.lower() == "s":
    celsius = float(input("Ingrese la temperatura en °C: "))
    celsius_a_fahrenheit(celsius)
    seguir = input("Querés calcular otra temperatura? (s/n): ")


# # 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.
seguir = "s"
while seguir.lower() == "s":
    a = int(input("Ingrese la nota A: "))
    b = int(input("Ingrese la nota B: "))
    c = int(input("Ingrese la nota C: "))
    calcular_promedio(a, b, c)
    seguir = input("Querés calcular otro promedio? (s/n): ")