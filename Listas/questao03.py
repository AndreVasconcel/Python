def verificar_primo(numero):
    cont = 0
    for i in range(999):
        if numero>1:
            if numero%(i+1)==0:
                cont+=1
    
    if cont==2:
        return True
    else:
        return False

numero = int(input("Número: "))

verificar_primo(numero)
        