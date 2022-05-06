"""Ejercicio No.5
Programa que calcula e imprime las raíces de la ecuación de segundo grado de coeficientes reales."""



print("-----------------------------------------")
print("------ ECUACIONES DE SEGUNDO GRADO ------")
print("-----------------------------------------")

#input
a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
c=float(input("Ingrese el valor de c: "))

#processing
disc=b**2-4*a*c
if disc<0:
    print("La ecuación no tiene solución(Dos raíces complejas)")
else:
    raiz=disc**0.5

    if disc>0:
        x1=(-b+raiz)/2*a
        x2=(-b-raiz)/2*a
        print("La solución es de dos raíces reales diferentes." + "x1= " + str(x1) + "x2= " + str(x2))
    else:
          x1=-b/2*a   
          print ("La solución es de dos raíces reales iguales, tiene una única solución: " + str(x1))
       

