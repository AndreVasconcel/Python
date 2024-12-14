def soma_matriz(m):
    soma = 0
    for linha in m:
        for elemento in linha:
            soma+=elemento
    
    return soma

matriz = [[5, 7, 3],[8, 9, 2]]

print("Soma dos elementos da matriz:")
print(soma_matriz(matriz))