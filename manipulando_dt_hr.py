"""
Manipulando data e hora
"""

import datetime

print(dir(datetime))

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

print(datetime.datetime.now())

agora = datetime.datetime.now()

print(agora.year)
print(agora.month)
print(agora.day)
print(agora.hour)
print(agora.minute)
print(agora.second)
print(agora.microsecond)