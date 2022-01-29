"""
Geradores


gen = conta_ate(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
"""

# Primeiro Exemplo de Função Geradora


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


gen = conta_ate(10)
print(next(gen))

print("---------------")

for asd in gen:
    print(asd)
