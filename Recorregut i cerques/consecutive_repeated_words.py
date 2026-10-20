"""
La entrada consiste en una secuencia de palabras no vacía.
La salida imprime el número de palabras de la subsecuencia consecutiva
más larga que solo contiene la primera palabra.

"""

import yogi
primeraparaula=yogi.read(str)
actual=1
millor=1


for paraulasegüent in yogi.tokens(str):
    if primeraparaula == paraulasegüent:
        actual = actual +1
        millor = max(millor, actual)
    else:
        actual=0
print(millor)





    

    