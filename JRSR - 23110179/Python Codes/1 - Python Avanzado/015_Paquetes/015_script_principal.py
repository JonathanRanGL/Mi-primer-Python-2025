# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Guía de Uso de Paquetes ---

# Importamos el módulo 'matematicas' desde 'mi_paquete'.
import mi_paquete.matematicas as mates

# Importamos el módulo 'formal' desde el subpaquete 'saludos'.
from mi_paquete.saludos import formal

# Usamos la función del primer módulo.
resultado = mates.sumar(100, 200)
print(f"Resultado de la suma: {resultado}")

# Usamos la función del segundo módulo.
mensaje = formal.saludar("Ana")
print(f"Mensaje de saludo: {mensaje}")