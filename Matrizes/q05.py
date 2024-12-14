def criar_matriz():
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))

    matriz = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elemento = int(input(f"Digite o elemento: "))
            linha.append(elemento)
        matriz.append(linha)

    return matriz

def soma_coluna_matriz(matriz_usuario, m):
    soma = 0

    for linha in matriz_usuario:
        cont=0
        for elemento in linha:
            cont+=1
            if cont==m:
                soma+=elemento

    return soma

matriz_usuario = criar_matriz()
m = int(input("Digite a coluna que deseja somar: "))

print("A soma da coluna da matriz é:", soma_coluna_matriz(matriz_usuario, m))
