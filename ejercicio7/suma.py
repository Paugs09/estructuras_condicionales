"""Ejercicio No.7
Programa que calcula e imprime las raíces de la ecuación de segundo grado de coeficientes reales."""

print("---------------------")
print("------ SUMA ---------")
print("---------------------")

#input
x=float(input("Ingrese el primer número: "))
y=float(input("Ingrese el segundo número: "))
z=float(input("Ingrese el tercer número: "))

#processing
s=x+y

#output
if s==z:
    print("La suma de los primeros dos números es igual al tercero.")
else:
    print("La suma de los dos primeros números NO es igual al tercero.")