"""
Recebendo dados do usuário
"""

# Entrada de dados
# print("Qual o seu nome? ")
nome = input("Qual o seu nome? ")
# print("Seja bem-vindo(a) {0} ".format(nome))
print(f"Seja bem-vindo(a) {nome}")
# print("Qual sua idade? ")
idade = input("Qual a sua idade? ")
# Processamento

# Saida
# print("Sr. %s sua idade é %s." % (nome, idade))
print(f"Sr. {nome}, você nasceu em {2021 - int(idade)}")
