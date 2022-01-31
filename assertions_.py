"""
Assertions (Afirmações / Questionamentos)
"""


def soma_positivos(a, b):
    assert a > 0 and b > 0, "Ambos os numéros precisa ser positivos."
    return a + b


# ret = soma_positivos(5, -8)
# print(ret)


def comer_fast_food(comida):
    assert comida in [
        "pizza",
        "hot dog",
        "picanha",
        "sorvete",
        "doces",
        "bata fritas"
    ], "A comida precisa ser fast food."
    return f"Eu estou comendo {comida}"


comida = input("Informa a comida: ")
print(comer_fast_food(comida))


# Cuiado ao usar o assert.

# Se algum programa em python for executado com o paramentro -o, elimina os assert