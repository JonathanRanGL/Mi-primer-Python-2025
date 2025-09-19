# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Introducción a los Diccionarios
# Descripción: Ejemplos completos de diccionarios y sus operaciones en Python

# Creación de diccionarios básicos
print("=== CREACIÓN DE DICCIONARIOS ===")

# Sintaxis general: {clave1: valor1, clave2: valor2, clave3: valor3}
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(f"Diccionario persona: {persona}")

# Diccionario vacío
diccionarioVacio = {}
print(f"Diccionario vacío: {diccionarioVacio}")

# Acceso a valores
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")

print()

# Operaciones básicas
print("=== OPERACIONES BÁSICAS ===")
estudiante = {"nombre": "Ana", "carrera": "Ingeniería", "semestre": 5}
print(f"Estudiante: {estudiante}")

# Agregar nueva clave-valor
estudiante["promedio"] = 8.5
print(f"Después de agregar promedio: {estudiante}")

# Modificar valor existente
estudiante["semestre"] = 6
print(f"Después de actualizar semestre: {estudiante}")

# Eliminar clave-valor
del estudiante["carrera"]
print(f"Después de eliminar carrera: {estudiante}")

print()

# Métodos útiles
print("=== MÉTODOS ÚTILES ===")
colores = {"rojo": "#FF0000", "verde": "#00FF00", "azul": "#0000FF"}
print(f"Diccionario de colores: {colores}")

# Obtener todas las claves
claves = list(colores.keys())
print(f"Claves: {claves}")

# Obtener todos los valores
valores = list(colores.values())
print(f"Valores: {valores}")

# Obtener pares clave-valor
items = list(colores.items())
print(f"Items: {items}")

print("\nFin del script de diccionarios en Python")
