"""
# Type Hinting
def cumprimentar(nome: str) -> str:
    return f"Olá, {nome}"


print(cumprimentar("Gustavo"))
"""


def cabecalho(texto: str, alinhamento: bool = False) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, "#")


print(cabecalho("Gustavo"))
print(cabecalho("Gustavo", True))
