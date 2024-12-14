def determinante_matriz(matriz):
    ordem = len(matriz)
    
    if ordem == 1:  
        return matriz[0][0]
    
    elif ordem == 2:  
        a = matriz[0][0]
        b = matriz[0][1]
        c = matriz[1][0]
        d = matriz[1][1]
        return a*d - b*c
    
    elif ordem == 3:  
        a = matriz[0][0]
        b = matriz[0][1]
        c = matriz[0][2]
        d = matriz[1][0]
        e = matriz[1][1]
        f = matriz[1][2]
        g = matriz[2][0]
        h = matriz[2][1]
        i = matriz[2][2]
        return a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h
    
    else:
        return "A função só calcula o determinante para matrizes de ordem 1, 2 ou 3."

m1 = [[3]]  
m2 = [[1, 2],  
      [3, 4]]
m3 = [[1, 2, 3], 
      [4, 5, 6],
      [7, 8, 9]]

print("Determinante de m1:", determinante_matriz(m1))
print("Determinante de m2:", determinante_matriz(m2))
print("Determinante de m3:", determinante_matriz(m3))