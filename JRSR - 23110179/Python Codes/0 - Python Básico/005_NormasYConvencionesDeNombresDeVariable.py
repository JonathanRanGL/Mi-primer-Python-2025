# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Normas y Convenciones de Nombres de Variable
# Descripción: Ejemplos de convenciones de nomenclatura en Python

# Convención 1: snake_case para variables y funciones (recomendado en Python)
nombreVariable = "Ejemplo"  # camelCase (usado en este script)
NOMBRE_CONSTANTE = "VALOR"  # UPPER_CASE para constantes
NombreClase = "Ejemplo"     # PascalCase para clases

print("Ejemplos de diferentes convenciones:")
print(f"camelCase: {nombreVariable}")
print(f"UPPER_CASE: {NOMBRE_CONSTANTE}")
print(f"PascalCase: {NombreClase}")

# Convención 2: Nombres descriptivos y específicos
numeroUno = 1
fechaActual = "2024-09-19"
resultadoOperacion = 42

print(f"\nNombres descriptivos:")
print(f"numeroUno: {numeroUno}")
print(f"fechaActual: {fechaActual}")
print(f"resultadoOperacion: {resultadoOperacion}")

# Ejemplos de nombres NO válidos (comentados para evitar errores):
# 1numero = 10        # No puede empezar con número
# $resultado = 20     # No puede contener símbolos especiales
# nombre-usuario = "" # No puede contener guiones

# Convención 3: Nombres válidos con caracteres especiales permitidos
_variablePrivada = "privada"  # Guión bajo al inicio indica uso interno
a1B2C3 = "alfanumérico"       # Combinación de letras y números

print(f"\nNombres con caracteres especiales:")
print(f"_variablePrivada: {_variablePrivada}")
print(f"a1B2C3: {a1B2C3}")

# Convención 4: Nombres descriptivos vs nombres genéricos
# Evitar nombres genéricos como 'a', 'x', 'data'
saludo = "Hola"           # Mejor que: a = "Hola"
numeroEntero = 7          # Mejor que: x = 7
numeroPreciso = 7.5657    # Mejor que: data = 7.5657

print(f"\nNombres descriptivos:")
print(f"saludo: {saludo}")
print(f"numeroEntero: {numeroEntero}")
print(f"numeroPreciso: {numeroPreciso}")

# Convención 5: Funciones con nombres descriptivos
def sumarDosNumeros(primerNumero, segundoNumero):
    """
    Función que suma dos números y retorna el resultado
    """
    return primerNumero + segundoNumero

resultadoSuma = sumarDosNumeros(5, 3)
print(f"\nResultado de la suma: {resultadoSuma}")

# Convención 6: Variables con múltiples palabras
nombreCompleto = "Juan Pérez"
horaActual = "14:30"
variableConVariasPalabras = "ejemplo largo"

print(f"\nVariables con múltiples palabras:")
print(f"nombreCompleto: {nombreCompleto}")
print(f"horaActual: {horaActual}")
print(f"variableConVariasPalabras: {variableConVariasPalabras}")

# Convención 7: Constantes vs Variables
PI = 3.14159  # Constante (por convención, en mayúsculas)
numero = 10   # Variable (puede cambiar)

print(f"\nConstantes y variables:")
print(f"PI (constante): {PI}")
print(f"numero (variable): {numero}")

# Cambiar el valor de la variable
numero = 20
print(f"numero actualizado: {numero}")

print("\nFin del script de convenciones de nomenclatura")
