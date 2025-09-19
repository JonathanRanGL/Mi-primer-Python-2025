# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Archivo 1: Clase Base (Superclase) ---
# Este archivo contiene la definición de la clase padre 'Usuarios'.

class Usuarios:
    tipoUsuario = "Free"
    publicidad = True

    def __init__(self, nid, alias, nombre, apellidos):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos

    def muestraDatos(self):
        print("--- Datos del Usuario ---")
        print(f"Nombre y apellidos: {self.nombre} {self.apellidos}")
        print(f"ID de usuario: {self.nid}")
        print(f"Alias: {self.alias}")