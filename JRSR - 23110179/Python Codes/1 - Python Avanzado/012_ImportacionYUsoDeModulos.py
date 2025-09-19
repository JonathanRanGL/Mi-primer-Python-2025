# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Guía de Importación y Uso de Módulos ---

# --- Método 1: Importar el módulo completo ---
# Se importa todo el módulo 'random'. Para usar sus funciones, se necesita el prefijo 'random.'.
import random
numeroAleatorio = random.randint(1, 10)
print(f"Método 1: Número aleatorio completo: {numeroAleatorio}")


# --- Método 2: Importar un elemento específico ---
# Se importa solo la función 'randint' del módulo 'random'. No se necesita prefijo.
from random import randint
numeroEspecifico = randint(11, 20)
print(f"Método 2: Número aleatorio específico: {numeroEspecifico}")


# --- Método 3: Importar varios elementos específicos ---
from random import choice, shuffle
opciones = ['piedra', 'papel', 'tijera']
opcionElegida = choice(opciones)
print(f"Método 3: Elemento elegido: {opcionElegida}")


# --- Método 4: Usar un alias para el módulo ---
# Se importa el módulo completo pero se le asigna un nombre más corto (alias) para comodidad.
import random as rd
lista = [1, 2, 3, 4, 5]
rd.shuffle(lista) # Usamos el alias 'rd'
print(f"Método 4: Lista desordenada con alias: {lista}")


# --- Método 5: Importar todo (NO RECOMENDADO) ---
# 'from random import *' importa todos los nombres del módulo al espacio de nombres actual.
# Es una mala práctica porque puede generar conflictos de nombres y hace el código menos legible.
# from random import *
# numeroDirecto = uniform(1.0, 2.0)
# print(f"Método 5: {numeroDirecto}")