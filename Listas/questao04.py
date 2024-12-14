def contar_vogais(texto):
    cont = 0
    for i in texto:
        if (i.upper()=="A") or (i.upper()=="E") or (i.upper()=="I") or (i.upper()=="O") or (i.upper()=="U"):
            cont+=1
    
    return cont






texto = input("Digite aqui: \n")

print(f"A quantidade de vogais é {contar_vogais(texto)}.")
