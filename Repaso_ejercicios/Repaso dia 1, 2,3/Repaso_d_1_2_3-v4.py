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






# <!-- 🟨 EJERCICIO 2 – Comparador de tres números

# Escribí un programa que:

# Pida tres números enteros.

# Muestre:

# El mayor

# El menor

# Si los tres son iguales

# No podés usar max() ni min().

# Bonus:

# Validar que sean distintos antes de comparar.

# 🟥 EJERCICIO 3 – Sistema de login simple

# Escribí un programa que:

# Defina internamente:

# usuario_correcto = "admin"
# password_correcto = "1234"

# Pida usuario y contraseña al usuario.

# Reglas:

# Si ambos coinciden → "Acceso concedido"

# Si solo el usuario es correcto → "Contraseña incorrecta"

# Si el usuario no existe → "Usuario no encontrado"

# Bonus:

# Que el usuario tenga solo 3 intentos. 