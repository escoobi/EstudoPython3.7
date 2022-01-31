import time
from threading import Thread

contador = 50000000


def contador_regressivo(n):
    while n > 0:
        n -= 1


t1 = Thread(target=contador_regressivo, args=(contador//2, ))
t2 = Thread(target=contador_regressivo, args=(contador//2, ))


inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()

print(f"Tempo em segundos: {fim - inicio}")