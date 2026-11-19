
"""
def area_y_perimetro(base: float, altura: float) -> (float,str ,float, str):
    return base * altura,"area", 2 * (base + altura),"perimetro"

area, mensaje,perimetro,mensaje1 = area_y_perimetro(4, 3)    # 12.0  y  14.0
print(area,mensaje,perimetro,mensaje1)


def area_y_perimetro(base: float, altura: float) -> (float,str ,float, str):
    area= base * altura,
    mensaje="area"
    perimetro=2 * (base + altura)
    mensaje1"perimetro"
    return 

area, mensaje,perimetro,mensaje1 = area_y_perimetro(4, 3)    # 12.0  y  14.0
print(area,mensaje,perimetro,mensaje1)
"""
#crear funcion calcular_compra:
#-recibe precio y cantidad
#-retorna 3 valores
    #importe total sin descuento
    #10% aplicado
    #precio final con descuento
    
def factura(unidad: float, precio: float) -> (str,float,str,float,str,float):
    return "Precio total: ",unidad * precio, "Descuento: ",(unidad * precio)*0.1 , "Precio final: ",(unidad * precio)-(unidad * precio)*0.1 

mensaje,precio_total, mensaje1,descuento, mensaje2,precio_final = factura(4, 3)    # 12.0  y  14.0
print(mensaje,precio_total, mensaje1,descuento, mensaje2,precio_final)