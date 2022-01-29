# Programación
<p><code>Introducción a la programación con Python</code></p>
<p>Creado por <code>Giancarlo Ortiz</code> para explicar los fundamentos de la <code>programación</code></p>

---
## Operadores y Operaciones 
Los operadores son elementos gramaticales o símbolos reservados por el propio lenguaje de programación que se utilizan para obtener resultados desde otros objetos definidos, mediante la ejecución de una o varias operaciones definidas para un tipo de dato.

* ><i>"Duda de los datos... Hasta que los datos no dejen lugar a dudas."</i><br>
<cite style="display:block; text-align: right">[Henri Poincaré](https://es.wikipedia.org/wiki/Henri_Poincar%C3%A9)</cite>


---
## </> Asignación
la operación mas básica suele ser la asignación de un valor literal a la variable.

```Python
# Asignación de un tipos
''' lógico, entero, float, complejo, lista y cadena. '''
booleano = True
numero_entero = 15
numero_real = 15.2
numero_complejo = 1j
lista = [1, 2, 3]
tupla = (1, 2)
cadena = "Hola mundo"
```


---
## </> Asignación multiple
En algunos lenguajes es posible inicializar varias variables en la misma instrucción.
```Python
a, b, c = 1, 2, 3   # asignación multiple de 3 variables
d = 1, 2, 3         # asignación de una tupla literal a una variable
```


## </> Construcción y Conversión de tipos
---
* Un constructor es una [__subrutina__](https://es.wikipedia.org/wiki/Subrutina) o método cuya misión es iniciar un objeto.
* A cada tipo de dato le corresponde un constructor.
* El proceso incluye la operación de asignación de un valor inicial a la variable.
* Es posible que el constructor sea el camino para hacer [**_type casting_**](https://es.wikipedia.org/wiki/Conversi%C3%B3n_de_tipos) o conversion de un tipo a otro.

```Python
numero_entero = int("15.2") # conversion de cadena a entero y asignación
```


---
## </> Constructores en Python
Python reserva una palabra para los constructores de cada uno de los 14 tipos de datos.

```Python
# Ejemplos:
booleano = bool(1) # True
numero_entero = int(15)
tupla_vacia = tuple()
lista = list(range(1, 5)) # [1, 2, 3, 4]
numero_flotante = float("15.2")
```


## Operaciones incluidas 
* Cada tipo de dato tiene definidas operaciones por defecto entre sus elementos u objetos.
* Algunos lenguajes permiten reemplazar el comportamiento por defecto.
* Las operaciones definidas se realizan sobre uno, dos o más objetos y tipos de datos.


---
## Mas Recursos
- [Arboles](https://es.wikipedia.org/wiki/%C3%81rbol_(inform%C3%A1tica)) (Wikipedia)
- [Pilas](https://es.wikipedia.org/wiki/Pila_(inform%C3%A1tica)) (Wikipedia)
- [Colas](https://es.wikipedia.org/wiki/Cola_(inform%C3%A1tica)) (Wikipedia)
- [Grafos](https://es.wikipedia.org/wiki/Grafo_(tipo_de_dato_abstracto)) (Wikipedia)