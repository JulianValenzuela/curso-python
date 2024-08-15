from random import shuffle

#Liata inicial
palitos=['-','--','---','----']

#mezclar palitos
def mezcar(lista):
  shuffle(lista)
  return lista

#pedir intento
def probar_suerte():
  intento= ''

  while intento not in ['1','2','3','4']:
    intento= input('Elige un numero entre 1 y 4: ')
    return int(intento)

#comprobar intento
def comprobar_intento(lista,intento):
  if lista[intento - 1] == '-':
    print('a la var la moto, guarro')

  else:
    print("Esta vez te has salvado")

  print(f"Te ha tocado {lista[intento-1]}")

palitos_mezados = mezcar(palitos)
seleccion = probar_suerte()
comprobar_intento(palitos_mezados,seleccion)