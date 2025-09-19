# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Introducción a los Condicionales y Bucles
# Descripción: Ejemplos de estructuras de control en Python

# Condicionales básicos
print("=== CONDICIONALES BÁSICOS ===")

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Condicionales múltiples
calificacion = 85
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 80:
    print("Muy bueno")
elif calificacion >= 70:
    print("Bueno")
else:
    print("Necesitas mejorar")

print()

# Bucle for
print("=== BUCLE FOR ===")
print("Números del 1 al 5:")
for i in range(1, 6):
    print(f"Número: {i}")

# Bucle for con lista
frutas = ["manzana", "pera", "uva"]
print("\nFrutas:")
for fruta in frutas:
    print(f"- {fruta}")

print()

# Bucle while
print("=== BUCLE WHILE ===")
contador = 1
print("Contando hasta 3:")
while contador <= 3:
    print(f"Contador: {contador}")
    contador += 1

print("\nFin del script de condicionales y bucles")
