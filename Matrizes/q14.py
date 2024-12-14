def matriz_nula(m):
    cont = 0
    cont2 = 0
    for linha in m:
        for elemento in linha:
            cont+=1
            if elemento==0:
                cont2+=1
    
    if cont==cont2:
        return True
    else:
        return False
    
m =[[0, 1, 0,], [0, 0, 0,]]

print(matriz_nula(m))
            