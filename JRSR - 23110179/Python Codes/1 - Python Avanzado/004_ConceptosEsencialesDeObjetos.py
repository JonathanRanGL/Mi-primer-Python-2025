# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Conceptos Esenciales de Objetos ---

# Se declara la clase que servirá como plantilla.
class Vehiculo:
    color = None
    longitudMetros = None
    ruedas = 4
    velocidadMaxima = 0 # Atributo con valor inicial.

    def arrancar(self):
        print("El motor ha arrancado.")

    def detener(self):
        print("El motor está detenido.")

# Instanciación: Creamos objetos a partir de la clase.
# Cada objeto es una entidad separada con sus propios datos.
vehiculo1 = Vehiculo()
vehiculo2 = Vehiculo()

# Acceso a atributos: Se usa la notación de punto (objeto.atributo).
print(f"Ruedas del vehículo 1: {vehiculo1.ruedas}")

# Modificación de atributos: Cada objeto mantiene sus propios valores.
vehiculo1.color = "Negro"
vehiculo2.color = "Azul"
vehiculo1.velocidadMaxima = 161

print(f"Color del vehículo 1: {vehiculo1.color}")
print(f"Color del vehículo 2: {vehiculo2.color}")
print(f"Velocidad máxima del vehículo 1: {vehiculo1.velocidadMaxima} km/h")
print(f"Velocidad máxima del vehículo 2: {vehiculo2.velocidadMaxima} km/h") # Mantiene el valor por defecto.

# Llamada a métodos: Se usa la notación de punto (objeto.metodo()).
print("\nAcciones del vehículo 1:")
vehiculo1.arrancar()