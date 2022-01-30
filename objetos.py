"""
Objetos


# Instancia classe lampada

lamp1 = Lampada("branco", 110, 60)
lamp1.ligar_desligar()
print(f"A lampada esta ligada: {lamp1.check_lampada()}")

cc1 = ContaCorrente(500, 1500)

user1 = Usuario("Gustavo", "Oliveira Cardozo", "gustavo@gmail.com", "123456")


"""


class Lampada:
    def __init__(self, cor, luminosidade, voltagem):
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__voltagem = voltagem
        self.__ligada = False

    def check_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f"O Cliente {self.__nome} diz oi!")


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__limite = limite
        self.__numero = ContaCorrente.contador + 1
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f"O Cliente é: {self.__cliente._Cliente__nome}")


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


cl1 = Cliente("Gustavo", "810.666.432-53")
cc = ContaCorrente(5000, 1500, cl1)
cc.mostra_cliente()
# Acessei de forma incorreta o nome do cliente atraves da classe conta corrente!
cc._ContaCorrente__cliente.diz()

