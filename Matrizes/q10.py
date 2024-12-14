def verifica_igualdade(m1, m2):
    x = len(m1)
    cont_j = 0
    cont_elementos_iguais = 0

    if len(m1)!=len(m2):
        return False
    else:
        for i in range(x):
            for j in range(len(m1[0])):
                cont_j+=1
                if m1[i][j]==m2[i][j]:
                    cont_elementos_iguais+=1
    
        if cont_elementos_iguais==cont_j:
            return True
        else:
            return False

m1 = [[-1, -2, 3],[4, 5, -6],[4, 5, -6]]
m2 = [[-1, -2, 3],[4, 5, -6]]

print(verifica_igualdade(m1, m2))