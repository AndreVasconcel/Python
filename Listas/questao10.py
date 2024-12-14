def verificar_anagrama(string1, string2):
    cont = 0
    x = len(string1)
    y = len(string2)
    if x==y:
        for i in range(len(string1)):
            if string1[i] in string2:
                cont+=1

    if cont==(len(string1)):
        return True
    else:
        return False

string1 = input("Palavra 1: ")
string2 = input("Palavra 2: ")

print(verificar_anagrama(string1, string2))