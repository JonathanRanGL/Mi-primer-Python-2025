# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Herencia: Superclases y Subclases ---

# SUPERCLASE (o clase padre): Define atributos y métodos comunes.
class Usuarios:
    tipoUsuario = "Free"
    publicidad = True

    def __init__(self, nid, alias, nombre, apellidos):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos

    def muestraDatos(self):
        print("--- Mostrando datos del usuario ---")
        print(f"Nombre y apellidos: {self.nombre} {self.apellidos}")
        print(f"ID de usuario: {self.nid}")
        print(f"Alias: {self.alias}")


# SUBCLASE (o clase hija): Hereda de la superclase 'Usuarios'.
# Adquiere todos los atributos y métodos de la clase padre.
class UsuariosPremium(Usuarios):
    # Puede sobrescribir atributos de la clase padre.
    tipoUsuario = "Premium"
    publicidad = False

# Se crea un objeto de la clase hija (subclase).
usuarioPremium1 = UsuariosPremium("001", "raulito43", "Raúl", "Fernández")

# El objeto 'usuarioPremium1' puede usar el método 'muestraDatos' heredado de 'Usuarios'.
usuarioPremium1.muestraDatos()

# Se accede a los atributos sobrescritos en la subclase.
print(f"Tipo de usuario: {usuarioPremium1.tipoUsuario}")
print(f"¿Tiene publicidad?: {usuarioPremium1.publicidad}")