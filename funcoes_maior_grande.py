"""
HOF - Higher order Functions


# Exemplo de definição


def soma(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def mult(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(a, b, funcao):
    return funcao(a, b)

# Vamos testar o uso dos HOF


print(calcular(4, 3, soma))
print(calcular(4, 3, subtrair))
print(calcular(4, 3, mult))
print(calcular(4, 3, dividir))



# Funções aninhadas --- função dentro de outra função

from random import choice


def comprimentar(pessoa):
    def humor():
        return choice(("E ai!", "Sai daqui", "Fica ai, vc é fera!")) # choice usado para selecionar um iten na tupla aleatoriamente
    return humor() + pessoa


print(comprimentar(" Gustavo"))


# Retornando função de outra função

from random import choice


def sorrir():
    def rir():
        return choice(("kkkkk", "hahahahaha", "uaheuhaeuheuahuae", "hashahhshashahshah"))
    return rir()


rindo = sorrir()
print(rindo)

"""
from random import choice


def sorrir_again(pessoa):
    def iniciar_sorriso():
        r = choice(("hahahahha", "kkkkkkkk", "uahsuahsuhashasuhu"))
        return f"{r} {pessoa}"
    return iniciar_sorriso()


testando = sorrir_again("Gustavo")
print(testando)
print(sorrir_again("Gustavo"))
print(testando)
