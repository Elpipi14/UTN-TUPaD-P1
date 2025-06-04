from itertools import product

# ======= INGRESO DE DATOS ========
dnis = ["31568054", "36054031", "28658781"]
años_nacimientos = [2003, 1999, 2000]

#1 ======= CREACIÓN DE CONJUNTOS ========
conjuntos_dni = []
for dni in dnis:
    digitos = set(int(d) for d in dni)
    conjuntos_dni.append(digitos)

print("Conjuntos de dígitos únicos por DNI:")
for i, c in enumerate(conjuntos_dni):
    print(f"Conjunto {i + 1}: {c}")

#2 ======= OPERACIONES ENTRE CONJUNTOS ========
print("\n--- Operaciones entre conjuntos ---")
union = set.union(*conjuntos_dni)
interseccion = set.intersection(*conjuntos_dni)
print(f"Unión: {union}")
print(f"Intersección: {interseccion}")

# Diferencias y diferencia simétrica entre pares
for i in range(len(conjuntos_dni)):
    for j in range(i + 1, len(conjuntos_dni)):
        a, b = conjuntos_dni[i], conjuntos_dni[j]
        print(f"\nConjunto {i+1} - Conjunto {j+1}: {a - b}")
        print(f"Conjunto {j+1} - Conjunto {i+1}: {b - a}")
        print(f"Diferencia simétrica ({i+1} Δ {j+1}): {a.symmetric_difference(b)}")

#3 ======= SUMA Y FRECUENCIA DE DÍGITOS ========
print("\n--- Frecuencia de dígitos y suma por DNI ---")
for dni in dnis:
    suma = sum(int(d) for d in dni)
    print(f"DNI {dni} → Suma: {suma}")
    for digito in sorted(set(dni)):
        print(f" - Dígito {digito} aparece {dni.count(digito)} veces")

#4 ======= CONDICIONES LÓGICAS ========
print("\n--- Evaluación de condiciones lógicas ---")
# diversidad numérica
for i, c in enumerate(conjuntos_dni):
    if len(c) > 6:
        print(f"Conjunto {i+1} tiene alta diversidad numérica.")

#dígito común
digito_comun = set.intersection(*conjuntos_dni)
if digito_comun:
    print(f"Dígito(s) compartido(s): {digito_comun}")

# Grupo sin ceros
if all(0 not in c for c in conjuntos_dni):
    print("Grupo sin ceros.")

# Cantidad de conjuntos pares e impares
pares = 0
print("\n--- Paridad de conjuntos por DNI ---")
for dni, conjunto in zip(dnis, conjuntos_dni):
    cantidad = len(conjunto)
    tipo = "PAR" if cantidad % 2 == 0 else "IMPAR"
    print(f"DNI {dni} → Conjunto de {cantidad} dígitos únicos → {tipo}")
    if tipo == "PAR":
        pares += 1

impares = len(conjuntos_dni) - pares

if pares > impares:
    print("\n✅ Grupo par.")
    

#5 ======= OPERACIONES CON AÑOS DE NACIMIENTO ========
print("\n--- Análisis de años de nacimiento ---")
pares_ = sum(1 for a in años_nacimientos if a % 2 == 0)
impares_ = len(años_nacimientos) - pares_
print(f"Años pares: {pares_} | Años impares: {impares_}")

# Grupo Z
if all(a > 2000 for a in años_nacimientos):
    print("Grupo Z")

# Año bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

if any(es_bisiesto(a) for a in años_nacimientos):
    print("Tenemos un año especial (bisiesto) en el grupo.")

# Producto cartesiano (años x edades actuales)
from datetime import datetime
anio_actual = datetime.now().year
edades = [anio_actual - a for a in años_nacimientos]
pc = list(product(años_nacimientos, edades))
print("\nProducto cartesiano (Años x Edades):")
for par in pc:
    print(par)
