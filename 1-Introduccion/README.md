# Programación
<p><code>Introducción a la programación con Python</code></p>
<p>Creado por <code>Giancarlo Ortiz</code> para explicar los fundamentos de la <code>programación</code></p>


---
## Plataforma Digital
Una plataforma digital ó [hardware](https://es.wikipedia.org/wiki/Hardware) necesita ser programada para proporcionar funcionalidad, estos programas ó [software](https://es.wikipedia.org/wiki/Software) son una secuencia ordenada de instrucciones que se ejecutan en el sistema proporcionando los resultados deseados.

* ><i>"Es indigno que hombres notables pierdan su tiempo como esclavos del cálculo cuando podrían dejar ese trabajo en manos de cualquiera si se usaran las máquinas."</i><br>
<cite style="display:block; text-align: right">[Gottfried Leibniz](https://es.wikipedia.org/wiki/Gottfried_Leibniz)</cite>


---
### Lenguaje de programación
* Permite describir soluciones de software o [programas](https://es.wikipedia.org/wiki/Programa_inform%C3%A1tico).
* Esta definido por un conjunto de reglas o [gramática](https://es.wikipedia.org/wiki/Gram%C3%A1tica).
* Debe traducirse a [código maquina](https://es.wikipedia.org/wiki/Lenguaje_de_m%C3%A1quina) por un compilador o un interprete.
* Se categorizan según su nivel de abstracción respecto de la plataforma o [arquitectura](https://es.wikipedia.org/wiki/Arquitectura_de_computadoras).
* Incluye herramientas de multiples [paradigmas de programación](https://es.wikipedia.org/wiki/Paradigma_de_programaci%C3%B3n).
* Pequeñas variaciones del lenguaje se conocen como [dialectos](https://es.wikipedia.org/wiki/Dialecto).
* Si permite una [maquina lógica universal](https://es.wikipedia.org/wiki/M%C3%A1quina_de_Turing_universal) se denomina Turing completo.


---
### Comparativa
Las implementaciones del lenguaje son paquetes de software que siguiendo su gramática, compilan o interpretan los programas en instrucciones que las arquitecturas de hardware puedan procesar.

| # | Compilador | Interprete |
|:---:|---|---|
| 1 | Para distribuir | Para prototipos |
| 2 | Lee todo el programa | Lee parcialmente el programa|
| 3 | Mejor manejo de errores | Interacción en tiempo Ejecución |
| 4 | Ejecución mas rápida | Menor consumo de memoria |


---
### Entorno de trabajo
Las herramientas de software que se usan para programar se consideran el entorno de desarrollo, que pueden soportar multiples lenguajes de programación y pueden incluir:
* Un [editor de código fuente](https://es.wikipedia.org/wiki/Editor_de_c%C3%B3digo_fuente) con opciones de resaltado y corrección de sintaxis, refactorización de código y herramientas de auto-completado inteligente o [IntelliSense](https://es.wikipedia.org/wiki/IntelliSense).
* Un [depurador](https://es.wikipedia.org/wiki/Depurador) que nos permite simular e inspeccionar en un entorno seguro la ejecución parcial y paso a paso de un conjunto de instrucciones o [programa](https://es.wikipedia.org/wiki/Programa_inform%C3%A1tico). 
* Es posibble que algunos entornos integren herramientas de [programación visual](https://es.wikipedia.org/wiki/Programaci%C3%B3n_visual).


---
### Modelos de licenciamiento de software 
* [**Software propietario:**](https://es.wikipedia.org/wiki/Software_libre) modelo de licenciamiento de software que se reserva los derechos patrimoniales, comerciales o de utilización de una aplicación informática.
    * **Ejemplos:** [Windows 11](https://es.wikipedia.org/wiki/Windows_11), [Microsoft Office](https://es.wikipedia.org/wiki/Microsoft_Office)
* [**Software libre:**](https://es.wikipedia.org/wiki/Software_libre) un conjunto de modelos de desarrollo que libera los derechos de utilización.
    * **Ejemplos:** [KDE neon](https://es.wikipedia.org/wiki/KDE_neon), [Calligra Suite](https://es.wikipedia.org/wiki/Calligra_Suite) 


---
### Licencias de código
* [**Copyright:**](https://es.wikipedia.org/wiki/Derecho_de_autor) licencias de software que se reservan los derechos patrimoniales y otorgan derechos de utilización bajo distintos modelos comerciales.
* [**Copyleft:**](https://es.wikipedia.org/wiki/Copyleft) licencias de software relacionadas con mantener libres los derechos patrimoniales y de utilización.
* [**Código abierto:**](https://es.wikipedia.org/wiki/Licencia_de_c%C3%B3digo_abierto) licencias que permiten que tanto el código fuente como los archivos binarios del software sean modificados y redistribuidos libremente favoreciendo la colaboración abierta.
* [**Dominio público:**](https://es.wikipedia.org/wiki/Dominio_p%C3%BAblico) obras y aplicaciones informáticas  que no tienen derechos exclusivos de autor, pertenecen a todos.
![img](img/licenses.png)


---
### Control de versiones
* Para la gestión de los diversos cambios que se realizan en una aplicación informática se asigna continuamente un [**código**](https://es.wikipedia.org/wiki/Versionado_de_software) indicando su nivel de desarrollo.
* Aunque el control de versiones puede realizarse de forma manual, existen los [**VCS**](https://es.wikipedia.org/wiki/Control_de_versiones) sistemas de control de versiones como [**GIT**](https://es.wikipedia.org/wiki/Git) que facilitan esta gestión de código.
* Adicionalmente existen servicios de alojamiento de código como [**GitHub**](https://es.wikipedia.org/wiki/GitHub) que facilitan esta gestión de código y el desarrollo colaborativo.


---
## Python
Es un lenguaje de programación de código abierto [**PSFL**](https://es.wikipedia.org/wiki/Python_Software_Foundation_License), interpretado, multiparadigma y multiplataforma cuya filosofía hace hincapié en la legibilidad de su código.

* ><i>"Python es un experimento sobre cuánta libertad necesitan los programadores. Demasiada libertad y nadie puede leer el código de otro; poca libertad y la expresividad estará en peligro."</i><br>
<cite style="display:block; text-align: right">[Guido van Rossum](https://es.wikipedia.org/wiki/Guido_van_Rossum)</cite>


---
## Implementaciones de Python
* [CPython][11] es la implementación oficial escrita en lenguaje C, su código fuente y binarios para multiples plataformas están disponibles en el sitio web oficial.
* Se puede mencionar implementaciones que extienden compatibilidad del lenguaje con la maquina virtual de Java o [.Net][12].
* Existen implementaciones como [PyPy][13] optimizadas para JIT.
* Incluso existen herramientas como [RPython][14] para construir un interprete personalizado.

[11]: https://es.wikipedia.org/wiki/CPython
[12]: https://ironpython.net/
[13]: https://es.wikipedia.org/wiki/PyPy
[14]: https://rpython.readthedocs.io/en/latest/


---
## Versiones de Python
* Python 2 - [Python 2.7.18][21]
* Python 3 - [Python 3.9.10][22] (Recomendado)
* Python 3 - [Python 3.10.2][23]
* Python 3 - [Código fuente][24]
* Python 3 - [Repositorio][25]

[21]: https://www.python.org/ftp/python/2.7.18/python-2.7.18.amd64.msi
[22]: https://www.python.org/ftp/python/3.9.10/python-3.9.10-amd64.exe
[23]: https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe
[24]: https://www.python.org/downloads/source/
[25]: https://github.com/python/cpython


---
## Instalación Básica de Python + VSCode
1. Elige una implementación y version estable del interprete de [**Python**][31].
1. Instala una implementación o interprete de [**Python**][32] del sitio web oficial.
1. Instala el editor [**Visual studio code**][33] del sitio web oficial.
1. Instala la extensión oficial de [**Microsoft para Python**][34] en VSCode.
1. Instala la extensión oficial de [**Github**][35] para VSCode.
1. Explorar otras extensiones en el [**Marketplace**][36] para VSCode.
1. Actualizar el administrador de paquetes [**pip**][37] de Python.

[31]: https://www.python.org/downloads/
[32]: https://www.python.org/downloads/
[33]: https://code.visualstudio.com/download
[34]: https://marketplace.visualstudio.com/items?itemName=ms-python.python
[35]: https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github
[36]: https://marketplace.visualstudio.com/
[37]: https://es.wikipedia.org/wiki/Pip_(administrador_de_paquetes)


---
## Mas Recursos
- [Lenguaje de programación](https://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n) (Wikipedia)
- [Compilador](https://es.wikipedia.org/wiki/Compilador) (Wikipedia)
- [Intérprete](https://es.wikipedia.org/wiki/Int%C3%A9rprete_(inform%C3%A1tica)) (Wikipedia)
- [Compilación en tiempo de ejecución](https://es.wikipedia.org/wiki/Compilaci%C3%B3n_en_tiempo_de_ejecuci%C3%B3n) (Wikipedia)