# 🟦 EJERCICIO 1 – Sistema de descuento

# Escribí un programa que:

# Pregunte el precio de un producto.

# Pregunte si el cliente tiene membresía (responder "si" o "no").

# Reglas:

# Si tiene membresía → 15% de descuento.

# Si el precio es mayor a 10000 → descuento adicional del 5%.

# Mostrar el precio final con 2 decimales.

# Validaciones:

# El precio debe ser positivo.

# Si no lo es → "Precio inválido". -->

precio= int(input("Ingrese el precio del producto: "))

membresia= input("Tiene membresía? ").lower()
rta_membresia_si= ["si","sí","s"]

if precio <= 0:
    print("Precio inválido")
else:
    total= precio
    total_dto_mem=0
    total_dto_ad= 0

    if membresia in rta_membresia_si:
        total-= precio * 0.15
        total_dto_mem= precio*0.15
    if precio >= 10000:
        total -=precio*0.05
        total_dto_ad= precio*0.05

print(f"Total descuento membresía: ${total_dto_mem}\nTotal descuento adicional: ${total_dto_ad}\nTotal a pagar: ${total:.2f}")






