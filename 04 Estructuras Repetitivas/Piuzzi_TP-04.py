# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# codigo:
# for i in range(0,101):
#     print(i);


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# codigo:
# seguir= "si"
# while seguir == "si":
#     numero = input("ingrese un numero positivo entero: ")
#     digitos = len(numero)
#     print ("cantidad de digitos: ", digitos)
#     seguir= input("desea seguir? si/no")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# codigo:
# seguir="si"
# while seguir.lower() == "si":
#     num1 = int(input("Ingrese el primer numero "))
#     num2 = int(input("Ingrese el segundo numero "))
#     suma = 0

#     print("La suma es: ", (num1+num2))
#     seguir= input("desea seguir? si/no: ")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# Codigo:
# acum = 0
# i= True

# # Se podria usar un True para convalidar el ciclo y una vez que ingrese 0 hacer un break
# while i == True:
#     num = int(input("Ingrese un numero entero: "))
#     if(num != 0):
#         acum += num
#     else:
#         print("El programa debe detenerse por ingreso del Cero")
#         # Break es más legible y directo que cambiar una variable booleana.
#         i = False
        

# print("Total acumulado de la sumatorias de enteros: ", acum)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# # Codigo:

# from random import *

# aleatorio = randint(0, 9);
# intentos = 0
# i=True

# while i == True:
#     intentos += 1
#     num = int(input("Ingrese número aleatorio entre 0 y 9 = "));
    
#     if(num == aleatorio):
#         print("Haz adivinado")
#         i = False
#     else:
#         print("Intenta de nuevo...")

# print("cantidad de intentos realizados: ", intentos)

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# Codigo:

# for cont in range(100,-2,-2):
#     print(cont)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# Codigo:

# user = int(input("Ingrese un número entero positivo: "))
# resultado = 0

# for i in range(0,user,1):
#     resultado += i

# print("El resultado de la suma es:", resultado)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Codigo:

# Inicialización de contadores:

# pares = 0
# impares = 0
# positivos = 0
# negativos = 0

# # Cambiá este número a 100 para cumplir 
# cantidad = 10  

# for i in range(cantidad):
#     num = int(input(f"Ingrésá el número: "))

#     # Par o impar
#     if num % 2 == 0:
#         pares += 1
#         print("Es par")
#     else:
#         impares += 1
#         print("Es impar")

#     # Positivo o negativo (el 0 no se cuenta como positivo ni negativo)
#     if num > 0:
#         positivos += 1
#     elif num < 0:
#         negativos += 1

# print("\n--- Resultados ---")
# print("Pares:", pares)
# print("Impares:", impares)
# print("Positivos:", positivos)
# print("Negativos:", negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# Codigo:

# totalNum = 0

# # Cambiá este número a 100 para cumplir 
# cantidad = 10  

# for i in range(cantidad):
#     num = int(input(f"Ingrésá el número para calcular media: "))
#     totalNum += num

# print("Total de la suma: ", totalNum);
# print("La media es: ", (totalNum/cantidad))


# 10) Escribe un programa que invierta el orden de los dígitos de un numero ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

# Codigo:

# numero = int(input("Ingresa un numero: "))

# invertido = 0

# while numero > 0:
#     # Tomamos el último digito
#     digito = numero % 10          
#     # Lo agregamos al numero invertido
#     invertido = invertido * 10 + digito  
#      # Quitamos el ultimo digito
#     numero = numero // 10        

# print("Numero invertido:", invertido)
