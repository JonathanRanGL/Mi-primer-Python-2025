# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179
# Script: Los Comentarios en Python
# Descripción: Ejemplos de diferentes tipos de comentarios y su uso en Python

# Ejemplo 1: Comentario de línea simple
# Los comentarios de línea simple comienzan con el símbolo #
print("¡Hola mundo!")

# Ejemplo 2: Comentario para desactivar código
# print("Esta línea no se ejecutará")  # Esta línea está comentada
print("Esta línea se ejecutará")

print()  # Línea en blanco para separar secciones

# Ejemplo 3: Función con comentarios organizacionales
def funcionLarga():
    """
    Función de ejemplo que demuestra el uso de comentarios
    para organizar secciones de código
    """
    # Primera sección
    # Esta sección realiza la inicialización
    pass
    
    # Segunda sección  
    # Esta sección procesa los datos
    pass
    
    # Tercera sección
    # Esta sección genera los resultados
    pass

# Ejemplo 4: Comentarios al final de línea
print("Línea 1.")
print("Línea 2.")  # Comentario al final de la línea
print("Línea 3.")

# Ejemplo 5: Comentario que desactiva una línea completa
print("Línea 1.")
# print("Línea 2.")  # Esta línea está completamente comentada
print("Línea 3.")

# Ejemplo 6: Bucle con comentario descriptivo
# Bucle que itera en sentido decreciente desde 10 hasta 1
for i in range(10, 0, -1):
    print(i)

# Ejemplo 7: Comentario explicativo detallado
# La función print() imprime un mensaje en la consola
# En este caso, imprime el texto "hola"
print("hola")

print()  # Separador visual

# Ejemplo 8: Comentarios multilínea con comillas triples
"""
Este es un comentario multilínea usando comillas dobles.
Permite escribir explicaciones extensas que abarcan
múltiples líneas de texto.
Útil para documentación detallada.
"""

'''
Este es un comentario multilínea usando comillas simples.
También permite escribir explicaciones extensas
en múltiples líneas.
Ambos formatos son válidos en Python.
'''

# Ejemplo 9: Código activo y código comentado
# Este código imprime los números del 1 al 10
for i in range(1, 11):
    print(i)

"""
Código comentado que no se ejecuta:
for i in range(10, 0, -1):
    print(i)
"""

# Ejemplo 10: Docstrings para documentación
"""Docstring del módulo - describe el propósito del archivo"""

class ClaseEjemplo:
    """Docstring de la clase - describe el propósito de la clase"""
    
    def metodoEjemplo(self):
        """Docstring del método - describe qué hace el método"""
        pass

def funcionEjemplo():
    """Docstring de la función - describe qué hace la función"""
    pass

print("Fin del script de comentarios en Python")
