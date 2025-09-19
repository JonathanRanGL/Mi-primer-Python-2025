# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- El Parámetro 'self' ---

class Usuario:
    # 'self' es el primer parámetro de los métodos de instancia.
    # Representa la instancia específica del objeto que está llamando al método.
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    # 'self' se usa para acceder a los atributos y métodos del propio objeto.
    def iniciarSesion(self):
        # Usamos self.nombre para obtener el nombre de esta instancia en particular.
        print(f"El usuario {self.nombre} ha iniciado sesión.")

    def mostrarDatos(self):
        print(f"Datos: {self.nombre} {self.apellidos}")

# Creamos dos instancias diferentes.
usuario1 = Usuario("Enrique", "Barros Fernández")
usuario2 = Usuario("Adriana", "Barca López")

# Al llamar al método, Python pasa automáticamente 'usuario1' como el argumento 'self'.
print("Acciones de Usuario 1:")
usuario1.iniciarSesion() # Equivale a Usuario.iniciarSesion(usuario1)
usuario1.mostrarDatos()

# Al llamar al método aquí, Python pasa 'usuario2' como el argumento 'self'.
print("\nAcciones de Usuario 2:")
usuario2.iniciarSesion() # Equivale a Usuario.iniciarSesion(usuario2)
usuario2.mostrarDatos()