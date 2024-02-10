"""conjuntos pt 1 Daniel felipe asencio martinez"""
print("Bienvenido\nRecuerda solo números enteros, por favor ;)")

def create(conjuntos):
    while True:
        subconjunto = []  
        numeros = int(input("¿Desea crear un conjunto? [1. SI / 2. NO]: "))
        if numeros == 1:
            conjuntos.append(subconjunto)
            print(f"Se ha creado el conjunto correctamente: {conjuntos}")
        elif numeros == 2:
            break

def add(conjuntos):
    while True:
        print(f"Tienes {len(conjuntos)} conjuntos")
        choice = int(input("¿A qué conjunto deseas agregar números?: ")) - 1 
        if choice < len(conjuntos):
            b = int(input("¿Cuántos números deseas agregar al conjunto existente?: "))
        for _ in range(b):
            number = int(input("Ingresa el número que deseas agregar: "))
            conjuntos[choice].append(number)
        print(f"el conjunto fue actualizado con exito")
        print("Todos los conjuntos:", conjuntos )
        subconjuntos = int(input("desea agregar numeros en otro conjunto? [1. SI / 2. NO]"))
        if subconjuntos == 1:
            continue
        elif subconjuntos == 2:
            print(f"estos son los conjutos que creaste {conjuntos}, hasta luego ")
            break

        else:
            print("conjunto no encontrado")

conjuntos = []  # Lista para almacenar los conjuntos

create(conjuntos)
add(conjuntos)
