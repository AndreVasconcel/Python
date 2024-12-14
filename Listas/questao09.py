def calcular_media_ponderada(notas, pesos, quant):
    calc = 0
    somapesos = 0
    media = 0
    
    for k in pesos:
        somapesos+=k

    for i in range(quant):
        calc += (notas[i]*pesos[i])
    
    media = calc/somapesos

    return media

notas = []
pesos = []
quant = int(input("Digite a quantidade de notas:\n"))

for i in range(quant):
    notas.append(float(input(f"Nota {i+1}: ")))
    pesos.append(float(input(f"Peso: ")))

print("Sua média:", calcular_media_ponderada(notas, pesos, quant))