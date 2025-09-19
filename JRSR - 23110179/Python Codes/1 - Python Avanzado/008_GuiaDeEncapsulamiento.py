# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Guía de Encapsulamiento (Público, Protegido, Privado) ---

class Usuario:
    def __init__(self, id, nombre, edad):
        # Atributo público: accesible desde cualquier lugar.
        self.id = id
        # Atributo protegido: por convención (_), no debe usarse fuera de la clase o subclases.
        self._nombre = nombre
        # Atributo privado: por convención (__), Python lo "oculta" (name mangling).
        self.__edad = edad

    # GETTER: Método público para obtener el valor de un atributo privado.
    def getEdad(self):
        return self.__edad

    # SETTER: Método público para establecer el valor de un atributo privado.
    def setEdad(self, nuevaEdad):
        if nuevaEdad > 0:
            self.__edad = nuevaEdad
        else:
            print("Error: La edad debe ser un valor positivo.")

# Creamos una instancia.
usuario1 = Usuario(1, "Enrique", 32)

# Acceso a atributo público (correcto).
print(f"ID público: {usuario1.id}")

# Acceso a atributo protegido (posible, pero no recomendado).
print(f"Nombre protegido: {usuario1._nombre}")

# Intentar acceder al atributo privado directamente dará un error.
# print(usuario1.__edad) # Descomentar esto causaría un AttributeError.

# La forma correcta de interactuar con atributos privados es a través de getters y setters.
print(f"Edad inicial (vía getter): {usuario1.getEdad()}")

# Usamos el setter para modificar la edad de forma controlada.
usuario1.setEdad(25)
print(f"Edad modificada (vía getter): {usuario1.getEdad()}")

# El setter puede incluir lógica de validación.
usuario1.setEdad(-5)