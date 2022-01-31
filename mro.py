"""
MRO - Method Resolution Order
Resolução de ordem de métodos
Quem será execultado primeiro?
A ordem é sempre de baixo para cima...
podemos ver a sequência atraves do comando help(Pinguim)
"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def cumprimentar(self):
        return f"Eu sou {self.__nome}"


class Aquatico(Animal):
    def __init__(self, nome):
        super(Aquatico, self).__init__(nome)

    def nadar(self):
        return f"Aninamel {self._Animal__nome} esta nadando"

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} do mar!"


class Terrestre(Animal):
    def __init__(self, nome):
        super(Terrestre, self).__init__(nome)

    def andar(self):
        return f"Animal {self._Animal__nome} esta andando!"

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} da terra!"


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super(Pinguim, self).__init__(nome)


fronze = Pinguim("Teba")
print(fronze.cumprimentar()) # ??? Method Resolution Order