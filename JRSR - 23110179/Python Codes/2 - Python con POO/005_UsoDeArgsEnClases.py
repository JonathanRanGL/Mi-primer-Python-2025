# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Uso de *args para argumentos flexibles ---

class Usuarios:
    # Atributos de clase.
    tipoUsuario = "Free"
    publicidad = True

    # Se utiliza *args para aceptar un número variable de argumentos posicionales adicionales.
    # Estos argumentos se agrupan en una tupla llamada 'args'.
    def __init__(self, nid, alias, nombre, apellidos, *args):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos
        self.args = args

# Al crear el objeto, los argumentos extra ("Persona estudiosa", "Amante de Python", "27")
# se empaquetan en la tupla 'usuario1.args'.
usuario1 = Usuarios("001", "PdePython", "Paula", "Bravo Rojas", "Persona estudiosa", "Amante de Python", "27")

print(f"Alias del usuario: {usuario1.alias}")
print(f"Atributos extra del usuario: {usuario1.args}")
print(f"Descripción del usuario: {usuario1.args[0]}")