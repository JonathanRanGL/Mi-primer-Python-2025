# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Introducción a los Sets (Conjuntos)
# Descripción: Ejemplos completos de sets y sus operaciones en Python

# Creación de sets básicos
print("=== CREACIÓN DE SETS ===")

# Sintaxis general: {elemento1, elemento2, elemento3, ...}
setColores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}
print(f"Set de colores: {setColores}")

# Los sets eliminan duplicados automáticamente
setConDuplicados = {"rojo", "verde", "azul", "rojo", "blanco", "rojo", "rojo"}
print(f"Set con duplicados eliminados: {setConDuplicados}")

print()

# Operaciones básicas con sets
print("=== OPERACIONES BÁSICAS ===")
setColores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}
print(f"Set original: {setColores}")

# Añadir un elemento al set
setColores.add("marrón")
print(f"Después de add('marrón'): {setColores}")

# Eliminar un valor del set
setColores.remove("azul")
print(f"Después de remove('azul'): {setColores}")

# Intentar eliminar un elemento que no existe con remove() causaría KeyError
# setColores.remove("cian")  # KeyError: 'cian'

# Usar discard() no causa error si el elemento no existe
setColores.discard("cian")
print(f"Después de discard('cian') (elemento inexistente): {setColores}")

print()

# Hashabilidad en sets
print("=== HASHABILIDAD EN SETS ===")
print("Los sets solo pueden contener elementos hashables")

# Intentar agregar una lista (no hashable) causaría error
listaNumeros = [10, 20, 30, 40]
try:
    setNumeros = {76, 47, listaNumeros}
    print(f"Set con lista: {setNumeros}")
except TypeError as e:
    print(f"Error al incluir lista: {e}")

# Las tuplas sí son hashables
tuplaNumeros = (10, 20, 30, 40)
setNumeros = {76, 47, tuplaNumeros}
print(f"Set con tupla (válido): {setNumeros}")

print()

# Funciones útiles con sets
print("=== FUNCIONES ÚTILES ===")
setColores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}

# Contar elementos
cantidadElementos = len(setColores)
print(f"El set tiene {cantidadElementos} elementos")

# Ejemplo con string
saludo = "Hola"
cantidadCaracteres = len(saludo)
print(f"El texto '{saludo}' tiene {cantidadCaracteres} caracteres")

# Funciones min y max con números
setNumeros = {100, 6578, 54, 4, 56, 2}
print(f"Set de números: {setNumeros}")

valorMinimo = min(setNumeros)
print(f"El valor mínimo del conjunto es: {valorMinimo}")

valorMaximo = max(setNumeros)
print(f"El valor máximo del conjunto es: {valorMaximo}")

# Funciones min y max con strings (orden alfabético)
setColores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}
colorMinimo = min(setColores)  # Orden alfabético
colorMaximo = max(setColores)
print(f"Color mínimo alfabéticamente: {colorMinimo}")
print(f"Color máximo alfabéticamente: {colorMaximo}")

print()

# Frozenset (set inmutable)
print("=== FROZENSET ===")
print("Frozenset: versión inmutable de set")

# Sintaxis: frozenset([elemento1, elemento2, elemento3, ...])
numeros = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {numeros}")

# Los frozensets no se pueden modificar
try:
    numeros.add(300)
    print(f"Frozenset modificado: {numeros}")
except AttributeError as e:
    print(f"Error: {e}")

print()

# Operaciones de conjuntos matemáticos
print("=== OPERACIONES DE CONJUNTOS ===")
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

print(f"Set A: {setA}")
print(f"Set B: {setB}")

# Unión
union = setA | setB
print(f"Unión (A | B): {union}")

# Intersección
interseccion = setA & setB
print(f"Intersección (A & B): {interseccion}")

# Diferencia
diferencia = setA - setB
print(f"Diferencia (A - B): {diferencia}")

# Diferencia simétrica
diferenciaSimetrica = setA ^ setB
print(f"Diferencia simétrica (A ^ B): {diferenciaSimetrica}")

print()

# Verificación de pertenencia
print("=== VERIFICACIÓN DE PERTENENCIA ===")
frutas = {"manzana", "pera", "uva", "naranja"}
print(f"Frutas disponibles: {frutas}")

# Verificar si un elemento está en el set
tieneManzana = "manzana" in frutas
tieneKiwi = "kiwi" in frutas

print(f"¿Tiene manzana?: {tieneManzana}")
print(f"¿Tiene kiwi?: {tieneKiwi}")

print()

# Ejemplo práctico: Eliminar duplicados de una lista
print("=== EJEMPLO PRÁCTICO: ELIMINAR DUPLICADOS ===")
listaConDuplicados = [1, 2, 2, 3, 3, 4, 4, 5, 1, 2]
print(f"Lista original: {listaConDuplicados}")

# Convertir a set para eliminar duplicados, luego de vuelta a lista
listaSinDuplicados = list(set(listaConDuplicados))
print(f"Lista sin duplicados: {listaSinDuplicados}")

# Mantener el orden original usando dict.fromkeys()
listaSinDuplicadosOrdenada = list(dict.fromkeys(listaConDuplicados))
print(f"Lista sin duplicados (orden preservado): {listaSinDuplicadosOrdenada}")

print("\nFin del script de sets (conjuntos) en Python")