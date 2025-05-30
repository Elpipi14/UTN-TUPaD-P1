# 1) Factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

limite = int(input("1) Ingrese un número para calcular factoriales hasta ese valor: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

print("\n" + "-"*50)

# 2) Serie de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("2) Ingrese la cantidad de términos de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(pos):
    print(fibonacci(i), end=" ")

print("\n" + "-"*50)

# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("3) Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))
print(f"{base}^{exp} = {potencia(base, exp)}")

print("\n" + "-"*50)

# 4) Decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ''
    return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("4) Ingrese un número para convertir a binario: "))
binario = decimal_a_binario(numero)
print(f"Binario de {numero} es {binario if binario else '0'}")

print("\n" + "-"*50)

# 5) Palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("5) Ingrese una palabra para verificar si es palíndromo: ").lower()
print("¿Es palíndromo?", es_palindromo(texto))

print("\n" + "-"*50)

# 6) Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

numero = int(input("6) Ingrese un número para sumar sus dígitos: "))
print(f"Suma de los dígitos de {numero} es {suma_digitos(numero)}")

print("\n" + "-"*50)

# 7) Contar bloques de una pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

nivel = int(input("7) Ingrese el número de bloques en la base: "))
print(f"Total de bloques necesarios: {contar_bloques(nivel)}")

print("\n" + "-"*50)

# 8) Contar cuántas veces aparece un dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

numero = int(input("8) Ingrese un número: "))
digito = int(input("¿Qué dígito desea contar?: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")
