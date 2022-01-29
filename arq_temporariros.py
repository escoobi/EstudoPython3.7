"""

import tempfile
import os

with tempfile.TemporaryDirectory() as tmp:
    print(f"Criei o arquivo temporario: {tmp}")
    with open(os.path.join(tmp, "arq.txt"), "w") as arq:
        arq.write("Vamos acabar com isso!\n")
    input()




import os
import tempfile


with tempfile.NamedTemporaryFile() as tmp:
    tmp.write(b"Teste!\n")
    tmp.seek(0)
    print(f"O caminho é: {tmp.name}")
    input()

"""




