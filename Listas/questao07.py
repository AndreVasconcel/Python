def buscar_elemento(lista, elemento):

    if elemento in lista:
        return True
    else:
        return False

lista = []   
for i in range(8):
    lista.append(input(f"Elemento {i+1}: "))

elemento = input("Elemento que deseja verificar: ")

print(buscar_elemento(lista,elemento))

