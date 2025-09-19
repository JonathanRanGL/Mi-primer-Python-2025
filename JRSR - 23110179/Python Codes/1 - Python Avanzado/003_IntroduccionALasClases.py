# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Introducción a las Clases ---

# Una clase es una plantilla para crear objetos.
# Define los atributos (datos) y métodos (comportamientos) que tendrán sus objetos.
class Vehiculo:
    """
    Esta clase representa las características y comportamientos básicos de un vehículo.
    """
    # Atributos de clase: valores iniciales para las instancias.
    color = None
    longitudMetros = None
    ruedas = 4

    # Métodos: funciones que pertenecen a la clase.
    def arrancar(self):
        print("El motor ha arrancado.")

    def detener(self):
        print("El motor está detenido.")

# Para usar la clase, primero creamos un objeto (una instancia).
coche = Vehiculo()

# Ahora podemos usar los métodos del objeto.
coche.arrancar()
coche.detener()