# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Introducción a la Programación Modular ---

# La programación modular consiste en dividir un programa grande en partes más pequeñas y manejables, llamadas módulos.
# Esto hace que el código sea más organizado, reutilizable y fácil de mantener.

# Un ejemplo simple de modularidad es usar funciones que ya vienen con Python.
# No necesitamos saber CÓMO funciona 'len()', solo la importamos (implícitamente) y la usamos.
cadena = "Hola, mundo!"
longitud = len(cadena)
print(f"La longitud de la cadena es: {longitud}")

# Un ejemplo más explícito es importar un módulo, como el módulo 'math'.
import math

# Ahora podemos usar las funciones y constantes definidas dentro de 'math'.
numero = 81
raizCuadrada = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es: {raizCuadrada}")

print(f"El valor de Pi es: {math.pi}")