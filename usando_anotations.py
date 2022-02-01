"""
Anotations
"""

import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


# print(circunferencia.__annotations__)
# nome: str = "Gustavo"
# peso: float = 73.5
# ativo: bool = True
# print(nome)
# print(peso)
# print(ativo)

class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.peso: float = peso

    def andar(self) -> str:
        return f"{self.__nome} está andando!"

