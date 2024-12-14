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
def eh_quadrada(matriz_usuario):
    cont_linhas = 0
    cont_colunas = 0

    for linha in matriz_usuario:
        cont_linhas+=1
        for elemento in linha:
            if cont_linhas==1:
                cont_colunas+=1
    
    if cont_linhas==cont_colunas:
        return True
    else:
        return False
def diagonal_matriz(matriz_usuario):
    new_list = []
    cont = 0
    for linha in matriz_usuario:
        cont+=1
        cont2 = 0
        for elemento in linha:
            cont2+=1
            if cont==cont2:
                new_list.append(elemento)

    return new_list

matriz_usuario = criar_matriz()
lista = []

if eh_quadrada(matriz_usuario)==True:
    print("Lista com os elementos da diagonal da matriz:\n", diagonal_matriz(matriz_usuario))
else:
    print(lista)