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

def soma_linha_matriz(matriz_usuario, k):
    cont_linhas = 0
    soma = 0

    for linha in matriz_usuario:
        cont_linhas+=1
        for elemento in linha:
            if k==cont_linhas:
                soma+=elemento
    
    return soma

matriz_usuario = criar_matriz()
k = int(input("Digite a linha que deseja somar: "))

print("A soma da linha da matriz é:", soma_linha_matriz(matriz_usuario, k))
