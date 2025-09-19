# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Guía Completa de Funciones en Python ---
import math

# --- 1. Definición Básica y 'return' ---
# Una función es un bloque de código reutilizable. 'return' devuelve un valor.
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

resultado = sumar(10, 56)
print(f"Resultado de la suma: {resultado}")


# --- 2. Parámetros y Argumentos ---
# 'a' y 'b' son parámetros. Se pueden pasar por posición o por nombre (keyword).
# También pueden tener valores por defecto.
def saludar(nombre, mensaje="qué tal"):
    print(f"Hola {nombre}, {mensaje}")

saludar("Ana") # Usa el valor por defecto
saludar("Luis", "buenos días") # Sobrescribe el valor por defecto
saludar(mensaje="buenas noches", nombre="Carlos") # Argumentos por nombre


# --- 3. Argumentos Flexibles (*args) ---
# '*args' empaqueta todos los argumentos posicionales extra en una tupla.
def crearLista(*args):
    print(f"Argumentos recibidos como tupla: {args}")
    return list(args)

miLista = crearLista(7, 45, 32, "texto", True)
print(f"Lista creada: {miLista}")


# --- 4. Argumentos de Palabra Clave Flexibles (**kwargs) ---
# '**kwargs' empaqueta todos los argumentos de palabra clave extra en un diccionario.
def mostrarInfo(**kwargs):
    print(f"Argumentos recibidos como diccionario: {kwargs}")
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize()}: {valor}")

mostrarInfo(nombre="Enrique", edad=32, ciudad="Madrid")


# --- 5. Funciones Lambda (Anónimas) ---
# Son funciones pequeñas de una sola línea. Útiles para operaciones rápidas.
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"\nCuadrados calculados con lambda: {cuadrados}")


# --- 6. Decoradores ---
# Un decorador es una función que toma otra función y extiende su comportamiento sin modificarla explícitamente.
def miDecorador(funcion):
    def wrapper(*args, **kwargs):
        print(">> Inicio del cálculo...")
        funcion(*args, **kwargs)
        print(">> Cálculo finalizado con éxito.\n")
    return wrapper

@miDecorador
def areaCirculo(radio):
    print(f"El área del círculo es {math.pi * radio ** 2}")

@miDecorador
def areaRectangulo(base, altura):
    print(f"El área del rectángulo es: {base * altura}")

areaCirculo(radio=2)
areaRectangulo(base=6, altura=10)


# --- 7. Generadores (yield) ---
# Los generadores son funciones que "pausan" su ejecución y la reanudan, produciendo valores uno a uno.
# Son muy eficientes con la memoria para secuencias grandes.
def generadorDePares(limite):
    for i in range(limite):
        if i % 2 == 0:
            yield i # 'yield' produce un valor y pausa la función.

print("--- Generador de Números Pares ---")
for par in generadorDePares(10):
    print(par)