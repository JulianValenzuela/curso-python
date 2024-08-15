"""Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> Fals"""

def cero_repetido(*args):
    for i in range(len(args)):
        if args[i] == 0:
            
            if args[i:i+2] == [0,0]:
                return True
    return False

print(cero_repetido(5,6,1,0,0,9,3,5))
