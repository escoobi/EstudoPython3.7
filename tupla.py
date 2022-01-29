"""
tupla1 = 1, 2, 3, 4, 5
print(tupla1)
print(type(tupla1))


tupla2 = (1, 2, 3, 4, 5)
print(tupla2)
print(type(tupla2))


tupla3 = 1 # is not a tuple
print(tupla3)
print(type(tupla3))


tupla4 = tuple(range(20))
print(tupla4)
print(type(tupla4))

tupla5 = "Correr", "não pode", "ficar", "parado!"

carro, verbo1, verbo2, verbo3 = tupla5

print(carro)
print(verbo1)
print(verbo2)
print(verbo3)

tupla6 = tuple(range(20))
print(sum(tupla6))
print(min(tupla6))
print(max(tupla6))
print(len(tupla6))
print(type(tupla6))

tupla7 = tuple(range(20))
tupla8 = tuple(range(50))
print(tupla7 + tupla8)
print(type(tupla7))
print(tupla7)
print(tupla8)


tupla1 = 50, 2, 3

for i, x in enumerate(tupla1):
    print(i, x)


tupla1 = "a", "b", "b", "c"
print(tupla1.count("z"))


"""
tupla1 = "a", "b", "y", "t", "r", "e",

print(tupla1[3:5])


