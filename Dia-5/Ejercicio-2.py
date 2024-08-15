"""Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']"""

def devolver_palabras_unicas(palabra):
  letras = list(palabra)
  letras_unicas = list(set(letras))
  letras_unicas.sort()
  return letras_unicas

print(devolver_palabras_unicas('hornitorinco'))