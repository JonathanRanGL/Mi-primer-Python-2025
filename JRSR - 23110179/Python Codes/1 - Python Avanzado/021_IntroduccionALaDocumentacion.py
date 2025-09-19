# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Guía de Documentación en Python ---

# --- 1. Comentarios Simples (#) ---
# Son para el programador. Explican el "porqué" de una línea de código.
# TODO: Implementar la función de 'calcular_impuestos()'.
# FIXME: Esta función es ineficiente, se debe optimizar.
def procesarValores(valores):
    pass


# --- 2. Docstrings (""") ---
# Son para el usuario del código. Explican QUÉ hace una función, clase o módulo.
# Son la forma oficial de documentar y se acceden con help() o __doc__.
def esPar(numero):
    """
    Comprueba si un número entero es par.

    Args:
        numero (int): El número entero a comprobar.

    Returns:
        bool: True si el número es par, False en caso contrario.
    """
    return numero % 2 == 0


# --- 3. Anotaciones de Tipo (Type Hinting) ---
# Indican el tipo de dato esperado para variables, parámetros y valores de retorno.
# Ayudan a la legibilidad y a herramientas de análisis estático, pero no son obligatorias en tiempo de ejecución.
def saludar(nombre: str, esFormal: bool) -> str:
    """
    Genera un saludo personalizado.

    Args:
        nombre (str): El nombre de la persona a saludar.
        esFormal (bool): Determina si el saludo es formal o informal.

    Returns:
        str: El saludo generado.
    """
    if esFormal:
        return f"Estimado/a {nombre}, reciba un cordial saludo."
    else:
        return f"¡Hola, {nombre}!"


# --- Accediendo a la documentación ---
print("--- Accediendo a Docstrings ---")
print("Usando __doc__:")
print(esPar.__doc__)

# Para ver la ayuda completa, descomenta la siguiente línea y ejecútala en una consola de Python.
# help(saludar)

# --- Usando las funciones documentadas ---
print("\n--- Probando las funciones ---")
print(f"El número 4 es par: {esPar(4)}")
print(saludar("Ana", esFormal=True))
print(saludar("Juan", esFormal=False))