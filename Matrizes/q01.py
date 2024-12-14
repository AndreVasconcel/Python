def imprime_matriz(matriz):
    for linha in matriz:
        print("|", end=" ")
        for elemento in linha:
            print(elemento, end = " ")
        print("|")

m1 = [[1, 2],[3, 4]]
m2 = [[5, 7, 3],[8, 9, 2]]

print("M1:")
imprime_matriz(m1)
print("M2:")
imprime_matriz(m2)
