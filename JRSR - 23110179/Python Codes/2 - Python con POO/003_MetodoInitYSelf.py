# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- El Método __init__ y el parámetro self ---

class Ninjas:
    # El método __init__ es el constructor de la clase. Se ejecuta automáticamente al crear un nuevo objeto.
    # 'self' representa la instancia del objeto que se está creando.
    # 'hp', 'resistencia', etc., son los parámetros que se deben proporcionar al crear el objeto.
    def __init__(self, hp, resistencia, xp, vidas):
        # Se asignan los valores de los parámetros a los atributos de la instancia (del objeto).
        self.hp = hp
        self.resistencia = resistencia
        self.xp = xp
        self.vidas = vidas
        print(f"¡Nuevo ninja creado con {self.hp} de HP y {self.vidas} vidas!")

    # Método de la clase.
    def gameOver(self):
        print('Game over')

# Se crea un objeto 'ninjaPrincipal' proporcionando los argumentos requeridos por __init__.
ninjaPrincipal = Ninjas(100, 50, 1, 3)

# Se crea otro objeto, 'ninjaEnemigo', con diferentes valores.
ninjaEnemigo = Ninjas(25, 10, 0, 1)

# Se puede acceder a los atributos de cada objeto de forma independiente.
print("\nDatos del Ninja Principal:")
print(f"HP: {ninjaPrincipal.hp}, Resistencia: {ninjaPrincipal.resistencia}")

print("\nDatos del Ninja Enemigo:")
print(f"HP: {ninjaEnemigo.hp}, Vidas: {ninjaEnemigo.vidas}")