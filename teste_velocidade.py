"""
Teste de velocidade usando generators



# Generator


def nums():
    for num in range(1, 10):
        yield num


gera = nums()
print(gera)
print(next(gera))
print(next(gera))
print(next(gera))


# Generator expression

gera01 = (num for num in range(1, 10))
print(gera01)
print(next(gera01))

"""

# Usando generator expression

import time


gen_inicio = time.time()
print(sum(num for num in range(1, 1000000000)))
gen_tempo = time.time() - gen_inicio


# Usando com List Comprehension
list_inicio = time.time()
print(sum(num for num in range(1, 1000000000)))
list_tempo = time.time() - list_inicio

print(f"Generador expression: {gen_tempo}")
print(f"List compreehsion: {list_tempo}")
