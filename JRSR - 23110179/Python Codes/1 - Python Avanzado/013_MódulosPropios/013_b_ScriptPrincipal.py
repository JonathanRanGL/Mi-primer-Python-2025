# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Script que Importa un Módulo Propio ---

# Se importa el módulo que acabamos de crear (el archivo '013_a_MiModuloDeCalculos.py').
import a_MiModuloDeCalculos as calculos

# Accedemos y utilizamos las funciones del módulo.
resultadoSuma = calculos.sumar(10, 22)
resultadoResta = calculos.restar(50, 20)

# Imprimimos los resultados en la consola.
print(f"El resultado de la suma es: {resultadoSuma}")
print(f"El resultado de la resta es: {resultadoResta}")
print(f"El valor de PI en mi módulo es: {calculos.PI}")