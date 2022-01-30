"""
Propriedades


# Como no java... mas em python a pegada é outra

"""


class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__conta = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    # As propriedades semprem vem primeiro que os métodos, para melhor visualização dos objetos
    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, novo_limite):
        self.__limite = novo_limite

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @property
    def saldo(self):
        return self.__saldo

    def extrato(self):
        return f"Valor extrato: {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor informado não pode ser menor ou = 0")

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print("Saldo insulficiente")
        else:
            print("Valor informado não pode ser menor ou = 0")

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def soma_saldo_total(self):
        return self.__saldo + self.__limite


conta01 = Conta("Gustavo", 500, 1000)
conta02 = Conta("Patricia", 500, 1000)


print(conta01.extrato())
print(conta02.extrato())


soma = conta01.saldo + conta02.saldo
print(f"O valor da soma das duas contas é: {soma}")

# print(conta01.__dict__)
# conta01.conta = 89
# print(conta01.__dict__)

print(conta01.soma_saldo_total())