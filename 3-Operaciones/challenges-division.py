# Hackerrank challenges
''' Task
The provided code stub reads two integers a,b from STDIN:
Add logic to print two lines; No rounding or formatting is necessary: 
* The first line should contain the result of integer division,  // . 
* The second line should contain the result of float division,  / '''

# División
''' Tarea
El código auxiliar proporcionado lee dos números enteros a,b de STDIN:
Agregar lógica para imprimir dos líneas; No es necesario redondear ni formatear:
* La primera línea debe contener el resultado de la división de enteros, // .
* La segunda línea debe contener el resultado de la división flotante, / '''

# Solution
if __name__ == '__main__':
    a = int(input("Number a:"))
    b = int(input("Number b:"))
    print(a//b)
    print(a/b)