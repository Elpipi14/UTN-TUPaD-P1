import random

# Operaciones posibles por nivel
OPERACIONES_NIVEL = {
    1: ['AND', 'OR', 'XOR'],
    2: ['AND', 'OR', 'XOR', 'AND OR'],
    3: ['AND', 'OR', 'XOR', 'AND OR XOR']
}

# Traducción a operadores Python
OPERADORES = {
    'AND': '&',
    'OR': '|',
    'XOR': '^'
}

def generar_variables(cantidad):
    return [random.randint(0, 1) for _ in range(cantidad)]


def generar_operacion(variables, nivel):
    operadores_raw = random.choice(OPERACIONES_NIVEL[nivel]).split()
    expr = str(variables[0])

    for i in range(1, len(variables)):
        operador = random.choice(operadores_raw)
        expr += f" {OPERADORES[operador]} {variables[i]}"

    return expr

def evaluar_expresion(expr):
    try:
        return int(eval(expr))
    except Exception as e:
        print(f"Error evaluando expresión: {e}")
        return None

def jugar_ronda(nivel):
    cantidad_variables = nivel + 1  # Nivel 1: 2 vars, Nivel 2: 3, etc.
    variables = generar_variables(cantidad_variables)
    expresion = generar_operacion(variables, nivel)
    resultado_real = evaluar_expresion(expresion)

    print(f"\nAdivina el resultado de la operación lógica:\n")
    print(f"  {expresion}")
    respuesta_usuario = input("¿Cuál es el resultado? (0 o 1): ")

    if respuesta_usuario not in ['0', '1']:
        print("Entrada no válida. Solo se permite 0 o 1.")
        return False

    if int(respuesta_usuario) == resultado_real:
        print("✅ ¡Correcto!")
        return True
    else:
        print(f"❌ Incorrecto. El resultado correcto era {resultado_real}")
        return False

def main():
    print("🎮 Juego de Adivinanza de Operaciones Lógicas")
    nivel = 1
    aciertos = 0
    rondas_por_nivel = 3

    while nivel <= 3:
        print(f"\n=== Nivel {nivel} ===")
        for _ in range(rondas_por_nivel):
            if jugar_ronda(nivel):
                aciertos += 1
        if aciertos >= rondas_por_nivel:
            print(f"\n✨ ¡Avanzás al nivel {nivel + 1}!")
            nivel += 1
            aciertos = 0
        else:
            print(f"\n🔁 Reintentá el nivel {nivel}. Necesitás más aciertos.")
            aciertos = 0

    print("\n🏁 ¡Juego finalizado! Gracias por jugar.")

if __name__ == "__main__":
    main()
