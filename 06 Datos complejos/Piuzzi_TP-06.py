# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
# Codigo:

lista = list(range(0,104,4))
print(lista)



# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

#  Codigo:

elementos = ["Nike", "Adidas", "Reebook", "UnderArmour", "Puma"]
print(elementos[3])
print(elementos[-2])



# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
# Codigo:

lista = []

lista.append('naranja')
lista.append('uva')
lista.append('pera')

print(f'Se agrega lista {lista}')


# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# Codigo:

animales = ["perro", "gato", "conejo", "pez"]

# Reemplaza 'gato' por 'loro'
pos1 = animales.index('gato')
animales[pos1] = 'loro'

# Reemplaza 'conejo' por 'oso'
pos2 = animales.index('conejo')
animales[pos2] = 'oso'

print(animales)



# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# explicación:
# En la lista de numeros aplicamos el metodo remove() junto con la funcion max().
# Esta funcion max busca el número más grande de la lista que es el 22 en este caso.
# una vez que encuetra el numero max, remove() elimina de la lista.



# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
# Codigo:

lista = list(range(10, 35, 5))

print(lista[0:2])



# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualquiera.
# Codigo:

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = 'up!'
autos[2] = 'vento'

print(autos)



# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.
# Codigo:

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)



# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# A:
compras[2].append("jugo")
# B:
pos_fideos = compras[1].index("fideos")
compras[1][pos_fideos] = "tallarines"
# C:
compras[0].remove("pan")
# D:
print(compras)



# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición # ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada = [15,True, [25.5, 57.9, 30.6], False]

print(lista_anidada)
