"""
Polimorfismo. Objetos de muitas formas ou se comportar de multiplas formas

Usamos o exemplo de animal, pois cada animal fala, porem são falas distintas
Uns latem outros mia e outras berrar.

Implementamos os métodos falar, pois cada fala de forma diferente mesmo sendo animal

Acontecendo o overridden ou subscrita de método.

"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def get_nome(self):
        return self.__nome

    def falar(self):
        raise NotImplementedError("A sub classe precisa ser implementada este método")

    def comer(self):
        print(f"{self.__nome} está comendo.")


class Cachorro(Animal):

    def __init__(self, nome):
        super(Cachorro, self).__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala au au!")


class Gato(Animal):

    def __init__(self, nome):
        super(Gato, self).__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala miau miau!")


class Boi(Animal):

    def __init__(self, nome):
        super(Boi, self).__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala mu mu!")


felix = Gato("felix")
felix.comer()
felix.falar()

muthley = Cachorro("muthley")
muthley.comer()
muthley.falar()

thor = Boi("thor")
thor.comer()
thor.falar()

