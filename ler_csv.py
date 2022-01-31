"""
Trabalhando com CSV



# Possível de se trabalhar, mas não é o ideal
with open("lutadores.csv", encoding="utf8") as arquivo:
    dados = arquivo.read()
    dados = dados.split(",")[2:]
    print(dados)

Python tem duas formas de trabalhar com arquivos CSV
1 Reader, permite que iteremos sobra as linhas do arquivo como lista
2 DisctReader, permite que iteremos sobre as linhas do arquivo como OrdereDict


#Reader

from csv import reader

with open("lutadores.csv", encoding="utf8") as arquivo:
    ler_csv = reader(arquivo)
    next(ler_csv) # Pular cabeçalho
    for linha in ler_csv:
        # Cada linha é uma lista
        print(f"{linha[0]} origem {linha[1]} e mede {linha[2]} centímetros.")

#DictReader

from csv import DictReader

with open("lutadores.csv", encoding="utf8") as arquivo:
    ler_csv = DictReader(arquivo)
    for linha in ler_csv:
        # Cada linha é uma OrderedDict
        print(f"{linha['Nome']} origem {linha['País']} e mede {linha['Altura (em cm)']} centímetros.")







"""

#DictReader

from csv import DictReader

with open("lutadores.csv", encoding="utf8") as arquivo:
    ler_csv = DictReader(arquivo, delimiter=",")
    for linha in ler_csv:
        # Cada linha é uma OrderedDict
        print(f"{linha['Nome']} origem {linha['País']} e mede {linha['Altura (em cm)']} centímetros.")



