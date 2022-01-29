"""
Atributos de classes
representa as caracteristicas do objeto. Ou seja, pelos atributos nós conseguimos
representar computacionalmente os estados de um objeto
No python atributos é divido em 3 partes
   Atributos de instância;
   Atributos de classes;
   Atributos dinamicos;



user = Acesso("gustavo@gmail.com", "123")
print(user.email)

# Temos acesso mesmo eles como private, isso não se faz! __ (Name Mangling)
print(user._Acesso__senha)

user.mostra()
user.mostra_email()


user1 = Acesso("valquiria@gmail.com", "123456")
user2 = Acesso("gustavo@gmail.com", "123456")


user1.mostra_email()
user2.mostra_email()




# Atributos de classes são atributos é declarado diretamente na classe, fora do construtor

class Produto:
    # Atributo de classe
    imposto = 1.05
    contator = 0

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        self.id = Produto.contator +1
        Produto.contator = self.id


p1 = Produto("ps4", "p jogar", 1.500)
p2 = Produto("cimento", "p construção", 60)


print(p1.valor)
print(p2.valor)
print(p1.id)
print(p2.id)


"""

# Atributo de instânica: São atributos declarados dentro do metodo construtor.
# Em Python, fico estabelecido que, todo atributo de uma classe é publico
# Para estabelecer um atributo de uma classe como private, usa no inicio do atributo __ (Name Mangling)


class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos publicos ou privado


class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Atributos dinamicos ----> criado em tempo de execução


class Produto:
    # Atributo de classe
    imposto = 1.05
    contator = 0

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        self.id = Produto.contator + 1
        Produto.contator = self.id


p1 = Produto("ps4", "joga", 4.500)
p1.peso = "15kg"
p2 = Produto("ps3", "joga", 1.500)
p2.peso = "5kg"

print(f"Produto: {p2.nome}, descrição: {p2.descricao}, valor: {p2.valor} e Peso: {p2.peso}")


print(p1.__dict__)
print(p2.__dict__)

del p2.nome

print(p1.__dict__)
print(p2.__dict__)
