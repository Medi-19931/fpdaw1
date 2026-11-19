# def:sirve para crear una funcion,un bloque de codigo al que puedes llamar cuando lo necesites
#ejemplo:
"""
def sumar(a,b):    #crea una funcion llamada sumar -- a y b son datos que recibe
    resultado=a+b
    return resultado   #devuelve el resultado calculado----return devuelve un valor para que puedas utilizarlo en otras operaciones
total=sumar(5,3)    #llama a la funcion con valores 5 y 3

print(total)
"""
"""
#A
n=0
i=0

for i in range(5):
    n=int(input("ingrese un numero: "))
    i=i+1#avanza
    suma=n
    suma=suma+n
    
print(suma)
"""
#correcion
suma=0

for i in range(5):
    n=int(input("ingrese un numero: "))
    suma=suma+n
    
print(f"la suma total es: {suma}")

##version1
for i in range(5):
    print(i)

#python controla las reoeticiones y asigna i con los valores 0,1,2,3 y4

##version2
i=0
while i<5:
    print(i)
    i=i*1   #avanza

#aqui si necesitas aumentar i manualmente de.de lo contrario,seguira valiendo 0 y el bucle no terminara




"""
#B
n=0
 

while n!=3:
    n=int(input("ingresa un numero del 1 al 10 que no sea 3:"))
    print("vuelve a ingresar")

    #funciona es olo que no se como poner despues usted salio formal mente solo muestra al ultimo vuelve a ingresar y se acabo cunado pongo el 3

"""
#B
n=0
 

while n!=3:
    n=int(input("ingresa un numero del 1 al 10 que no sea 3:"))
    
    if n!=3:##opcional da igual solo si quieres controlar el mensaje -if
        print("vuelve a ingresar")

print("has salido correctamente")

    #funciona es olo que no se como poner despues usted salio formal mente solo muestra al ultimo vuelve a ingresar y se acabo cunado pongo el 3



"""
#c
IVA=0.2
precio=0
unidad=0
precioTotal=0

unidad=float(input("ingrese la cantidad de productos que compro:"))
precio=float(input("ingrese el precio del producto: "))

precioTotal=unidad*precio
def precioIVA(precioTotal,IVA):
    porsentaje=precioTotal*IVA
    return porsentaje

total=precioTotal+precioIVA

print(f"sub total:{precioTotal} ,iva:{precioIVA} ,total:{total}")
#nose, tengo una ideo equivocada de en que se podria o como usar def no entiando
#nose ayuda solo cipie lo que tu ya me diste de ejemplo y lo intente copiar y poner a la fuersa y sin querer cree una constante si escribo en mayuscula todo creo que creo una constante en python en java es final int IVA=0.2;
#todo lo ise con copia y intentar con mi cerebro como encajar
"""

#c
IVA=0.2
precio=0
unidad=0
precioTotal=0

unidad=float(input("ingrese la cantidad de productos que compro:"))
precio=float(input("ingrese el precio del producto: "))

precioTotal=unidad*precio
def precioIVA(precioTotal,IVA):
    porsentaje=precioTotal*IVA
    return porsentaje

IvaCalculado=precioIVA(precioTotal,IVA)#guarda  el resultado del calculo


total=precioTotal+IvaCalculado

print(f"sub total:{precioTotal:.2f} ,iva:{IvaCalculado:.2f} ,total:{total:.2f}")



