#!/usr/bin/python3
import sys

# Descripción de la función: 
# Calcula el factorial de un número de manera recursiva.

# Parámetros:
# - n: El número del cual se desea calcular el factorial. Se espera un número entero.

# Retorno:
# - Devuelve el factorial de n. Si n es 0, devuelve 1. Si n es mayor que 0, devuelve n * factorial(n-1).
def factorial(n):
    if n == 0:  # Caso base, el factorial de 0 es 1
        return 1
    else:
        return n * factorial(n-1)  # Llamada recursiva

if __name__ == "__main__":
    # Verificamos si se pasó un argumento
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)

    try:
        # Convertimos el argumento a un número entero
        num = int(sys.argv[1])
        # Verificamos si el número es negativo
        if num < 0:
            print("Error: The number must be non-negative.")
            sys.exit(1)
    except ValueError:
        # Si el argumento no es un número entero, mostramos un mensaje de error
        print("Error: Please provide a valid integer.")
        sys.exit(1)

    # Calculamos el factorial
    f = factorial(num)
    print(f)
