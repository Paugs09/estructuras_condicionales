"""Ejercicio No.5
Programa para calcular el gasto de agua de una vivienda"""

print("---------------------------")
print("------ GASTO DE AGUA ------")
print("---------------------------")

cuota_fija=10000

#input 
m2=int(input("Ingrese los m2 de agua gastados: "))

#processing 
if m2<50:
    print("El valor a pagar es de: " + str(cuota_fija))
else:
    if m2>=50 and m2<=200:
        cobro1=(m2*2000)+cuota_fija
        print("El valor a pagar es de: " + str(cobro1))
    else: 
        cobro2=(m2*3000)+cuota_fija
        print("El valor a pagar es de: " + str(cobro2))