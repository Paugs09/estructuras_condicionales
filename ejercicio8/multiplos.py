"""Ejercicio No.8
Programa que lee dos números enteros y averigüa si el uno es múltiplo del otro."""

print("-------------------")
print("---- MÚLTIPLOS ----")
print("-------------------")

#input 
a=int(input("Digite el valor de a: "))
b=int(input("Digite el valor de b: "))

#processing
if a>b:
    r=a%b
    if r==0:
        print("a es múltiplo de b.")
    else:
        print("a NO es múltiplo de b.")
else:
    r=b%a
    if r==0:
        print("b es múltiplo de a.")
    else:
        print("b NO es múltiplo de a.")

