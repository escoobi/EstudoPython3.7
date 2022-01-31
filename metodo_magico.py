"""
Métodos Magicos, são os que utilizam os dunder __init__ que é o método construtor

1 def __repr__(self):
    return f"Titulo: {self.titulo} autor: {self.autor}"

"""


class Livro:
    def __init__(self, titulo, autor, pg):
        self.titulo = titulo
        self.autor = autor
        self.pg = pg

    def __repr__(self):
        return f"Titulo: {self.titulo} autor: {self.autor}"

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.pg

    def __del__(self):
        print("Um Objeto do tipo livro foi deletado da memória!")

    def __add__(self, outro):
        return f"{self} - {outro}"

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ""
            for n in range(outro):
                msg += " " + str(self)
            return msg
        return "Não posso multiplicar"


livro01 = Livro("O investidor inteligente", "Benjamin Graham", 520)
livro02 = Livro("O jeito peter linth de investir", "Petter Linth", 320)
livro03 = Livro("Inteligencia Artificiacom Python", "Gustavo O. Cardozo", 628)

print(livro01)
print(livro02)
print(livro03)


print(len(livro01))
print(len(livro02))
print(len(livro03))

print(livro01 + livro02)


print(livro01 * 2)