"""Ejercicio No.5
Programa para calcular el gasto de agua de una vivienda"""

print("---------------------------")
print("------ GASTO DE AGUA ------")
print("---------------------------")

cuota_fija=10000

#input 
m3=int(input("Ingrese los m3 de agua gastados: "))

#processing 
if m3<50:
    print("El valor a pagar es de: " + str(cuota_fija))
else:
    if m3>=50 and m3<=200:
        cobro1=cuota_fija+2000*(m3-50)
        print("El valor a pagar es de: " + str(cobro1))
    else: 
        cobro2=cuota_fija+3000*(m3-50)
        print("El valor a pagar es de: " + str(cobro2))