# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Polimorfismo en Clases ---

# Polimorfismo significa "muchas formas". Permite que objetos de diferentes clases
# respondan al mismo método de manera específica para cada clase.

class Animal:
    def hablar(self):
        print("Soy un animal genérico")

class Perro(Animal):
    # Sobrescribe el método 'hablar' de la clase padre.
    def hablar(self):
        print("Woof!")

class Gato(Animal):
    # Sobrescribe el método 'hablar' de la clase padre.
    def hablar(self):
        print("Meow!")

# Esta función demuestra el polimorfismo.
# No le importa qué tipo de objeto recibe, siempre y cuando tenga un método 'hablar'.
def emitirSonido(animal):
    animal.hablar()


# Creamos objetos de diferentes clases.
animalGenerico = Animal()
miPerro = Perro()
miGato = Gato()

# Pasamos diferentes tipos de objetos a la misma función.
print("Llamando a la función con diferentes objetos:")
emitirSonido(animalGenerico)
emitirSonido(miPerro)
emitirSonido(miGato)