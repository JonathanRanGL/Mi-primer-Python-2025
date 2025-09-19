# Jonathan Rodrigo Sánchez Rangel - 6E - 23110179

# --- Guía de PIP y Entornos Virtuales ---

# Este archivo es una guía. Las siguientes líneas son comandos para la terminal, no código Python ejecutable.
# Puedes copiar y pegar estos comandos en tu terminal (CMD, PowerShell, Bash, etc.).

# -----------------------------------------------------
# 1. GESTIÓN DE PAQUETES CON PIP
# -----------------------------------------------------

# 'pip' es el gestor de paquetes de Python. Permite instalar librerías de terceros.

# Comando para instalar un paquete (ejemplo con 'requests', para hacer peticiones HTTP)
# >> pip install requests

# Comando para ver los paquetes instalados en tu entorno actual
# >> pip freeze

# Comando para desinstalar un paquete
# >> pip uninstall requests

# Comando para actualizar un paquete a su última versión
# >> pip install --upgrade requests

# -----------------------------------------------------
# 2. ENTORNOS VIRTUALES (VENV)
# -----------------------------------------------------

# Un entorno virtual es una carpeta que contiene una instalación de Python aislada del resto del sistema.
# Es una BUENA PRÁCTICA usar un entorno virtual para cada proyecto.

# Paso 1: Crear un entorno virtual.
# Navega a la carpeta de tu proyecto en la terminal y ejecuta:
# Se creará una carpeta llamada 'mi_entorno'.
# >> python -m venv mi_entorno

# Paso 2: Activar el entorno virtual.
# En Windows (CMD/PowerShell):
# >> mi_entorno\\Scripts\\activate
#
# En Linux/macOS:
# >> source mi_entorno/bin/activate

# Una vez activado, tu terminal mostrará el nombre del entorno, ej: (mi_entorno) C:\...

# Paso 3: Instalar paquetes dentro del entorno.
# Los paquetes que instales ahora solo existirán en este entorno.
# (mi_entorno) >> pip install numpy

# Paso 4: Trabajar en tu proyecto.
# ... aquí escribirías y ejecutarías tu código Python ...

# Paso 5: Desactivar el entorno virtual.
# Cuando termines de trabajar, simplemente ejecuta:
# (mi_entorno) >> deactivate

print("Este script es una guía. Ejecuta los comandos comentados en tu terminal.")