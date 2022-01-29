"""
for letra in "Gustavo":
    print(letra)


for numero in [1, 2, 3, 4]:
    print(numero)


"""


def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for("Gustavo")


numero = [1, 2, 3, 4, 5]

meu_for(numero)
