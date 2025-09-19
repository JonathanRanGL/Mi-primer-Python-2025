# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Guía para Trabajar con Fechas (Módulo datetime) ---

import datetime
import locale

# --- Crear objetos de tiempo (time) ---
horaEspecifica = datetime.time(14, 30, 20)
print(f"Hora creada: {horaEspecifica}")
print(f"Minutos: {horaEspecifica.minute}")

# --- Crear objetos de fecha (date) ---
fechaEspecifica = datetime.date(2027, 12, 20)
print(f"\nFecha creada: {fechaEspecifica}")
# Obtener la fecha actual
fechaHoy = datetime.date.today()
print(f"Fecha de hoy: {fechaHoy}")
print(f"Año actual: {fechaHoy.year}")

# --- Crear objetos de fecha y hora (datetime) ---
fechaYHoraActual = datetime.datetime.now()
print(f"\nFecha y hora actuales: {fechaYHoraActual}")

# --- Formatear fechas (strftime) ---
# strftime convierte un objeto datetime en una cadena de texto con un formato específico.
# %d: día, %B: mes completo, %Y: año, %H: hora (24h), %M: minutos.
formatoPersonalizado = fechaYHoraActual.strftime("%d de %B de %Y a las %H:%M")
print(f"Fecha formateada (inglés): {formatoPersonalizado}")

# Para formatear en español, es necesario configurar el 'locale'.
try:
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
    formatoEspanol = fechaYHoraActual.strftime("Hoy es %A, %d de %B de %Y").capitalize()
    print(f"Fecha formateada (español): {formatoEspanol}")
except locale.Error:
    print("Locale 'es_ES.UTF-8' no soportado en este sistema. Mostrando formato por defecto.")