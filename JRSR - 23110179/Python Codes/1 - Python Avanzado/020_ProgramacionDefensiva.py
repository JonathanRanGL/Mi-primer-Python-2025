# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Guía de Programación Defensiva en Python ---

# --- 1. Manejo de Excepciones (try...except...finally) ---
# Permite controlar errores que pueden ocurrir durante la ejecución del programa.
def dividir(dividendo, divisor):
    try:
        # Intenta ejecutar este bloque de código.
        resultado = round(dividendo / divisor, 2)
        print(f"El resultado de la división es: {resultado}")
    except ZeroDivisionError:
        # Se ejecuta si ocurre una división por cero.
        print("Error: No se puede dividir por cero.")
    except TypeError:
        # Se ejecuta si los tipos de datos son incorrectos.
        print("Error: Ambos valores deben ser numéricos.")
    finally:
        # Se ejecuta siempre, haya ocurrido un error o no.
        print("--- Operación de división finalizada. ---\n")

print("--- Manejo de Excepciones ---")
dividir(10, 3)
dividir(10, 0)
dividir(10, "texto")


# --- 2. Validación de Entradas de Usuario ---
# Es crucial asegurarse de que los datos del usuario son del tipo y formato esperados.
def solicitarEdad():
    while True:
        try:
            edad = int(input("Introduce tu edad: "))
            # Si la conversión a 'int' tiene éxito, salimos del bucle.
            break
        except ValueError:
            # Si el usuario no introduce un número, se lo indicamos y el bucle continúa.
            print("Valor no válido. Por favor, introduce un número entero.")
    print(f"Tu edad es: {edad}\n")

# Descomenta la siguiente línea para probar la validación de entrada.
# solicitarEdad()


# --- 3. Aserciones (assert) ---
# 'assert' comprueba si una condición es verdadera. Si no lo es, lanza un AssertionError.
# Se usa para verificar condiciones internas del programa que NUNCA deberían ser falsas (debugging).
def calcularImc(peso, altura):
    assert peso > 0, "El peso debe ser un valor positivo."
    assert altura > 0, "La altura debe ser un valor positivo."
    return peso / (altura ** 2)

print("--- Aserciones ---")
try:
    calcularImc(peso=-70, altura=1.75)
except AssertionError as e:
    print(f"Aserción fallida: {e}\n")


# --- 4. Lanzar Excepciones Personalizadas (raise) ---
# Se pueden crear y lanzar excepciones propias para manejar errores específicos de la lógica del programa.
class ExcepcionRango(Exception):
    """Excepción personalizada para valores fuera de un rango específico."""
    pass

def validarRango(numero, minimo, maximo):
    if not minimo <= numero <= maximo:
        # 'raise' lanza una excepción.
        raise ExcepcionRango(f"El valor {numero} está fuera del rango permitido ({minimo}-{maximo}).")
    print("El número está dentro del rango permitido.")

print("--- Excepciones Personalizadas ---")
try:
    validarRango(500, 0, 300)
except ExcepcionRango as e:
    print(f"Error personalizado: {e}")