# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Introducción a las Cadenas de Caracteres
# Descripción: Ejemplos de manipulación y operaciones con strings en Python

# Creación de cadenas básicas
print("=== CREACIÓN DE CADENAS ===")
cadenaSimple = "Hola mundo"
cadenaComillasSimples = 'Python es genial'
cadenaMultilinea = """Esta es una cadena
que abarca múltiples
líneas de texto"""

print(f"Cadena simple: {cadenaSimple}")
print(f"Cadena con comillas simples: {cadenaComillasSimples}")
print(f"Cadena multilínea:\n{cadenaMultilinea}")

print()

# Concatenación de cadenas
print("=== CONCATENACIÓN DE CADENAS ===")
fragmentoUno = "La programación es como la vida: "
fragmentoDos = "llena de errores, pero también de posibilidades."

# Concatenar los dos strings
fraseCompleta = fragmentoUno + fragmentoDos
print(f"Frase completa: {fraseCompleta}")

# Concatenación con espacios
nombre = "Juan"
apellido = "Pérez"
nombreCompleto = nombre + " " + apellido
print(f"Nombre completo: {nombreCompleto}")

print()

# Repetición de cadenas
print("=== REPETICIÓN DE CADENAS ===")
patron = "Python "
patronRepetido = patron * 3
print(f"Patrón repetido: {patronRepetido}")

separador = "-" * 20
print(f"Separador: {separador}")

print()

# Indexación de cadenas
print("=== INDEXACIÓN DE CADENAS ===")
palabra = "Python"
print(f"Palabra: {palabra}")
print(f"Primer carácter (índice 0): {palabra[0]}")
print(f"Último carácter (índice -1): {palabra[-1]}")
print(f"Tercer carácter (índice 2): {palabra[2]}")

print()

# Slicing (rebanado) de cadenas
print("=== SLICING DE CADENAS ===")
frase = "Aprendiendo Python"
print(f"Frase original: {frase}")
print(f"Primeros 5 caracteres: {frase[:5]}")
print(f"Últimos 6 caracteres: {frase[-6:]}")
print(f"Caracteres del 3 al 8: {frase[3:9]}")
print(f"Cada segundo carácter: {frase[::2]}")

print()

# Métodos de cadenas
print("=== MÉTODOS DE CADENAS ===")
textoEjemplo = "  Hola Mundo Python  "
print(f"Texto original: '{textoEjemplo}'")

# Métodos de limpieza
textoLimpio = textoEjemplo.strip()
print(f"Sin espacios al inicio y final: '{textoLimpio}'")

# Métodos de transformación
textoMayusculas = textoLimpio.upper()
textoMinusculas = textoLimpio.lower()
textoTitulo = textoLimpio.title()

print(f"En mayúsculas: {textoMayusculas}")
print(f"En minúsculas: {textoMinusculas}")
print(f"En formato título: {textoTitulo}")

print()

# Métodos de búsqueda y reemplazo
print("=== BÚSQUEDA Y REEMPLAZO ===")
oracion = "Python es un lenguaje de programación. Python es fácil de aprender."
print(f"Oración original: {oracion}")

# Buscar subcadenas
posicionPython = oracion.find("Python")
print(f"Primera aparición de 'Python' en posición: {posicionPython}")

cantidadPython = oracion.count("Python")
print(f"Número de veces que aparece 'Python': {cantidadPython}")

# Reemplazar texto
oracionModificada = oracion.replace("Python", "Java")
print(f"Reemplazando 'Python' por 'Java': {oracionModificada}")

print()

# Métodos de verificación
print("=== MÉTODOS DE VERIFICACIÓN ===")
textoNumerico = "12345"
textoAlfabetico = "Python"
textoMixto = "Python123"

print(f"'{textoNumerico}' es numérico: {textoNumerico.isdigit()}")
print(f"'{textoAlfabetico}' es alfabético: {textoAlfabetico.isalpha()}")
print(f"'{textoMixto}' es alfanumérico: {textoMixto.isalnum()}")

# Verificar mayúsculas y minúsculas
textoMayus = "PYTHON"
textoMinus = "python"
print(f"'{textoMayus}' está en mayúsculas: {textoMayus.isupper()}")
print(f"'{textoMinus}' está en minúsculas: {textoMinus.islower()}")

print()

# División y unión de cadenas
print("=== DIVISIÓN Y UNIÓN DE CADENAS ===")
listaFrutas = "manzana,pera,uva,naranja"
frutasArray = listaFrutas.split(",")
print(f"Lista original: {listaFrutas}")
print(f"Array de frutas: {frutasArray}")

# Unir elementos de una lista
frutasUnidas = " - ".join(frutasArray)
print(f"Frutas unidas con guión: {frutasUnidas}")

print()

# Formateo de cadenas
print("=== FORMATEO DE CADENAS ===")
nombrePersona = "Ana"
edadPersona = 25
alturaPersona = 1.65

# Formateo con f-strings (recomendado)
mensajeFormateado = f"Hola, soy {nombrePersona}, tengo {edadPersona} años y mido {alturaPersona:.2f} metros."
print(f"Con f-string: {mensajeFormateado}")

# Formateo con .format()
mensajeFormat = "Hola, soy {}, tengo {} años y mido {:.2f} metros.".format(nombrePersona, edadPersona, alturaPersona)
print(f"Con .format(): {mensajeFormat}")

print()

# Caracteres de escape
print("=== CARACTERES DE ESCAPE ===")
textoConComillas = "Él dijo: \"Python es increíble\""
textoConApostrofe = 'It\'s a beautiful day'
textoConSaltoLinea = "Primera línea\nSegunda línea\nTercera línea"
textoConTabulacion = "Columna1\tColumna2\tColumna3"

print(f"Con comillas: {textoConComillas}")
print(f"Con apóstrofe: {textoConApostrofe}")
print(f"Con salto de línea:\n{textoConSaltoLinea}")
print(f"Con tabulación:\n{textoConTabulacion}")

print("\nFin del script de cadenas de caracteres")
