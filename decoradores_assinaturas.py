"""
Decorator com argumentos
"""


def verificar_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f"Valor incorreto: {valor}"
            return funcao(*args, **kwargs)
        return outra
    return interna


@verificar_primeiro_argumento("pizza")
def comida_favorida(*args):
    print(args)


@verificar_primeiro_argumento(10)
def soma_dez(n1, n2):
    return n1 + n2


print(soma_dez(10, 12))

print(soma_dez(1, 21))


print(comida_favorida("pizza", "churrasco"))
print(comida_favorida("feijão", "churrasco"))
