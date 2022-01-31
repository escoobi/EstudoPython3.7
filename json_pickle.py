"""
Json e Pickle


import json

ret = json.dumps(["protudo", {"cerveja": ("2TB", "Novo", "220v", 1500)}])


print(type(ret))
print(ret)



import json


class Gato():
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato("Felix", "Vira-Lata")
ret = json.dumps(felix.__dict__)
print(ret)


import jsonpickle


class Gato():
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato("Felix", "Vira-Lata")
ret = jsonpickle.encode(felix)
print(ret)


# Escrevendo o arquivo JSON Pickle
import jsonpickle


class Gato():
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato("Felix", "Vira-Lata")

with open("felix.json", "w") as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

"""
# Lendo o arquivo JSON Pickle
import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


with open("felix.json", "r") as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret.nome)
    print(ret.raca)
