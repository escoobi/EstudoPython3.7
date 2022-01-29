"""


for n in range(11):
    print(a)

"""


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


cont = Contador(1, 10)

inter = iter(cont)

print(next(inter))
print(next(inter))
print(next(inter))
print(next(inter))
print(next(inter))
print(next(inter))
print(next(inter))
print(next(inter))
print(next(inter))
# print(next(inter))
