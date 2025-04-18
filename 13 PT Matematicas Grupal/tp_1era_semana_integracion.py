import random  # Importamos el módulo random para generar números aleatorios

# Diccionario que define las operaciones posibles en cada nivel
OPERACIONES_NIVEL = {
    1: ['AND', 'OR', 'XOR'],
    2: ['AND', 'OR', 'XOR', 'AND OR'],
    3: ['AND', 'OR', 'XOR', 'AND OR XOR']
}

# Diccionario que traduce los nombres de las operaciones a operadores de Python
OPERADORES = {
    'AND': '&',   # AND lógico
    'OR': '|',    # OR lógico
    'XOR': '^'    # XOR lógico (exclusiva)
}

# Función para generar una lista de valores binarios aleatorios (0 o 1)
def generar_variables(cantidad):
    return [random.randint(0, 1) for _ in range(cantidad)]

# Función que crea una expresión lógica a partir de las variables y el nivel
def generar_operacion(variables, nivel):
    operadores_raw = random.choice(OPERACIONES_NIVEL[nivel]).split()  # Elige combinación de operadores
    expr = str(variables[0])

    for i in range(1, len(variables)):
        operador = random.choice(operadores_raw)  # Selecciona un operador aleatorio permitido
        expr += f" {OPERADORES[operador]} {variables[i]}"  # Construye la expresión lógica

    return expr

# Función para evaluar la expresión lógica generada
def evaluar_expresion(expr):
    try:
        return int(eval(expr))  # Evalúa la expresión lógica
    except Exception as e:
        print(f"Error evaluando expresión: {e}")
        return None

# Función que ejecuta una ronda del juego para el nivel actual
def jugar_ronda(nivel):
    cantidad_variables = nivel + 1  # Nivel 1: 2 variables, Nivel 2: 3, etc.
    variables = generar_variables(cantidad_variables)
    expresion = generar_operacion(variables, nivel)
    resultado_real = evaluar_expresion(expresion)

    print(f"\nAdivina el resultado de la operación lógica:\n")
    print(f"  {expresion}")
    respuesta_usuario = input("¿Cuál es el resultado? (0 o 1): ")

    # Validación de entrada del usuario
    if respuesta_usuario not in ['0', '1']:
        print("Entrada no válida. Solo se permite 0 o 1.")
        return False

    # Comparación del resultado ingresado por el usuario con el correcto
    if int(respuesta_usuario) == resultado_real:
        print("✅ ¡Correcto!")
        return True
    else:
        print(f"❌ Incorrecto. El resultado correcto era {resultado_real}")
        return False

# Función principal del juego
def main():
    print("🎮 Juego de Adivinanza de Operaciones Lógicas")
    nivel = 1
    aciertos = 0
    rondas_por_nivel = 3  # Cantidad de rondas que se juegan por nivel

    while nivel <= 3:
        print(f"\n=== Nivel {nivel} ===")
        for _ in range(rondas_por_nivel):
            if jugar_ronda(nivel):
                aciertos += 1
        # Si se alcanza el mínimo de aciertos, se avanza de nivel
        if aciertos >= rondas_por_nivel:
            print(f"\n✨ ¡Avanzás al nivel {nivel + 1}!")
            nivel += 1
            aciertos = 0
        else:
            print(f"\n🔁 Reintentá el nivel {nivel}. Necesitás más aciertos.")
            aciertos = 0

    print("\n🏁 ¡Juego finalizado! Gracias por jugar.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
