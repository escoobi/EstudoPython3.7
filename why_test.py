"""
Por que testar códigos
    Reduzir bugs
    Novos recursos da app não crach os antigos
    Garantir bugs que corrigidos continua OK
    Garantir refatoração não apresenta novos bugs

Teste automatizados
Desenvolvimento guiado por teste - TDD
"""


class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def mia(self):
        return f"O gato {self.nome} faz miau miau!"


felix = Gato("Felix")
print(felix.mia())
print(felix.nome)
