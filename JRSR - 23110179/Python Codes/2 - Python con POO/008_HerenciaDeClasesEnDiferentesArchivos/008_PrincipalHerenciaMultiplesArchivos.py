# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Archivo Principal: Uso de Clases Importadas ---

# Se importan las clases desde sus respectivos archivos.
from a_ClaseBase import Usuarios
from b_SubclasePremium import UsuariosPremium
from c_SubclasePremiumPlus import UsuariosPremiumPlus

# Se crean instancias de cada una de las clases.
usuario1 = Usuarios("001", "raulito43", "Raúl", "Fernández")
usuario2 = UsuariosPremium("002", "PdePython", "Paula", "Vega", 10, 500)
usuario3 = UsuariosPremiumPlus("003", "BreakTheSystem", "Ana", "García", 25, 1500)

print("\n>>> DATOS USUARIO 1 - Usuarios (Clase Base)")
usuario1.muestraDatos()

print("\n>>> DATOS USUARIO 2 - UsuariosPremium (Subclase)")
usuario2.muestraDatos()

print("\n>>> DATOS USUARIO 3 - UsuariosPremiumPlus (Subclase de Subclase)")
usuario3.muestraDatos()