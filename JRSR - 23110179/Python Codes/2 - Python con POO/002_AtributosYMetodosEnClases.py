# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Atributos y Métodos en Clases ---

class NinjaPrincipal:
    # Atributos de clase: Son compartidos por todas las instancias de la clase.
    hp = 100
    resistencia = 50
    xp = 1

    # Método de instancia: Una función que pertenece a la clase.
    # El primer parámetro 'self' se refiere a la instancia del objeto que llama al método.
    def gameOver(self):
        print('Game over')

# Se crea una instancia (objeto) de la clase NinjaPrincipal.
ninja = NinjaPrincipal()

# Se accede y se imprime el valor del atributo 'hp' del objeto 'ninja'.
print("HP inicial del ninja:", ninja.hp)

# Se modifica el valor del atributo 'hp' para esta instancia específica.
ninja.hp = 0
print("HP del ninja después del combate:", ninja.hp)


# Se comprueba una condición y se llama a un método del objeto.
if ninja.hp == 0:
    ninja.gameOver()