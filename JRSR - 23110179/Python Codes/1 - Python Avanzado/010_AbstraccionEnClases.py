# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Abstracción en Clases (Clases Abstractas) ---

# La abstracción oculta la complejidad y muestra solo la funcionalidad esencial.
# En Python, se logra con el módulo 'abc' (Abstract Base Classes).
from abc import ABC, abstractmethod

# Una clase abstracta no se puede instanciar. Sirve como una plantilla obligatoria.
class Animal(ABC):

    # Un método abstracto debe ser implementado por cualquier subclase concreta.
    @abstractmethod
    def hablar(self):
        pass

# Si una clase hereda de 'Animal' pero no implementa 'hablar', no se puede instanciar.
# class Perro(Animal):
#     def correr(self): # No implementa hablar()
#         print("Corriendo")
# perro = Perro() # Esto daría un TypeError.

# Clase Concreta: hereda de la clase abstracta e implementa TODOS sus métodos abstractos.
class Gato(Animal):
    def hablar(self):
        print("Meow!")

class Vaca(Animal):
    def hablar(self):
        print("Mooo!")

# No se puede crear un objeto de la clase abstracta 'Animal'.
# animal = Animal() # Esto daría un TypeError.

# Sí se pueden crear objetos de las clases concretas.
gato = Gato()
vaca = Vaca()

gato.hablar()
vaca.hablar()