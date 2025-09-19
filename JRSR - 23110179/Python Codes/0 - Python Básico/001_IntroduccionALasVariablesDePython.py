# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Introducción a las Variables de Python
# Descripción: Ejemplos básicos de declaración, asignación y uso de variables en Python

# Ejemplo 1: Declaración y asignación básica de variables
# En Python no necesitamos declarar el tipo de variable explícitamente
edad = 28
print(f"Edad: {edad}")

# Ejemplo 2: Asignación de diferentes tipos de datos a la misma variable
numeroUno = 10
print(f"Número inicial: {numeroUno}")

# Python permite cambiar el tipo de dato de una variable
numeroUno = "Hola"
print(f"Ahora es texto: {numeroUno}")

# Ejemplo 3: Reasignación de valores
edad = 20
print(f"Nueva edad: {edad}")

edad = 32
print(f"Edad actualizada: {edad}")

edad = 26
print(f"Edad final: {edad}")

# Ejemplo 4: Inicialización con None
numeroUno = None
print(f"Variable inicializada con None: {numeroUno}")

# Ejemplo 5: Inicialización con constructor de tipo
numeroUno = int()  # Equivale a numeroUno = 0
print(f"Variable inicializada con int(): {numeroUno}")

# Ejemplo 6: Asignación múltiple
numeroUno, numeroDos, numeroTres = 10, 12, 17
print(f"Asignación múltiple - Número 1: {numeroUno}, Número 2: {numeroDos}, Número 3: {numeroTres}")

# Ejemplo 7: Demostración de variables en diferentes líneas
numeroUno = 10
print(f"Primera asignación: {numeroUno}")

numeroUno = 20
print(f"Segunda asignación: {numeroUno}")

# Ejemplo 8: Separación visual con línea en blanco
print()
print("Fin del script de introducción a variables")
