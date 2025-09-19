# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Matemáticas Básicas con Python
# Descripción: Ejemplos de operaciones matemáticas básicas en Python

# Operaciones aritméticas básicas
print("=== OPERACIONES ARITMÉTICAS BÁSICAS ===")

# Suma
resultadoSuma = 10 + 46
print(f"10 + 46 = {resultadoSuma}")

resultadoSuma2 = 56 + 58
print(f"56 + 58 = {resultadoSuma2}")

# Resta
resultadoResta = 20 - 5
print(f"20 - 5 = {resultadoResta}")

# Multiplicación
resultadoMultiplicacion = 8 * 7
print(f"8 * 7 = {resultadoMultiplicacion}")

# División
resultadoDivision = 100 / 4
print(f"100 / 4 = {resultadoDivision}")

# División entera
resultadoDivisionEntera = 100 // 3
print(f"100 // 3 = {resultadoDivisionEntera}")

# Módulo (resto de división)
resultadoModulo = 100 % 3
print(f"100 % 3 = {resultadoModulo}")

# Potenciación
resultadoPotencia = 2 ** 8
print(f"2 ** 8 = {resultadoPotencia}")

print()

# Operaciones con variables
print("=== OPERACIONES CON VARIABLES ===")
numeroA = 15
numeroB = 25

sumaVariables = numeroA + numeroB
print(f"{numeroA} + {numeroB} = {sumaVariables}")

restaVariables = numeroB - numeroA
print(f"{numeroB} - {numeroA} = {restaVariables}")

multiplicacionVariables = numeroA * numeroB
print(f"{numeroA} * {numeroB} = {multiplicacionVariables}")

divisionVariables = numeroB / numeroA
print(f"{numeroB} / {numeroA} = {divisionVariables}")

print()

# Operaciones con números decimales
print("=== OPERACIONES CON DECIMALES ===")
numeroDecimalA = 10.5
numeroDecimalB = 3.2

sumaDecimales = numeroDecimalA + numeroDecimalB
print(f"{numeroDecimalA} + {numeroDecimalB} = {sumaDecimales}")

multiplicacionDecimales = numeroDecimalA * numeroDecimalB
print(f"{numeroDecimalA} * {numeroDecimalB} = {multiplicacionDecimales}")

print()

# Orden de operaciones (precedencia)
print("=== ORDEN DE OPERACIONES ===")
resultadoComplejo = 2 + 3 * 4
print(f"2 + 3 * 4 = {resultadoComplejo}")  # Multiplicación primero

resultadoConParentesis = (2 + 3) * 4
print(f"(2 + 3) * 4 = {resultadoConParentesis}")  # Paréntesis primero

print()

# Funciones matemáticas básicas
print("=== FUNCIONES MATEMÁTICAS ===")
import math

numeroParaRaiz = 16
raizCuadrada = math.sqrt(numeroParaRaiz)
print(f"Raíz cuadrada de {numeroParaRaiz} = {raizCuadrada}")

numeroParaPotencia = 2
exponente = 10
potenciaConMath = math.pow(numeroParaPotencia, exponente)
print(f"{numeroParaPotencia} elevado a {exponente} = {potenciaConMath}")

# Valor absoluto
numeroNegativo = -15
valorAbsoluto = abs(numeroNegativo)
print(f"Valor absoluto de {numeroNegativo} = {valorAbsoluto}")

# Redondeo
numeroDecimal = 3.7
numeroRedondeado = round(numeroDecimal)
print(f"Redondeo de {numeroDecimal} = {numeroRedondeado}")

print()

# Operadores de asignación compuesta
print("=== OPERADORES DE ASIGNACIÓN COMPUESTA ===")
contador = 10
print(f"Valor inicial: {contador}")

contador += 5  # Equivale a: contador = contador + 5
print(f"Después de += 5: {contador}")

contador -= 3  # Equivale a: contador = contador - 3
print(f"Después de -= 3: {contador}")

contador *= 2  # Equivale a: contador = contador * 2
print(f"Después de *= 2: {contador}")

contador //= 4  # Equivale a: contador = contador // 4
print(f"Después de //= 4: {contador}")

print("\nFin del script de matemáticas básicas")
