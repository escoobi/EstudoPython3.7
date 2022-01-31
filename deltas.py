"""
Deltas


import datetime

data_hoje = datetime.datetime.now()
data_aniversario = datetime.datetime(2022, 10, 7, 0, 0, 0, 0)
tempo_p_evento = data_aniversario - data_hoje
print(type(tempo_p_evento))
print(repr(tempo_p_evento))
print(tempo_p_evento)

"""

import datetime

data_compra = datetime.datetime.now()
regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)
vencimento_boleto = data_compra + regra_boleto

print(vencimento_boleto)