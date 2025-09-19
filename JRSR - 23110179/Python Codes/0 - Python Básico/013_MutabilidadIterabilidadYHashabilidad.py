# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Mutabilidad, Iterabilidad y Hashabilidad
# Descripción: Conceptos fundamentales de mutabilidad, iterabilidad y hashabilidad en Python

# Concepto de Mutabilidad
print("=== MUTABILIDAD ===")
print("Mutabilidad: capacidad de un objeto de cambiar después de ser creado")

# Ejemplo 1: Lista (mutable)
print("\nEjemplo con lista (MUTABLE):")
lista = [10, 10, 30, 40]
print(f"Lista original: {lista}")

# Reasignar el valor 20 a la posición 1 de la lista
lista[1] = 20
print(f"Lista modificada: {lista}")

# Ejemplo 2: Tupla (inmutable)
print("\nEjemplo con tupla (INMUTABLE):")
tupla = (10, 10, 30, 40)
print(f"Tupla original: {tupla}")

# Intentar reasignar causaría error
# tupla[1] = 20  # TypeError: 'tuple' object does not support item assignment
print("Las tuplas no se pueden modificar después de crear")

print()

# Concepto de Iterabilidad
print("=== ITERABILIDAD ===")
print("Iterabilidad: capacidad de recorrer elementos uno por uno")

# Ejemplo con string (iterable)
print("\nEjemplo con string (ITERABLE):")
saludo = "Hola"
print(f"String: {saludo}")
print("Caracteres individuales:")
for i, caracter in enumerate(saludo):
    print(f"  Posición {i}: {caracter}")

# Los strings son inmutables
print("\nLos strings son INMUTABLES:")
print(f"String original: {saludo}")
# saludo[0] = "h"  # TypeError: 'str' object does not support item assignment

# Para "cambiar" un string, creamos uno nuevo
saludoNuevo = "Adiós"
print(f"Nuevo string: {saludoNuevo}")

print()

# Concepto de Hashabilidad
print("=== HASHABILIDAD ===")
print("Hashabilidad: capacidad de generar un valor hash único")

# Ejemplo con string (hashable)
print("\nEjemplo con string (HASHABLE):")
saludo = "Hola"
valorHash = hash(saludo)
print(f"String: {saludo}")
print(f"Hash del string: {valorHash}")

# Ejemplo con lista (no hashable)
print("\nEjemplo con lista (NO HASHABLE):")
numeros = [10, 20, 30]
print(f"Lista: {numeros}")
try:
    valorHashLista = hash(numeros)
    print(f"Hash de la lista: {valorHashLista}")
except TypeError as e:
    print(f"Error: {e}")

# Las listas son iterables
print("\nLas listas son ITERABLES:")
print(f"Lista: {numeros}")
print("Elementos individuales:")
for i, numero in enumerate(numeros):
    print(f"  Posición {i}: {numero}")

# Los enteros no son iterables
print("\nLos enteros NO son iterables:")
numero = 10
print(f"Entero: {numero}")
try:
    print(f"Primer elemento: {numero[0]}")
except TypeError as e:
    print(f"Error: {e}")

print()

# Resumen de propiedades
print("=== RESUMEN DE PROPIEDADES ===")

tiposDatos = [
    ("Lista", [1, 2, 3]),
    ("Tupla", (1, 2, 3)),
    ("String", "abc"),
    ("Set", {1, 2, 3}),
    ("Diccionario", {"a": 1}),
    ("Entero", 42)
]

for nombre, objeto in tiposDatos:
    print(f"\n{nombre}: {objeto}")
    
    # Verificar mutabilidad
    esMutable = hasattr(objeto, '__setitem__') or hasattr(objeto, 'append')
    print(f"  Mutable: {esMutable}")
    
    # Verificar iterabilidad
    try:
        iter(objeto)
        esIterable = True
    except TypeError:
        esIterable = False
    print(f"  Iterable: {esIterable}")
    
    # Verificar hashabilidad
    try:
        hash(objeto)
        esHashable = True
    except TypeError:
        esHashable = False
    print(f"  Hashable: {esHashable}")

print("\nFin del script de mutabilidad, iterabilidad y hashabilidad")