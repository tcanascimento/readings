from math import pi


def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("Deve ser um número inteiro positivo")
    if r < 0:
        raise ValueError("O raio não pode ser negativo (ò.ó)")
    return pi * (r ** 2)
