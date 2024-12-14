def mult_matriz(m1, x):
    matriz_resu = []
    for linha in m1:
        lin_matriz = []
        for elemento in linha:
            lin_matriz.append(elemento*x)
        matriz_resu.append(lin_matriz)
    
    return matriz_resu




m1 = [[1, 2, 3],[4, 5, 6]]
x = int(input("Informe o X: "))

print("Matriz resultante:\n", mult_matriz(m1,x))