# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Listas de Python para Principiantes
# Descripción: Introducción completa a las listas en Python y sus operaciones

# Creación de listas básicas
print("=== CREACIÓN DE LISTAS ===")

# Lista que representa una camiseta con diferentes tipos de datos
camiseta = ["rojo", "L", 100, 10]  # [color, talla, precio, cantidad]
print(f"Lista camiseta: {camiseta}")

# Comparación con variables individuales
print("\nComparación con variables individuales:")
color = "rojo"
talla = "L"
precio = 100
cantidad = 10
print(f"Color: {color}, Talla: {talla}, Precio: {precio}, Cantidad: {cantidad}")

# Sintaxis general de listas: [elemento1, elemento2, elemento3, ...]
listaNumeros = [1, 2, 3, 4, 5]
listaTextos = ["Python", "Java", "JavaScript", "C++"]
listaMixta = ["Ana", 25, True, 3.14]

print(f"\nLista de números: {listaNumeros}")
print(f"Lista de textos: {listaTextos}")
print(f"Lista mixta: {listaMixta}")

print()

# Acceso a elementos por índice
print("=== ACCESO A ELEMENTOS ===")
frutas = ["manzana", "pera", "uva", "naranja", "kiwi"]
print(f"Lista de frutas: {frutas}")

print(f"Primera fruta (índice 0): {frutas[0]}")
print(f"Segunda fruta (índice 1): {frutas[1]}")
print(f"Última fruta (índice -1): {frutas[-1]}")
print(f"Penúltima fruta (índice -2): {frutas[-2]}")

print()

# Slicing de listas
print("=== SLICING DE LISTAS ===")
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista original: {numeros}")

print(f"Primeros 3 elementos: {numeros[:3]}")
print(f"Últimos 3 elementos: {numeros[-3:]}")
print(f"Elementos del índice 2 al 6: {numeros[2:7]}")
print(f"Elementos pares (cada 2): {numeros[::2]}")
print(f"Lista invertida: {numeros[::-1]}")

print()

# Modificación de listas
print("=== MODIFICACIÓN DE LISTAS ===")
colores = ["rojo", "verde", "azul"]
print(f"Lista original: {colores}")

# Cambiar un elemento
colores[1] = "amarillo"
print(f"Después de cambiar índice 1: {colores}")

# Cambiar múltiples elementos
colores[0:2] = ["negro", "blanco"]
print(f"Después de cambiar índices 0-1: {colores}")

print()

# Métodos de listas - Agregar elementos
print("=== AGREGAR ELEMENTOS ===")
animales = ["perro", "gato"]
print(f"Lista inicial: {animales}")

# append() - agregar al final
animales.append("pájaro")
print(f"Después de append('pájaro'): {animales}")

# insert() - insertar en posición específica
animales.insert(1, "pez")
print(f"Después de insert(1, 'pez'): {animales}")

# extend() - agregar múltiples elementos
animales.extend(["conejo", "hamster"])
print(f"Después de extend(['conejo', 'hamster']): {animales}")

print()

# Métodos de listas - Eliminar elementos
print("=== ELIMINAR ELEMENTOS ===")
numeros = [1, 2, 3, 4, 5, 3, 6]
print(f"Lista inicial: {numeros}")

# remove() - eliminar primera aparición
numeros.remove(3)
print(f"Después de remove(3): {numeros}")

# pop() - eliminar por índice
elementoEliminado = numeros.pop(2)
print(f"Después de pop(2), elemento eliminado: {elementoEliminado}, lista: {numeros}")

# pop() sin índice - eliminar último
ultimoElemento = numeros.pop()
print(f"Después de pop(), último elemento: {ultimoElemento}, lista: {numeros}")

# clear() - vaciar lista
numerosBackup = numeros.copy()
numeros.clear()
print(f"Después de clear(): {numeros}")
numeros = numerosBackup  # Restaurar para continuar

print()

# Métodos de búsqueda y conteo
print("=== BÚSQUEDA Y CONTEO ===")
letras = ["a", "b", "c", "b", "d", "b", "e"]
print(f"Lista de letras: {letras}")

# index() - encontrar índice de elemento
indiceB = letras.index("b")
print(f"Índice de primera 'b': {indiceB}")

# count() - contar apariciones
cantidadB = letras.count("b")
print(f"Cantidad de 'b' en la lista: {cantidadB}")

# in - verificar si elemento existe
existeC = "c" in letras
existeZ = "z" in letras
print(f"'c' está en la lista: {existeC}")
print(f"'z' está en la lista: {existeZ}")

print()

# Métodos de ordenamiento
print("=== ORDENAMIENTO ===")
numerosDesordenados = [5, 2, 8, 1, 9, 3]
print(f"Lista desordenada: {numerosDesordenados}")

# sort() - ordenar la lista original
numerosDesordenados.sort()
print(f"Después de sort(): {numerosDesordenados}")

# sorted() - crear nueva lista ordenada
palabras = ["zebra", "oso", "abeja", "perro"]
palabrasOrdenadas = sorted(palabras)
print(f"Lista original: {palabras}")
print(f"Lista ordenada (nueva): {palabrasOrdenadas}")

# reverse() - invertir orden
numerosDesordenados.reverse()
print(f"Después de reverse(): {numerosDesordenados}")

print()

# Operaciones con listas
print("=== OPERACIONES CON LISTAS ===")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Concatenación
listaConcatenada = lista1 + lista2
print(f"Lista1 + Lista2: {listaConcatenada}")

# Repetición
listaRepetida = lista1 * 3
print(f"Lista1 * 3: {listaRepetida}")

# Longitud
longitudLista = len(listaConcatenada)
print(f"Longitud de lista concatenada: {longitudLista}")

print()

# Funciones útiles con listas
print("=== FUNCIONES ÚTILES ===")
calificaciones = [85, 92, 78, 96, 88, 91]
print(f"Calificaciones: {calificaciones}")

# Funciones estadísticas
sumaTotal = sum(calificaciones)
valorMaximo = max(calificaciones)
valorMinimo = min(calificaciones)
promedio = sumaTotal / len(calificaciones)

print(f"Suma total: {sumaTotal}")
print(f"Calificación máxima: {valorMaximo}")
print(f"Calificación mínima: {valorMinimo}")
print(f"Promedio: {promedio:.2f}")

print()

# Listas anidadas (listas dentro de listas)
print("=== LISTAS ANIDADAS ===")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matriz 3x3: {matriz}")

# Acceder a elementos de listas anidadas
print(f"Elemento en fila 0, columna 1: {matriz[0][1]}")
print(f"Elemento en fila 2, columna 2: {matriz[2][2]}")

# Modificar elemento en lista anidada
matriz[1][1] = 50
print(f"Después de cambiar matriz[1][1] = 50: {matriz}")

print()

# Comprensión de listas (list comprehension)
print("=== COMPRENSIÓN DE LISTAS ===")
numerosOriginales = [1, 2, 3, 4, 5]

# Crear lista de cuadrados
cuadrados = [x**2 for x in numerosOriginales]
print(f"Números originales: {numerosOriginales}")
print(f"Cuadrados: {cuadrados}")

# Lista con condición
numerosPares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Números pares del 1 al 10: {numerosPares}")

print()

# Ejemplo práctico: Lista de compras
print("=== EJEMPLO PRÁCTICO: LISTA DE COMPRAS ===")
listaCompras = []

# Agregar productos
productos = ["leche", "pan", "huevos", "queso", "manzanas"]
for producto in productos:
    listaCompras.append(producto)

print(f"Lista de compras: {listaCompras}")

# Simular compra (eliminar productos)
productoComprado = listaCompras.pop(0)
print(f"Compraste: {productoComprado}")
print(f"Lista actualizada: {listaCompras}")

# Verificar si necesitas algo específico
necesitasPan = "pan" in listaCompras
print(f"¿Necesitas pan?: {necesitasPan}")

print(f"Productos restantes por comprar: {len(listaCompras)}")

print("\nFin del script de listas de Python")
