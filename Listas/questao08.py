def contar_palavras(string):
    lista = []
    new_lista = []
    new_string = ""
    for i in range(len(string)):
        new_string+=string[i]
        if string[i]==" " or i==(len(string)-1):
            lista.append(new_string)
            new_string = ""
    
    cont=1
 
    for palavra in lista:
        if palavra not in new_lista:
            new_lista.append(f"{palavra}({cont})")
        else:
            cont = new_lista.count(palavra) + 1
            print(cont)
            new_lista.append(f"{palavra}({cont})")

    return new_lista


string = input("Digite aqui:\n")

print(contar_palavras(string))