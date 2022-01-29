"""
Metadados
e
wraps


# Problema

def ver_log(funcao):
    def logas(*args, **kwargs):
        '''Eu sou uma função (loga) dentro de outra'''
        print(f"Este é o nome -> {funcao.__name__}")
        print(f"Esta é a documentação -> {funcao.__doc__}")
        return funcao(*args, **kwargs)
    return logas


@ver_log
def soma(a, b):
    '''Soma dois numeros'''
    return a + b


# print(soma(10, 30.5))


print(soma.__doc__)
print(soma.__name__)



"""


# Solução
from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logas(*args, **kwargs):
        """Eu sou uma função (loga) dentro de outra"""
        print(f"Este é o nome -> {funcao.__name__}")
        print(f"Esta é a documentação -> {funcao.__doc__}")
        return funcao(*args, **kwargs)
    return logas


@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b


# print(soma(10, 30.5))


print(soma.__doc__)
print(soma.__name__)


