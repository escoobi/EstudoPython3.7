def comer(comida, saudavel):
    if saudavel:
        final = "quero manter a forma."
    else:
        final = "a gente só vive uma vez."
    return f"Estou comendo {comida} porque {final}"


def dormir(num_horas):
    if num_horas > 8:
        return f"Ptz! Dormi muito! Estou atrasado para o trabalho!"
    else:
        return f"Continuo cansado após dormir por {num_horas} horas. :("
