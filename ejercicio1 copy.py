def area_y_perimetro(base: float, altura: float) -> (float,float,float):
    
    return base * altura,2*(base+altura),base * altura


area,perimetro,myarea= area_y_perimetro(4,3)
print(f"el area: {area} perimetro :{perimetro} mi area :{myarea}")
