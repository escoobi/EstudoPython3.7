"""
Herança Multipla

# Exemplo multiderivação direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Multiderivada(Base1, Base2, Base3):
    pass

# Exemplo multiderivação indireta


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiinderivada(Base3):
    pass




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


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super(Pinguim, self).__init__(nome)


baleia = Aquatico("Dolli")
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre("Jaum")
print(tatu.andar())
print(tatu.cumprimentar())

fronze = Pinguim("Teba")
print(fronze.andar())
print(fronze.nadar())
print(fronze.cumprimentar()) # ??? Method Resolution Order