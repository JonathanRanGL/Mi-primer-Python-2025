# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Guía de Espacios de Nombres y Ámbito (Scope) ---

# Ámbito Global (Global Scope)
# Esta variable existe fuera de cualquier función.
nombreGlobal = "PCMaster"

def gestionarAmbitos():
    # Ámbito Local (Local Scope)
    # Esta variable solo existe dentro de la función 'gestionarAmbitos'.
    nombreLocal = "Programación Fácil"
    print(f"Dentro de la función (local): {nombreLocal}")

    # Python busca primero en el ámbito local. Como 'nombreLocal' existe aquí, la usa.
    # Si no la encontrara, buscaría en el ámbito global.
    print(f"Accediendo a la variable global desde la función: {nombreGlobal}")

print("--- Demostración de Ámbitos ---")
gestionarAmbitos()
# Fuera de la función, 'nombreLocal' no existe y daría un NameError.
# print(nombreLocal)
print(f"Fuera de la función (global): {nombreGlobal}")


# --- Modificar una variable global con la palabra clave 'global' ---
contador = 0

def incrementarContador():
    # Le decimos a Python que queremos usar la variable 'contador' del ámbito global.
    global contador
    contador += 1
    print(f"Contador dentro de la función: {contador}")

print("\n--- Modificando Variable Global ---")
incrementarContador()
incrementarContador()
print(f"Contador fuera de la función: {contador}") # El valor ha sido modificado.