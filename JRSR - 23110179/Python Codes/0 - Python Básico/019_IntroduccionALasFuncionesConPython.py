# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Introducción a las Funciones con Python
# Descripción: Ejemplos de definición y uso de funciones en Python

# Función básica sin parámetros
print("=== FUNCIONES BÁSICAS ===")

def saludar():
    """
    Función que imprime un saludo
    """
    print("Hola, bienvenido a Python!")

# Llamar a la función
saludar()

print()

# Función con parámetros
def saludarPersona(nombre):
    """
    Función que saluda a una persona específica
    """
    print(f"Hola, {nombre}!")

# Llamar función con parámetro
saludarPersona("Ana")
saludarPersona("Carlos")

print()

# Función que retorna un valor
def sumar(a, b):
    """
    Función que suma dos números y retorna el resultado
    """
    resultado = a + b
    return resultado

# Usar función que retorna valor
suma = sumar(5, 3)
print(f"La suma de 5 + 3 = {suma}")

print()

# Función con parámetros por defecto
def presentarse(nombre, edad=25):
    """
    Función con parámetro por defecto
    """
    print(f"Me llamo {nombre} y tengo {edad} años")

# Llamar con y sin parámetro opcional
presentarse("Juan")
presentarse("María", 30)

print("\nFin del script de funciones en Python")
