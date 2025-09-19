# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Introducción a las Tuplas con Python
# Descripción: Ejemplos completos de tuplas y sus operaciones en Python

# Creación de tuplas básicas
print("=== CREACIÓN DE TUPLAS ===")

# Sintaxis general: (elemento1, elemento2, elemento3, ...)
tuplaColores = ("rojo", "verde", "azul")
print(f"Tupla de colores: {tuplaColores}")

# Tupla con diferentes tipos de datos
tuplaPersona = ("Ana", 25, True, 1.65)
print(f"Tupla persona: {tuplaPersona}")

# Tupla vacía
tuplaVacia = ()
print(f"Tupla vacía: {tuplaVacia}")

# Tupla con un solo elemento (necesita coma)
tuplaUnElemento = ("único",)
print(f"Tupla con un elemento: {tuplaUnElemento}")

print()

# Acceso a elementos
print("=== ACCESO A ELEMENTOS ===")
coordenadas = (10, 20, 30)
print(f"Coordenadas: {coordenadas}")

print(f"Coordenada X (índice 0): {coordenadas[0]}")
print(f"Coordenada Y (índice 1): {coordenadas[1]}")
print(f"Coordenada Z (índice 2): {coordenadas[2]}")

# Índices negativos
print(f"Última coordenada (índice -1): {coordenadas[-1]}")
print(f"Penúltima coordenada (índice -2): {coordenadas[-2]}")

print()

# Slicing de tuplas
print("=== SLICING DE TUPLAS ===")
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Tupla original: {numeros}")

print(f"Primeros 3 elementos: {numeros[:3]}")
print(f"Últimos 3 elementos: {numeros[-3:]}")
print(f"Elementos del índice 2 al 6: {numeros[2:7]}")
print(f"Elementos pares: {numeros[::2]}")

print()

# Inmutabilidad de tuplas
print("=== INMUTABILIDAD DE TUPLAS ===")
frutas = ("manzana", "pera", "uva")
print(f"Tupla original: {frutas}")

# Las tuplas no se pueden modificar
# frutas[0] = "naranja"  # Esto causaría un TypeError

print("Las tuplas son inmutables - no se pueden modificar después de crear")

# Pero se puede crear una nueva tupla
frutasNuevas = ("naranja",) + frutas[1:]
print(f"Nueva tupla con cambio: {frutasNuevas}")

print()

# Métodos de tuplas
print("=== MÉTODOS DE TUPLAS ===")
letras = ("a", "b", "c", "b", "d", "b")
print(f"Tupla de letras: {letras}")

# count() - contar apariciones
cantidadB = letras.count("b")
print(f"Cantidad de 'b' en la tupla: {cantidadB}")

# index() - encontrar índice
indiceC = letras.index("c")
print(f"Índice de 'c': {indiceC}")

print()

# Operaciones con tuplas
print("=== OPERACIONES CON TUPLAS ===")
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Concatenación
tuplaConcatenada = tupla1 + tupla2
print(f"Tupla1 + Tupla2: {tuplaConcatenada}")

# Repetición
tuplaRepetida = tupla1 * 3
print(f"Tupla1 * 3: {tuplaRepetida}")

# Longitud
longitudTupla = len(tuplaConcatenada)
print(f"Longitud de tupla concatenada: {longitudTupla}")

# Verificar pertenencia
existeTres = 3 in tupla1
existeOcho = 8 in tupla1
print(f"¿3 está en tupla1?: {existeTres}")
print(f"¿8 está en tupla1?: {existeOcho}")

print()

# Desempaquetado de tuplas
print("=== DESEMPAQUETADO DE TUPLAS ===")
puntoTridimensional = (5, 10, 15)
x, y, z = puntoTridimensional
print(f"Punto 3D: {puntoTridimensional}")
print(f"X: {x}, Y: {y}, Z: {z}")

# Desempaquetado con asterisco
numeros = (1, 2, 3, 4, 5)
primero, segundo, *resto = numeros
print(f"Primero: {primero}, Segundo: {segundo}, Resto: {resto}")

print()

# Tuplas anidadas
print("=== TUPLAS ANIDADAS ===")
matriz = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"Matriz como tupla: {matriz}")

# Acceder a elementos anidados
print(f"Elemento [0][1]: {matriz[0][1]}")
print(f"Elemento [2][2]: {matriz[2][2]}")

print()

# Conversión entre tuplas y listas
print("=== CONVERSIÓN TUPLAS-LISTAS ===")
listaOriginal = [1, 2, 3, 4, 5]
tuplaConvertida = tuple(listaOriginal)
print(f"Lista original: {listaOriginal}")
print(f"Convertida a tupla: {tuplaConvertida}")

# De tupla a lista
tuplaOriginal = ("a", "b", "c", "d")
listaConvertida = list(tuplaOriginal)
print(f"Tupla original: {tuplaOriginal}")
print(f"Convertida a lista: {listaConvertida}")

print()

# Funciones útiles con tuplas
print("=== FUNCIONES ÚTILES ===")
calificaciones = (85, 92, 78, 96, 88)
print(f"Calificaciones: {calificaciones}")

sumaTotal = sum(calificaciones)
valorMaximo = max(calificaciones)
valorMinimo = min(calificaciones)
promedio = sumaTotal / len(calificaciones)

print(f"Suma total: {sumaTotal}")
print(f"Calificación máxima: {valorMaximo}")
print(f"Calificación mínima: {valorMinimo}")
print(f"Promedio: {promedio:.2f}")

print()

# Cuándo usar tuplas vs listas
print("=== CUÁNDO USAR TUPLAS ===")
print("Usa tuplas cuando:")
print("- Los datos no cambiarán (inmutables)")
print("- Necesites una estructura de datos más rápida")
print("- Quieras usar como clave en diccionarios")
print("- Representes coordenadas, puntos, o datos relacionados")

# Ejemplo práctico: información de estudiante
estudiante = ("Juan Pérez", 20, "Ingeniería", 8.5)
nombre, edad, carrera, promedio = estudiante
print(f"\nEjemplo práctico:")
print(f"Estudiante: {nombre}")
print(f"Edad: {edad} años")
print(f"Carrera: {carrera}")
print(f"Promedio: {promedio}")

print()

# Tupla como valor de retorno de función
def obtenerDatosPersona():
    """
    Función que retorna múltiples valores usando una tupla
    """
    return ("María García", 28, "Doctora")

datosPersona = obtenerDatosPersona()
nombrePersona, edadPersona, profesionPersona = datosPersona

print("=== FUNCIÓN QUE RETORNA TUPLA ===")
print(f"Datos recibidos: {datosPersona}")
print(f"Nombre: {nombrePersona}")
print(f"Edad: {edadPersona}")
print(f"Profesión: {profesionPersona}")

print("\nFin del script de tuplas en Python")
