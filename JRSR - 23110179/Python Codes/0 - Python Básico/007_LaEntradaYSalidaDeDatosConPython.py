# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: La Entrada y Salida de Datos con Python
# Descripción: Ejemplos de entrada y salida de datos usando print() e input()

# Función print() básica
print("=== FUNCIÓN PRINT BÁSICA ===")
print("¡Hola mundo!")
print("Esta es una línea de texto")

print()  # Línea en blanco

# Sintaxis completa de print()
# print(*objects, sep=' ', end='\n', file=None, flush=False)
print("=== PARÁMETROS DE PRINT ===")

# Imprimir múltiples valores
print("El resultado", "de sumar", 10, "más", 50.65, "es:", 10 + 50.65)

print()

# Parámetro sep (separador)
print("=== PARÁMETRO SEP ===")
print("Palabra1", "Palabra2", "Palabra3")  # Separador por defecto (espacio)
print("Palabra1", "Palabra2", "Palabra3", sep="-")  # Separador personalizado
print("A", "B", "C", sep="")  # Sin separador

print()

# Parámetro end (final de línea)
print("=== PARÁMETRO END ===")
print("Esta línea", end=" ")
print("continúa en la misma línea")

print("Primera línea", end=".\n")
print("Segunda línea")

print()

# Caracteres de escape
print("=== CARACTERES DE ESCAPE ===")
print("Línea 1\nLínea 2\nLínea 3")  # \n para nueva línea
print("Texto con\ttabulación")        # \t para tabulación
print("Comillas \"dobles\" en el texto")  # \" para comillas dobles
print('Comillas \'simples\' en el texto')  # \' para comillas simples

print()

# Función input() para entrada de datos
print("=== FUNCIÓN INPUT ===")

# Entrada básica de texto
nombreUsuario = input("Ingresa tu nombre: ")
print(f"Hola, {nombreUsuario}!")

# Entrada de números (conversión necesaria)
edadTexto = input("Ingresa tu edad: ")
edadNumero = int(edadTexto)  # Convertir texto a entero
print(f"Tu edad es: {edadNumero} años")

# Entrada directa con conversión
alturaMetros = float(input("Ingresa tu altura en metros: "))
print(f"Tu altura es: {alturaMetros} metros")

print()

# Operaciones con datos de entrada
print("=== OPERACIONES CON ENTRADA ===")
primerNumero = float(input("Ingresa el primer número: "))
segundoNumero = float(input("Ingresa el segundo número: "))

resultadoSuma = primerNumero + segundoNumero
resultadoMultiplicacion = primerNumero * segundoNumero

print(f"La suma de {primerNumero} + {segundoNumero} = {resultadoSuma}")
print(f"La multiplicación de {primerNumero} * {segundoNumero} = {resultadoMultiplicacion}")

print()

# Formateo de salida con f-strings
print("=== FORMATEO CON F-STRINGS ===")
nombreProducto = "Laptop"
precioProducto = 15999.99
cantidadStock = 25

print(f"Producto: {nombreProducto}")
print(f"Precio: ${precioProducto:.2f}")  # Dos decimales
print(f"Stock disponible: {cantidadStock} unidades")

# Cálculo del total
totalInventario = precioProducto * cantidadStock
print(f"Valor total del inventario: ${totalInventario:,.2f}")  # Con comas y decimales

print()

# Ejemplo práctico: Calculadora simple
print("=== CALCULADORA SIMPLE ===")
print("Calculadora de área de rectángulo")

baseRectangulo = float(input("Ingresa la base del rectángulo: "))
alturaRectangulo = float(input("Ingresa la altura del rectángulo: "))

areaRectangulo = baseRectangulo * alturaRectangulo
perimetroRectangulo = 2 * (baseRectangulo + alturaRectangulo)

print(f"\nResultados:")
print(f"Base: {baseRectangulo} unidades")
print(f"Altura: {alturaRectangulo} unidades")
print(f"Área: {areaRectangulo} unidades cuadradas")
print(f"Perímetro: {perimetroRectangulo} unidades")

print("\nFin del script de entrada y salida de datos")
