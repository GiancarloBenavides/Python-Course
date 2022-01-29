# Hackerrank challenges
''' Task
You are given a polynomial P of a single indeterminate (or variable x).
You are also given the values of x and k.
Your task is to verify if P(x)=k. '''

# División
'''Tarea
Te dan un polinomio P de un solo indeterminado (o variable x).
También se le dan los valores de x y k.
Tu tarea es verificar si P(x)=k. '''

# Solution
if __name__ == '__main__':
    x, k = input().split(" ")
    equation = input().replace("x", x)
    print(eval(equation)==int(k))

