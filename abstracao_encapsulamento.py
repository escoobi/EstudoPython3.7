"""
Abstração e Encapsulamento



# Agora como privado essa etapa já não passa
print(conta01.titular)
print(conta01.saldo)
print(conta01.limite)

# Quando os atributos não estar privados dentro da classe... podemos acessar e alterar os valores deles.
# Exemplo:

# Agora como privado essa etapa já não passa
conta01.conta = "456"
conta01.titular = "Alguem"
conta01.limite = 0
conta01.saldo = 0

conta01.extrato()
print(conta01._Conta__titular) # Ainda acesso usando o Name Mangling. OBS: Python tem esse poder

# Alterar o nome do titular mesmo ele estando como private usando o Name Mangling
conta01._Conta__titular = "Barata"

print(conta01.__dict__)

# Vamos depositar!

conta01.depositar(5)

print(conta01.__dict__)

conta01.sacar(15)
print(conta01.__dict__)


"""


class Conta:
    contador = 4999

    def __init__(self, titular, saldo, limite):
        self.__conta = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f"O saldo da conta é: {self.__saldo} do titular {self.__titular} com limite {self.__limite}")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor igual ou inferior 0!")

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print("Saldo insulficiente!")
        else:
            print("Valor incorreto!")

    def transferencia(self, valor, conta_destino):
        # 1 remover o valor da conta de destino.
        self.__saldo -= valor

        # 2 adicionar o valor na conta de destino.
        conta_destino.__saldo += valor
conta01 = Conta("Gustavo", 500, 150)
conta01.extrato()
conta02 = Conta("Elaine", 1000, 1500)
conta02.extrato()


# Elaine transfere para Gustavo.
conta02.transferencia(50, conta01)

conta01.extrato()
conta02.extrato()