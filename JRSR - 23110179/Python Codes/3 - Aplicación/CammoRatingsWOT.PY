# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

def obtener_dato_numerico(mensaje_prompt):
    """
    Solicita un dato numérico al usuario y lo valida.
    Vuelve a pedir el dato hasta que se ingrese un número válido.
    """
    while True:
        try:
            dato = float(input(mensaje_prompt))
            return dato
        except ValueError:
            print("Error: Por favor, introduce un valor numérico válido.")

def calcular_y_mostrar_tabla(nombre_tanque, camo_estacionario, camo_al_disparar, rango_vision_enemigo):
    """
    Calcula las distancias de detección y muestra los resultados en una tabla formateada.
    """
    # Límites fijos del juego en metros
    MAX_SPOTTING_RANGE = 445.0
    MIN_SPOTTING_RANGE = 50.0

    # Escenarios de cobertura
    escenarios = {
        "Campo Abierto": 0.0,
        "Arbusto 25%": 0.25,
        "Arbusto 50%": 0.50,
        "Arbusto 80%": 0.80
    }

    # Convertimos los porcentajes de camuflaje a factores decimales
    factor_camo_estacionario = camo_estacionario / 100.0
    factor_camo_al_disparar = camo_al_disparar / 100.0
    
    # Listas para almacenar los resultados calculados
    distancias_estacionario = []
    distancias_al_disparar = []

    # Calculamos las distancias para el estado ESTACIONARIO
    for bono_arbusto in escenarios.values():
        factor_total = factor_camo_estacionario + bono_arbusto
        distancia = rango_vision_enemigo - (rango_vision_enemigo - MIN_SPOTTING_RANGE) * factor_total
        distancia_final = min(MAX_SPOTTING_RANGE, max(MIN_SPOTTING_RANGE, distancia))
        distancias_estacionario.append(f"{distancia_final:.2f}m")
        
    # Calculamos las distancias para el estado AL DISPARAR
    for bono_arbusto in escenarios.values():
        factor_total = factor_camo_al_disparar + bono_arbusto
        distancia = rango_vision_enemigo - (rango_vision_enemigo - MIN_SPOTTING_RANGE) * factor_total
        distancia_final = min(MAX_SPOTTING_RANGE, max(MIN_SPOTTING_RANGE, distancia))
        distancias_al_disparar.append(f"{distancia_final:.2f}m")

    # --- IMPRESIÓN DE LA TABLA DE RESULTADOS ---
    print("\n" + "="*85)
    print(f"--- Tabla de Detección para el Tanque: {nombre_tanque.upper()} ---")
    print(f"--- Simulado contra un enemigo con {rango_vision_enemigo} m de visión ---")
    print("="*85)
    
    # Encabezados de la tabla
    headers = ["Estado", *escenarios.keys()]
    print(f"{headers[0]:<15} | {headers[1]:<15} | {headers[2]:<15} | {headers[3]:<15} | {headers[4]:<15}")
    print("-"*85)
    
    # Fila de datos para ESTACIONARIO
    print(f"{'Estacionario':<15} | {distancias_estacionario[0]:<15} | {distancias_estacionario[1]:<15} | {distancias_estacionario[2]:<15} | {distancias_estacionario[3]:<15}")
    
    # Fila de datos para AL DISPARAR
    print(f"{'Al Disparar':<15} | {distancias_al_disparar[0]:<15} | {distancias_al_disparar[1]:<15} | {distancias_al_disparar[2]:<15} | {distancias_al_disparar[3]:<15}")
    print("="*85)

def main():
    """
    Función principal que solicita los datos al usuario y ejecuta el cálculo.
    """
    # --- ENTRADA DE DATOS DEL USUARIO ---
    nombre_tanque = input("Ingresar nombre del tanque: ")
    camo_estacionario = obtener_dato_numerico("Ingresar camuflaje en estacionario (%): ")
    camo_al_disparar = obtener_dato_numerico("Ingresar camuflaje después de disparar (%): ")
    rango_vision_enemigo = obtener_dato_numerico("Ingresar rango de visión del enemigo (en metros): ")

    # Llamamos a la función que calcula y muestra la tabla
    calcular_y_mostrar_tabla(nombre_tanque, camo_estacionario, camo_al_disparar, rango_vision_enemigo)

if __name__ == "__main__":
    main()