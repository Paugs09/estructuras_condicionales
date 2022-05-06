"""Ejercicio No.9
Programa que muestra los días de la semana."""

print("----------------------------")
print("----- DÍAS DE LA SEMANA ----")
print("----------------------------")

#input
opcion=int(input("Elija el número del día de la semana que desea ver: "))

#processing
if opcion==1:
    print("Lunes")
elif opcion==2:
    print("Martes")
elif opcion==3:
    print("Miércoles")
elif opcion==4:
    print("Jueves")
elif opcion==5:
    print("Viernes")
elif opcion==6:
    print("Sábado")
elif opcion==7:
    print("Domingo")
else:
    print("Ingresó un número que no es válido.")
