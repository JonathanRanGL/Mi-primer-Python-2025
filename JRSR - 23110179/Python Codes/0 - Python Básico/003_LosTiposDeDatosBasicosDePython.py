# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Los Tipos de Datos Básicos de Python
# Descripción: Ejemplos de los tipos de datos fundamentales en Python

# Tipo de dato: String (cadena de caracteres)
# Las cadenas pueden usar comillas dobles o simples
saludo = "Hola alumnos"
print(f"Cadena con comillas dobles: {saludo}")

saludoAlterno = 'Hola alumnos'
print(f"Cadena con comillas simples: {saludoAlterno}")

# Importante: Las comillas de apertura y cierre deben coincidir
# saludo = 'Hola alumnos"  # Esto causaría un SyntaxError

# Tipo de dato: Integer (número entero)
# Los enteros pueden ser positivos, negativos o cero
edad = 32
print(f"Entero positivo: {edad}")

temperatura = -10
print(f"Entero negativo: {temperatura}")

# Tipo de dato: Float (número decimal)
# Los números decimales usan punto como separador decimal
pi = 3.14159
print(f"Número decimal positivo: {pi}")

valorNegativo = -17.6743
print(f"Número decimal negativo: {valorNegativo}")

# Tipo de dato: Boolean (booleano)
# Solo puede tener dos valores: True o False
valorVerdadero = True
valorFalso = False

print(f"Valor booleano verdadero: {valorVerdadero}")
print(f"Valor booleano falso: {valorFalso}")

# Verificación de tipos usando type()
print(f"\nTipo de '{saludo}': {type(saludo)}")
print(f"Tipo de {edad}: {type(edad)}")
print(f"Tipo de {pi}: {type(pi)}")
print(f"Tipo de {valorVerdadero}: {type(valorVerdadero)}")

print("\nFin del script de tipos de datos básicos")
