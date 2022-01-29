"""
Decoradores de função - Syntax Sugar


def seja_educado_mesmo(funcao):
    def sendo_educado():
        print("Fou um prazer lhe conhecer!")
        funcao()
        print("Tenha um otimo dia!")
    return sendo_educado()


@seja_educado_mesmo
def apresentacao():
    print("Meu nome é Gustavo")


# apresentacao()


@seja_educado_mesmo
def domir():
    print("Quero dormir!")


# domir()


"""

