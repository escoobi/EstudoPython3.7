"""
Pickle


# Escrevendo arquivo pickle - Binario


felix = Gato("felix")
muthley = Cachorro("muthley")

with open("animal.pickle", "wb") as arquivo:
    pickle.dump((felix, muthley), arquivo)

"""
import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f"{self.nome} está comendo!")


class Gato(Animal):

    def __init__(self, nome):
        super(Gato, self).__init__(nome)

    def mia(self):
        print(f"{self.nome} miau miau")


class Cachorro(Animal):

    def __init__(self, nome):
        super(Cachorro, self).__init__(nome)

    def late(self):
        print(f"{self.nome} au au au")

# Faznedo a leitura


with open("animal.pickle", "rb") as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f"O gato se chama {gato.nome}")
    gato.mia()
    print(f"O cachorro se chama {cachorro.nome}")
    cachorro.late()

