"""
Herança
A ideia é aproveitar os codigos extendendo as classes

# Exemplo sem herança

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


cl01 = Cliente("Gustavo", "Oliveira Cardozo", "810.666.432-53", 3.300)
fu01 = Funcionario("Elaine", "Paganini", "111.111.111-89", 9999)

print(cl01.nome_completo())
print(fu01.nome_completo())


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

class Cliente(Pessoa):
    # Cliente recebe herança da classe Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        super(Cliente, self).__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):
    # Funcionario recebe herança da classe Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super(Funcionario, self).__init__(nome, sobrenome, cpf)
        self.__matricula = matricula




cl01 = Cliente("Gustavo", "Oliveira Cardozo", "810.666.432-53", 3.300)
fu01 = Funcionario("Elaine", "Paganini", "111.111.111-89", 9999)

print(cl01.nome_completo())
print(fu01.nome_completo())

"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

class Cliente(Pessoa):
    """Cliente recebe herança da classe Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super(Cliente, self).__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):
    """Funcionario recebe herança da classe Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super(Funcionario, self).__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f" Funcionario: {self.__matricula} Nome: {self._Pessoa__nome}"


cl01 = Cliente("Gustavo", "Oliveira Cardozo", "810.666.432-53", 3.300)
fu01 = Funcionario("Elaine", "Paganini", "111.111.111-89", 9999)

print(cl01.nome_completo())
print(fu01.nome_completo())