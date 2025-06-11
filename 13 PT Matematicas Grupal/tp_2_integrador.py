from itertools import product, combinations
from datetime import datetime

# ======= INGRESO DE DATOS ========
dnis = ["31568054", "36054031"]
años_nacimientos = [2003, 1999, 2000]

# ======= 1. CREACIÓN DE CONJUNTOS ========
conjuntos_dni = []
for dni in dnis:
    digitos = set(int(d) for d in dni)
    conjuntos_dni.append(digitos)

print("Conjuntos de dígitos únicos por DNI:")
for i, c in enumerate(conjuntos_dni):
    print(f"Conjunto {i + 1}: {c}")

# ======= 2. OPERACIONES ENTRE CONJUNTOS ========
print("\n--- OPERACIONES ENTRE CONJUNTOS ---")
print("UNIÓN:", set.union(*conjuntos_dni))
print("INTERSECCIÓN:", set.intersection(*conjuntos_dni))

for i, j in combinations(range(len(conjuntos_dni)), 2):
    a, b = conjuntos_dni[i], conjuntos_dni[j]
    
    dif_ab = a - b
    dif_ba = b - a
    sim = a.symmetric_difference(b)
    
    print(f"\nDIFERENCIA {i+1} - {j+1}:",
          dif_ab if dif_ab else "{}")
    
    print(f"DIFERENCIA {j+1} - {i+1}:",
          dif_ba if dif_ba else "{}")
    
    print(f"DIFERENCIA SIMÉTRICA ({i+1} Δ {j+1}):",
          sim if sim else "{}  ← No hay diferencia simétrica: los conjuntos son idénticos.")

# ======= 3. SUMA Y FRECUENCIA DE DÍGITOS ========
print("\n--- Frecuencia de dígitos y suma por DNI ---")
for dni in dnis:
    suma = sum(int(d) for d in dni)
    print(f"DNI {dni} → Suma: {suma}")
    for digito in sorted(set(dni)):
        print(f" - Dígito {digito} aparece {dni.count(digito)} veces")

# ======= 4. CONDICIONES LÓGICAS ========
print("\n--- Evaluación de condiciones lógicas ---")
# diversidad numérica
for i, c in enumerate(conjuntos_dni):
    if len(c) > 6:
        print(f"Conjunto {i+1} tiene alta diversidad numérica.")

# dígito común
digito_comun = set.intersection(*conjuntos_dni)
if digito_comun:
    print(f"Dígito(s) compartido(s): {digito_comun}")

# Grupo sin ceros
if all(0 not in c for c in conjuntos_dni):
    print("✅ Ningún conjunto contiene el dígito 0 (grupo sin ceros).")
else:
    print("⚠️ Al menos un conjunto contiene el dígito 0.")

# Paridad de conjuntos
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

# ======= 5. OPERACIONES CON AÑOS DE NACIMIENTO ========
print("\n--- Análisis de años de nacimiento ---")
pares_ = sum(1 for a in años_nacimientos if a % 2 == 0)
impares_ = len(años_nacimientos) - pares_
print(f"Años pares: {pares_} | Años impares: {impares_}")

# Grupo Z
if all(a > 2000 for a in años_nacimientos):
    print("✅ Todos nacieron después del año 2000 → Grupo Z")
else:
    print("Grupo no Z (hay nacimientos en o antes del 2000).")

# Año bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

if any(es_bisiesto(a) for a in años_nacimientos):
    print("✅ Tenemos al menos un año bisiesto en el grupo.")
else:
    print("ℹ️ Ninguno de los años es bisiesto.")

# ======= 5.1 PRODUCTO CARTESIANO (AÑOS X EDADES ACTUALES) ========
anio_actual = datetime.now().year
edades = [anio_actual - a for a in años_nacimientos]

print("\nAÑO ACTUAL:", anio_actual)
print("EDADES CALCULADAS POR AÑO DE NACIMIENTO:")
for a, e in zip(años_nacimientos, edades):
    print(f" - AÑO {a} → EDAD {e} AÑOS")

pc = list(product(años_nacimientos, edades))
print("\nPRODUCTO CARTESIANO (AÑOS X EDADES):")
for anio, edad in pc:
    print(f"AÑO: {anio} - EDAD: {edad}")

