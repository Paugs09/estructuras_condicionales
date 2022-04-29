"""Ejercicio 2
Programa que permite realizar un préstamo bancario, teniendo en cuenta una serie de requisitos."""

print("------------------------------")
print("------ PRÉSTAMO BANCARIO -----")
print("------------------------------")

#input 
ingresos=int(input("¿Cuántos son sus ingresos?: "))

#processing 
if ingresos<945200:
    print("No es apto para recibir el préstamo")
else: 
    deudas=int(input("¿Posee deudas? 1)Sí 2)No: "))
    if deudas==2:
        print("Es apto para recibir el préstamo")
    else: 
        print("No es apto para recibir el préstamo")