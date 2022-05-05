"""Ejercicio No.3
Programa para calcular el precio de venta de un artículo"""

print("--------------------------------")
print("-------- PRECIO DE VENTA -------")
print("--------------------------------")

#input
precio_costo=float(input("Dame el precio de costo del artículo: "))

#processing 
if precio_costo<3000:
    ganancia=0.15*precio_costo
else:
    if precio_costo<=6000:
        ganancia=500
    else: 
        ganancia=0.25*precio_costo

precio_venta=precio_costo+ganancia

#output
print("El precio de costo es: " + str(precio_costo))
print("La ganancia del artículo es: " + str(ganancia))
print("El precio de venta es: " + str(precio_venta))
