import time
from threading import Thread

contador = 50000000


def contador_regressivo(n):
    while n > 0:
        n -= 1


inicio = time.time()
contador_regressivo(contador)
fim = time.time()

print(f"Tempo em segundos: {fim - inicio}")
