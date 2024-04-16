"""
Autor: Luis Pérez Cantarero

Este programa suma 2 números y devuelve el resultado.
"""
def suma(a, b):
    resultado = a + b
    return resultado

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = suma(num1, num2)
print("La suma es: ", resultado)
