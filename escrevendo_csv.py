"""
Escrevendo CSV

Podemos escrever de duas formas
Forma 1 atraves de uma lista
from csv import writer

with open("filmes.cvs", "w", encoding="utf8") as arquivo:
    escritor_csv = writer(arquivo) # Gera o objeto para podermos escrever
    filme = None
    escritor_csv.writerow(["Título", "Gênero", "Duração"]) # Para escrever cada linha no objeto
    while filme != "Sair":
        filme = input("Informe o nome do filme: ")
        filme = filme.title()
        if filme != "Sair":
            genero = input("Informe o gênero: ")
            duracao = input("Informe a duração (em minutos): ")
            escritor_csv.writerow([filme, genero, duracao])
Forma 2 atraves de um OrdeneddDict
"""


# Usando o DictWriter

from csv import DictWriter

with open("filmes_dicwriter.cvs", "w", encoding="utf8") as arquivo:
    cabecalho = ["Título", "Gênero", "Duração"]
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho) # Gera o objeto para podermos escrever com o cabeçalho
    escritor_csv.writeheader()
    filme = None
    while filme != "Sair":
        filme = input("Informe o nome do filme: ")
        filme = filme.title()
        if filme != "Sair":
            genero = input("Informe o gênero: ")
            duracao = input("Informe a duração (em minutos): ")
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})

