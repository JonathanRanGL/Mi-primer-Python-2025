# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Atributos Obligatorios a través de __init__ ---

class Ninja:
    # El método __init__ define los atributos que son obligatorios al momento de crear un objeto.
    def __init__(self, hp, resistencia, xp, vidas):
        self.hp = hp
        self.resistencia = resistencia
        self.xp = xp
        self.vidas = vidas

    def gameOver(self):
        print('Game over')

# Para crear una instancia de 'Ninja', es obligatorio proporcionar todos los argumentos definidos en __init__.
ninjaPrincipal = Ninja(100, 50, 1, 3)

# La siguiente línea, si se descomenta, provocaría un error (TypeError) porque faltan los argumentos.
# ninjaEnemigo = Ninja()

# También se pueden agregar atributos a una instancia después de su creación.
# Esto es flexible, pero no garantiza que todos los objetos de la clase tengan los mismos atributos.
ninjaPrincipal.salto = True

print(f"HP del ninja principal: {ninjaPrincipal.hp}")
print(f"¿El ninja principal puede saltar? {ninjaPrincipal.salto}")