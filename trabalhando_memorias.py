"""
Teste de Memorias usando generators


# Funcao usando Lista fez o uso constante de 492M de Memoria RAM.
def lista_fibo(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums



for n in lista_fibo(100000):
    print(n)

"""


# Funcao usando Generators fez o uso constante de 4.4M na Memória RAM, ou seja, os Generators tem performace melhor.

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador <= max:
        a, b = b, a + b
        yield a
        contador = contador + 1


for nn in fib_gen(100000):
    print(nn)
