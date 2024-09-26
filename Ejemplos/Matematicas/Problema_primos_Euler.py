
#  Problema de Euler. Cúal es el mayor factor primo de un número dado.
#
# Ejemplo: de 13195 sus factores primos son: 5, 7, 13 y 29
#          para 10, el mayor factor primo es 5. Para 17, es 17.



def solucion(n: int = 600851475143) -> int:
    """Devuelve el mayor factor primo del numero n dado.
    >>> solucion(13195)
    29
    >>> solucion(10)
    5
    >>> solucion(17)
    17
    >>> solucion(3.4)
    3
    >>> solucion(0)
    Traceback (most recent call last):
        ...
    ValueError: Parámetro n debe ser mayor que cero.
    >>> solucion(-17)
    Traceback (most recent call last):
        ...
    ValueError: Parámetro n debe ser mayor que cero.
    >>> solucion([])
    Traceback (most recent call last):
        ...
    TypeError: Parámetro n debe ser entero.
    >>> solucion("asd")
    Traceback (most recent call last):
        ...
    TypeError: Parámetro n debe ser entero.
    """
    #  Verificamos que el número de entrada es numérico y mayor que cero
    try:
        n = int(n)
    except (TypeError, ValueError):
        raise TypeError("Parámetro n debe ser entero.")
    if n <= 0:
        raise ValueError("Parámetro n debe ser mayor que cero.")

    i = 2
    ans = 0

    if n == 2:
        return 2

    while n > 2:
        while n % i != 0:
            i += 1

        ans = i

        while n % i == 0:
            n = n / i

        i += 1

    return int(ans)



if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(solucion(int(input("Vamos a calcular el mayor factor primo del número que indiques: ").strip())))