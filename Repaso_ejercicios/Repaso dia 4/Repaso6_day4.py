# EJERCICIO 3 – Lista de contactos (versión ampliada)
# Creá una lista vacía de contactos.

# Preguntar al usuario 2 veces:

# "Nombre del contacto 1: "

# "Teléfono del contacto 1: "
# (Repetir para contacto 2)

# Guardar cada contacto como una sublista:
# Ejemplo: contactos = [["Juan", "123456"], ["Maria", "789012"]]

# Mostrar al final:

# text
# Contacto 1: Juan - Teléfono: 123456
# Contacto 2: Maria - Teléfono: 789012
# Bonus: Preguntar al usuario "¿Qué contacto querés ver?" y mostrar solo el teléfono del que elija (usando if con el índice).


contactos = []

nombre1 = input("Nombre del contacto 1: ").lower().strip()

telefono1 = int(input("Teléfono del contacto 1:"))

contacto1 = (f"{nombre1.capitalize()}, {telefono1}")  

contactos.append(contacto1)

nombre2 = input("Nombre del contacto 2: ").lower().strip()

telefono2 = int(input("Teléfono del contacto 2:"))

contacto2 = (f"{nombre2.capitalize()}, {telefono2}")  

contactos.append(contacto2)

nombre3 = input("Nombre del contacto 3: ").lower().strip()

telefono3 = int(input("Teléfono del contacto 3:"))

contacto3 = (f"{nombre3.capitalize()}, {telefono3}")  

contactos.append(contacto3)

buscar_contacto = input("¿Qué contacto querés ver?").lower().strip()

nombres = [nombre1,nombre2,nombre3]

print(contacto1)

print(contacto2)

print(contacto3)

if buscar_contacto not in nombres:
    print(f"{buscar_contacto.capitalize()} no se encuentra en nuestros registros")
else:
    if buscar_contacto == nombre1:
        print(contacto1)
    elif buscar_contacto == nombre2:
        print(contacto2)        
    elif buscar_contacto == nombre3:
        print(contacto3)        
    


