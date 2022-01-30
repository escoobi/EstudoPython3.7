"""
super
"""


class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    @property
    def nome(self):
        return self.__nome

    @property
    def especie(self):
        return self.__especie

    def faz_som(self, som):
        return f"O {self.__nome} faz: {som}"


class Gato(Animal):
    def __init__(self, nome, especie, raca):

        # Animal.__init__(self, nome, especie) # Ou pode herdar assim
        super(Gato, self).__init__(nome, especie)
        self.__raca = raca

    @property
    def raca(self):
        return self.__raca


felix = Gato("Felix", "Felino", "Angorá")
print(felix.faz_som("miau!!!!"))