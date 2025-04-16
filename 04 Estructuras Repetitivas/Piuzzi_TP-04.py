# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# codigo:
# for i in range(0,102):
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

secuencia = 0
cantidad= 0
i=1
while i != 0:
   num = int(input("Ingresar números enteros  "))
   if(num == 0):
    print("Ingresaste un 0, se detiene el programa")
    break;
   else: 
    secuencia += num
    cantidad += 1

print("cantidad de numero ingresado: ", cantidad)
print("total sumado: ", secuencia)