# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Guía de Herencia en Clases ---

# Clase Padre (Superclase): Define características comunes.
class Ciudadano:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion

    def saludar(self):
        print(f"Hola, soy {self.nombre}. Mi profesión es {self.profesion}.")

# Clase Hija (Subclase): Hereda de 'Ciudadano'.
# Adquiere todos sus atributos y métodos.
class Medico(Ciudadano):
    # Usa super() para llamar al constructor de la clase padre
    # y establecer la profesión automáticamente.
    def __init__(self, nombre):
        super().__init__(nombre, "médico")

# Otra subclase que hereda de 'Ciudadano'.
class Policia(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, "policía")

# Instanciamos objetos de cada clase.
persona1 = Ciudadano("Julia", "informática")
persona2 = Medico("Raúl")
persona3 = Policia("Raquel")

# Todos los objetos pueden usar el método 'saludar' heredado de 'Ciudadano'.
persona1.saludar()
persona2.saludar()
persona3.saludar()