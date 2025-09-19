# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Los Valores Literales con Python
# Descripción: Ejemplos de valores literales y su uso en Python

# Concepto de valores literales
print("=== VALORES LITERALES EN PYTHON ===")
print("Los valores literales son datos que se escriben directamente en el código")

print()

# Ejemplo 1: Literales de cadena (string)
print("=== LITERALES DE CADENA ===")
frase = "Aprendiendo Python"  # Literal de cadena
print(f"Frase original: {frase}")

# Cambiar el valor de la variable con otro literal
frase = "La frase ha cambiado totalmente"
print(f"Frase modificada: {frase}")

print()

# Ejemplo 2: Entrada de usuario vs literales
print("=== ENTRADA DE USUARIO VS LITERALES ===")
print("Ejemplo de entrada de usuario:")

# Simular entrada de usuario (en lugar de input real para que el script sea ejecutable)
nombreUsuario = "Juan"  # Simulamos la entrada del usuario
print(f"Su nombre es: {nombreUsuario}")

print()

# Ejemplo 3: Literales numéricos
print("=== LITERALES NUMÉRICOS ===")
numeroUno = 10      # Literal entero
numeroDos = 586     # Literal entero
numeroDecimal = 3.14159  # Literal decimal

print(f"Número uno: {numeroUno}")
print(f"Número dos: {numeroDos}")
print(f"Número decimal: {numeroDecimal}")

print()

# Ejemplo 4: Diferentes tipos de literales
print("=== TIPOS DE LITERALES ===")

# Literales de cadena
literalCadena = "Este es un literal de cadena"
print(f"Literal de cadena: {literalCadena}")

# Literales numéricos
literalEntero = 42
literalFlotante = 3.14
print(f"Literal entero: {literalEntero}")
print(f"Literal flotante: {literalFlotante}")

# Literales booleanos
literalVerdadero = True
literalFalso = False
print(f"Literal booleano verdadero: {literalVerdadero}")
print(f"Literal booleano falso: {literalFalso}")

# Literal None
literalNulo = None
print(f"Literal None: {literalNulo}")

print()

# Ejemplo 5: Literales en estructuras de datos
print("=== LITERALES EN ESTRUCTURAS DE DATOS ===")

# Lista con literales
listaLiterales = [1, 2, 3, "Python", True]
print(f"Lista con literales: {listaLiterales}")

# Tupla con literales
tuplaLiterales = (10, "Hola", False, 3.14)
print(f"Tupla con literales: {tuplaLiterales}")

# Diccionario con literales
diccionarioLiterales = {"nombre": "Ana", "edad": 25, "activo": True}
print(f"Diccionario con literales: {diccionarioLiterales}")

print()

# Ejemplo 6: Literales vs variables
print("=== LITERALES VS VARIABLES ===")
print("Un literal es un valor fijo escrito directamente en el código")
print("Una variable es un contenedor que puede almacenar diferentes valores")

# Literal directo (no recomendado para valores que se usan múltiples veces)
print("El valor literal 100 aparece directamente en el código")

# Mejor práctica: usar variables para valores que se reutilizan
valorImportante = 100  # Asignar literal a variable
print(f"El valor almacenado en variable: {valorImportante}")

print()

# Nota sobre literales "sueltos"
print("=== NOTA IMPORTANTE ===")
print("Los literales 'sueltos' en el código no tienen efecto:")

# Este literal está "suelto" y no hace nada útil
# "Este valor es literal y no tiene soporte, está 'suelto en el código'."

print("El literal anterior no se muestra porque no está asignado ni impreso")
print("Para usar un literal, debe asignarse a una variable o usarse en una función")

# Uso correcto del literal
mensajeLiteral = "Este valor literal ahora está asignado a una variable"
print(f"Uso correcto: {mensajeLiteral}")

print("\nFin del script de valores literales en Python")