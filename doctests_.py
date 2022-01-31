"""
Doctests

São teste que colocamos dentros das docstring das funções/métodos

python -m doctest -v nome_app.py

"""


def soma(a, b):
    """Essa função soma os paramentros a e b

    >>> soma(1, 2)
    3

    """
    return a + b


# Exemplo usando TDD

def duplica_valor(valores):
    """Duplica valores em uma lista
    >>> duplica_valor([1, 2, 3, 4])
    [2, 4, 6, 8]
    """
    return [2 * elemento for elemento in valores]


# Erro inesperato

def fala_oi():
    """Fala oi
    >>> fala_oi()
    'oi'
    """
    return "oi"


def verdade():
    """Retornar verdade
    >>> verdade()
    True
    """
    return True

