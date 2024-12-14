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
def soma_linhas(matriz_usuario):
    lista = []

    for linha in matriz_usuario:
        soma = 0
        cont = 0
        for elemento in linha:
            soma+=elemento
            cont+=1
            if cont==len(matriz_usuario[0]):
                lista.append(soma)
            
    
    return lista


matriz_usuario = criar_matriz()

print("Lista da soma das linhas:\n", soma_linhas(matriz_usuario))