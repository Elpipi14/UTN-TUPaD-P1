# Este archivo contiene las funciones de la actividad  
# Se modularizó para mantener el código ordenado y reutilizable en otros programas.

import math

# # Funcion de la actividad Nº 1: 
def imprimir_hola_mundo ():
    return print("Hola Mundo!")


# # Funcion de la actividad Nº2:
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!!")


# # Funcion de la actividad Nº3
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# # Funcion de la actividad Nº4=
#  Calcula el area del círculo
def calcular_area_circulo(radio):
     return math.pi*radio**2

#  Calcula el perímetro (circunferencia) del círculo
def calcular_perimetro_circulo(radio):
     return math.pi*2*radio

# # Imprime el resultado del área y el perímetro usando las funciones anteriores
def resultado_area_perimetro(radio):
      return print(f"El area del circulo es: {calcular_area_circulo(radio)} y el perimetro es: {calcular_perimetro_circulo(radio)}")


# # Funcion de la actividad Nº5

def segundos_a_horas(seg):
     if seg > 0:
          hora = round(seg / 3600, 2)  # Redondea a 2 decimales
          return print(f"La conversion de segundo a hora equivale: {hora}hs")
     else:
          return print("Error: el valor debe ser mayor que cero")
     

# # Funcion de la activdad Nº6
def tabla_multiplicar(numero):
    if numero > 0:
        print(f"Tabla de multiplicar del {numero}:")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    else:
        print("Error: ingrese un número mayor a 0")


# # Funcion de la activdad Nº7
def operaciones_basicas(a, b):
     if a >= b:
        suma = a + b # suma
        resta = a - b # resta 
        multiplicacion = a * b # multiplicación
        if b != 0:
            division = a / b # division
        else:
            division = "No se puede dividir por cero"
        # tupla con los resultados
        return print(f"resultados de las opertaciones:\n suma: {a} + {b} = {suma},\n resta: {a} - {b} = {resta},\n division: {a} / {b} = {division}\n multiplicacion: {a} x {b} = {multiplicacion}")
     else:
          return print("1er numero  tiene que ser mayor o igual que 2do numero")


# # Funcion de la activdad Nº8   
def calcular_imc(peso, altura):
    if peso > 0 and altura > 0:
        imc = round(peso / (altura ** 2), 2)
        return print(f"su indece IMC es: {imc} y se clasifica: {clasificar_imc(imc)}")
    else:
        return print("Error: peso y altura deben ser mayores a 0")
    
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad grado I"
    elif imc < 40:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"
    

# # Funcion de la activdad Nº9
def celsius_a_fahrenheit(c):
    f = round(c * 9 / 5 + 32, 2)
    return print(f"{c}°C equivalen a {f}°F")


def calcular_promedio(a, b, c):
    if a > 0 and b > 0 and c > 0:
        promedio = round((a + b + c) / 3, 2)
        print(f"El promedio de las 3 notas es: {promedio}")
    else:
        print("Las notas tienen que ser mayores que 0")