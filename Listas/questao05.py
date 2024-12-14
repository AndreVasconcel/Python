def inverter_string(texto):
    tam = len(texto)
    nova_string = ""

    for i in range(len(texto) - 1, -1, -1):
        nova_string += texto[i]
    
    return nova_string

texto = input("Texto: \n")

x = inverter_string(texto)
print("String invertida:", x)