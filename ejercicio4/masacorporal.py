"""Ejercicio No.4
Programa que calcula el índice de masa corporal de una persona (IMC = peso[kg] / altura2 [m]) e indica el estado en el que se encuentra esa persona en función del valor del IMC:
"""
print("---------------")
print("------IMC------")
print("---------------")

#input 
peso=int(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura: "))

#processing
IMC=peso/(altura*altura)

#output 
if IMC<16:
    print("Su estado es: " + "Criterio de ingreso a hospital.")
else:
    if IMC>=16 and IMC<17:
        print("Su estado es: " + "Infrapeso")
    else:
        if IMC>=17 and IMC<18:
            print("Su estado es: " + "Bajo peso")
        else: 
            if IMC>=18 and IMC<25:
                print("Su estado es: " + "Peso normal(Saludable)")
            else:
                if IMC>=25 and IMC<30:
                    print("Su estado es: " + "Sobrepeso(Obesidad de grado I)")
                else:
                    if IMC>=30 and IMC<35:
                        print("Su estado es: " + "Sobrepeso crónico(Obesidad de grado II)")
                    else: 
                        if IMC>=35 and IMC<40:
                             print("Su estado es: " + "Obesidad premórbida(Obesidad de grado III)")
                        else:  
                         print("Su estado es: " + "Obesidad mórbida(Obesidad de grado IV)")
