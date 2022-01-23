# test_01.py
''' VERSIÓN DE LA IMPLEMENTACIÓN 
Ejemplo para el curso de programación en python
por Ing. Giancarlo Ortiz. '''
# Operaciones con cadenas en python 3
""" En programación, Las obras o aplicaciones de software 
tienen operaciones con cadenas.
El versionado de software es el proceso de asignación de un nombre, 
código o número único, a un software para indicar su nivel de desarrollo

Python usa la codificación Unicode en lugar de ASCII.
Lo que hace posibles mas de 100.000 Caracteres.
Type("x") → <class 'str'> → cadena Unicode. """

# Importando funcionalidad al script 
import sys

# Asignaciones y operaciones con cadenas
info = sys.version
version = info.split(" ")[0]
plataforma = info[info.find("[")+1:len(info)-1]

# Salida estándar
print("---------------------------------------")
print(f"la instalación de Python {version} fue exitosa")
print(f"Tu plataforma elegida es {plataforma}...")
print(f"buena suerte como pythonista", "...")
print("---------------------------------------")
