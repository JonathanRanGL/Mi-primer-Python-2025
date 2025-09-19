# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Extendiendo el constructor con super() ---

# Clase Padre
class Usuarios:
    def __init__(self, nid, alias, nombre, apellidos):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos

    def muestraDatos(self):
        print(f"Mostrando datos base: {self.alias} ({self.nid})")


# Clase Hija
class UsuariosPremium(Usuarios):
    # El constructor de la subclase define sus propios atributos y los que necesita la superclase.
    def __init__(self, nid, alias, nombre, apellidos, participacionSorteos, puntosPremios):
        # super().__init__(...) llama al constructor de la clase padre (Usuarios)
        # para inicializar los atributos que le corresponden a ella.
        super().__init__(nid, alias, nombre, apellidos)

        # Después, se inicializan los atributos propios de la subclase.
        self.participacionSorteos = participacionSorteos
        self.puntosPremios = puntosPremios
        self.contenidoPremium = True

# Se crea una instancia de la subclase, proporcionando todos los argumentos necesarios.
usuario1 = UsuariosPremium("002", "PdePython", "Paula", "Vega", 10, 500)

# El objeto 'usuario1' tiene acceso tanto a los atributos de la clase padre...
print(f"Alias del usuario (del padre): {usuario1.alias}")

# ...como a los atributos definidos en su propia clase.
print(f"Puntos para premios (del hijo): {usuario1.puntosPremios}")