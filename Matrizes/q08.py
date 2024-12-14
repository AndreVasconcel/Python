def soma_matrizes(m1, m2):
    soma = []
    for i in range(len(m1)):
        linha_soma = []
        for j in range(len(m1[0])):
            soma_elemento = m1[i][j] + m2[i][j]
            linha_soma.append(soma_elemento)
        soma.append(linha_soma)
    
    return soma

m1 = [[1, 2, 3],[4, 5, 6]]
m2 = [[5, 7, 3],[8, 9, 2]]

resultado = soma_matrizes(m1, m2)
print("Soma das matrizes:")
for linha in resultado:
    print(linha)