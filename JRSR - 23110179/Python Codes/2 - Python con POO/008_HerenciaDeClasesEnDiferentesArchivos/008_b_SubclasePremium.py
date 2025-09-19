# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Archivo 2: Subclase Premium ---
# Se importa la clase 'Usuarios' desde el archivo '008_a_ClaseBase'.
from a_ClaseBase import Usuarios

class UsuariosPremium(Usuarios):
    tipoUsuario = "Premium"
    publicidad = False

    def __init__(self, nid, alias, nombre, apellidos, participacionSorteos, puntosPremios):
        super().__init__(nid, alias, nombre, apellidos)
        self.participacionSorteos = participacionSorteos
        self.puntosPremios = puntosPremios
        self.contenidoPremium = True

    # Se extiende el método muestraDatos para incluir información adicional.
    def muestraDatos(self):
        super().muestraDatos() # Llama al método original del padre.
        print(f"Puntos para premios: {self.puntosPremios}")
        print(f"Participaciones en sorteos: {self.participacionSorteos}")