# EJERCICIO 3 – Lista de compras (limitada)
# Creá una lista vacía.

# Agregá 3 productos usando .append().

# Mostrar:

# text
# Lista de compras:
# 1. [producto1]
# 2. [producto2]
# 3. [producto3]
# Bonus: Preguntá al usuario el nombre de cada producto con input().

Lista = []

Producto1 = input("Escribe el producto que quieras agregar: ").capitalize().strip()
Lista.append(Producto1)


Producto2 = input("Escribe el producto que quieras agregar: ").capitalize().strip()
Lista.append(Producto2)


Producto3 = input("Escribe el producto que quieras agregar: ").capitalize().strip()
Lista.append(Producto3)

print(f"Lista de compras: \n1.{Producto1}\n2.{Producto2}\n3.{Producto3}")