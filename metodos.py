"""
Orientação a Objetos, Metodos
Representa as ações dos objetos.

Metodos Instancia e Metodos da Classe


# Para poder acessar a classe precisamos instanciar ela

p1 = Produto("maça", "ortifrutes", 1.52)
print(p1.desconto(10))

# Instancia da classe Usuario
u1 = Usuario("Gustavo", "Oliveira Cardozo", "gustavo@gmail.com", "1234")
u2 = Usuario("Elaine", "Paganini", "elaine@gmail.com", "1234")
u3 = Usuario("Arthur", "Paganini Cardozo", "arthur@gmail.com", "1234")

print(u1.nome_completo())
print(u2.nome_completo())
print(u3.nome_completo())

print(f"Senha u1: {u1._Usuario__senha}") # Acesso ao atributo de forma errada

nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
email= input("email: ")
senha = input("senha: ")
re_senha = input("re-senha: ")

if senha == re_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print("Senha não confere!")
    exit(1)

print("Usuário criado com sucesso!")
senha = input("Informe a senha para acesso: ")
if user.chega_senha(senha):
    print("Acesso permitido!")
else:
    print("Senha incorreta!")

print(f"Sua senha criptografada: {user._Usuario__senha}") # Acesso os atributos de forma incorreta! Novamente rs.....

#Métodos de Classe

user = Usuario("Gustavo", "Oliveira Cardozo", "gustavo@gmail.com", "123456")

Usuario.conta_usuario() # Forma correta

user.conta_usuario() # Possivel mas incorreto

user = Usuario("Gustavo", "Oliveira Cardozo", "gustavo@email.com", "123456")

print(user._Usuario__gera_usuario()) # Acesso o metodo privado de forma incorreta

"""

from passlib.hash import pbkdf2_sha256 as cryp


# Metodos Instacia


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor: cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor da porcentagem com o desconto """
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:
    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f"Temos {cls.contador}  usuario no sistema!")

    @classmethod
    def imprimir_algo(cls):
        print("Imprimir algo")

    @staticmethod
    def definicao():
        return "uxcr333"

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f"Usuario criado: {self.__gera_usuario()}")


    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    """Metodo para verificar a senha"""
    def chega_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        else:
            False
    # Método privado - Apenas para uso dentro do proprio objeto
    def __gera_usuario(self):
        return self.__email.split("@")[0]

# Método estaticos

print(Usuario.contador)
print(Usuario.definicao())

user = Usuario("Gustavo", "Oliveira Cardozo", "gustavo@gmail.com", "123456")

print(user.contador)
print(user.definicao())