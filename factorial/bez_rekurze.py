def factorial(n):
    if n == 0:
        return 1

    vysledek = n
    while n > 1:
        n -= 1
        vysledek *= n
    return vysledek
