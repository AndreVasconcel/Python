def matriz_transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    transposta = []
    for j in range(colunas):
        linha_transposta = []
        for i in range(linhas):
            linha_transposta.append(matriz[i][j])
        transposta.append(linha_transposta)

    return transposta

matriz_exemplo = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

matriz_transposta_exemplo = matriz_transposta(matriz_exemplo)

print("Matriz original:")
for linha in matriz_exemplo:
    print(linha)

print("\nMatriz transposta:")
for linha in matriz_transposta_exemplo:
    print(linha)