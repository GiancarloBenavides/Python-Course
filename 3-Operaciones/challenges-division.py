# Hackerrank challenges
''' Task
The provided code stub reads two integers a,b from STDIN:
Add logic to print two lines. 
* The first line should contain the result of integer division,  // . 
* The second line should contain the result of float division,  / .
* No rounding or formatting is necessary. '''

# División
''' Tarea
El código auxiliar proporcionado lee dos números enteros a,b de STDIN:
Agregar lógica para imprimir dos líneas. 
* La primera línea debe contener el resultado de la división de enteros, // .
* La segunda línea debe contener el resultado de la división flotante, / .
* No es necesario redondear ni formatear. '''

# Solution
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)