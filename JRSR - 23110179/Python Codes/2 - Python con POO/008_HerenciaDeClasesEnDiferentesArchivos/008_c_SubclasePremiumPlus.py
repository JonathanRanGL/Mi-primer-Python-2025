# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Archivo 3: Subclase Premium Plus ---
# Se importa la clase 'UsuariosPremium' desde el archivo '008_b_SubclasePremium'.
from b_SubclasePremium import UsuariosPremium

class UsuariosPremiumPlus(UsuariosPremium):
    # Se sobrescribe un atributo de la clase de la que hereda.
    participacionSorteos = 25

    # Se extiende nuevamente el método para añadir más detalles.
    def muestraDatos(self):
        super().muestraDatos() # Llama a la versión del método de 'UsuariosPremium'.
        print("¡Este usuario tiene acceso a contenido exclusivo Plus!")