# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Existen las Constantes en Python
# Descripción: Explicación sobre las constantes en Python y convenciones de nomenclatura

# Concepto de constantes en Python
print("=== ¿EXISTEN LAS CONSTANTES EN PYTHON? ===")
print("Python no tiene constantes verdaderas, pero usa convenciones de nomenclatura")

print()

# Ejemplo 1: Convención para constantes (MAYÚSCULAS)
print("=== CONVENCIÓN PARA CONSTANTES ===")
CONSTANTE_PI = 3.1415926  # Por convención, se escribe en MAYÚSCULAS
print(f"Valor de PI: {CONSTANTE_PI}")

# Otras constantes comunes
VELOCIDAD_LUZ = 299792458  # metros por segundo
GRAVEDAD_TIERRA = 9.81     # m/s²
NUMERO_EULER = 2.71828

print(f"Velocidad de la luz: {VELOCIDAD_LUZ} m/s")
print(f"Gravedad terrestre: {GRAVEDAD_TIERRA} m/s²")
print(f"Número de Euler: {NUMERO_EULER}")

print()

# Ejemplo 2: Diferencia entre constantes y variables
print("=== CONSTANTES VS VARIABLES ===")

# Variable normal (puede cambiar)
nombreVariable = 10
print(f"Variable inicial: {nombreVariable}")

nombreVariable = 20  # La variable puede cambiar
print(f"Variable modificada: {nombreVariable}")

# "Constante" (por convención no debería cambiar)
CONSTANTE_MAXIMA = 100
print(f"Constante máxima: {CONSTANTE_MAXIMA}")

# Técnicamente se puede modificar, pero no se debe hacer
# CONSTANTE_MAXIMA = 200  # ¡No recomendado!

print()

# Ejemplo 3: Uso práctico de constantes
print("=== USO PRÁCTICO DE CONSTANTES ===")

# Constantes para configuración
LIMITE_INTENTOS = 3
TIEMPO_ESPERA = 5
MENSAJE_BIENVENIDA = "¡Bienvenido al sistema!"

print(f"Límite de intentos: {LIMITE_INTENTOS}")
print(f"Tiempo de espera: {TIEMPO_ESPERA} segundos")
print(f"Mensaje: {MENSAJE_BIENVENIDA}")

# Simulación de entrada de usuario (sin input real)
numeroUsuario = "42"  # Simulamos entrada del usuario
print(f"Número ingresado por el usuario: {numeroUsuario}")

print()

# Ejemplo 4: Constantes matemáticas comunes
print("=== CONSTANTES MATEMÁTICAS COMUNES ===")

# Usando el módulo math para constantes reales
import math

print(f"PI desde math: {math.pi}")
print(f"E desde math: {math.e}")
print(f"Infinito: {math.inf}")

# Comparación con nuestras constantes
print(f"Nuestra PI: {CONSTANTE_PI}")
print(f"Diferencia: {abs(math.pi - CONSTANTE_PI)}")

print()

# Ejemplo 5: Buenas prácticas con constantes
print("=== BUENAS PRÁCTICAS ===")
print("1. Usar MAYÚSCULAS para nombres de constantes")
print("2. Definir constantes al inicio del archivo")
print("3. Usar nombres descriptivos")
print("4. No modificar valores de constantes durante la ejecución")
print("5. Agrupar constantes relacionadas")

# Ejemplo de agrupación de constantes
print("\nEjemplo de constantes agrupadas:")
# Constantes de configuración de base de datos
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "mi_base_datos"

print(f"Host: {DB_HOST}")
print(f"Puerto: {DB_PORT}")
print(f"Base de datos: {DB_NAME}")

print("\nFin del script sobre constantes en Python")
