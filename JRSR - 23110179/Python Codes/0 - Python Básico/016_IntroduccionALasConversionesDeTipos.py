# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Introducción a las Conversiones de Tipos
# Descripción: Ejemplos de conversiones entre diferentes tipos de datos en Python

# Conversiones básicas
print("=== CONVERSIONES BÁSICAS ===")

# String a número
textoNumero = "123"
numeroEntero = int(textoNumero)
numeroDecimal = float(textoNumero)

print(f"Texto original: {textoNumero} (tipo: {type(textoNumero)})")
print(f"Convertido a int: {numeroEntero} (tipo: {type(numeroEntero)})")
print(f"Convertido a float: {numeroDecimal} (tipo: {type(numeroDecimal)})")

print()

# Número a string
numero = 456
textoDesdeNumero = str(numero)
print(f"Número original: {numero} (tipo: {type(numero)})")
print(f"Convertido a string: {textoDesdeNumero} (tipo: {type(textoDesdeNumero)})")

print()

# Conversiones con listas y tuplas
print("=== CONVERSIONES LISTAS Y TUPLAS ===")
listaOriginal = [1, 2, 3, 4, 5]
tuplaDesdeList = tuple(listaOriginal)
print(f"Lista original: {listaOriginal}")
print(f"Convertida a tupla: {tuplaDesdeList}")

tuplaOriginal = (6, 7, 8, 9, 10)
listaDesdeeTupla = list(tuplaOriginal)
print(f"Tupla original: {tuplaOriginal}")
print(f"Convertida a lista: {listaDesdeeTupla}")

print("\nFin del script de conversiones de tipos")
