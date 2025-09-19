# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Guía del Módulo 'math' ---

import math

# --- Constantes ---
print(f"Valor de Pi (π): {math.pi}")
print(f"Valor de e (Número de Euler): {math.e}")

# --- Funciones comunes ---

# Raíz cuadrada
numero = 64
raiz = math.sqrt(numero)
print(f"\nLa raíz cuadrada de {numero} es {raiz}")

# Potencia (eleva el primer número a la potencia del segundo)
base = 2
exponente = 3
potencia = math.pow(base, exponente)
print(f"{base} elevado a la {exponente} es {potencia}")

# Redondeo
decimal = 10.6
# 'ceil' redondea hacia arriba al entero más cercano.
redondeoArriba = math.ceil(decimal)
# 'floor' redondea hacia abajo al entero más cercano.
redondeoAbajo = math.floor(decimal)
print(f"\nEl redondeo de {decimal} hacia arriba (ceil) es: {redondeoArriba}")
print(f"El redondeo de {decimal} hacia abajo (floor) es: {redondeoAbajo}")

# Factorial (5! = 5 * 4 * 3 * 2 * 1)
numFactorial = 5
factorial = math.factorial(numFactorial)
print(f"\nEl factorial de {numFactorial} es: {factorial}")