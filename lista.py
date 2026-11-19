"""notas: list[float] = [5.0, 7.5, 9.0, 4.5]

print(notas[0])        # 5.0    primer elemento (se empieza en 0)
print(notas[-1])       # 4.5    último
print(len(notas))      # 4      cuántos elementos hay
print(type(notas))
print(max(notas))
print(min(notas))

notas.append(3.1) #añadir
print(notas)
notas.remove(5.0)#saca
print(notas)

notas.pop(2)#borra por indice o especifico
print(notas)

def media(numeros: list[float]) -> float:
    return sum(numeros) / len(numeros)
list1 :list[float] = [5.0, 7.5, 9.0]
print(media([5.0, 7.5, 9.0]))      # 7.166666666666667

import math

print(math.sqrt(16))      # 4.0     raíz cuadrada
print(math.pi)            # 3.141592653589793
print(math.floor(3.7))    # 3       redondea hacia abajo
print(math.ceil(3.2))     # 4       redondea hacia arriba

import statistics
print(statistics.mean([2, 4, 6]))     # 4      media
print(statistics.median([1, 5, 9]))   # 5      mediana

list1 :list[float] = [5.0, 7.5, 9.0]
print(statistics.mean(list1)) 

from math import sqrt, pi

print(sqrt(25))     # 5.0    ya no hace falta escribir math.


import random
print(random.randint(1, 6))        # número al azar entre 1 y 6
print(random.choice(["a", "b"]))   # elemento al azar de una lista"""

import random

vocales :list[str] = ["a","e","i"]
print(random.choice(vocales))