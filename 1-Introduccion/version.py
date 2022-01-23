# -*- coding: utf-8 -*-
''' VERSIÓN DE LA IMPLEMENTACIÓN 
Ejemplo para el curso de programación en python
por Ing. Giancarlo Ortiz. '''
# Control de versiones
""" En programación, Las obras o aplicaciones de software 
tienen un nombre código o número único, a un software 
para indicar su nivel de desarrollo. """

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
