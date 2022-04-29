"""Ejercicio 1
Programa que lee las coordenadas cartesianas (x, y) de un punto en el plano y
calcula el cuadrante al cual pertenece el punto."""

print("----------------------------------")
print("----- COORDENADAS CARTESIANAS ----")
print("----------------------------------")

#input 
x=int(input("Ingrese el valor de x: "))
y=int(input("Ingrese el valor de y: "))

#processing 
if x>=0 and y>=0:
    print("Las coordenadas: " + "(" +str(x)+"," + str(y) + ")" + " se encuentran en el CUADRANTE 1. ")
else:
    if x<=0 and y>=0:
        print("Las coordenadas: " + "(" +str(x)+"," + str(y) + ")" +" se encuentran en el CUADRANTE 2. ")
    else:
        if x<=0 and y<=0:
            print("Las coordenadas: " + "(" +str(x)+"," + str(y) + ")" +" se encuentran en el CUADRANTE 3. ")
        else:
            if x>=0 and y<=0:
                print("Las coordenadas: " + "(" +str(x)+"," + str(y) + ")" +" se encuentran en el CUADRANTE 4. ")
    
