# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- El Método Constructor __init__ ---

class Usuario:
    # Atributo de clase: es compartido por todas las instancias.
    plataforma = "Educación Online"

    # El método __init__ es el constructor. Se ejecuta al crear un nuevo objeto.
    # Permite inicializar los atributos de la instancia con valores específicos.
    def __init__(self, nombre, apellidos, edad, telefono):
        # Atributos de instancia: pertenecen a cada objeto específico.
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.telefono = telefono
        self.direccion = "Sin dirección" # Atributo con valor por defecto.

    def iniciarSesion(self):
        print(f"El usuario {self.nombre} ha iniciado sesión.")

    def cambiarNombrePerfil(self, nuevoNombre):
        self.nombre = nuevoNombre
        print(f"Nombre actualizado a: {self.nombre}")

# Instanciación: Al crear el objeto, se deben pasar los argumentos requeridos por __init__.
usuario1 = Usuario("Enrique", "Barros Fernández", 32, "123456789")

# Se puede acceder a los atributos inicializados.
print(f"Usuario creado: {usuario1.nombre} {usuario1.apellidos}")
print(f"Dirección inicial: {usuario1.direccion}")

# Y se pueden modificar después si es necesario.
usuario1.direccion = "C/Programación Fácil n.º 34"
print(f"Dirección actualizada: {usuario1.direccion}")