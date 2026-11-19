#Tema 1 · Por qué funciones¶
#1.1. Este código repite lo mismo tres veces. Reescríbelo con una sola función:
"""
print(f"Hola, Ada")
print(f"Hola, Alan")
print(f"Hola, Grace")

def saludos(nombre:str)->(str):
    print(f"Hola ,{nombre}")

    

saludos("Ada")
saludos("Ala")
saludos("Grace")
"""
#1.3. Escribe la función más pequeña posible que evite repetir el cálculo del IVA en un programa que factura tres artículos.
"""
IVA:int=20

def conIVA (precio:float) -> (float):
    return precio* (1+IVA /100)





print(f"precio: {conIVA(25.5):.2f} ")
print(f"precio: {conIVA(1.50):.2f} ")
print(f"precio: {conIVA(29.9):.2f} ")
"""
#Tema 2 · Definir y llamar funciones¶
#2.1. Escribe es_par(n) que devuelva True o False, con sus tipos y su docstring.

#def es_par(n: int) -> bool:
"""
def es_par(numero:int) -> (int):
    
    
    return numero % 2==0



print(es_par(1))
print(es_par(2))
print(es_par(3))
"""
#2.2. ¿Qué diferencia hay entre estas dos funciones? Ejecútalas y mira lo que devuelven.
"""
def a(x): print(x * 2)
def b(x): return x * 2
"""
#asi no hacen nadanada ninguna imprime nada no muestran nada

def a(x: int) -> None:
    """Muestra el doble por pantalla."""
    print(x * 2)


def b(x: int) -> int:
    """Devuelve el doble."""
    return x * 2

resultado_a = a(5)   # -> 10   (lo imprime la propia funcion)
resultado_b = b(5)

print(resultado_a)   # -> None   a() no devuelve nada
print(resultado_b)   # -> 10     b() SI devuelve, y por eso se puede reutilizar
print(b(5) + b(3))   # -> 16     esto con a() seria imposible

#2.3. Escribe mayor(a, b) que devuelva el mayor de dos números, sin usar max().