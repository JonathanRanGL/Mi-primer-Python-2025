# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Introducción a las Expresiones Lógica Booleana
# Descripción: Ejemplos completos de operadores lógicos y expresiones booleanas en Python

# Operadores de comparación
print("=== OPERADORES DE COMPARACIÓN ===")

# Operador de igualdad (==)
print("=== OPERADOR DE IGUALDAD (==) ===")
# Sintaxis: valor_izquierda == valor_derecha

# Ejemplo básico
resultado = 10 == 20
print(f"10 == 20: {resultado}")

# Ejemplo con variables
a = 10
b = 15
comparacion = a == b
print(f"{a} == {b}: {comparacion}")

# Ejemplo donde son iguales
a = 10
b = 10
comparacion = a == b
print(f"{a} == {b}: {comparacion}")

print()

# Operador de desigualdad (!=)
print("=== OPERADOR DE DESIGUALDAD (!=) ===")

a = 10
b = 15
comparacion = a != b
print(f"{a} != {b}: {comparacion}")

a = 10
b = 10
comparacion = a != b
print(f"{a} != {b}: {comparacion}")

print()

# Operadores de comparación numérica
print("=== OPERADORES DE COMPARACIÓN NUMÉRICA ===")

# Mayor que (>)
a = 10
b = 15
comparacion = a > b
print(f"{a} > {b}: {comparacion}")

# Menor que (<)
a = 10
b = 15
comparacion = a < b
print(f"{a} < {b}: {comparacion}")

# Mayor o igual que (>=)
a = 10
b = 10
comparacion = a >= b
print(f"{a} >= {b}: {comparacion}")

# Menor o igual que (<=)
a = 10
b = 15
comparacion = a <= b
print(f"{a} <= {b}: {comparacion}")

print()

# Operador lógico AND
print("=== OPERADOR LÓGICO AND ===")
print("Sintaxis: expresion1 and expresion2")
print("Ejemplo: a > b and c == d")

# Ejemplo con valores booleanos directos
resultadoAnd = True and False
print(f"True and False: {resultadoAnd}")

# Ejemplo práctico con variables
a = 15
b = 17
c = 13

# Comparaciones con AND
comparacionUno = a < b and b > c  # True and True = True
comparacionDos = a > b and b > c  # False and True = False

print(f"Variables: a={a}, b={b}, c={c}")
print(f"a < b and b > c: {comparacionUno}")
print(f"a > b and b > c: {comparacionDos}")

print()

# Operador lógico OR
print("=== OPERADOR LÓGICO OR ===")
print("Sintaxis: expresion1 or expresion2")

a = 15
b = 17
c = 13

# Comparaciones con OR
comparacionUno = a < b or b > c  # True or True = True
comparacionDos = a == b or b < c  # False or False = False

print(f"Variables: a={a}, b={b}, c={c}")
print(f"a < b or b > c: {comparacionUno}")
print(f"a == b or b < c: {comparacionDos}")

print()

# Operador lógico NOT
print("=== OPERADOR LÓGICO NOT ===")
print("Sintaxis: not expresion")

a = 5
b = 3

# Comparación sin NOT
comparacion = a == b
print(f"Variables: a={a}, b={b}")
print(f"a == b: {comparacion}")

# Comparación con NOT
comparacion = not a == b
print(f"not a == b: {comparacion}")

print()

# Expresiones complejas
print("=== EXPRESIONES COMPLEJAS ===")

# Ejemplo de expresión compleja con paréntesis
expresionCompleja = not (10 > 7 and (10 == 11 or 11 != 10))
print(f"not (10 > 7 and (10 == 11 or 11 != 10)): {expresionCompleja}")

# Desglosando la expresión paso a paso
print("\nDesglose paso a paso:")
paso1 = (10 == 11 or 11 != 10)  # False or True = True
print(f"(10 == 11 or 11 != 10): {paso1}")

paso2 = (10 > 7 and paso1)  # True and True = True
print(f"(10 > 7 and True): {paso2}")

paso3 = not paso2  # not True = False
print(f"not (True): {paso3}")

print()

# Tabla de verdad para AND
print("=== TABLA DE VERDAD PARA AND ===")
print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False:", False and False)

print()

# Tabla de verdad para OR
print("=== TABLA DE VERDAD PARA OR ===")
print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)

print()

# Tabla de verdad para NOT
print("=== TABLA DE VERDAD PARA NOT ===")
print("not True:", not True)
print("not False:", not False)

print()

# Ejemplos prácticos
print("=== EJEMPLOS PRÁCTICOS ===")

# Validación de edad y licencia
edad = 18
tieneLicencia = True

puedeConducir = edad >= 18 and tieneLicencia
print(f"Edad: {edad}, Tiene licencia: {tieneLicencia}")
print(f"¿Puede conducir?: {puedeConducir}")

# Validación de acceso
esAdmin = False
esUsuarioRegistrado = True
tienePermiso = True

puedeAcceder = esAdmin or (esUsuarioRegistrado and tienePermiso)
print(f"\nEs admin: {esAdmin}, Usuario registrado: {esUsuarioRegistrado}, Tiene permiso: {tienePermiso}")
print(f"¿Puede acceder?: {puedeAcceder}")

# Validación de rango numérico
numero = 25
enRangoValido = numero >= 10 and numero <= 100
fueraDeRango = not enRangoValido

print(f"\nNúmero: {numero}")
print(f"¿Está en rango válido (10-100)?: {enRangoValido}")
print(f"¿Está fuera de rango?: {fueraDeRango}")

print()

# Precedencia de operadores
print("=== PRECEDENCIA DE OPERADORES ===")
print("Orden de precedencia (mayor a menor):")
print("1. Paréntesis ()")
print("2. not")
print("3. and")
print("4. or")

# Ejemplo de precedencia
resultado1 = True or False and False  # True or (False and False) = True
resultado2 = (True or False) and False  # (True or False) and False = False

print(f"\nTrue or False and False: {resultado1}")
print(f"(True or False) and False: {resultado2}")

print("\nFin del script de expresiones lógicas booleanas")
