def eh_quadrada(m):
    cont_linhas = 0
    cont_colunas = 0

    for linha in m:
        cont_linhas+=1
        for elemento in linha:
            if cont_linhas==1:
                cont_colunas+=1
    
    if cont_linhas==cont_colunas:
        return True
    else:
        return False
    
matriz1 = [[5, 7, 3],[8, 9, 2]]
matriz2 = [[1, 2],[3, 4]]

eh_quadrada(matriz1)
eh_quadrada(matriz2)