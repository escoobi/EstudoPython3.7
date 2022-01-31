"""
Métodos data/hora

import datetime

agora = datetime.datetime.now()
hoje = datetime.datetime.today()
print(agora)
print(hoje)

# Exemplo para manutenção programa no sistema.
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)

# Encontrar o dia da semana usando weekday()
# Os dias da semana usando o weekday inicia com 0, sendo essa Segunda-Feira
print(manutencao.weekday())



import datetime

aniversario = input("Qual sua data de aniversário? dd/mm/aaaa: ")

aniversario = aniversario.split("/")
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print("Você nasceu em uma Segunda-Feira")
elif aniversario.weekday() == 1:
    print("Você nasceu em uma Terça-Feira")
elif aniversario.weekday() == 2:
    print("Você nasceu em uma Quarta-Feira")
elif aniversario.weekday() == 3:
    print("Você nasceu em uma Quinta-Feira")
elif aniversario.weekday() == 4:
    print("Você nasceu em uma Sexta-Feira")
elif aniversario.weekday() == 5:
    print("Você nasceu em uma Sabado")
elif aniversario.weekday() == 6:
    print("Você nasceu em uma Domingo")


# Formatação data/hora
import datetime

hoje = datetime.datetime.today()

print(hoje)

print(f"Hoje formatado: {hoje.strftime('%d de %B de %Y')}")




def formatar_data(data):
    if data.moth == 1:
        return f" {data.day} de Janeiro de {data.year}"
    elif data.moth == 2:
        return f" {data.day} de Fevereiro de {data.year}"
    elif data.moth == 3:
        return f" {data.day} de Março de {data.year}"
    elif data.moth == 4:
        return f" {data.day} de Abril de {data.year}"
    elif data.moth == 5:
        return f" {data.day} de Maio de {data.year}"
    elif data.moth == 6:
        return f" {data.day} de Junho de {data.year}"
    elif data.moth == 7:
        return f" {data.day} de Julho de {data.year}"
    elif data.moth == 8:
        return f" {data.day} de Agosto de {data.year}"
    elif data.moth == 9:
        return f" {data.day} de Setembro de {data.year}"
    elif data.moth == 10:
        return f" {data.day} de Outubro de {data.year}"
    elif data.moth == 11:
        return f" {data.day} de Novembro de {data.year}"
    elif data.moth == 12:
        return f" {data.day} de Dezembro de {data.year}"


# Formatação data/hora
import datetime

from textblob import TextBlob


def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()

print(formata_data(hoje))


# Formatação data/hora
import datetime


nascimento = input("Qual a data do seu aniversário? dd/mm/aaaa: ")

nascimento = datetime.datetime.strptime(nascimento, "%d/%m/%Y")

print(nascimento)



import datetime


almoco = datetime.time(12, 30, 0)

print(almoco)



import timeit

# Marcando o tempo de execução de um determinado código.


# Loop for
tempo = timeit.timeit("' - '.join(str(n) for n in range(100))", number=10000)
print(tempo)
# List comprehension
tempo = timeit.timeit("' - '.join([str(n) for n in range(100)])", number=10000)
print(tempo)

# Map
tempo = timeit.timeit("' - '.join(map(str, range(100)))", number=10000)
print(tempo)


"""


# Formatação data/hora


import timeit, functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num +4
    return soma


print(timeit.timeit(functools.partial(teste, 5), number=10000))