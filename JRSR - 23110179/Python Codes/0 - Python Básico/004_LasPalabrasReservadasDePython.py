# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Las Palabras Reservadas de Python
# Descripción: Demostración de palabras reservadas y cómo evitar conflictos

# Ejemplo 1: Intento de usar una palabra reservada como nombre de variable
# global = 10  # Esto causaría un SyntaxError
# Las palabras reservadas no pueden usarse como nombres de variables

# Solución: Usar nombres alternativos descriptivos
variableGlobal = 10
print(f"Variable con nombre válido: {variableGlobal}")

# Ejemplo 2: Obtener la lista completa de palabras reservadas
import keyword

print("Lista de palabras reservadas en Python:")
palabrasReservadas = keyword.kwlist
for i, palabra in enumerate(palabrasReservadas, 1):
    print(f"{i:2d}. {palabra}")

print(f"\nTotal de palabras reservadas: {len(palabrasReservadas)}")

# Ejemplo 3: Verificar si una palabra es reservada
def esPalabraReservada(palabra):
    """
    Función que verifica si una palabra es reservada en Python
    """
    return keyword.iskeyword(palabra)

# Pruebas con diferentes palabras
palabrasPrueba = ["global", "variable", "if", "miVariable", "class", "def"]

print("\nVerificación de palabras:")
for palabra in palabrasPrueba:
    esReservada = esPalabraReservada(palabra)
    estado = "RESERVADA" if esReservada else "DISPONIBLE"
    print(f"'{palabra}' -> {estado}")

# Ejemplo 4: Buenas prácticas para nombres de variables
# Usar nombres descriptivos que no conflicten con palabras reservadas
valorMatch = 10  # En lugar de 'match' (palabra reservada en Python 3.10+)
contadorFor = 0  # En lugar de 'for'
resultadoIf = True  # En lugar de 'if'

print(f"\nEjemplos de nombres válidos:")
print(f"valorMatch: {valorMatch}")
print(f"contadorFor: {contadorFor}")
print(f"resultadoIf: {resultadoIf}")

print("\nFin del script de palabras reservadas")
