#Tema 1 · Tu primer programa¶
#1.1. Descompón en entrada, proceso y salida el cálculo del área de un rectángulo. No escribas código todavía: solo los tres bloques.
"""
print("AREA RECTANGULO")

base=float(input("Ingresa la base: "))
altura=float(input("Ingresa la altura:"))

area:float=base*altura

print(f"EL area es: {area}")
"""
#1.2. Escribe en lenguaje natural el algoritmo para decidir si un número es par.
"""
print("ES PAR ?")

numero=int(input("ingresa un numero: "))
#si el resto es 0-> es par
calculo=numero%2
if calculo==0 :
    print(f"tu numero{numero}es :par")
else:
    print(f"tu numero{numero}es :impar")

"""
#1.3. Ordena estos pasos del ciclo de desarrollo: ejecutar, analizar el problema, escribir 
# el código, corregir errores, diseñar el algoritmo.



# analizar el problema, 
# diseñar el algoritmo.
# escribir el código
# ejecutar
# corregir errores, 




#1.4. Escribe un programa con la estructura entrada → proceso → salida que pida el nombre 
# del usuario y lo salude.
"""
nombre:str=""

mensaje=str(input("ingrerse su nombre: "))
print(f"hola {mensaje}")

#forma mas correcta

# Entrada
nombre: str = input("¿Cómo te llamas? ")

# Proceso
saludo: str = f"¡Hola, {nombre}!"

# Salida
print(saludo)   # -> ¡Hola, Ada!
"""
#1.5. Pide dos números enteros y muestra su suma. Marca con comentarios dónde está cada bloque del ciclo.
n1:int
n2:int

# Entrada
n1 = int(input("ingrese un numero: "))
n2 = int(input("ingrese otro numero: "))
# Proceso
suma= n1 + n2

# Salida
print(f"{n1}+{n2}={suma}")   

#otra forma
# Entrada
a: int = int(input("Primer número: "))
b: int = int(input("Segundo número: "))

# Proceso
suma: int = a + b

# Salida
print(f"La suma es {suma}")   # -> La suma es 12
