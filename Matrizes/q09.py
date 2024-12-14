def matriz_oposta(m):
    matriz_reversa = []
    x = len(m)

    for i in range(x):
        for j in range(len(m[0])):
            matriz_reversa.append((m[i][j])*(-1))
    
    return matriz_reversa

m = [[-1, -2, 3],[4, 5, -6]]

print(matriz_oposta(m))